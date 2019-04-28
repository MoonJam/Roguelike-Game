from component import *
from map import map_frame, player_entity
from numpy import any, isin
from pygame import display, event, init, KEYDOWN, quit
from setting import *


# Basic functions that make things happen within the game.
def assess_location(components):
    """Looks at the list of an entity's component types and returns
    whichever governs location."""
    if MapFrame in components:
        return MapFrame
    elif MapObject in components:
        return MapObject
    elif Rectangle in components:
        return Rectangle


def draw(entity, window, location_component):
    """Draws each of an entity's sprites on each relevant coordinate."""
    if location_component == MapFrame:
        tiles = entity.access(MapFrame).tiles
        base_sprite = entity.access(MapFrame).base_sprite.image

        for tile in tiles:
            window.blit(base_sprite, tile.access(MapObject).location)
    else:
        location = entity.access(MapObject).location
        window.blit(entity.access(Sprite).image, location)


def draw_entities(*entities):
    """This function draws all entities passed, using assess_location to
    figure out which of the entity's components contains location data."""
    governance = (Sprite, MapFrame, MapObject, Rectangle)
    window = display.get_surface()

    for entity in entities:
        available_components = entity.available

        if any(isin(available_components, governance)):
            draw(entity, window, assess_location(available_components))


def move_player(player, key, movement=(move_keys, move_values),
                modifier=cell):
    """Updates the location of an entity for the purpose of movement."""
    current = array(player.access(MapObject).location)
    update = array(movement[1][movement[0].index(key)]) * modifier

    player.access(MapObject).location = tuple(current + update)


def process_input(player_character, user_events, quit_game=quit_input):
    """This function moves all entities passed"""
    for user_event in user_events:
        if user_event.type in quit_game:
            return True

        elif user_event.type == KEYDOWN:
            if user_event.key in quit_game:
                return True
            elif user_event.key in move_keys:
                move_player(player_character, user_event.key)
                return False
        else:
            return False


# Basic functions to make the game happen.
def open_window():
    """This function initializes the main window."""
    init()
    return display.set_mode(window_size)


def run_game():
    """This function runs the main game loop."""
    window = open_window()
    exit_game = False

    while not exit_game:
        window.fill((100, 100, 100))

        draw_entities(map_frame, player_entity)
        exit_game = process_input(player_entity, event.get())

        display.update()

    quit()
    exit()
