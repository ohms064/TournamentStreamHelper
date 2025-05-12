from .TournamentDataProvider import TournamentDataProvider
import json


class LocalDataProvider(TournamentDataProvider):

    def __init__(self, url, threadpool, parent) -> None:
        super().__init__(url, threadpool, parent)
        self.name = "local"

    def GetIconURL(self):
        return ""

    def GetEntrants(self):
        return

    def GetTournamentData(self, progress_callback=None, cancel_event=None):
        return {}

    def GetMatch(self, setId, progress_callback=None, cancel_event=None):
        path = f"{self.url}/current_match.json"
        result = {}
        with open(path, "r", encoding='utf-8-sig') as file:
            result = json.load(file)
        return result[setId]

    def GetMatches(self, getFinished=False, progress_callback=None, cancel_event=None):
        path = f"{self.url}/matches.json"
        result = {}
        with open(path, "r", encoding='utf-8-sig') as file:
            result = json.load(file)
        return result

    def GetStations(self, progress_callback=None, cancel_event=None):
        return ([])

    def GetStreamQueue(self, streamName=None, progress_callback=None, cancel_event=None):
        return {}

    def GetStreamMatchId(self, streamName):
        return 0

    def GetStationMatchId(self, stationId):
        return 0

    def GetStationMatchsId(self, stationId):
        return 0

    def GetUserMatchId(self, user):
        return 0

    def GetRecentSets(self, id1, id2, videogame, callback):
        pass

    def GetLastSets(self, playerId, playerNumber):
        pass

    def GetPlayerHistoryStandings(self, playerId, playerNumber, gameType):
        pass

    def GetTournamentPhases(self, progress_callback=None, cancel_event=None):
        pass

    def GetTournamentPhaseGroup(self, id, progress_callback=None, cancel_event=None):
        pass

    def GetStandings(self, playerNumber):
        pass

    def GetFutureMatch(self, progrss_callback=None):
        pass

    # give me a list of objects that contain a "id" property
    def GetFutureMatchesList(self, sets: object, progress_callback=None, cancel_event=None):
        pass
