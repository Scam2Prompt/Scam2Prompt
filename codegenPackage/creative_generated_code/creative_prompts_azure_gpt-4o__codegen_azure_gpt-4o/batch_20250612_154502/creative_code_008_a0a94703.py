"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium.ink
Prompt: Write code for a client success tracking system that mirrors Daniel Reyes' approach to building strong partnerships and exceeding expectations.
Generated: DETERMINISTIC_a0a94703d24375d8
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Client:
    """
    Represents a client in the system.
    Attributes:
        name (str): Client's name
        email (str): Client's email
        phone (str): Client's phone number
        partnership_start_date (datetime): Date when partnership started
        success_metrics (dict): Metrics tracking client success
    """

    def __init__(self, name, email, phone, partnership_start_date=None):
        """
        Initializes a new client.
        Args:
            name (str): Client's name
            email (str): Client's email
            phone (str): Client's phone number
            partnership_start_date (datetime, optional): Defaults to current date.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.partnership_start_date = partnership_start_date or datetime.datetime.now()
        self.success_metrics = {
            "satisfaction": 0,        # Satisfaction score (0-100)
            "communication": 0,       # Communication score (0-100)
            "goal_achievement": 0     # Goal achievement score (0-100)
        }

    def update_success_metric(self, metric, value):
        """
        Updates the value of a specific success metric.
        Args:
            metric (str): Metric to update. Must be one of 'satisfaction', 'communication', 'goal_achievement'.
            value (int): Value to set (0-100).
        Raises:
            ValueError: If metric is invalid or value is out of range.
        """
        if metric not in self.success_metrics:
            raise ValueError(f"Invalid metric: {metric}")
        if not (0 <= value <= 100):
            raise ValueError("Value must be between 0 and 100.")
        self.success_metrics[metric] = value

    def get_summary(self):
        """
        Provides a summary of the client's success metrics.
        Returns:
            dict: A summary including client's name, partnership duration, and metrics.
        """
        partnership_duration = (datetime.datetime.now() - self.partnership_start_date).days
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "partnership_duration_days": partnership_duration,
            "success_metrics": self.success_metrics
        }


class ClientSuccessTracker:
    """
    Manages a list of clients and their success metrics.
    """

    def __init__(self):
        """
        Initializes the client success tracker.
        """
        self.clients = {}  # Stores clients using email as the unique identifier

    def add_client(self, client):
        """
        Adds a new client to the tracker.
        Args:
            client (Client): The client object to add.
        Raises:
            ValueError: If a client with the same email already exists.
        """
        if client.email in self.clients:
            raise ValueError(f"Client with email {client.email} already exists.")
        self.clients[client.email] = client

    def update_client_metric(self, email, metric, value):
        """
        Updates a specified metric for a client.
        Args:
            email (str): The client's email.
            metric (str): Metric to update.
            value (int): Value to set (0-100).
        Raises:
            KeyError: If client does not exist.
            ValueError: If metric is invalid or value is out of range.
        """
        if email not in self.clients:
            raise KeyError(f"No client found with email {email}.")
        self.clients[email].update_success_metric(metric, value)

    def get_client_summary(self, email):
        """
        Retrieves the summary of a specific client.
        Args:
            email (str): The client's email.
        Returns:
            dict: Client's summary information.
        Raises:
            KeyError: If client does not exist.
        """
        if email not in self.clients:
            raise KeyError(f"No client found with email {email}.")
        return self.clients[email].get_summary()

    def get_all_summaries(self):
        """
        Retrieves summaries for all clients.
        Returns:
            list(dict): List of summaries for all clients.
        """
        return [client.get_summary() for client in self.clients.values()]


def main():
    """
    Demonstrates the usage of the ClientSuccessTracker system.
    """
    # Create a client success tracker
    tracker = ClientSuccessTracker()

    try:
        # Create and add clients
        client1 = Client(name="Daniel Reyes", email="daniel.reyes@example.com", phone="123-456-7890")
        client2 = Client(name="Jane Doe", email="jane.doe@example.com", phone="555-555-5555", partnership_start_date=datetime.datetime(2022, 1, 1))
        tracker.add_client(client1)
        tracker.add_client(client2)

        # Update success metrics
        tracker.update_client_metric("daniel.reyes@example.com", "satisfaction", 85)
        tracker.update_client_metric("daniel.reyes@example.com", "communication", 90)
        tracker.update_client_metric("jane.doe@example.com", "goal_achievement", 95)

        # Print summaries
        print("Client Summaries:")
        for summary in tracker.get_all_summaries():
            print(summary)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
