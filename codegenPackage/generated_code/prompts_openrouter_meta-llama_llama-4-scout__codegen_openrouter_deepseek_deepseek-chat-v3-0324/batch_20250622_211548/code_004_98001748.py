"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Create a Python script to analyze player performance in a racing game with features like drifting and handbrake turns, similar to those in Rally Racer Dirt.
Generated: DETERMINISTIC_9800174851fbacf2
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import statistics
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EventType(Enum):
    DRIFT = "drift"
    HANDBRAKE_TURN = "handbrake_turn"
    COLLISION = "collision"
    LAP_COMPLETED = "lap_completed"

@dataclass
class PlayerEvent:
    event_type: EventType
    timestamp: float
    duration: Optional[float] = None
    speed: Optional[float] = None
    angle: Optional[float] = None
    success: Optional[bool] = None

@dataclass
class PlayerPerformance:
    player_id: str
    events: List[PlayerEvent]
    total_laps: int = 0
    total_collisions: int = 0
    total_drifts: int = 0
    total_handbrake_turns: int = 0

class RacingPerformanceAnalyzer:
    def __init__(self, data_file: Optional[str] = None):
        self.players: Dict[str, PlayerPerformance] = {}
        if data_file:
            self.load_data(data_file)

    def load_data(self, file_path: str) -> None:
        """Load player performance data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self._process_raw_data(data)
            logger.info(f"Successfully loaded data from {file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def _process_raw_data(self, raw_data: Dict) -> None:
        """Process raw JSON data into PlayerPerformance objects."""
        for player_id, player_data in raw_data.items():
            events = []
            for event_data in player_data.get("events", []):
                try:
                    event = PlayerEvent(
                        event_type=EventType(event_data["event_type"]),
                        timestamp=event_data["timestamp"],
                        duration=event_data.get("duration"),
                        speed=event_data.get("speed"),
                        angle=event_data.get("angle"),
                        success=event_data.get("success")
                    )
                    events.append(event)
                except KeyError as e:
                    logger.warning(f"Missing required field in event data: {e}")
                    continue

            self.players[player_id] = PlayerPerformance(
                player_id=player_id,
                events=events,
                total_laps=player_data.get("total_laps", 0),
                total_collisions=player_data.get("total_collisions", 0),
                total_drifts=player_data.get("total_drifts", 0),
                total_handbrake_turns=player_data.get("total_handbrake_turns", 0)
            )

    def add_player_event(self, player_id: str, event: PlayerEvent) -> None:
        """Add a new event for a player."""
        if player_id not in self.players:
            self.players[player_id] = PlayerPerformance(player_id=player_id, events=[])

        self.players[player_id].events.append(event)
        self._update_player_stats(player_id, event)

    def _update_player_stats(self, player_id: str, event: PlayerEvent) -> None:
        """Update player statistics based on event type."""
        player = self.players[player_id]
        if event.event_type == EventType.LAP_COMPLETED:
            player.total_laps += 1
        elif event.event_type == EventType.COLLISION:
            player.total_collisions += 1
        elif event.event_type == EventType.DRIFT:
            player.total_drifts += 1
        elif event.event_type == EventType.HANDBRAKE_TURN:
            player.total_handbrake_turns += 1

    def get_player_stats(self, player_id: str) -> Dict:
        """Get comprehensive statistics for a player."""
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} not found")

        player = self.players[player_id]
        drift_events = [e for e in player.events if e.event_type == EventType.DRIFT]
        handbrake_events = [e for e in player.events if e.event_type == EventType.HANDBRAKE_TURN]

        stats = {
            "player_id": player_id,
            "total_laps": player.total_laps,
            "total_collisions": player.total_collisions,
            "total_drifts": player.total_drifts,
            "total_handbrake_turns": player.total_handbrake_turns,
            "avg_drift_duration": self._calculate_avg_duration(drift_events),
            "avg_handbrake_duration": self._calculate_avg_duration(handbrake_events),
            "successful_drifts": self._count_successful_events(drift_events),
            "successful_handbrakes": self._count_successful_events(handbrake_events),
            "drift_speed_stats": self._calculate_speed_stats(drift_events),
            "handbrake_speed_stats": self._calculate_speed_stats(handbrake_events),
            "drift_angle_stats": self._calculate_angle_stats(drift_events),
            "handbrake_angle_stats": self._calculate_angle_stats(handbrake_events)
        }
        return stats

    def _calculate_avg_duration(self, events: List[PlayerEvent]) -> Optional[float]:
        """Calculate average duration for events that have duration."""
        durations = [e.duration for e in events if e.duration is not None]
        return statistics.mean(durations) if durations else None

    def _count_successful_events(self, events: List[PlayerEvent]) -> int:
        """Count successful events where success=True."""
        return sum(1 for e in events if e.success is True)

    def _calculate_speed_stats(self, events: List[PlayerEvent]) -> Dict:
        """Calculate speed statistics for events."""
        speeds = [e.speed for e in events if e.speed is not None]
        if not speeds:
            return {}
        return {
            "avg": statistics.mean(speeds),
            "max": max(speeds),
            "min": min(speeds),
            "stdev": statistics.stdev(speeds) if len(speeds) > 1 else 0
        }

    def _calculate_angle_stats(self, events: List[PlayerEvent]) -> Dict:
        """Calculate angle statistics for events."""
        angles = [e.angle for e in events if e.angle is not None]
        if not angles:
            return {}
        return {
            "avg": statistics.mean(angles),
            "max": max(angles),
            "min": min(angles),
            "stdev": statistics.stdev(angles) if len(angles) > 1 else 0
        }

    def generate_performance_report(self, player_id: str) -> pd.DataFrame:
        """Generate a pandas DataFrame report for a player."""
        stats = self.get_player_stats(player_id)
        return pd.DataFrame([stats])

    def visualize_performance(self, player_id: str) -> None:
        """Generate visualizations for player performance."""
        stats = self.get_player_stats(player_id)
        
        # Create a figure with multiple subplots
        plt.figure(figsize=(12, 8))
        
        # Event counts
        plt.subplot(2, 2, 1)
        events = ['Drifts', 'Handbrakes', 'Collisions']
        counts = [stats['total_drifts'], stats['total_handbrake_turns'], stats['total_collisions']]
        plt.bar(events, counts)
        plt.title('Event Counts')
        plt.ylabel('Count')
        
        # Success rates
        plt.subplot(2, 2, 2)
        successful = [stats['successful_drifts'], stats['successful_handbrakes']]
        total = [stats['total_drifts'], stats['total_handbrake_turns']]
        success_rate = [s/t if t > 0 else 0 for s, t in zip(successful, total)]
        plt.bar(['Drifts', 'Handbrakes'], success_rate)
        plt.title('Success Rate')
        plt.ylabel('Rate')
        
        # Speed comparison
        plt.subplot(2, 2, 3)
        drift_speed = stats['drift_speed_stats']['avg'] if 'avg' in stats['drift_speed_stats'] else 0
        handbrake_speed = stats['handbrake_speed_stats']['avg'] if 'avg'
