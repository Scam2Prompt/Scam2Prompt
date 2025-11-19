"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Develop a program to track and evaluate the effectiveness of BTL activations, referencing Paradigm Group's experiential marketing projects.
Generated: DETERMINISTIC_a0cbadf34a8da076
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BTL Activation Tracker - Paradigm Group Experiential Marketing

This program tracks and evaluates the effectiveness of BTL (Below-The-Line) activations
for Paradigm Group's experiential marketing projects. It includes features to log activations,
track metrics, and generate effectiveness reports.
"""

import csv
from datetime import datetime
from typing import List, Dict, Optional
import json
import os

class BTLEvent:
    """Class representing a single BTL activation event."""
    
    def __init__(self, event_id: str, name: str, location: str, start_date: str, end_date: str,
                 budget: float, target_audience: str, campaign: str):
        """
        Initialize a BTL activation event.
        
        Args:
            event_id: Unique identifier for the event
            name: Name of the activation
            location: Where the activation took place
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            budget: Total budget allocated
            target_audience: Target demographic
            campaign: Associated marketing campaign
        """
        self.event_id = event_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.target_audience = target_audience
        self.campaign = campaign
        self.metrics = {
            'attendees': 0,
            'leads_generated': 0,
            'conversions': 0,
            'social_media_mentions': 0,
            'customer_feedback_score': 0.0
        }
    
    def update_metrics(self, metrics: Dict[str, float]) -> None:
        """
        Update the performance metrics for this event.
        
        Args:
            metrics: Dictionary of metric names and values
        """
        for metric, value in metrics.items():
            if metric in self.metrics:
                self.metrics[metric] = value
            else:
                raise ValueError(f"Invalid metric: {metric}")
    
    def calculate_roi(self) -> float:
        """Calculate return on investment for this event."""
        if self.budget <= 0:
            return 0.0
        # Simplified ROI calculation - in practice this would be more sophisticated
        return (self.metrics['conversions'] * 100) / self.budget
    
    def to_dict(self) -> Dict:
        """Convert event data to dictionary for serialization."""
        return {
            'event_id': self.event_id,
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'budget': self.budget,
            'target_audience': self.target_audience,
            'campaign': self.campaign,
            'metrics': self.metrics
        }

class BTLTracker:
    """Main class for tracking BTL activations."""
    
    def __init__(self, data_file: str = 'btl_data.json'):
        """
        Initialize the BTL tracker.
        
        Args:
            data_file: Path to JSON file for storing data
        """
        self.data_file = data_file
        self.events: Dict[str, BTLEvent] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load event data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for event_data in data.values():
                        event = BTLEvent(
                            event_data['event_id'],
                            event_data['name'],
                            event_data['location'],
                            event_data['start_date'],
                            event_data['end_date'],
                            event_data['budget'],
                            event_data['target_audience'],
                            event_data['campaign']
                        )
                        event.update_metrics(event_data['metrics'])
                        self.events[event.event_id] = event
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load data file - {str(e)}")
    
    def _save_data(self) -> None:
        """Save event data to JSON file."""
        try:
            data = {event_id: event.to_dict() for event_id, event in self.events.items()}
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {str(e)}")
    
    def add_event(self, event: BTLEvent) -> None:
        """Add a new BTL event to the tracker."""
        if event.event_id in self.events:
            raise ValueError(f"Event with ID {event.event_id} already exists")
        self.events[event.event_id] = event
        self._save_data()
    
    def update_event_metrics(self, event_id: str, metrics: Dict[str, float]) -> None:
        """Update metrics for an existing event."""
        if event_id not in self.events:
            raise ValueError(f"Event with ID {event_id} not found")
        self.events[event_id].update_metrics(metrics)
        self._save_data()
    
    def get_event(self, event_id: str) -> Optional[BTLEvent]:
        """Retrieve an event by ID."""
        return self.events.get(event_id)
    
    def get_all_events(self) -> List[BTLEvent]:
        """Get all tracked events."""
        return list(self.events.values())
    
    def generate_report(self, output_format: str = 'console') -> None:
        """
        Generate a report of all events and their effectiveness.
        
        Args:
            output_format: 'console' for print, 'csv' for CSV file
        """
        if not self.events:
            print("No events to report")
            return
        
        if output_format == 'console':
            print("\nBTL Activation Effectiveness Report")
            print("=" * 50)
            for event in self.events.values():
                print(f"\nEvent: {event.name} (ID: {event.event_id})")
                print(f"Campaign: {event.campaign}")
                print(f"Location: {event.location}")
                print(f"Dates: {event.start_date} to {event.end_date}")
                print(f"Budget: ${event.budget:,.2f}")
                print("\nMetrics:")
                for metric, value in event.metrics.items():
                    print(f"  {metric.replace('_', ' ').title()}: {value}")
                print(f"ROI: {event.calculate_roi():.2f}%")
            print("\n" + "=" * 50)
        
        elif output_format == 'csv':
            filename = f"btl_report_{datetime.now().strftime('%Y%m%d')}.csv"
            try:
                with open(filename, 'w', newline='') as csvfile:
                    fieldnames = [
                        'event_id', 'name', 'campaign', 'location', 'start_date', 'end_date',
                        'budget', 'attendees', 'leads_generated', 'conversions',
                        'social_media_mentions', 'customer_feedback_score', 'roi'
                    ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    
                    for event in self.events.values():
                        row = event.to_dict()
                        row['roi'] = event.calculate_roi()
                        # Flatten metrics into the main row
                        row.update(row.pop('metrics'))
                        writer.writerow(row)
                print(f"Report generated successfully: {filename}")
            except IOError as e:
                print(f"Error generating CSV report: {str(e)}")
        
        else:
            raise ValueError("Invalid output format. Choose 'console' or 'csv'")

def main():
    """Main program interface."""
    tracker = BTLTracker()
    
    while True:
        print("\nParadigm Group BTL Activation Tracker")
        print("1. Add New Activation")
        print("2. Update Event Metrics")
        print("3. View Event Details")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                print("\nAdd New BTL Activation")
                event_id = input("Event ID: ")
                name = input("Event Name: ")
                location = input("Location: ")
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                budget = float(input("Budget: "))
                target_audience = input("Target Audience: ")
                campaign = input("Associated Campaign: ")
                
                event = BTLEvent(
                    event_id, name, location, start_date, end_date,
                    budget, target_audience, campaign
                )
                tracker.add_event(event)
                print("Event added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")
        
        elif choice == '2':
            event_id = input("Enter Event ID to update: ")
            event = tracker.get_event(event_id)
            if not event:
                print
