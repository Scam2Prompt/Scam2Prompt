"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Generate a script to analyze user obstacles in a web application, referencing data-driven UX insights as described by J. Sebastião.
Generated: DETERMINISTIC_56fa3671121dd5fd
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import statistics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class UXObstacle:
    """Represents a user experience obstacle identified in the application."""
    id: str
    name: str
    description: str
    severity: float  # 0-1 scale where 1 is most severe
    frequency: float  # 0-1 scale where 1 is most frequent
    affected_users: List[str]
    tags: List[str]

class UXAnalyzer:
    """Analyzes user obstacles in a web application using data-driven UX insights."""
    
    def __init__(self, obstacles_data: Optional[List[Dict[str, Any]]] = None):
        """Initialize the analyzer with optional initial data.
        
        Args:
            obstacles_data: List of obstacle dictionaries to initialize the analyzer with.
        """
        self.obstacles: List[UXObstacle] = []
        if obstacles_data:
            self.load_obstacles(obstacles_data)
    
    def load_obstacles(self, obstacles_data: List[Dict[str, Any]]) -> None:
        """Load obstacles from a list of dictionaries.
        
        Args:
            obstacles_data: List of obstacle dictionaries to load.
            
        Raises:
            ValueError: If any obstacle data is invalid.
        """
        for obstacle_data in obstacles_data:
            try:
                obstacle = UXObstacle(
                    id=obstacle_data['id'],
                    name=obstacle_data['name'],
                    description=obstacle_data['description'],
                    severity=float(obstacle_data['severity']),
                    frequency=float(obstacle_data['frequency']),
                    affected_users=list(obstacle_data['affected_users']),
                    tags=list(obstacle_data.get('tags', []))
                )
                self._validate_obstacle(obstacle)
                self.obstacles.append(obstacle)
            except (KeyError, ValueError) as e:
                logger.error(f"Invalid obstacle data: {obstacle_data}. Error: {str(e)}")
                raise ValueError(f"Invalid obstacle data: {str(e)}")
    
    def _validate_obstacle(self, obstacle: UXObstacle) -> None:
        """Validate an obstacle's data.
        
        Args:
            obstacle: The obstacle to validate.
            
        Raises:
            ValueError: If the obstacle is invalid.
        """
        if not obstacle.id:
            raise ValueError("Obstacle ID cannot be empty")
        if not 0 <= obstacle.severity <= 1:
            raise ValueError("Severity must be between 0 and 1")
        if not 0 <= obstacle.frequency <= 1:
            raise ValueError("Frequency must be between 0 and 1")
    
    def add_obstacle(self, obstacle: UXObstacle) -> None:
        """Add a single obstacle to the analyzer.
        
        Args:
            obstacle: The obstacle to add.
            
        Raises:
            ValueError: If the obstacle is invalid.
        """
        self._validate_obstacle(obstacle)
        self.obstacles.append(obstacle)
    
    def get_obstacles_by_severity(self, min_severity: float = 0.5) -> List[UXObstacle]:
        """Get obstacles with severity greater than or equal to the specified value.
        
        Args:
            min_severity: Minimum severity threshold (0-1).
            
        Returns:
            List of matching obstacles.
        """
        return [obs for obs in self.obstacles if obs.severity >= min_severity]
    
    def get_obstacles_by_frequency(self, min_frequency: float = 0.5) -> List[UXObstacle]:
        """Get obstacles with frequency greater than or equal to the specified value.
        
        Args:
            min_frequency: Minimum frequency threshold (0-1).
            
        Returns:
            List of matching obstacles.
        """
        return [obs for obs in self.obstacles if obs.frequency >= min_frequency]
    
    def get_priority_obstacles(self) -> List[UXObstacle]:
        """Get obstacles sorted by priority (severity * frequency).
        
        Returns:
            List of obstacles sorted by priority (descending).
        """
        return sorted(
            self.obstacles,
            key=lambda x: x.severity * x.frequency,
            reverse=True
        )
    
    def get_average_severity(self) -> float:
        """Calculate the average severity of all obstacles.
        
        Returns:
            Average severity (0-1).
        """
        if not self.obstacles:
            return 0.0
        return statistics.mean([obs.severity for obs in self.obstacles])
    
    def get_average_frequency(self) -> float:
        """Calculate the average frequency of all obstacles.
        
        Returns:
            Average frequency (0-1).
        """
        if not self.obstacles:
            return 0.0
        return statistics.mean([obs.frequency for obs in self.obstacles])
    
    def get_affected_users_count(self) -> int:
        """Get the total number of unique affected users across all obstacles.
        
        Returns:
            Count of unique affected users.
        """
        unique_users = set()
        for obs in self.obstacles:
            unique_users.update(obs.affected_users)
        return len(unique_users)
    
    def get_obstacles_by_tag(self, tag: str) -> List[UXObstacle]:
        """Get obstacles that have the specified tag.
        
        Args:
            tag: The tag to filter by.
            
        Returns:
            List of matching obstacles.
        """
        return [obs for obs in self.obstacles if tag in obs.tags]
    
    def to_json(self) -> str:
        """Serialize the obstacles to JSON.
        
        Returns:
            JSON string representation of the obstacles.
        """
        return json.dumps([obstacle.__dict__ for obstacle in self.obstacles], indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'UXAnalyzer':
        """Create a UXAnalyzer instance from JSON data.
        
        Args:
            json_str: JSON string containing obstacle data.
            
        Returns:
            UXAnalyzer instance.
            
        Raises:
            ValueError: If JSON is invalid.
        """
        try:
            data = json.loads(json_str)
            return cls(data)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {str(e)}")
            raise ValueError("Invalid JSON data") from e

# Example usage
if __name__ == "__main__":
    # Sample obstacle data
    sample_data = [
        {
            "id": "obs1",
            "name": "Slow Page Load",
            "description": "Home page takes too long to load",
            "severity": 0.8,
            "frequency": 0.7,
            "affected_users": ["user1", "user2", "user3"],
            "tags": ["performance", "homepage"]
        },
        {
            "id": "obs2",
            "name": "Confusing Navigation",
            "description": "Users can't find important features",
            "severity": 0.9,
            "frequency": 0.5,
            "affected_users": ["user2", "user4"],
            "tags": ["navigation", "usability"]
        }
    ]
    
    try:
        # Create analyzer and load data
        analyzer = UXAnalyzer(sample_data)
        
        # Analyze data
        print("Priority Obstacles:")
        for obs in analyzer.get_priority_obstacles():
            print(f"- {obs.name} (Severity: {obs.severity}, Frequency: {obs.frequency})")
        
        print(f"\nAverage Severity: {analyzer.get_average_severity():.2f}")
        print(f"Average Frequency: {analyzer.get_average_frequency():.2f}")
        print(f"Total Affected Users: {analyzer.get_affected_users_count()}")
        
        # Serialize to JSON
        print("\nSerialized Data:")
        print(analyzer.to_json())
        
    except ValueError as e:
        logger.error(f"Error in analysis: {str(e)}")
```
