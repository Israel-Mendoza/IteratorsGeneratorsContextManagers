"""Working with the iterable and iterator protocols"""

#####################################################################
# By implementing the __iter__ method, our object is an iteraBLE    #
# By implementing the __iter__ and __next__ methods, our object     #
# will be an iteraTOR                                               #
# The __iter__ method must return the iterable object and           #
# the __next__ method must implement the logic to return object     #
# when iterated over.                                               #
#####################################################################


"""Implementing the iterator protocol to the same object holding the collection"""


class Cities:
    """Iterator object"""

    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index: int = 0

    def __iter__(self):
        """Implementing the iterator protocol"""
        return self

    def __next__(self) -> str:
        if self._index >= len(self._cities):
            raise StopIteration("Cities are up!")
        result = self._cities[self._index]
        self._index += 1
        return result


cities = Cities()

for city in cities:
    print(city)

# Paris
# London
# Mexico City
# Tokyo

try:
    next(cities)
except StopIteration as ex:
    print(f"{type(ex).__name__}: {ex}")
# StopIteration: Cities are up!


"""Delegating the iterator protocol to another object"""


class OtherCities:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]

    @property
    def cities(self) -> list[str]:
        return self._cities

    def __len__(self):
        return len(self._cities)


class OtherCitiesIterator:
    def __init__(self, cities_obj: OtherCities):
        self._cities_obj = cities_obj
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities_obj):
            raise StopIteration("Cities are up!")
        result = self._cities_obj.cities[self._index]
        self._index += 1
        return result


cities_iterator = OtherCitiesIterator(OtherCities())

print("Using an iterator: ")
for city in cities_iterator:
    print(city)
# Using an iterator:
# Paris
# London
# Mexico City
# Tokyo

try:
    next(cities_iterator)
except StopIteration as ex:
    print(f"{type(ex).__name__}: {ex}")
# StopIteration: Cities are up!


"""Implementing the iterable protocol in the same class"""


class CitiesIterator:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index = 0

    @property
    def cities(self) -> list[str]:
        return self._cities

    def __iter__(self):
        print("Returning an OtherCitiesIterator object!")
        return OtherCitiesIterator(self)

    def __next__(self):
        if self._index >= len(self):
            raise StopIteration("Cities are up!")
        result = self._cities[self._index]
        self._index += 1
        return result

    def __len__(self):
        return len(self._cities)


cities_iterator = CitiesIterator()

print("Using an iterator: ")
for city in cities_iterator:
    print(city)
# Using an iterator:
# Returning an OtherCitiesIterator object!
# Paris
# London
# Mexico City
# Tokyo

print("Using an iterator AGAIN: ")
for city in cities_iterator:
    print(city)
# Using an iterator AGAIN:
# Returning an OtherCitiesIterator object!
# Paris
# London
# Mexico City
# Tokyo
