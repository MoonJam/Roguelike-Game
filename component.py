from numpy import array, isin
from setting import cell


class Entity:
    """A class to contain components and generate an entity."""
    def __init__(self, *components):
        keys = [type(component) for component in components]
        values = [component for component in components]
        self.available = keys
        self.composition = dict(zip(keys, values))

    def access(self, component):
        return self.composition[component]

    def add_component(self, component):
        self.composition[type(component)] = component

    def contains(self, *components):
        component_array = array([component for component in components])
        composition_array = array([key for key in self.composition.keys()])

        return isin(component_array, composition_array)


class MapFrame:
    """Component for the basic map that appears on screen."""
    def __init__(self, dimensions, base_sprite):
        self.base_sprite = Sprite(base_sprite)
        self.dimensions = dimensions
        self.tiles = []

        for y in range(0, self.dimensions[1]):
            for x in range(0, self.dimensions[0]):
                self.tiles.append((x, y))

        self.tiles = [Entity(MapObject(t[0], t[1])) for t in self.tiles]


class MapObject:
    """Component for anything to be drawn or shown on the map grid."""
    def __init__(self, x, y, navigable=False, modifier=cell):
        self.x = x * modifier
        self.y = y * modifier
        self.location = (self.x, self.y)
        self.navigable = navigable


class Player:
    """Component for player-controlled entities."""


class Rectangle:
    """Component for rectangular map entities composed of multiple sprites."""
    def __init__(self, x, y, width, height, modifier=cell):
        self.location = []
        self.x = x * modifier
        self.y = y * modifier
        self.width = width * modifier
        self.height = height * modifier

        for w in range(self.x, self.x + self.width, modifier):
            for h in range(self.y, self.y + self.height, modifier):
                self.location.append((w, h))


class Sprite:
    """Component for entities represented on screen by a sprite."""
    def __init__(self, image):
        self.image = image
