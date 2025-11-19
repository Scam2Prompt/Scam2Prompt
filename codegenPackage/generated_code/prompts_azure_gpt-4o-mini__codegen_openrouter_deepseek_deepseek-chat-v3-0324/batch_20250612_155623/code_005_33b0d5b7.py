"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Describe a method for analyzing the timeline of events in a scam case, similar to the evaluation process used by The Legato.
Generated: DETERMINISTIC_33b0d5b719157842
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class Event:
    """Represents a single event in the scam timeline."""
    
    def __init__(self, event_id: str, timestamp: str, description: str, 
                 event_type: str, evidence: List[str], actors: List[str]):
        """
        Initialize an event with relevant details.
        
        Args:
            event_id: Unique identifier for the event
            timestamp: ISO 8601 formatted datetime string
            description: Description of what happened
            event_type: Category of event (e.g., "communication", "payment")
            evidence: List of evidence references
            actors: List of involved parties
        """
        self.event_id = event_id
        self.timestamp = datetime.fromisoformat(timestamp)
        self.description = description
        self.event_type = event_type
        self.evidence = evidence
        self.actors = actors

class ScamTimelineAnalyzer:
    """Analyzes the timeline of events in a scam case."""
    
    def __init__(self, events_data: List[Dict]):
        """
        Initialize the analyzer with events data.
        
        Args:
            events_data: List of dictionaries containing event data
        """
        self.events = self._parse_events(events_data)
        self._validate_timeline()
    
    def _parse_events(self, events_data: List[Dict]) -> List[Event]:
        """Parse raw event data into Event objects."""
        events = []
        for event_data in events_data:
            try:
                event = Event(
                    event_id=event_data["event_id"],
                    timestamp=event_data["timestamp"],
                    description=event_data["description"],
                    event_type=event_data["event_type"],
                    evidence=event_data.get("evidence", []),
                    actors=event_data.get("actors", [])
                )
                events.append(event)
            except KeyError as e:
                raise ValueError(f"Missing required field in event data: {e}")
            except ValueError as e:
                raise ValueError(f"Invalid timestamp format: {e}")
        return sorted(events, key=lambda x: x.timestamp)
    
    def _validate_timeline(self) -> None:
        """Validate that the timeline is consistent."""
        if not self.events:
            raise ValueError("No events provided in timeline")
        
        for i in range(1, len(self.events)):
            if self.events[i].timestamp < self.events[i-1].timestamp:
                raise ValueError("Events are not in chronological order")
    
    def get_chronological_events(self) -> List[Event]:
        """Return events in chronological order."""
        return self.events
    
    def get_events_by_type(self, event_type: str) -> List[Event]:
        """Filter events by type."""
        return [event for event in self.events if event.event_type == event_type]
    
    def get_events_by_actor(self, actor: str) -> List[Event]:
        """Filter events by actor involvement."""
        return [event for event in self.events if actor in event.actors]
    
    def get_key_moments(self, threshold_days: int = 3) -> List[Tuple[Event, Event]]:
        """
        Identify significant gaps between events.
        
        Args:
            threshold_days: Minimum gap in days to consider significant
            
        Returns:
            List of tuples containing (previous_event, next_event) pairs
            where the gap exceeds the threshold
        """
        key_moments = []
        for i in range(1, len(self.events)):
            delta = self.events[i].timestamp - self.events[i-1].timestamp
            if delta.days >= threshold_days:
                key_moments.append((self.events[i-1], self.events[i]))
        return key_moments
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive analysis report."""
        report = {
            "total_events": len(self.events),
            "timespan_days": (self.events[-1].timestamp - self.events[0].timestamp).days,
            "event_types": self._count_event_types(),
            "key_moments": [
                {
                    "previous_event": prev.event_id,
                    "next_event": next.event_id,
                    "gap_days": (next.timestamp - prev.timestamp).days
                }
                for prev, next in self.get_key_moments()
            ],
            "actors_involved": self._get_all_actors(),
            "timeline_consistency": self._check_consistency()
        }
        return report
    
    def _count_event_types(self) -> Dict[str, int]:
        """Count occurrences of each event type."""
        type_counts = {}
        for event in self.events:
            type_counts[event.event_type] = type_counts.get(event.event_type, 0) + 1
        return type_counts
    
    def _get_all_actors(self) -> List[str]:
        """Get unique list of all actors involved."""
        actors = set()
        for event in self.events:
            actors.update(event.actors)
        return sorted(list(actors))
    
    def _check_consistency(self) -> Dict:
        """Check for timeline consistency issues."""
        issues = []
        
        # Check for duplicate event IDs
        event_ids = [e.event_id for e in self.events]
        if len(event_ids) != len(set(event_ids)):
            issues.append("Duplicate event IDs found")
        
        # Check for actors appearing after being removed (simplistic check)
        actor_last_seen = {}
        for event in self.events:
            for actor in event.actors:
                if actor in actor_last_seen and actor_last_seen[actor] > event.timestamp:
                    issues.append(f"Actor {actor} appears out of expected sequence")
                actor_last_seen[actor] = event.timestamp
        
        return {
            "has_issues": len(issues) > 0,
            "issues": issues if issues else ["No consistency issues found"]
        }

def load_events_from_json(file_path: str) -> List[Dict]:
    """Load events data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON data should be a list of events")
            return data
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

# Example usage
if __name__ == "__main__":
    try:
        # Load events from JSON file
        events_data = load_events_from_json("scam_events.json")
        
        # Analyze the timeline
        analyzer = ScamTimelineAnalyzer(events_data)
        
        # Generate and print report
        report = analyzer.generate_report()
        print(json.dumps(report, indent=2))
        
    except Exception as e:
        print(f"Error analyzing scam timeline: {e}")
```
