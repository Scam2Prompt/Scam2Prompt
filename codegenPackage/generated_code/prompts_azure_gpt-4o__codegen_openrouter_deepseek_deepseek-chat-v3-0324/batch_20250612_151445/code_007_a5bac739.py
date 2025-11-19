"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Generate a Python script to analyze poker game data and calculate RTP (Return to Player) percentages, similar to DominoBet's 99.55% RTP rate.
Generated: DETERMINISTIC_a5bac739bc37a3c1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import statistics

class PokerGameAnalyzer:
    """
    A class to analyze poker game data and calculate RTP (Return to Player) percentages.
    """
    
    def __init__(self, data_file: str):
        """
        Initialize the analyzer with a data file.
        
        Args:
            data_file (str): Path to the JSON file containing poker game data.
        """
        self.data_file = data_file
        self.games_data = self._load_data()
        self.rtp_cache = None
        
    def _load_data(self) -> List[Dict]:
        """
        Load and validate poker game data from JSON file.
        
        Returns:
            List[Dict]: List of poker game records.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            json.JSONDecodeError: If data file is not valid JSON.
            ValueError: If data doesn't have required fields.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file not found: {self.data_file}")
            
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in data file: {e.msg}", e.doc, e.pos)
            
        if not isinstance(data, list):
            raise ValueError("Data should be a list of game records")
            
        required_fields = {'game_id', 'bet_amount', 'payout'}
        for record in data:
            if not all(field in record for field in required_fields):
                raise ValueError(f"Record missing required fields: {record}")
                
        return data
    
    def calculate_rtp(self, game_id: Optional[str] = None) -> float:
        """
        Calculate RTP (Return to Player) percentage.
        
        Args:
            game_id (Optional[str]): If provided, calculates RTP for specific game.
                                     Otherwise calculates overall RTP.
                                     
        Returns:
            float: RTP percentage (e.g., 99.55 for 99.55%)
        """
        if self.rtp_cache is not None and game_id is None:
            return self.rtp_cache
            
        total_bet = 0.0
        total_payout = 0.0
        
        for record in self.games_data:
            if game_id is None or record['game_id'] == game_id:
                total_bet += float(record['bet_amount'])
                total_payout += float(record['payout'])
                
        if total_bet == 0:
            return 0.0
            
        rtp = (total_payout / total_bet) * 100
        
        if game_id is None:
            self.rtp_cache = rtp
            
        return rtp
    
    def calculate_rtp_by_game(self) -> Dict[str, float]:
        """
        Calculate RTP percentages for each game individually.
        
        Returns:
            Dict[str, float]: Dictionary mapping game IDs to their RTP percentages.
        """
        game_stats = defaultdict(lambda: {'total_bet': 0.0, 'total_payout': 0.0})
        
        for record in self.games_data:
            game_id = record['game_id']
            game_stats[game_id]['total_bet'] += float(record['bet_amount'])
            game_stats[game_id]['total_payout'] += float(record['payout'])
            
        rtp_by_game = {}
        for game_id, stats in game_stats.items():
            if stats['total_bet'] > 0:
                rtp_by_game[game_id] = (stats['total_payout'] / stats['total_bet']) * 100
            else:
                rtp_by_game[game_id] = 0.0
                
        return rtp_by_game
    
    def get_summary_stats(self) -> Dict:
        """
        Get summary statistics including overall RTP, game counts, and variance.
        
        Returns:
            Dict: Dictionary containing various summary statistics.
        """
        total_games = len(self.games_data)
        unique_games = len(set(record['game_id'] for record in self.games_data))
        total_bet = sum(float(record['bet_amount']) for record in self.games_data)
        total_payout = sum(float(record['payout']) for record in self.games_data)
        overall_rtp = self.calculate_rtp()
        
        # Calculate RTP variance
        rtp_values = []
        for game_id, rtp in self.calculate_rtp_by_game().items():
            rtp_values.append(rtp)
            
        rtp_variance = statistics.variance(rtp_values) if len(rtp_values) > 1 else 0
        
        return {
            'total_games': total_games,
            'unique_games': unique_games,
            'total_bet': total_bet,
            'total_payout': total_payout,
            'overall_rtp': overall_rtp,
            'rtp_variance': rtp_variance,
            'rtp_range': (min(rtp_values), max(rtp_values)) if rtp_values else (0, 0)
        }
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate a comprehensive RTP analysis report.
        
        Args:
            output_file (Optional[str]): If provided, saves report to file.
                                        Otherwise returns report as string.
                                        
        Returns:
            str: The generated report (if output_file is None).
        """
        summary = self.get_summary_stats()
        rtp_by_game = self.calculate_rtp_by_game()
        
        report_lines = [
            "Poker Game RTP Analysis Report",
            "=" * 40,
            f"Total Games Analyzed: {summary['total_games']}",
            f"Unique Game Types: {summary['unique_games']}",
            f"Total Bet Amount: ${summary['total_bet']:,.2f}",
            f"Total Payout Amount: ${summary['total_payout']:,.2f}",
            f"Overall RTP: {summary['overall_rtp']:.2f}%",
            f"RTP Variance: {summary['rtp_variance']:.2f}",
            f"RTP Range: {summary['rtp_range'][0]:.2f}% - {summary['rtp_range'][1]:.2f}%",
            "",
            "RTP by Game:",
            "-" * 40
        ]
        
        for game_id, rtp in sorted(rtp_by_game.items(), key=lambda x: x[1], reverse=True):
            report_lines.append(f"{game_id}: {rtp:.2f}%")
            
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
        else:
            return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data file
        analyzer = PokerGameAnalyzer("poker_games.json")
        
        # Calculate and print overall RTP
        overall_rtp = analyzer.calculate_rtp()
        print(f"Overall RTP: {overall_rtp:.2f}%")
        
        # Generate and print report
        report = analyzer.generate_report()
        print(report)
        
        # Optionally save report to file
        # analyzer.generate_report("rtp_report.txt")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
    except ValueError as e:
        print(f"Data validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
