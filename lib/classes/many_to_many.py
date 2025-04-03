class Game:
    all = []

    def __init__(self, title):
        # Validate title: must be a non-empty string
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) == 0:
            raise Exception("Title must be at least 1 character long")
        # Check if title has already been set (for immutability)
        if hasattr(self, "_title"):
            raise Exception("Title is immutable")
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    def results(self):
        # Return all results associated with this game
        return [result for result in Result.all if result.game == self]

    def players(self):
        # Return a list of unique players who played this game
        return list({result.player for result in self.results()})

    def average_score(self, player):
        # Return the average score of a player for this game
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Player:
    all = []

    def __init__(self, username):
        # Username must be a string between 2 and 16 characters
        if not isinstance(username, str):
            raise Exception("Username must be a string")
        if not (2 <= len(username) <= 16):
            raise Exception("Username must be between 2 and 16 characters")
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise Exception("Username must be a string")
        if not (2 <= len(new_username) <= 16):
            raise Exception("Username must be between 2 and 16 characters")
        self._username = new_username

    def results(self):
        # Return all results for this player
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        # Return a list of unique games this player has played
        return list({result.game for result in self.results()})

    def played_game(self, game):
        # Return True if player has played the given game
        return game in self.games_played()

    def num_times_played(self, game):
        # Return how many times this player has played the given game
        return len([result for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        # Return the player with the highest average score in the given game
        players = game.players()
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))


class Result:
    all = []

    def __init__(self, player, game, score):
        # Validate player and game types
        if not isinstance(player, Player):
            raise Exception("player must be an instance of Player")
        if not isinstance(game, Game):
            raise Exception("game must be an instance of Game")
        # Validate score range and type
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise Exception("score must be an integer between 1 and 5000")

        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
