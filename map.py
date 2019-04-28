from component import *
from graphics import sprite_catalog

floor_sprite = sprite_catalog['environment']['floor_1']
map_frame = Entity(MapFrame((50, 35), floor_sprite))

player_sprite = Sprite(sprite_catalog['character']['masked_orc_idle_anim_f0'])
player_entity = Entity(MapObject(1, 1), Player(), player_sprite)
