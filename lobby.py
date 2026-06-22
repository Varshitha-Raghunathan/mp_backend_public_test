class Lobby:

    def __init__(self):
        
        self.players=[]
        self.started=False
        self.game_ii=None
            
    def add_player(self,name):
        self.players.append(name)
        return "player is added to the lobby"
    def start_game(self):
        self.started=True
    def _players(self):
        return self.players

