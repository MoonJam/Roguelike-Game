from pygame import image
from utility import *

catalog = list_subs('./sprites')
catalog_names = ['character', 'environment', 'equipment', 'item', 'npc', 'ui']

character = dir_dict(image.load, 'png', catalog[0])
environment = dir_dict(image.load, 'png', catalog[1])
equipment = dir_dict(image.load, 'png', catalog[2])
item = dir_dict(image.load, 'png', catalog[3])
npc = dir_dict(image.load, 'png', catalog[4])
ui = dir_dict(image.load, 'png', catalog[5])

sprite_catalog = dict(zip(catalog_names,
                          [character, environment, equipment, item, npc, ui]))
