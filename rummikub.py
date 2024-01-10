from random import shuffle
from typing import Type

#global constants
colour_list = ["Black","Red","Orange","Blue"]
max_number = 13
num_tile_copies = 2
num_jokers = 2
starting_hand_size = 14


class Tile:
    __slots__ = ("is_joker","colour",'number')
    def __init__(self,is_joker : bool,colour : str,number : int):
        self.is_joker = is_joker
        self.colour = colour
        self.number = number

    #display a tiles contents
    def display(self):
        if self.is_joker:
            print("Joker")
        else:
            print(self.colour," ",self.number)

    #does this tile match up with the requested tile
    def match_tile(self,is_joker : bool ,colour : str, number : int) -> bool:
        if is_joker:
            if self.is_joker:
                return True
            else:
                return False
        else:
            if (self.colour==colour) and (self.number==number):
                return True
            else:
                return False

#the bag stores the tiles which have not yet been selected by the player
class Bag:
    __slots__ = ("tiles")
    #fill the bag with tiles and shuffle them
    def __init__(self):
        self.tiles = self.create_tiles(colour_list,max_number,num_tile_copies,num_jokers)
        shuffle(self.tiles)
    
    #create the tiles which fill the bag
    def create_tiles(self,colours : list[str],max_number : int,num_copies : int, num_jokers : int) ->list[Tile]:
        tiles : list[Tile] = []
        #create regular tiles
        for colour in colours:
            for i in range(1,max_number+1):
                new_tile = Tile(False,colour,i)
                for j in range(num_copies):
                    tiles.append(new_tile)

        joker = Tile(True,"Na",0)
        for i in range(num_jokers):
            tiles.append(joker)
        return tiles
    
    #display all the tiles in the bag
    def display_tiles(self):
        for tile in self.tiles:
            tile.display()
        print("num tiles in bag = ",len(self.tiles))
        print()
    
    #pick out a tile and remove it from the bag
    def pick_tile(self) -> Tile:
        if len(self.tiles)==0:
            return None
        else:
            new_tile = self.tiles.pop()
            return new_tile

#hand class stores the contents of a players hand
class Hand:
    __slots__ = ("bag","tiles")
    def __init__(self,bag : Bag,starting_hand_size : int):
        self.bag = bag#bag we are drawing cards from
        self.tiles = self.get_starting_hand(starting_hand_size)

    #get a starting hand of the specificed size from the bag
    def get_starting_hand(self, starting_hand_size : int):
        tiles : list[Tile] = []
        for i in range(starting_hand_size):
            new_tile = self.bag.pick_tile()
            tiles.append(new_tile)
        return tiles

    #pick an individual tile from the bag and add it to the hand
    def pick_tile_from_bag(self):
        new_tile = self.bag.pick_tile()
        self.tiles.append(new_tile)
    
    #remove a tile from the hand
    def remove_tile_from_hand(self,tile_is_joker : bool,tile_colour : str,tile_number : int) -> bool:
        found_tile = False
        for i,tile in enumerate(self.tiles):
            tile_match = tile.match_tile(tile_is_joker,tile_colour,tile_number)
            if tile_match:
                found_tile = True
                self.tiles.pop(i)
                break
        return found_tile

    def display_hand(self):
        for tile in self.tiles:
            tile.display()
        print("num tiles in hand = ",len(self.tiles))
        print()

#The player class represents a player agent, includes a hand object which stores the games hand. Derived classes encode strategies
class Player:
    __slots__ = ("hand")
    def __init__(self,hand : Hand):
        self.hand = hand




if __name__ == "__main__":
    game_bag = Bag()
    hand = Hand(game_bag,starting_hand_size)
    print("hand")
    hand.display_hand()
    found_tile = hand.remove_tile_from_hand(True,"",-1)
    print("found tile = ",found_tile)
    print("hand after picking joker ")
    hand.display_hand()
    found_tile = hand.remove_tile_from_hand(False,"Red",8)
    print("found tile = ",found_tile)
    print("hand after picking Red 8 ")
    hand.display_hand()
    