from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=4),
            PetsTable(name="Buddy", type="dog", id=47),
            PetsTable(name="Krypto", type="dog", id=5),
        ]
    
    def test_list_pets ():
        controller = PetListerController(MockPetsRepository())
        response = controller.list()

        expected_response = {
            "data": {
                "type": "Pets",
                "count": len(3),
                "attributes": [
                    { "name": "Fluffy", "id": 4 },
                    { "name": "Buddy", "id": 47 },
                    { "name": "Krypto", "id": 5 }
                    ]
            }
        }

        assert response == expected_response