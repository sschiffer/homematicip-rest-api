import pytest

from homematicip.base.base_connection import BaseConnection, ATTR_AUTH_TOKEN, ATTR_CLIENT_AUTH


@pytest.fixture
def get_tokens():
    _auth_token = 'abc'
    _access_point_id = '2114-F711-A123-0FF3-A634-32AB'
    return _auth_token, _access_point_id


@pytest.fixture
def get_base_connection() -> BaseConnection:
    return BaseConnection()


def test_client_characteristics(get_base_connection):
    _connection = get_base_connection

    assert _connection.clientCharacteristics['clientCharacteristics'][
               'applicationIdentifier'] == 'homematicip-python'
    assert _connection.clientCharacteristics['id'] is None
    assert _connection.headers[ATTR_AUTH_TOKEN] is None


def test_init_connection(get_base_connection, get_tokens):
    with pytest.raises(NotImplementedError):
        get_base_connection.init(get_tokens[1])


def test_set_auth_token(get_base_connection, get_tokens):
    get_base_connection.set_auth_token(get_tokens[0])
    assert get_base_connection.headers[ATTR_AUTH_TOKEN] == get_tokens[0]


AUTH_TOKEN_RESULT = '7D9FFAF54AB5A88BB3B7D9774EAF3193EAA87294AD86EC70214F87FADA2EB8DD886E92DC4013B11DA3761A81A0FA2BA69D712E17AAF177036E1ADDEE9EA6BB67'


def test_set_token_and_characteristics(get_base_connection, get_tokens):
    assert get_base_connection.headers[ATTR_CLIENT_AUTH] is None
    get_base_connection.set_token_and_characteristics(get_tokens[1])
    assert get_base_connection.headers[ATTR_CLIENT_AUTH] is not None
    assert get_base_connection.clientauth_token == AUTH_TOKEN_RESULT
