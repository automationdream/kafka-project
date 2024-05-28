import pytest
from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config
from wiremock.client import *
import requests
import time


@pytest.fixture(scope="session")  # (1)
def wm_server():
    with wiremock_container(secure=False) as wm:

        Config.base_url = wm.get_url("__admin")  # (2)
        Mappings.create_mapping(
            Mapping(
                request=MappingRequest(method=HttpMethods.GET, url="/world"),
                response=MappingResponse(status=200, json_body={"response": "world"}),
            )
        )
        Mappings.create_mapping(
            Mapping(
                request=MappingRequest(method=HttpMethods.GET, url="/hello"),
                response=MappingResponse(status=200, json_body={"response": "hello"}),
            )
        )
        yield wm


def test_get_hello(wm_server):  # (4)

    resp1 = requests.get(wm_server.get_url("/hello"))

    assert resp1.status_code == 200
    assert resp1.json() == {"response": "hello"}


def test_get_world(wm_server):  # (4)

    resp1 = requests.get(wm_server.get_url("/world"))

    assert resp1.status_code == 200
    assert resp1.json() == {"response": "world"}
