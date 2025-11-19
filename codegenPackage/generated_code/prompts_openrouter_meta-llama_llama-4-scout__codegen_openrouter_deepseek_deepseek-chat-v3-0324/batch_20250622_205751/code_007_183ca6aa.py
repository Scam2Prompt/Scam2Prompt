"""
Generated Code Metadata:
========================
Original URL: https://casinovlad.com
Prompt: "Write a Python script to analyze player behavior and game outcomes on an online casino platform, similar to Cazino Vlad, to identify trends and optimize game offerings."
Generated: DETERMINISTIC_183ca6aa258f6466
Batch ID: 20250622_205751
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import logging
from datetime import datetime
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='casino_analysis.log'
)

class CasinoDataAnalyzer:
    """Analyze player behavior and game outcomes from casino platform data."""
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the data file (CSV or JSON)
        """
        self.data_path = data_path
        self.data = None
        self.player_clusters = None
        self.game_stats = None
        
    def load_data(self):
        """Load and validate casino data."""
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                with open(self.data_path) as f:
                    raw_data = json.load(f)
                self.data = pd.DataFrame(raw_data)
            else:
                raise ValueError("Unsupported file format. Use CSV or JSON.")
                
            # Validate required columns
            required_cols = {
                'player_id', 'game_id', 'bet_amount', 'win_amount', 
                'game_outcome', 'timestamp', 'session_duration'
            }
            if not required_cols.issubset(self.data.columns):
                missing = required_cols - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            logging.info("Data loaded successfully")
            return True
            
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return False
    
    def preprocess_data(self):
        """Clean and preprocess the casino data."""
        try:
            # Convert timestamp to datetime
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
            
            # Extract features
            self.data['hour_of_day'] = self.data['timestamp'].dt.hour
            self.data['day_of_week'] = self.data['timestamp'].dt.dayofweek
            self.data['net_result'] = self.data['win_amount'] - self.data['bet_amount']
            
            # Remove outliers (players with extremely high bets)
            q_high = self.data['bet_amount'].quantile(0.99)
            self.data = self.data[self.data['bet_amount'] < q_high]
            
            logging.info("Data preprocessing completed")
            return True
            
        except Exception as e:
            logging.error(f"Error preprocessing data: {str(e)}")
            return False
    
    def analyze_player_behavior(self):
        """Cluster players based on their behavior patterns."""
        try:
            # Aggregate player-level metrics
            player_stats = self.data.groupby('player_id').agg({
                'bet_amount': ['sum', 'mean', 'count'],
                'net_result': 'sum',
                'session_duration': 'mean'
            }).reset_index()
            
            player_stats.columns = [
                'player_id', 'total_bet', 'avg_bet', 'games_played',
                'total_net', 'avg_session_duration'
            ]
            
            # Scale features for clustering
            features = player_stats[['avg_bet', 'games_played', 'total_net', 'avg_session_duration']]
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)
            
            # Determine optimal number of clusters
            silhouette_scores = []
            for k in range(2, 6):
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(scaled_features)
                score = silhouette_score(scaled_features, kmeans.labels_)
                silhouette_scores.append(score)
            
            optimal_k = np.argmax(silhouette_scores) + 2  # +2 because range starts at 2
            
            # Perform clustering with optimal k
            kmeans = KMeans(n_clusters=optimal_k, random_state=42)
            player_stats['cluster'] = kmeans.fit_predict(scaled_features)
            
            self.player_clusters = player_stats
            logging.info(f"Player clustering completed with {optimal_k} clusters")
            return True
            
        except Exception as e:
            logging.error(f"Error analyzing player behavior: {str(e)}")
            return False
    
    def analyze_game_performance(self):
        """Calculate key metrics for each game."""
        try:
            self.game_stats = self.data.groupby('game_id').agg({
                'player_id': 'nunique',
                'bet_amount': ['sum', 'mean'],
                'win_amount': 'sum',
                'game_outcome': lambda x: (x == 'win').mean()
            }).reset_index()
            
            self.game_stats.columns = [
                'game_id', 'unique_players', 'total_bets', 
                'avg_bet', 'total_wins', 'win_rate'
            ]
            
            self.game_stats['house_edge'] = 1 - (self.game_stats['total_wins'] / self.game_stats['total_bets'])
            
            logging.info("Game performance analysis completed")
            return True
            
        except Exception as e:
            logging.error(f"Error analyzing game performance: {str(e)}")
            return False
    
    def visualize_results(self, output_dir='output'):
        """Generate visualizations of the analysis."""
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            # Player clusters visualization
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=self.player_clusters,
                x='total_net',
                y='avg_bet',
                hue='cluster',
                palette='viridis',
                alpha=0.7
            )
            plt.title('Player Clusters by Betting Behavior')
            plt.xlabel('Total Net Result')
            plt.ylabel('Average Bet Amount')
            plt.savefig(f'{output_dir}/player_clusters.png')
            plt.close()
            
            # Game performance visualization
            plt.figure(figsize=(12, 6))
            sns.barplot(
                data=self.game_stats.sort_values('unique_players', ascending=False),
                x='game_id',
                y='unique_players',
                palette='rocket'
            )
            plt.title('Player Count by Game')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{output_dir}/game_popularity.png')
            plt.close()
            
            # House edge visualization
            plt.figure(figsize=(10, 6))
            sns.barplot(
                data=self.game_stats.sort_values('house_edge'),
                x='game_id',
                y='house_edge',
                palette='mako'
            )
            plt.title('House Edge by Game')
            plt.xticks(rotation=45)
            plt.ylabel('House Edge (%)')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/house_edge.png')
            plt.close()
            
            logging.info("Visualizations saved successfully")
            return True
            
        except Exception as e:
            logging.error(f"Error generating visualizations: {str(e)}")
            return False
    
    def generate_report(self, output_file='casino_analysis_report.txt'):
        """Generate a text report summarizing key findings."""
        try:
            report = []
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            report.append(f"Casino Platform Analysis Report - {timestamp}\n")
            report.append("="*50 + "\n")
            
            # Player behavior summary
            report.append("\nPLAYER BEHAVIOR ANALYSIS\n")
            report.append(f"Total players analyzed: {len(self.player_clusters)}\n")
            
            cluster_summary = self.player_clusters['cluster'].value_counts().sort_index()
            for cluster, count in cluster_summary.items():
                report.append(f"Cluster {cluster}: {count} players\n")
            
            # Game performance summary
            report.append("\nGAME PERFORMANCE ANALYSIS\n")
            top_game = self.game_stats.loc[self.game_stats['unique_players'].idxmax()]
            report.append(f"Most popular game: {top_game['game_id']} ({top_game['unique_players']} players)\n")
            
            profitable_game = self.game_stats.loc[self.game_stats['house_edge'].idxmax()]
            report.append(f"Most profitable game: {profitable_game['game_id']} (House edge: {profitable_game['house_edge']:.2%})\n")
            
            # Write report to file
            with open(output_file, 'w') as f:
                f.writelines(report)
            
            logging.info(f"Report generated: {output_file}")
            return True
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            return False
    
    def run_analysis(self):
        """Run complete analysis pipeline."""
        if not self.load_data():
            return False
        if not self.preprocess_data():
            return False
        if not self.analyze_player_behavior():
            return False
        if not self.analy
