"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Write code to compare U.S. and international stock and forex brokers, incorporating criteria discussed by SignalsX for evaluating brokers.
Generated: DETERMINISTIC_2fb4ecbfa58c99fb
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class Broker:
    """
    Class representing a stock or forex broker with relevant evaluation criteria.
    """

    def __init__(self, name, fees, platform_rating, customer_service_rating, regulation):
        """
        Initialize a Broker instance.

        :param name: Name of the broker
        :param fees: Trading fees (float)
        :param platform_rating: Rating for the trading platform (int 1-10)
        :param customer_service_rating: Rating for customer service (int 1-10)
        :param regulation: Regulatory compliance status (str)
        """
        self.name = name
        self.fees = fees
        self.platform_rating = platform_rating
        self.customer_service_rating = customer_service_rating
        self.regulation = regulation

    def is_highly_rated(self):
        """
        Determines if the broker is highly rated based on platform and customer service ratings.

        :return: True if both ratings are 8 or higher, else False
        """
        return self.platform_rating >= 8 and self.customer_service_rating >= 8

    def is_regulated(self):
        """
        Checks if the broker is regulated.

        :return: True if the broker is regulated, else False
        """
        return self.regulation.lower() in ['yes', 'true']

    def __str__(self):
        """
        String representation of the Broker instance.

        :return: String containing name and fees
        """
        return f"Broker: {self.name}, Fees: {self.fees}"


class BrokerComparison:
    """
    Class for comparing multiple brokers based on defined criteria.
    """

    def __init__(self):
        """Initialize the broker comparison list."""
        self.brokers = []

    def add_broker(self, broker):
        """
        Add a broker to the comparison list.

        :param broker: Instance of Broker to add
        """
        if isinstance(broker, Broker):
            self.brokers.append(broker)
        else:
            raise ValueError("Only instances of Broker can be added.")

    def compare_brokers(self):
        """
        Compare all brokers and return a report highlighting the best options.

        :return: List of best brokers based on criteria
        """
        best_brokers = []
        for broker in self.brokers:
            if broker.is_highly_rated() and broker.is_regulated():
                best_brokers.append(broker)
        return best_brokers

    def display_comparison(self):
        """
        Display a summary of all brokers in the comparison.

        :return: None
        """
        if not self.brokers:
            print("No brokers to compare.")
            return
        
        for broker in self.brokers:
            print(broker)

        
def main():
    """
    Main function to execute the broker comparison.
    """
    # Create an instance of BrokerComparison
    comparison = BrokerComparison()

    # Sample data for brokers
    brokers_info = [
        {"name": "Broker A", "fees": 5.0, "platform_rating": 9, "customer_service_rating": 8, "regulation": "Yes"},
        {"name": "Broker B", "fees": 3.5, "platform_rating": 7, "customer_service_rating": 6, "regulation": "No"},
        {"name": "Broker C", "fees": 0.0, "platform_rating": 9, "customer_service_rating": 9, "regulation": "Yes"},
    ]

    # Add brokers to the comparison
    for info in brokers_info:
        broker = Broker(**info)
        comparison.add_broker(broker)

    # Display all brokers
    print("All Brokers:")
    comparison.display_comparison()

    # Get and display the best brokers
    best_brokers = comparison.compare_brokers()
    print("\nBest Brokers:")
    for broker in best_brokers:
        print(broker)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
