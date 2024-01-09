from random import shuffle

#global constants
colour_list = ["Black","Red","Orange","Blue"]
max_number = 13
num_tile_copies = 2
num_jokers = 2


class Tile:
    __slots__ = ("is_joker","colour",'number')
    def __init__(self,is_joker : bool,colour : str,number : int):
        self.is_joker = is_joker
        self.colour = colour
        self.number = number

    def display(self):
        if self.is_joker:
            print("Joker")
        else:
            print(self.colour," ",self.number)

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
    
    def display_tiles(self):
        for tile in self.tiles:
            tile.display()
    
    #pick out a tile
    def pick_tile(self) -> Tile:
        if len(self.tiles)==0:
            return None
        else:
            new_tile = self.tiles.pop()
            return new_tile

if __name__ == "__main__":
    game_bag = Bag()
    game_bag.display_tiles()
    print()
    picked_tile = game_bag.pick_tile()
    picked_tile.display()
    print()
    game_bag.display_tiles()
