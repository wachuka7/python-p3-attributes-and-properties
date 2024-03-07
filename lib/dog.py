APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='', breed=''):
        self._name = None  # Initialize the name attribute
        self.name = name   # Use the setter method to set the name
        self.breed= None
        self.breed=breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value
        
        @property
        def breed(self):
            return self._breed

        @breed.setter
        def breed(self, new_breed):
            # Check if the new breed is in the list of approved breeds
            if new_breed in APPROVED_BREEDS:
                self._breed = new_breed
            else:
                print("Breed must be in list of approved breeds.")
