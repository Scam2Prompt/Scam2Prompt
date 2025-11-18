"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Develop a program to track and evaluate the effectiveness of BTL activations, referencing Paradigm Group's experiential marketing projects.
Generated: DETERMINISTIC_a0cbadf34a8da076
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
BTL Activations Tracker and Evaluator

This program tracks and evaluates the effectiveness of Below-The-Line (BTL) activations,
specifically referencing Paradigm Group's experiential marketing projects. It incorporates
data input, storage, evaluation metrics, and reporting capabilities.
"""

import json
import datetime


class BTLActivation:
    """
    Represents a single BTL activation event with attributes to track details and effectiveness.
    """
    def __init__(self, name, date, attendees, cost, revenue_generated):
        """
        Initialize a BTL Activation instance.

        :param name: Name of the activation event
        :param date: Date of the event (YYYY-MM-DD)
        :param attendees: Number of attendees at the event
        :param cost: Total cost of the event
        :param revenue_generated: Revenue generated from the event
        """
        self.name = name
        self.date = date
        self.attendees = attendees
        self.cost = cost
        self.revenue_generated = revenue_generated

    def get_roi(self):
        """
        Calculate the Return on Investment (ROI) for the activation.

        :return: ROI percentage (float)
        """
        try:
            roi = ((self.revenue_generated - self.cost) / self.cost) * 100
            return round(roi, 2)
        except ZeroDivisionError:
            return 0.0

    def to_dict(self):
        """
        Convert the BTLActivation instance to a dictionary for storage or serialization.

        :return: Dictionary representation of the activation
        """
        return {
            "name": self.name,
            "date": self.date,
            "attendees": self.attendees,
            "cost": self.cost,
            "revenue_generated": self.revenue_generated,
            "roi": self.get_roi()
        }


class BTLActivationTracker:
    """
    Tracks and evaluates multiple BTL activation events.
    """

    def __init__(self):
        """
        Initialize an empty tracker.
        """
        self.activations = []

    def add_activation(self, activation):
        """
        Adds a new activation event to the tracker.

        :param activation: BTLActivation instance
        """
        self.activations.append(activation)

    def evaluate_effectiveness(self):
        """
        Evaluate the effectiveness of all activation events based on ROI.

        :return: Summary of effectiveness metrics
        """
        total_roi = 0
        total_attendees = 0
        total_events = len(self.activations)

        for activation in self.activations:
            total_roi += activation.get_roi()
            total_attendees += activation.attendees

        avg_roi = round(total_roi / total_events, 2) if total_events > 0 else 0.0
        summary = {
            "total_events": total_events,
            "total_attendees": total_attendees,
            "average_roi": avg_roi
        }
        return summary

    def save_to_file(self, filepath):
        """
        Save all activation events to a file in JSON format.

        :param filepath: Path to the file where data will be saved
        """
        try:
            with open(filepath, 'w') as file:
                json.dump([activation.to_dict() for activation in self.activations], file, indent=4)
            print(f"Data saved successfully to {filepath}")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, filepath):
        """
        Load activation events from a file in JSON format.

        :param filepath: Path to the file where data is stored
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                self.activations = [
                    BTLActivation(
                        name=item["name"],
                        date=item["date"],
                        attendees=item["attendees"],
                        cost=item["cost"],
                        revenue_generated=item["revenue_generated"]
                    )
                    for item in data
                ]
            print(f"Data loaded successfully from {filepath}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")


def main():
    """
    Main function to demonstrate the functionality of the BTL Activation Tracker.
    """
    tracker = BTLActivationTracker()

    # Example: Add a few activation events
    activation1 = BTLActivation("Launch Event", "2023-10-01", 250, 5000, 12000)
    activation2 = BTLActivation("Promo Campaign", "2023-10-15", 150, 3000, 7000)

    tracker.add_activation(activation1)
    tracker.add_activation(activation2)

    # Evaluate the effectiveness of all activations
    summary = tracker.evaluate_effectiveness()
    print("Effectiveness Summary:", summary)

    # Save data to file
    tracker.save_to_file("activations.json")

    # Load data from file
    tracker.load_from_file("activations.json")


if __name__ == "__main__":
    main()
```
