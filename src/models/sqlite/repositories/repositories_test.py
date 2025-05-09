import pytest
from src.models.sqlite.settings.connection import dbconnectionhandler
from .pets_repository import PetsRepository

#dbconnectionhandler.connect_to_db()

@pytest.mark.skip(reason="db iter")
def test_list_pets():
    repo = PetsRepository(db_connection=dbconnectionhandler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="db iter")
def test_delete_pet():
    pet_name = "cobra"
    repo = PetsRepository(db_connection=dbconnectionhandler)
    repo.delete_pets(pet_name)