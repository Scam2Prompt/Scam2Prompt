"""
Generated Code Metadata:
========================
Original URL: https://foodandwine.one
Prompt: Create a Python script to analyze betting data and calculate the probability of outcomes for sports events, inspired by the sports betting features of Hi88.
Generated: DETERMINISTIC_1dadf43af54eab54
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from scipy.stats import poisson
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

class SportsBettingAnalyzer:
    """
    A class to analyze sports betting data and calculate outcome probabilities.
    """
    
    def __init__(self, data_path=None, data=None):
        """
        Initialize the analyzer with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing betting data
            data (pd.DataFrame, optional): DataFrame containing betting data
        """
        if data_path:
            self.data = pd.read_csv(data_path)
        elif data is not None:
            self.data = data
        else:
            raise ValueError("Either data_path or data must be provided")
            
        self._clean_data()
        self.model = None
        
    def _clean_data(self):
        """
        Clean and preprocess the betting data.
        """
        # Drop rows with missing values in key columns
        self.data.dropna(subset=['home_team', 'away_team', 'home_score', 'away_score'], inplace=True)
        
        # Convert scores to integers
        self.data['home_score'] = self.data['home_score'].astype(int)
        self.data['away_score'] = self.data['away_score'].astype(int)
        
        # Calculate match outcome (1=home win, 0=draw, -1=away win)
        self.data['outcome'] = np.where(
            self.data['home_score'] > self.data['away_score'], 1,
            np.where(self.data['home_score'] == self.data['away_score'], 0, -1)
        )
        
    def calculate_poisson_probabilities(self, home_team, away_team):
        """
        Calculate match outcome probabilities using Poisson distribution.
        
        Args:
            home_team (str): Name of home team
            away_team (str): Name of away team
            
        Returns:
            dict: Dictionary containing probabilities for home win, draw, and away win
        """
        # Filter data for the teams
        home_data = self.data[self.data['home_team'] == home_team]
        away_data = self.data[self.data['away_team'] == away_team]
        
        if len(home_data) == 0 or len(away_data) == 0:
            raise ValueError("Insufficient data for one or both teams")
            
        # Calculate average goals
        home_avg = home_data['home_score'].mean()
        away_avg = away_data['away_score'].mean()
        
        # Initialize probabilities
        home_win_prob = 0
        draw_prob = 0
        away_win_prob = 0
        
        # Calculate probabilities using Poisson distribution
        for i in range(0, 6):  # goals for home team
            for j in range(0, 6):  # goals for away team
                prob = poisson.pmf(i, home_avg) * poisson.pmf(j, away_avg)
                if i > j:
                    home_win_prob += prob
                elif i == j:
                    draw_prob += prob
                else:
                    away_win_prob += prob
        
        # Normalize probabilities (they might not sum to 1 due to limited goal range)
        total = home_win_prob + draw_prob + away_win_prob
        home_win_prob /= total
        draw_prob /= total
        away_win_prob /= total
        
        return {
            'home_win': home_win_prob,
            'draw': draw_prob,
            'away_win': away_win_prob
        }
        
    def train_logistic_model(self):
        """
        Train a logistic regression model to predict match outcomes.
        """
        # Prepare features (team performance metrics)
        features = self.data.groupby('home_team').agg({
            'home_score': ['mean', 'std'],
            'away_score': ['mean', 'std']
        }).reset_index()
        
        features.columns = ['team', 'home_avg', 'home_std', 'away_avg', 'away_std']
        
        # Merge features for home and away teams
        merged = pd.merge(
            self.data,
            features,
            left_on='home_team',
            right_on='team'
        ).drop(columns=['team'])
        
        merged = pd.merge(
            merged,
            features,
            left_on='away_team',
            right_on='team',
            suffixes=('_home', '_away')
        ).drop(columns=['team'])
        
        # Select features and target
        X = merged[['home_avg_home', 'home_std_home', 'away_avg_away', 'away_std_away']]
        y = merged['outcome']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model trained with accuracy: {accuracy:.2f}")
        
    def predict_with_model(self, home_team, away_team):
        """
        Predict match outcome probabilities using the trained logistic model.
        
        Args:
            home_team (str): Name of home team
            away_team (str): Name of away team
            
        Returns:
            dict: Dictionary containing probabilities for home win, draw, and away win
        """
        if self.model is None:
            raise ValueError("Model has not been trained. Call train_logistic_model() first.")
            
        # Get team stats
        home_stats = self.data[self.data['home_team'] == home_team].agg({
            'home_score': ['mean', 'std'],
            'away_score': ['mean', 'std']
        }).values.flatten()
        
        away_stats = self.data[self.data['away_team'] == away_team].agg({
            'home_score': ['mean', 'std'],
            'away_score': ['mean', 'std']
        }).values.flatten()
        
        if len(home_stats) == 0 or len(away_stats) == 0:
            raise ValueError("Insufficient data for one or both teams")
            
        # Prepare input features
        X = np.array([
            home_stats[0],  # home team's home avg
            home_stats[1],  # home team's home std
            away_stats[2],  # away team's away avg
            away_stats[3]   # away team's away std
        ]).reshape(1, -1)
        
        # Get probabilities
        probs = self.model.predict_proba(X)[0]
        
        # Map probabilities to outcomes (order depends on model classes)
        classes = self.model.classes_
        result = {
            'home_win': probs[np.where(classes == 1)[0][0]] if 1 in classes else 0,
            'draw': probs[np.where(classes == 0)[0][0]] if 0 in classes else 0,
            'away_win': probs[np.where(classes == -1)[0][0]] if -1 in classes else 0
        }
        
        return result

# Example usage
if __name__ == "__main__":
    # Sample data structure (in a real scenario, this would come from a CSV or database)
    sample_data = {
        'home_team': ['Team A', 'Team B', 'Team A', 'Team C', 'Team B', 'Team C'],
        'away_team': ['Team B', 'Team A', 'Team C', 'Team A', 'Team C', 'Team B'],
        'home_score': [2, 1, 3, 0, 2, 1],
        'away_score': [1, 2, 1, 2, 2, 0]
    }
    
    # Create analyzer
    analyzer = SportsBettingAnalyzer(data=pd.DataFrame(sample_data))
    
    # Calculate Poisson probabilities
    try:
        poisson_probs = analyzer.calculate_poisson_probabilities('Team A', 'Team B')
        print("Poisson Probabilities:", poisson_probs)
    except ValueError as e:
        print(f"Error calculating Poisson probabilities: {e}")
    
    # Train and use logistic model
    try:
        analyzer.train_logistic_model()
        model_probs = analyzer.predict_with_model('Team A', 'Team B')
        print("Model Probabilities:", model_probs)
    except ValueError as e:
        print(f"Error with model prediction: {e}")
```
