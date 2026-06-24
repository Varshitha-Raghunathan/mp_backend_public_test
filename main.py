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
class Lobby(BaseModel):
    player_name:str

class TurnRequest(BaseModel):
    player_name:str


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
import lobby
from collections import defaultdict

GAMES={}
PLAYERS=[]
LOBBBIES={}
current_player_id=0
current_object_id="NA"
game_id=1
lobby_id=1

@app.get("/")
async def read_server():
    return {"message":"Server is running"}



@app.get("/start_game/{lobby_id}")
async def create_game(lobby_id:int):
    players=LOBBBIES[lobby_id]._players()
    game_instance=game_copy.Game(players)
    for player in game_instance.players:
        PLAYERS.append(player)
    global game_id
    GAMES[game_id]=game_instance
    print(GAMES)
    gid=game_id
    LOBBBIES[lobby_id].started=True
    LOBBBIES[lobby_id].game_ii=game_id
    game_id=game_id+1
    state=game_instance.get_state()
    return {"STATE":state,"game_id":gid}



@app.get("/join_game/{game_id}")
async def join_game(game_id:int):
    game=GAMES[game_id]
    return {"m":"m"}


@app.get("/create_lobbies")
async def create_lobbies():
    lobby_instance=lobby.Lobby()
    global lobby_id
    LOBBBIES[lobby_id]=lobby_instance
    current_lobby_id=lobby_id
    lobby_id+=1
    return {"lobby_id":current_lobby_id}
@app.post("/join_lobby/{lobby_id}")
async def join_lobby(lobby_id:int,player:Lobby):
    lobby_i=LOBBBIES[lobby_id]
    lobby_i.add_player(player.player_name)
    return {"added"}

@app.get("/get_lobbies/{lobby_id}")
async def get_lobby(lobby_id:int):
    lobby_i=LOBBBIES[lobby_id]
    players=lobby_i._players()
    return {"players":players}


@app.get("/lobby_status/{lobby_id}")
async def lobby_status(lobby_id:int):
    lobby_i=LOBBBIES[lobby_id]
    return {
        "started":lobby_i.started,
        "game_id":lobby_i.game_ii
    }

@app.post("/turn/{game_id}")
async def your_turn(game_id:int,request:TurnRequest):

    global current_player_id
    global current_object_id
    game_instance=GAMES[game_id]
    result=game_instance.turn(request.player_name)
    if result==False:
        return {"Turn":"Not yours"}
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
@app.get("/current_player/{game_id}")
async def get_player(game_id:int):
    global current_player_id
    current_name=PLAYERS[current_player_id].name
    return {'cn':current_name}

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
