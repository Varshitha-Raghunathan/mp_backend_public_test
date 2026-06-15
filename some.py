from re import A
from collections import defaultdict
class Player:
  count=0
  def __init__(self,name,account=1500,skip_turn=False,current_position=0,in_jail=False):
    self.name=name
    self.account=account
    self.skip_turn=skip_turn
    self.current_position=current_position
    self.cities=defaultdict(set)
    self.airports=[]
    self.companies=[]
    Player.count+=1
    self.id=Player.count
    self.in_jail=in_jail
  def credit(self,amount):
    self.account+=amount
    return self.account
  def debit(self,amount):
    self.account-=amount
    return self.account
  def update_position(self,no):
    #print("am being called")
    self.current_position=(self.current_position+no)%40
    return self.current_position
  def up(self,no):
    self.current_position=no
    return self.current_position
  def add_to_property_country(self,object):
    self.cities[object.country].add(object)
    return self.cities
  def add_to_property_airport(self,object):
    self.airports.append(object)
    return self.airports
  def add_to_property_company(self,object):
    self.companies.append(object)
    return self.companies
#################################################################
class City:
  def __init__(self,country,name,price,rent,h1p,h2p,h3p,hotelprice,h1r,h2r,h3r,hotelrent,id,bought=False,owner=None,no_of_houses_built=0):
    self.name=name
    self.country=country
    self.price=price
    self.rent=rent
    self.h1p=h1p
    self.h2p=h2p
    self.h3p=h3p
    self.hotelprice=hotelprice
    self.h1r=h1r
    self.h2r=h2r
    self.h3r=h3r
    self.hotelrent=hotelrent
    self.bought=bought
    self.owner=owner
    self.id=id
    self.no_of_houses_built=no_of_houses_built
##############################################################
class Company:
  def __init__(self,name,price,id,bought=False,owner=None):
    self.name=name
    self.price=price
    self.bought=bought
    self.owner=owner
    self.id=id
###############################################################
class Airport:
    def __init__(self,name,price,id,bought=False,owner=None):
      self.name=name
      self.price=price
      self.bought=bought
      self.owner=owner,
      self.id=id
############################################################
###CREATION OF THE BOARD####
water_company = Company("Water Works", 150,"WC")
electric_company = Company("Electric Company", 150,"EC")
airport1 = Airport("Heathrow Airport", 200,"A1")
airport2 = Airport("Dubai International Airport", 220,"A2")
airport3 = Airport("Changi Airport", 210,"A3")
airport4 = Airport("JFK Airport", 230,"A4")
    # USA (3 cities)
city1 = City("USA", "New York", 200, 50, 100, 150, 200, 300, 25, 50, 75, 100,"NYC")
city2 = City("USA", "Los Angeles", 180, 45, 90, 140, 190, 280, 20, 45, 70, 95,"LA")
city3 = City("USA", "Chicago", 160, 40, 80, 130, 180, 260, 18, 40, 65, 90,"CH")

# India (3 cities)
city4 = City("India", "Chennai", 120, 30, 60, 100, 140, 200, 15, 30, 50, 70,"CE")
city5 = City("India", "Mumbai", 150, 35, 70, 110, 150, 220, 18, 35, 55, 75,"MU")
city6 = City("India", "Delhi", 140, 32, 65, 105, 145, 210, 16, 32, 52, 72,"DE")

# UK (2 cities)
city7 = City("UK", "London", 220, 55, 110, 160, 210, 320, 30, 55, 80, 110,"LO")
city8 = City("UK", "Manchester", 170, 42, 85, 135, 185, 270, 22, 42, 67, 92,"MS")

# Australia (2 cities)
city9 = City("Australia", "Sydney", 210, 52, 105, 155, 205, 310, 28, 52, 78, 105,"SY")
city10 = City("Australia", "Melbourne", 190, 48, 95, 145, 195, 290, 25, 48, 73, 100,"MB")
# Germany (3 cities)
city11 = City("Germany", "Berlin", 170, 42, 85, 135, 185, 275, 22, 42, 68, 95,"BE")
city12 = City("Germany", "Munich", 190, 48, 95, 145, 195, 300, 25, 48, 72, 100,"MN")
city13 = City("Japan", "Kyoto", 160, 40, 80, 130, 180, 260, 20, 40, 65, 90,"KY")

# Japan (1 city)
city14 = City("Japan", "Tokyo", 230, 60, 120, 170, 220, 350, 35, 60, 85, 120,"TK")
# France (3 cities)
city15 = City("France", "Paris", 210, 55, 110, 160, 210, 320, 30, 55, 80, 110,"PS")
city16 = City("France", "Lyon", 170, 42, 85, 135, 185, 270, 22, 42, 68, 92,"LY")
city17 = City("France", "Marseille", 160, 40, 80, 130, 180, 260, 20, 40, 65, 90,"MA")

# Canada (2 cities)
city18 = City("Canada", "Toronto", 200, 50, 100, 150, 200, 300, 28, 50, 75, 105,"TO")
city19 = City("Canada", "Vancouver", 195, 48, 95, 145, 195, 290, 26, 48, 73, 102,"VC")

# UAE (2 cities)
city20 = City("UAE", "Dubai", 220, 58, 115, 165, 215, 340, 32, 58, 82, 115,"DU")
city21 = City("UAE", "Abu Dhabi", 210, 55, 110, 160, 210, 320, 30, 55, 80, 110,"AD")

# Italy (3 cities)
city22 = City("Italy", "Rome", 190, 48, 95, 145, 195, 300, 25, 48, 72, 100,"RO")
city23 = City("Italy", "Milan", 200, 52, 100, 150, 200, 310, 27, 52, 75, 105,"MI")
cities=[city1,city2,city3,city4,city5,city6,city7,city8,city9,city10,city11,city12,city13,city14,city15,city16,city17,city18,city19,city20,city21,city22,city23]
airports=[airport1,airport2,airport3,airport4]
companies=[water_company,electric_company]
country_sets=defaultdict(list)
for var in cities:
  country_sets[var.country].append(var)

for city in cities:
  city.no_of_houses_built=0


print("country",country_sets)

"""def board_create():
    return {

        0: {"type": "start", "name": "GO"},

        1: {"type": "city", "data": city4},   # Chennai
        2: {"type": "treasure"},
        3: {"type": "city", "data": city5},   # Mumbai
        4: {"type": "income_tax"},

        5: {"type": "airport", "data": airport1},

        6: {"type": "city", "data": city6},   # Delhi
        7: {"type": "treasure"},
        8: {"type": "city", "data": city1},   # New York
        9: {"type": "city", "data": city2},   # Los Angeles

        10: {"type": "jail", "name": "Jail / Just Visiting"},

        11: {"type": "city", "data": city3},  # Chicago
        12: {"type": "company", "data": electric_company},
        13: {"type": "city", "data": city7},  # London
        14: {"type": "city", "data": city8},  # Manchester

        15: {"type": "airport", "data": airport2},

        16: {"type": "city", "data": city9},   # Sydney
        17: {"type": "treasure"},
        18: {"type": "city", "data": city10},  # Melbourne
        19: {"type": "income_tax"},
        20: {"type": "city", "data": city11},  # Berlin

        21: {"type": "free_parking", "name": "Vacation"},

        22: {"type": "city", "data": city12},  # Munich
        23: {"type": "treasure"},
        24: {"type": "city", "data": city13},  # Kyoto
        25: {"type": "city", "data": city14},  # Tokyo

        26: {"type": "airport", "data": airport3},

        27: {"type": "city", "data": city15},  # Paris
        28: {"type": "company", "data": water_company},
        29: {"type": "city", "data": city16},  # Lyon
        30: {"type": "go_to_jail"},

        31: {"type": "city", "data": city17},  # Marseille
        32: {"type": "income_tax"},
        33: {"type": "city", "data": city18},  # Toronto
        34: {"type": "city", "data": city19},  # Vancouver

        35: {"type": "airport", "data": airport4},

        36: {"type": "treasure"},
        37: {"type": "city", "data": city20},  # Dubai
        38: {"type": "income_tax"},
        39: {"type": "city", "data": city21},  # Abu Dhabi
    }
"""
def board_create():


    for city in cities:
      city.no_of_houses_built=0
    return {

        0: {"type": "start", "name": "GO"},

        1: {"type": "city", "data": city4},
        2: {"type": "treasure"},
        3: {"type": "city", "data": city5},
        4: {"type": "income_tax"},

        5: {"type": "airport", "data": airport1},

        6: {"type": "city", "data": city6},
        7: {"type": "treasure"},
        8: {"type": "city", "data": city1},
        9: {"type": "city", "data": city2},

        10: {"type": "jail", "name": "Jail / Just Visiting"},

        11: {"type": "city", "data": city3},
        12: {"type": "company", "data": electric_company},
        13: {"type": "city", "data": city7},
        14: {"type": "city", "data": city8},

        15: {"type": "airport", "data": airport2},

        16: {"type": "city", "data": city9},
        17: {"type": "treasure"},
        18: {"type": "city", "data": city10},
        19: {"type": "income_tax"},
        20: {"type": "city", "data": city11},

        21: {"type": "free_parking", "name": "Vacation"},

        22: {"type": "city", "data": city12},
        23: {"type": "treasure"},
        24: {"type": "city", "data": city13},
        25: {"type": "city", "data": city14},

        26: {"type": "airport", "data": airport3},

        27: {"type": "city", "data": city15},
        28: {"type": "company", "data": water_company},
        29: {"type": "city", "data": city16},
        30: {"type": "go_to_jail"},

        31: {"type": "city", "data": city17},
        32: {"type": "income_tax"},
        33: {"type": "city", "data": city18},
        34: {"type": "city", "data": city19},

        35: {"type": "airport", "data": airport4},

        36: {"type": "treasure"},
        37: {"type": "city", "data": city20},
        38: {"type": "income_tax"},
        39: {"type": "city", "data": city21},
    }

import random
def roll_die():
    no=random.randint(1,13)
    return no

def skip_turn(player):
  player.skip_turn=True
  return player

def prison(player,choice="N"):
  if choice=="Y":
    player.debit(50)
    return player
  else:
    skip_turn()
    return player
treasures = [
    ("Bank error in your favor, collect 100", +100),
    ("Doctor's fees, pay 50", -50),
    ("You received a scholarship, collect 150", +150),
    ("Car repair charges, pay 100", -100),
    ("Won a coding competition, collect 200", +200),
    ("Paid electricity bill, pay 75", -75),
    ("Birthday gift from friends, collect 50", +50),
    ("Traffic fine, pay 60", -60),
    ("Freelance project completed, collect 120", +120),
    ("Lost your wallet, pay 80", -80)
]

import random
def treasure(player):
  no=random.randint(0,10)
  print(type(treasures))
  treas=treasures[no]
  print(treas)
  print(treas[0],treas[1])
  print(treas[0])
  player.account=player.credit(treas[1])
  return {"treaure":treas,"player":player}

def pay_rent(player1,player2,object):

  amount=object.price
  if isinstance(object,City):
    if object.no_of_houses_built==0:
      amount=object.rent
    elif object.no_of_houses_built==1:
      amount=object.h1r
    elif object.no_of_houses_built==2:
      amount=object.h2r
    elif object.no_of_houses_built==3:
      amount=object.h3r
    elif object.no_of_houses_built==4:
      amount=object.hotelrent
    elif object.no_of_houses_built==5:
      amount=object.hotelprice
  
  print("the rent to be paid is",amount)
  #print("the account balance before the transaction for both the players",player1.account,player2.account)
  player1.debit(amount)
  player2.credit(amount)
  #print("the account balance after the transaction for both the players",player1.account,player2.account)
  return {
    "rent":amount,
    "player1":player1,
    "player2":player2,
    "object":object
  }




def jail(player,pay):
  print("printing from some.py",pay)
  if player.in_jail:
    if pay:
      print("I am inside true")
      player.debit(50)
    else:
      print("I am inside false")
      player.skip_turn=True
  player.in_jail=False
  return player

def trade(player1,player2,properties1,cash1,properties2,cash2,acceptance):
  #player 1 is creating a trade with player 2
  #properties 1 is the set of properties that player1 has whose ownership will be transferred to player2
  #cash1 ad cash2 transferred resectively
  if acceptance:
    for property_id in properties1:

      property=object_tracker_name(property_id)
      print("the property of player 1 now is",property)
      if property:
        property.owner=player2
        if isinstance(property,City):
          player2.add_to_property_country(property)
          for key,value in player1.cities.items():
            for city in value.copy():
              if city==property:
                value.remove(property)

        elif isinstance(property,Airport):
          player2.add_to_property_airport(property)
          player1.airports.remove(property)

        elif isinstance(property,Company):
          player2.add_to_property_company(property)
          player1.companies.remove(property)

    for property_id in properties2:
      
      property=object_tracker_name(property_id)
      print("the property of player 2 now is",property)
      if property:
        property.owner=player1
        if isinstance(property,City):
          player1.add_to_property_country(property)
          for key,value in player2.cities.items():
            for city in value.copy():
              if city==property:
                value.remove(property)

        elif isinstance(property,Airport):
          player1.add_to_property_airport(property)
          player2.airports.remove(property)

        elif isinstance(property,Company):
          player1.add_to_property_company(property)
          player2.companies.remove(property)
    print("WE ARE IN THE ACCEPTANCE")
    print("player1 account before",player1.account)
    print("cash set by player 1",cash1)
    player1.debit(cash1)
    player1.credit(cash2)
    print("player1 account after",player1.account)
    

    print("player2 account before",player2.account)
    print("cash set by player 2",cash2)
    player2.debit(cash2)
    player2.credit(cash1)
    print("cash has been credited to player2")
    print("player2 account after",player2.account)
    print("the trade has happened",player1.cities,player2.cities)
    return "TRADE ACCEPTED"
  return "TRADE DECLINED"
    
        
    





def move(board,player,no):
  print("am being called")
  #SKIP TURN NO NEED FOR BUY DECISON
  if player.skip_turn:
    player.skip_turn=False
    return {"player_id":player.id,
            "previous position":player.current_position,
            "current_position":player.current_position,
            "action":"SKIP TURN",
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":False,
            "name":player.name,
            "log":"you are skipping a turn"}
  
  #MISCELLENEOUS TILE NO NEED FOR BUY DECISION
  
  previous_position=player.current_position
  player.current_position=player.update_position(no)
  if previous_position>player.current_position:
    print("player has crossed the start point")
    player.credit(200)
    print("200 has been credited")
  current=player.current_position
  landed_on=board[player.current_position]
  if landed_on["type"]=="jail":
      player.in_jail=True
      return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"NEED TO ASK JAIL FREE CARD",
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":True,
            "name":player.name,
            "log":"you landed in jail"
            }
    
  if landed_on["type"]=="income_tax":
    non=random.randint(1,6)
    if non%2==0:
      player.credit(100)
    else:
      player.debit(75)
    return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"INCOME_TAX",
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you landed in it"
            }
  
  if landed_on["type"]=="free_parking":
    player.skip_turn=True
    return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"VACATION",
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you landed in vacation"
            }
  
    
  if landed_on["type"]=="treasure":
    tnrps=random.randint(0,9)
    (a,b)=treasures[tnrps]
    player.credit(b)
  
    return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"treasure"+a,
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you landed in treasure"
            }
  
  if landed_on["type"]!="city" and landed_on["type"]!="airport" and landed_on["type"]!="company":
    print(landed_on["type"],"logic not yet written")
    return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"MISCELLANEOUS",
            "buy_decision":False,
            "object_id":"NIL",
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you landed in it"
            }
  

  actual_obj=landed_on["data"]
  #ALREADY OWNED NO NEED FOR BUY DECISION
  if actual_obj.bought and actual_obj.owner!=player:
    print(actual_obj.name,"is already owned by",actual_obj.owner,"so you have to pay rent mr/ms",player.name)
    #player,actual_obj.owner,actual_obj=pay_rent(player,actual_obj.owner,actual_obj)
    rent_details=pay_rent(player,actual_obj.owner,actual_obj)
    player=rent_details["player1"]
    actual_obj.owner=rent_details["player2"]
    actual_obj=rent_details["object"]
    return   {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"PAY RENT",
            "buy_decision":False,
            "object_id":actual_obj.id,
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you landed in"+actual_obj.owner.name+" property"}
  
  #PAY RENT NO NEED FOR BUY DECISION
  if actual_obj.bought and actual_obj.owner==player:
    print("you already own this property mr/ms",player.name)
    return   {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"NOT BUY CAUSE PLAYER ALREADY OWNS THIS PLACE",
            "buy_decision":False,
            "object_id":actual_obj.id,
            "in_jail":False,
            "name":player.name,
            "log":player.name+" pay rent"}
  
 #NOT ENOUGH BALANCE NO  NEED FOR BUY DECISON
  print("you have come across an unbought land")
  if actual_obj.price>player.account:
    print("you do not have enough money to purchase this land")
    return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"NOT BUY CAUSE PLAYER HAS NO MONEY",
            "buy_decision":False,
            "object_id":actual_obj.id,
            "in_jail":False,
            "name":player.name,
            "log":player.name+" you do not have enough money"}
  return {"player_id":player.id,
            "previous position":previous_position,
            "current_position":current,
            "no":no,
            "action":"NEED TO ASK FOR BUY DECISON",
            "buy_decision":True,
            "object_id":actual_obj.id,
            "in_jail":False,
            "name":player.name}

def buy_b(actual_obj,player,buy_decision):
  
  if buy_decision:
    if isinstance(actual_obj,City):
      player.cities=player.add_to_property_country(actual_obj)
    if isinstance(actual_obj,Airport):
      player.airports=player.add_to_property_airport(actual_obj)
    if isinstance(actual_obj,Company):
      player.companies=player.add_to_property_company(actual_obj)
    player=buy(actual_obj,player)
  return  {
            "action":"BUY"}

def update_owner(object,player):
  object.owner=player
  return object
def buy(object,player):
  if object.bought:
    print("object cannot be bought")
    return player
  print("player bought",object.name)
  amount=object.price
  player.account=player.debit(amount)
  object=update_owner(object,player)
  object.bought=True
  return player
def object_tracker(id):
    for city in cities:
        if city.id==id:
            return city
    for airport in airports:
        if airport.id==id:
            return airport
    for company in companies:
        if company.id==id:
            return company
def object_tracker_name(name):
    for city in cities:
        if city.name==name:
            return city
    for airport in airports:
        if airport.name==name:
            return airport
    for company in companies:
        if company.name==name:
            return company
      
def is_set(city,owner):
  country=city.country
  for var in country_sets[country]:
    if var.owner!=owner:
      return False
  return True


"""def Game(ryan,steve):
    board={}
    board=board_create()
    
    print(ryan.current_position,ryan.account,ryan.airports,ryan.cities,ryan.companies)
    print(steve.current_position,steve.account,steve.airports,steve.cities,steve.companies)
    
    for i in range(10):
        result_ryan=move(board,ryan,roll_die())
        print("ryan's result",result_ryan)
        if result_ryan["object"]=="NA" or result_ryan["buy_decision"]==0:
          print("no need to ask for buy decision")
        else:
          obj=object_tracker(result_ryan["object"])
          buy(obj,ryan)

        result_steve=move(board,steve,roll_die())
        print("steve's result",result_steve)
        if result_steve["object"]=="NA" or result_steve["buy_decision"]==0:
          print("no need to ask for buy decision")
        else:
          obj=object_tracker(result_steve["object"])
          buy(obj,steve)

if __name__=="__main__":
  ryan=Player("ryan")
  steve=Player("steve")
  print("ryan's id",ryan.id)
  print("steve' id",steve.id)
  Game(ryan,steve)"""