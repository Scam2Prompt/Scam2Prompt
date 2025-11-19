"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Outline a program that predicts college football outcomes for the 2025 season, utilizing the FPI metrics mentioned in the content.
Generated: DETERMINISTIC_73422f0a37389b8e
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://site.web.api.espn.com/apis/fitt/v3/sports/football/college-football": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FPIException(Exception):
    """Custom exception for FPI-related errors."""
    pass

class CollegeFootballPredictor:
    """
    A class to predict college football outcomes using ESPN's FPI (Football Power Index) metrics.
    
    Attributes:
        base_url (str): Base URL for ESPN's FPI API.
        headers (Dict): Headers for HTTP requests.
        fpi_data (pd.DataFrame): Stores FPI data for teams.
        schedule_data (pd.DataFrame): Stores schedule data for games.
    """
    
    def __init__(self):
        self.base_url = "https://site.web.api.espn.com/apis/fitt/v3/sports/football/college-football"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.fpi_data = None
        self.schedule_data = None

    def fetch_fpi_data(self) -> None:
        """
        Fetches FPI data from ESPN API and stores it in a DataFrame.
        
        Raises:
            FPIException: If data fetching fails.
        """
        try:
            url = f"{self.base_url}/fpi"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            teams = data.get('teams', [])
            
            # Extract relevant FPI metrics
            fpi_records = []
            for team in teams:
                fpi_records.append({
                    'team_id': team['id'],
                    'team_name': team['name'],
                    'fpi': team['fpi'],
                    'offensive_efficiency': team.get('offensiveEfficiency', None),
                    'defensive_efficiency': team.get('defensiveEfficiency', None),
                    'special_teams_efficiency': team.get('specialTeamsEfficiency', None),
                })
            
            self.fpi_data = pd.DataFrame(fpi_records)
            logger.info("Successfully fetched FPI data.")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch FPI data: {e}")
            raise FPIException(f"API request failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error while fetching FPI data: {e}")
            raise FPIException(f"Unexpected error: {e}")

    def fetch_schedule_data(self, year: int = 2025) -> None:
        """
        Fetches schedule data for the given year from ESPN API.
        
        Args:
            year (int): Year for which to fetch schedule data. Defaults to 2025.
            
        Raises:
            FPIException: If data fetching fails.
        """
        try:
            url = f"{self.base_url}/schedule?season={year}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            events = data.get('events', [])
            
            # Extract relevant schedule data
            schedule_records = []
            for event in events:
                for competition in event.get('competitions', []):
                    teams = competition.get('competitors', [])
                    if len(teams) != 2:
                        continue
                    
                    home_team = next((t for t in teams if t.get('homeAway') == 'home'), None)
                    away_team = next((t for t in teams if t.get('homeAway') == 'away'), None)
                    
                    if not home_team or not away_team:
                        continue
                    
                    schedule_records.append({
                        'game_id': competition['id'],
                        'date': competition.get('date', ''),
                        'home_team_id': home_team['team']['id'],
                        'away_team_id': away_team['team']['id'],
                        'neutral_site': competition.get('neutralSite', False),
                    })
            
            self.schedule_data = pd.DataFrame(schedule_records)
            logger.info(f"Successfully fetched schedule data for {year}.")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch schedule data: {e}")
            raise FPIException(f"API request failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error while fetching schedule data: {e}")
            raise FPIException(f"Unexpected error: {e}")

    def predict_games(self) -> pd.DataFrame:
        """
        Predicts outcomes for all games in the schedule using FPI data.
        
        Returns:
            pd.DataFrame: DataFrame with predictions for each game.
            
        Raises:
            FPIException: If FPI or schedule data is not loaded.
        """
        if self.fpi_data is None or self.schedule_data is None:
            raise FPIException("FPI or schedule data not loaded. Call fetch_fpi_data() and fetch_schedule_data() first.")
        
        try:
            # Merge schedule with FPI data for home and away teams
            merged = self.schedule_data.merge(
                self.fpi_data, 
                left_on='home_team_id', 
                right_on='team_id', 
                suffixes=('', '_home')
            ).merge(
                self.fpi_data, 
                left_on='away_team_id', 
                right_on='team_id', 
                suffixes=('_home', '_away')
            )
            
            # Calculate predicted margin (FPI difference + home field advantage)
            merged['home_fpi_advantage'] = merged['fpi_home'] - merged['fpi_away']
            merged['home_field_advantage'] = merged.apply(
                lambda row: 2.5 if not row['neutral_site'] else 0, 
                axis=1
            )
            merged['predicted_margin'] = merged['home_fpi_advantage'] + merged['home_field_advantage']
            
            # Determine predicted winner
            merged['predicted_winner'] = merged.apply(
                lambda row: row['team_name_home'] if row['predicted_margin'] > 0 else row['team_name_away'], 
                axis=1
            )
            
            # Select relevant columns for output
            predictions = merged[[
                'game_id', 'date', 
                'team_name_home', 'team_name_away', 
                'predicted_margin', 'predicted_winner'
            ]].rename(columns={
                'team_name_home': 'home_team',
                'team_name_away': 'away_team',
            })
            
            logger.info("Successfully generated predictions.")
            return predictions
            
        except Exception as e:
            logger.error(f"Error while predicting games: {e}")
            raise FPIException(f"Prediction failed: {e}")

    def save_predictions(self, predictions: pd.DataFrame, output_file: str) -> None:
        """
        Saves predictions to a CSV file.
        
        Args:
            predictions (pd.DataFrame): DataFrame containing predictions.
            output_file (str): Path to output CSV file.
            
        Raises:
            FPIException: If saving fails.
        """
        try:
            predictions.to_csv(output_file, index=False)
            logger.info(f"Predictions saved to {output_file}.")
        except Exception as e:
            logger.error(f"Failed to save predictions: {e}")
            raise FPIException(f"Failed to save predictions: {e}")

def main():
    """Main function to execute the prediction pipeline."""
    try:
        predictor = CollegeFootballPredictor()
        
        # Fetch data
        predictor.fetch_fpi_data()
        predictor.fetch_schedule_data(year=2025)
        
        # Generate and save predictions
        predictions = predictor.predict_games()
        output_file = f"college_football_predictions_{datetime.now().strftime('%Y%m%d')}.csv"
        predictor.save_predictions(predictions, output_file)
        
    except FPIException as e:
        logger.error(f"Prediction pipeline failed: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in prediction pipeline: {e}")

if __name__ == "__main__":
    main()
```
