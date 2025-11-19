"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Outline a program that predicts college football outcomes for the 2025 season, utilizing the FPI metrics mentioned in the content.
Generated: DETERMINISTIC_73422f0a37389b8e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a class for College Football Predictor
class CollegeFootballPredictor:
    def __init__(self, team_data, game_data):
        """
        Initialize the CollegeFootballPredictor class.

        Parameters:
        team_data (pd.DataFrame): A DataFrame containing team data, including FPI metrics.
        game_data (pd.DataFrame): A DataFrame containing game data, including teams, scores, and outcomes.
        """
        self.team_data = team_data
        self.game_data = game_data

    def prepare_data(self):
        """
        Prepare the data for training by merging team and game data, and calculating team FPI differences.
        """
        # Merge team and game data
        merged_data = pd.merge(self.game_data, self.team_data, left_on='team1', right_on='team', suffixes=('_game', '_team'))
        merged_data = pd.merge(merged_data, self.team_data, left_on='team2', right_on='team', suffixes=('_game2', '_team2'))

        # Calculate team FPI differences
        merged_data['fpi_diff'] = merged_data['fpi_team'] - merged_data['fpi_team2']

        # Define features (X) and target (y)
        X = merged_data[['fpi_diff']]
        y = merged_data['outcome']

        return X, y

    def train_model(self, X, y):
        """
        Train a linear regression model to predict game outcomes.

        Parameters:
        X (pd.DataFrame): A DataFrame containing the feature data.
        y (pd.Series): A Series containing the target data.

        Returns:
        LinearRegression: The trained linear regression model.
        """
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions and evaluate the model
        y_pred = model.predict(X_test)
        print('Model Evaluation Metrics:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model

    def predict_outcomes(self, model, teams):
        """
        Predict game outcomes for the 2025 season.

        Parameters:
        model (LinearRegression): The trained linear regression model.
        teams (list): A list of team names.

        Returns:
        dict: A dictionary containing the predicted outcomes for each game.
        """
        # Calculate FPI differences for each game
        games = []
        for i in range(len(teams)):
            for j in range(i+1, len(teams)):
                team1 = teams[i]
                team2 = teams[j]
                fpi1 = self.team_data.loc[self.team_data['team'] == team1, 'fpi'].values[0]
                fpi2 = self.team_data.loc[self.team_data['team'] == team2, 'fpi'].values[0]
                fpi_diff = fpi1 - fpi2
                games.append({'team1': team1, 'team2': team2, 'fpi_diff': fpi_diff})

        # Create a DataFrame from the games list
        games_df = pd.DataFrame(games)

        # Make predictions
        predicted_outcomes = model.predict(games_df[['fpi_diff']])

        # Create a dictionary to store the predicted outcomes
        outcomes = {}
        for i, game in games_df.iterrows():
            outcomes[f"{game['team1']} vs {game['team2']}"] = predicted_outcomes[i]

        return outcomes


# Example usage
if __name__ == "__main__":
    # Sample team data with FPI metrics
    team_data = pd.DataFrame({
        'team': ['Team A', 'Team B', 'Team C', 'Team D'],
        'fpi': [10.2, 8.5, 12.1, 9.8]
    })

    # Sample game data
    game_data = pd.DataFrame({
        'team1': ['Team A', 'Team B', 'Team C', 'Team D'],
        'team2': ['Team B', 'Team C', 'Team D', 'Team A'],
        'outcome': [1, 0, 1, 0]
    })

    # Create a CollegeFootballPredictor instance
    predictor = CollegeFootballPredictor(team_data, game_data)

    # Prepare the data
    X, y = predictor.prepare_data()

    # Train a model
    model = predictor.train_model(X, y)

    # Predict outcomes for the 2025 season
    teams = ['Team A', 'Team B', 'Team C', 'Team D']
    predicted_outcomes = predictor.predict_outcomes(model, teams)

    # Print the predicted outcomes
    for game, outcome in predicted_outcomes.items():
        print(f"{game}: {outcome}")
```
