import some
def create_player(name1):
    return some.Player(name1)
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
        self.board=some.board_create()
        self.current_player=0
        self.pending_state=False
        self.pending_state={"buy_decision":False,"player_id":0,"obj_id":"NIL"}
        
    
    def create_players(self):
        for i in range(self.no_of_players):
            name=input("Enter player name")
            self.players.append(create_player(name))
        return self.players
    
    def turn(self,player_id,buy_decision=True):
            if self.current_player!=player_id:
                return False
            no=some.roll_die()
            res=some.move(self.board,self.players[self.current_player],no)
            self.current_player=(self.current_player+1)%self.no_of_players
            
            self.pending_state["buy_decision"]=res["buy_decision"]
            self.pending_state["player_id"]=res["player_id"]
            self.pending_state["object_id"]=res["object_id"]
            return res
    def buy_now(self,buy_decision=True):
        obj=some.object_tracker(self.pending_state["object_id"])
        player_print=""
        for player in self.players:
            if player.id==self.pending_state["player_id"]:
                some.buy_b(obj,player,buy_decision)
                player_print=player.name
        if buy_decision:
            return player_print+" bought "+obj.name
        return "property not bought"

    def jail_time(self,player,pay=True):
        print("printing from game_copy.py")
        print(pay)
        
        if player.in_jail==True:
            some.jail(player,pay)
        return "sigh"
    def trade_t(self,player1,player2,properties1,cash1,properties2,cash2,acceptance=True):
        print("am being called from game_copy.py")
        print("player1",player1)
        print("player2",player2)
        print("properties owned by player1",properties1)
        print("properties owned by player2",properties2)
        print("cash by player1",cash1)
        print("cash by player2",cash2)
        some.trade(player1,player2,properties1,cash1,properties2,cash2,acceptance)
        return "OK"


    
    def buy_house(self,no_of_houses,city_id,player):
        city=some.object_tracker(city_id)
        print("no of houses",city.no_of_houses_built)
        print("city is",city)
        print("am being called")
        if isinstance(city,some.City):
            print("yes we are inside")
            if some.is_set(city,player): #first check if the player has the set to build a house
                if city.no_of_houses_built==0:
                    #check if the player has enough money to buy house
                    if city.h1p>player.account:
                        print("not enough money",city.h1p)
                        return 0
                    print("amount being debited is",city.h1p)
                    player.debit(city.h1p)
                    city.no_of_houses_built+=1
                    return "BOUGHT"
                if city.no_of_houses_built==1:
                    if city.no_of_houses_built!=1:
                        return
                    if city.h2p>player.account:
                        print("not enough money")
                        return 0
                    print("amount being debited is",city.h1p)
                    player.debit(city.h2p)
                    city.no_of_houses_built+=1
                    return "BOUGHT"
                if city.no_of_houses_built==2:
                    if city.no_of_houses_built!=2:
                        return
                    if city.h3p>player.account:
                        print("not enough money")
                        return 0
                    print("amount being debited is",city.h1p)
                    player.debit(city.h3p)
                    city.no_of_houses_built+=1
                    return "BOUGHT"
                if city.no_of_houses_built==3:
                    if city.no_of_houses_built!=3:
                        return
                    if city.hotelprice>player.account:
                        print("not enough money")
                        return 0
                    print("amount being debited is",city.h1p)
                    player.debit(city.hotelprice)
                    city.no_of_houses_built+=1
                    return "BOUGHT"
               
            return "BOUGHT"
    


    
    def get_state(self):
        return[
                 {"name":player.name,
                  "id":player.id,
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
            if self.pending_state["buy_decision"]:
                self.buy_now()
            another_turn=int(input("do u want to continue 0/1?"))
        return self.get_state()
        
      


"""L=["ohm","hanuman","ram"]
g=Game(L)
print(g.start_game())"""