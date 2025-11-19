"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Describe a method for analyzing the timeline of events in a scam case, similar to the evaluation process used by The Legato.
Generated: DETERMINISTIC_33b0d5b719157842
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json


class ScamTimelineAnalyzer:
    """
    A class to analyze the timeline of events in a scam case.
    """

    def __init__(self):
        """
        Initializes the ScamTimelineAnalyzer with an empty list of events.
        """
        self.events = []

    def add_event(self, event_name: str, event_time: str):
        """
        Adds an event to the timeline.
        
        :param event_name: Name of the event (e.g., "Victim contacted").
        :param event_time: Timestamp of the event (ISO 8601 format, e.g., "2023-10-01T14:30:00").
        :raises ValueError: If the event_time is not a valid ISO 8601 timestamp.
        """
        try:
            # Parse the timestamp to ensure it's valid
            parsed_time = datetime.datetime.fromisoformat(event_time)
            self.events.append({"name": event_name, "time": parsed_time})
        except ValueError as e:
            raise ValueError(f"Invalid timestamp format: {event_time}. Must be ISO 8601.") from e

    def analyze_timeline(self):
        """
        Analyzes the timeline of events.
        
        :return: A dictionary summarizing the timeline (earliest event, latest event, duration).
        """
        if not self.events:
            return {"message": "No events to analyze."}

        # Sort events by time
        sorted_events = sorted(self.events, key=lambda x: x["time"])
        
        # Extract start and end times
        earliest_event = sorted_events[0]
        latest_event = sorted_events[-1]
        
        # Calculate duration
        duration = latest_event["time"] - earliest_event["time"]
        
        return {
            "earliest_event": {
                "name": earliest_event["name"],
                "time": earliest_event["time"].isoformat(),
            },
            "latest_event": {
                "name": latest_event["name"],
                "time": latest_event["time"].isoformat(),
            },
            "duration": str(duration),
        }

    def export_timeline(self, file_path: str):
        """
        Exports the timeline to a JSON file.
        
        :param file_path: Path to the file where the timeline will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            # Convert events to a serializable format
            export_data = [
                {"name": event["name"], "time": event["time"].isoformat()}
                for event in self.events
            ]
            with open(file_path, "w") as file:
                json.dump(export_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {file_path}.") from e


# Example usage
if __name__ == "__main__":
    analyzer = ScamTimelineAnalyzer()

    # Adding events to the timeline
    try:
        analyzer.add_event("Victim contacted", "2023-10-01T14:30:00")
        analyzer.add_event("Scammer requested payment", "2023-10-01T15:00:00")
        analyzer.add_event("Payment sent", "2023-10-01T15:30:00")
    except ValueError as ve:
        print(f"Error adding event: {ve}")

    # Analyze the timeline
    timeline_summary = analyzer.analyze_timeline()
    print("Timeline Analysis:", timeline_summary)

    # Export the timeline to a JSON file
    try:
        analyzer.export_timeline("scam_timeline.json")
        print("Timeline successfully exported to scam_timeline.json")
    except IOError as ioe:
        print(f"Error exporting timeline: {ioe}")
```
