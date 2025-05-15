import pytest
from lib.owner_pet import Pet, Owner

def test_owner_init():
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)
    assert pet.owner == owner

    Pet.all = []

def test_has_pet_types():
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    Pet.all = []

def test_checks_pet_type():
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")
    Pet.all = []

def test_pet_has_all():
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")
    assert pet1 in Pet.all
    assert pet2 in Pet.all
    assert len(Pet.all) == 2
    Pet.all = []

def test_owner_has_pets():
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    assert owner.pets() == [pet1, pet2]
    Pet.all = []

def test_owner_adds_pets():
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)
    assert pet.owner == owner
    assert owner.pets() == [pet]
    Pet.all = []

def test_add_pet_checks_isinstance():
    owner = Owner("Jim")
    with pytest.raises(Exception):
        owner.add_pet("Lucky")
    Pet.all = []

def test_get_sorted_pets():
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)

    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]
    Pet.all = []
