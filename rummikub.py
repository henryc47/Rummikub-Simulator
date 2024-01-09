from random import shuffle

#global constants
colour_list = ["black","red","orange","blue"]
max_number = 13
num_tile_copies = 2
num_jokers = 2


class Tile:
    __slots__ = ("is_joker","colour",'number')
    def __init__(self,is_joker : bool,colour : str,number : int):
        self.is_joker = is_joker
        self.colour = colour
        self.number = number

class Bag:
    __slots__ = ("tiles")
    def __init__(self):
        self.tiles = self.create_tiles(colour_list,max_number,num_tile_copies,num_jokers)
        shuffle(self.tiles)
    
    def create_tiles(self,colours : list[str],max_number : int,num_copies : int, num_jokers : int):
        tiles = []
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
    


if __name__ == "__main__":
    game_bag = Bag()
    print(len(game_bag.tiles))

