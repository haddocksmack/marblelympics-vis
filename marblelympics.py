import csv


class Team():
    """A class to keep track of various stats for each team"""

    def __init__(self, team_name, filename='main_results.csv'):
        """Initializes class information"""
        self.filename = filename
        self.team_name = team_name
        self.scores = []

        self.get_scores()

        self.total_score = sum(self.scores)
        self.avg_score = self.total_score / len(self.scores)
        self.cumulative_score = []

    def get_scores(self):
        """Gets list of scores from csv file"""
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            row = ['null']
            while row[0] != self.team_name:
                row = next(reader)
            self.scores = row[1:-1]
            while '' in self.scores:
                self.scores.remove('')
            for i in range(len(self.scores)):
                self.scores[i] = int(self.scores[i])

    def get_cumulative_scores(self):
        

teams = [
    'Green Ducks',
    'Raspberry Racers',
    'Hazers',
    'Savage Speeders',
    "Crazy Cat's Eyes",
    'Mellow Yellow',
    'Midnight Wisps',
    'Team Galactic',
    'Jungle Jumpers',
    'Chocolatiers',
    "O'rangers",
    'Thunderbolts',
    'Indigo Stars',
    'Pinkies',
    'Balls of Chaos',
    'Oceanics'
]

team_list = [Team(team) for team in teams]