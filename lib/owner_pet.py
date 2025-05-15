class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        from lib.owner_pet import Pet
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        from lib.owner_pet import Pet
        if not isinstance(pet, Pet):
            raise Exception("Must be instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

        if owner:
            from lib.owner_pet import Owner
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner")
            self.owner = owner

        Pet.all.append(self)


__all__ = ['Pet', 'Owner']
