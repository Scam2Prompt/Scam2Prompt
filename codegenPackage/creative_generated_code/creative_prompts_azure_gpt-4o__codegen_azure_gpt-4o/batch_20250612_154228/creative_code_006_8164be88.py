"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Write a program to analyze user activity on BaxBet and generate reports on popular casino games and betting trends.
Generated: DETERMINISTIC_8164be881256b55a
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from collections import Counter, defaultdict

class BaxBetAnalyzer:
    def __init__(self, activity_log_file):
        """
        Initialize the analyzer with the activity log file.
        
        :param activity_log_file: Path to the JSON file containing user activity logs
        """
        self.activity_log_file = activity_log_file
        self.user_activity = []
        self.game_popularity = Counter()
        self.betting_trends = defaultdict(list)

    def load_activity_logs(self):
        """
        Load user activity logs from the JSON file into memory.
        """
        try:
            with open(self.activity_log_file, 'r') as file:
                self.user_activity = json.load(file)
        except FileNotFoundError:
            print(f"Error: File {self.activity_log_file} not found.")
            raise
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data. Please check the file format.")
            raise

    def analyze_game_popularity(self):
        """
        Analyze popular casino games based on user activity logs.
        """
        for activity in self.user_activity:
            game = activity.get('game')
            if game:
                self.game_popularity[game] += 1

    def analyze_betting_trends(self):
        """
        Analyze betting trends based on user activity logs.
        """
        for activity in self.user_activity:
            game = activity.get('game')
            bet_amount = activity.get('bet_amount')
            bet_date = activity.get('bet_date')
            if game and bet_amount and bet_date:
                try:
                    bet_date_parsed = datetime.datetime.strptime(bet_date, '%Y-%m-%d').date()
                    self.betting_trends[game].append({'date': bet_date_parsed, 'bet_amount': bet_amount})
                except ValueError:
                    print(f"Error: Invalid date format in activity log: {bet_date}")
                    continue

    def generate_reports(self):
        """
        Generate and print reports on game popularity and betting trends.
        """
        print("=== Popular Casino Games ===")
        for game, count in self.game_popularity.most_common():
            print(f"Game: {game}, Plays: {count}")
        
        print("\n=== Betting Trends ===")
        for game, bets in self.betting_trends.items():
            bets_sorted = sorted(bets, key=lambda x: x['date'])
            print(f"Game: {game}")
            for bet in bets_sorted:
                print(f"  Date: {bet['date']}, Bet Amount: ${bet['bet_amount']:.2f}")

    def run_analysis(self):
        """
        Execute the full analysis process: load data, analyze it, and generate reports.
        """
        self.load_activity_logs()
        self.analyze_game_popularity()
        self.analyze_betting_trends()
        self.generate_reports()


if __name__ == "__main__":
    # Specify the path to the user activity log JSON file
    activity_log_file = "user_activity_logs.json"
    
    try:
        analyzer = BaxBetAnalyzer(activity_log_file)
        analyzer.run_analysis()
    except Exception as e:
        print(f"Analysis failed due to an error: {e}")
```
