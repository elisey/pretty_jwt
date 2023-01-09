import pytest as pytest

from pretty_jwt.pretty_jwt import parce as parce, ParceError


@pytest.fixture
def jwt():
    yield


def test_normal_jwt():
    jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ."
        "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )
    parced_jwt = parce(jwt)
    assert parced_jwt.header == {'alg': 'HS256', 'typ': 'JWT'}
    assert parced_jwt.payload == {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }
    assert parced_jwt.signature == "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


def test_no_signature():
    jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
    )
    with pytest.raises(ParceError):
        _ = parce(jwt)


def test_invalid_payload():
    jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.aGVsb"
        "G8gd29ybGQ.SIr03zM64awWRdPrAM_61QWsZchAtgDV"
        "3pphfHPPWkI"
    )
    with pytest.raises(ParceError):
        _ = parce(jwt)


def test_empty_jwt():
    jwt = ""
    with pytest.raises(ParceError):
        _ = parce(jwt)


def test_invalid_base64_data():
    jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyf."
        "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )
    with pytest.raises(ParceError):
        _ = parce(jwt)
