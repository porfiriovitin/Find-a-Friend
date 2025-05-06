import pytest
from .connection import dbconnectionhandler
from sqlalchemy.engine import Engine

# :: Teste de integração de banco de dados
@pytest.mark.skip(reason="db interaction")
def test_connect_to_db():
    assert dbconnectionhandler.get_engine() is None

    dbconnectionhandler.connect_to_db()
    db_engine = dbconnectionhandler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)