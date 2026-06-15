from re import A
from collections import defaultdict
class Player:
  def __init__(self,name,account=1500,skip_turn=False,current_position=0):
    self.name=name
    self.account=account
    self.skip_turn=skip_turn
    self.current_position=current_position
    self.cities=defaultdict(set)
    self.airports=[]
    self.companies=[]
  def credit(self,amount):
    self.account+=amount
    return self.account
  def debit(self,amount):
    self.account-=amount
    return self.account
  def update_position(self,no):
    #print("am being called")
    self.current_position=(self.current_position+no)%41
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
  def __init__(self,country,name,price,rent,h1p,h2p,h3p,hotelprice,h1r,h2r,h3r,hotelrent,bought=False,owner=None):
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
##############################################################
class Company:
  def __init__(self,name,price,bought=False,owner=None):
    self.name=name
    self.price=price
    self.bought=bought
    self.owner=owner
###############################################################
class Airport:
    def __init__(self,name,price,bought=False,owner=None):
      self.name=name
      self.price=price
      self.bought=bought
      self.owner=owner
############################################################
###CREATION OF THE BOARD####
def board_create(board):
    water_company = Company("Water Works", 150)
    electric_company = Company("Electric Company", 150)
    airport1 = Airport("Heathrow Airport", 200)
    airport2 = Airport("Dubai International Airport", 220)
    airport3 = Airport("Changi Airport", 210)
    airport4 = Airport("JFK Airport", 230)
    # USA (3 cities)
    city1 = City("USA", "New York", 200, 50, 100, 150, 200, 300, 25, 50, 75, 100)
    city2 = City("USA", "Los Angeles", 180, 45, 90, 140, 190, 280, 20, 45, 70, 95)
    city3 = City("USA", "Chicago", 160, 40, 80, 130, 180, 260, 18, 40, 65, 90)

    # India (3 cities)
    city4 = City("India", "Chennai", 120, 30, 60, 100, 140, 200, 15, 30, 50, 70)
    city5 = City("India", "Mumbai", 150, 35, 70, 110, 150, 220, 18, 35, 55, 75)
    city6 = City("India", "Delhi", 140, 32, 65, 105, 145, 210, 16, 32, 52, 72)

    # UK (2 cities)
    city7 = City("UK", "London", 220, 55, 110, 160, 210, 320, 30, 55, 80, 110)
    city8 = City("UK", "Manchester", 170, 42, 85, 135, 185, 270, 22, 42, 67, 92)

    # Australia (2 cities)
    city9 = City("Australia", "Sydney", 210, 52, 105, 155, 205, 310, 28, 52, 78, 105)
    city10 = City("Australia", "Melbourne", 190, 48, 95, 145, 195, 290, 25, 48, 73, 100)
    # Germany (3 cities)
    city11 = City("Germany", "Berlin", 170, 42, 85, 135, 185, 275, 22, 42, 68, 95)
    city12 = City("Germany", "Munich", 190, 48, 95, 145, 195, 300, 25, 48, 72, 100)
    city13 = City("Japan", "Kyoto", 160, 40, 80, 130, 180, 260, 20, 40, 65, 90)

    # Japan (1 city)
    city14 = City("Japan", "Tokyo", 230, 60, 120, 170, 220, 350, 35, 60, 85, 120)
    # France (3 cities)
    city15 = City("France", "Paris", 210, 55, 110, 160, 210, 320, 30, 55, 80, 110)
    city16 = City("France", "Lyon", 170, 42, 85, 135, 185, 270, 22, 42, 68, 92)
    city17 = City("France", "Marseille", 160, 40, 80, 130, 180, 260, 20, 40, 65, 90)

    # Canada (2 cities)
    city18 = City("Canada", "Toronto", 200, 50, 100, 150, 200, 300, 28, 50, 75, 105)
    city19 = City("Canada", "Vancouver", 195, 48, 95, 145, 195, 290, 26, 48, 73, 102)

    # UAE (2 cities)
    city20 = City("UAE", "Dubai", 220, 58, 115, 165, 215, 340, 32, 58, 82, 115)
    city21 = City("UAE", "Abu Dhabi", 210, 55, 110, 160, 210, 320, 30, 55, 80, 110)

    # Italy (3 cities)
    city22 = City("Italy", "Rome", 190, 48, 95, 145, 195, 300, 25, 48, 72, 100)
    city23 = City("Italy", "Milan", 200, 52, 100, 150, 200, 310, 27, 52, 75, 105)
    cities=[city1,city2,city3,city4,city5,city6,city7,city8,city9,city10,city11,city12,city13,city14,city15,city16,city17,city18,city19,city20,city21,city22,city23]
    airports=[airport1,airport2,airport3,airport4]
    companies=[water_company,electric_company]
    # --- YOUR CITY OBJECTS (unchanged) ---
# (Assuming you've already created city1 to city23 exactly as given)

    board = {

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
    return board
############################################################
#####CITY SET LOGIC NOT YET WRITTEN#####

############################################################
##### SOME MAIN METHODS#####
import random
def roll_die():
    no=random.randint(1,13)
    return no
def skip_turn(player):
  player.skip_turn=True
  return player
def prison(player):
  choice=input("Do you want to give 50 to get out of prison")
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
  return player
def pay_rent(player1,player2,object):

  amount=object.price
  print("the rent to be paid is",amount)
  print("the account balance before the transaction for both the players",player1.account,player2.account)
  player1.debit(amount)
  player2.credit(amount)
  print("the account balance after the transaction for both the players",player1.account,player2.account)
  return player1,player2,object
def move(board,player):
  if player.skip_turn:
    print("You cannot play this turn")
    return player
  no=roll_die()
  print(player.name,"rolled a",no)
  print("previous position of",player.name,"is",player.current_position)
  player.current_position=player.update_position(no)
  on_the_board=board[player.current_position]
  print(on_the_board)
  print("current position of",player.name,"is",player.current_position)
  landed_on=board[player.current_position]
  if landed_on["type"]!="city" and landed_on["type"]!="airport" and landed_on["type"]!="company":
    print(landed_on["type"],"logic not yet written")
    return player
  actual_obj=landed_on["data"]
  if actual_obj.bought and actual_obj.owner!=player:
    print(actual_obj.name,"is already owned by",actual_obj.owner,"so you have to pay rent mr/ms",player.name)
    player,actual_obj.owner,actual_obj=pay_rent(player,actual_obj.owner,actual_obj)
    return player
  if actual_obj.bought and actual_obj.owner==player:
    print("you already own this property mr/ms",player.name)
    return player
  print("you have come across an unbought land")
  if actual_obj.price>player.account:
    print("you do not have enough money to purchase this land")
    return player
  if landed_on["type"]=="city":
    player.cities=player.add_to_property_country(actual_obj)
  if landed_on["type"]=="airport":
    player.airports=player.add_to_property_airport(actual_obj)
  if landed_on["type"]=="company":
    player.companies=player.add_to_property_company(actual_obj)
  player=buy(actual_obj,player)
  return player
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



def Game():
    board={}
    board=board_create(board)
    ryan=Player("Ryan")
    steve=Player("Steve")
    print(ryan.current_position,ryan.account,ryan.airports,ryan.cities,ryan.companies)
    print(steve.current_position,steve.account,steve.airports,steve.cities,steve.companies)
    for i in range(10):
        move(board,ryan)
        move(board,steve)

if __name__=="__main__":
  Game()