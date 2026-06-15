import monopoly_utils

def create_player(name1):
    return monopoly_utils.Player(name1)
def get_cities(dictionary,L):
    for country,city_set in dictionary.items():
        for city in city_set:
            L.append(city.name)
    return L
class Game:
    def __init__(self,player_names):
        self.no_of_players=len(player_names)
        self.player_names=player_names
        self.players=[create_player(name) for name in self.player_names]
        self.board=monopoly_utils.board_create()
        self.current_player=0
        self.pending_state={"buy_decision":False,"player_id":0,"obj_id":"NIL"}
        
    
    def create_players(self):
        for i in range(self.no_of_players):
            name=input("Enter player name")
            self.players.append(create_player(name))
        return self.players
    
    def turn(self):
            no=monopoly_utils.roll_die()
            res=monopoly_utils.move(self.board,self.players[self.current_player],no)
            self.current_player=(self.current_player+1)%self.no_of_players
            self.pending_state["buy_decision"]=res["buy_decision"]
            self.pending_state["player_id"]=res["player_id"]
            self.pending_state["object_id"]=res["object_id"]
            return res
    def get_state(self):
        return[
                 {"name":player.name,
                  "amount":player.account,
                  "position":player.current_position,
                  "cities":get_cities(player.cities,[]),
                  "airports":[airport.name for airport in player.airports],
                  "companies":[company.name for company in player.companies]}
        for player in self.players]
 
        

    def start_game(self):
        #self.players=self.create_players()
        print("The players are")
        for i in self.players:
            print(i)
        another_turn=1
        while another_turn:
            result=self.turn()
            print(result)
            another_turn=int(input("do u want to continue 0/1?"))
            
            
      


"""L=["ohm","raichu","toastitaa"]
g=Game(L)
g.start_game()"""