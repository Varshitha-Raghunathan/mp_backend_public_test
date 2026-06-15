from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body
import some

class GameClass(BaseModel):
    players:list[str]
class BD(BaseModel):
    buy_decision:bool
class city(BaseModel):
    city_id:str
class Pay50(BaseModel):
    pay:bool
class Trade(BaseModel):
    properties1:list
    properties2:list
    cash1:float
    cash2:float
    player1_id:int
    player2_id:int
    acceptance:bool


from fastapi.middleware.cors import CORSMiddleware





app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import some
import game_copy

GAMES={}
PLAYERS=[]
current_player_id=0
current_object_id="NA"
game_id=1

@app.get("/")
async def read_server():
    return {"message":"Server is running"}

@app.post("/start_game")
async def create_game(gc:GameClass):
    game_instance=game_copy.Game(gc.players)
    for player in game_instance.players:
        PLAYERS.append(player)
    global game_id
    GAMES[game_id]=game_instance
    print(GAMES)
    gid=game_id
    game_id=game_id+1
    state=game_instance.get_state()
    return {"STATE":state,"game_id":gid}



@app.get("/turn/{game_id}")
async def your_turn(game_id:int):

    global current_player_id
    global current_object_id
    game_instance=GAMES[game_id]
    result=game_instance.turn()
    current_player_id=result["player_id"]
    current_object_id=result["object_id"]
    print("result",result)
    return result

@app.post("/buy/{game_id}")
async def buy_property(game_id:int,buy_decision:BD):
    bd=buy_decision.buy_decision
    game_instance=GAMES[game_id]
    if game_instance.pending_state["buy_decision"]:

        log=game_instance.buy_now(bd)
        return log
    else:
        return "no need to buy"
@app.get("/get_state/{game_id}")
async def get_the_state(game_id:int):
    game_instance=GAMES[game_id]
    current_game_state=game_instance.get_state()
    return_result={}
    for i in current_game_state:
        return_result[i["name"]]=i
    return return_result

@app.post("/get_house/{game_id}")
async def get_the_house(game_id:int,city_id:city):
    print("the method get house from main.py is being called")
    game_instance=GAMES[game_id]
    print("the game instance is",game_instance)
    print("the current player is",current_player_id)
    p=None
    for ply in PLAYERS:
        print("am in the loop and",ply)
        if ply.id==current_player_id:
            print("found the player object",ply)
            p=ply
    print(p)
    print(current_object_id)
    game_instance.buy_house(1,city_id.city_id,p)

    return {"log":p+"bought a house  in "+city}

@app.post("/jail_time_skip/{game_id}")
async def in_jail_skip(game_id:int,pay_50:Pay50=Body((...))):
    game_instance=GAMES[game_id]
    print("the current player is",current_player_id)
    p=None
    for ply in PLAYERS:
        print("am in the loop and",ply)
        if ply.id==current_player_id:
            print("found the player object",ply)
            p=ply
    print(p)
    print("printing from the main.py")
    print(pay_50)
    print(pay_50.pay)
    game_instance.jail_time(p,pay_50.pay)
    return {"log":p+" skipped turn"}

@app.post("/jail_time_pay/{game_id}")
async def in_jail_pay(game_id:int,pay_50:Pay50=Body((...))):
    game_instance=GAMES[game_id]
    print("the current player is",current_player_id)
    p=None
    for ply in PLAYERS:
        print("am in the loop and",ply)
        if ply.id==current_player_id:
            print("found the player object",ply)
            p=ply
    print(p)
    print("printing from the main.py")
    print(pay_50)
    game_instance.jail_time(p,pay_50.pay)
    return {"log"+p+ " payed 50 to get out of jail"}


@app.post("/trade/{game_id}")
async def trading(game_id:int,trade_stuff:Trade=Body((...))):
    print("i am inside")
    print(trade_stuff.player1_id)
    game_instance=GAMES[game_id]
    player1=None
    player2=None
    for p in PLAYERS:
        if p.id==trade_stuff.player1_id:
            player1=p
        if p.id==trade_stuff.player2_id:
            player2=p
    game_instance.trade_t(player1,player2,trade_stuff.properties1,trade_stuff.cash1,trade_stuff.properties2,trade_stuff.cash2,trade_stuff.acceptance)
    log_ac="Successful trade"
    if not trade_stuff.acceptance:
        log_ac="your trade has been declined"
    return {"log":log_ac}
