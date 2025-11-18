"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Generate Python code for tracking the first 50,000 investors in a cryptocurrency project, as described in the Aye Aye Coin presale phase.
Generated: DETERMINISTIC_f353397f33487a1d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

class InvestorTracker:
    """
    Class to track the first 50,000 investors in a cryptocurrency presale project.
    """

    def __init__(self, max_investors=50000):
        """
        Initializes the InvestorTracker instance.
        
        :param max_investors: Maximum number of investors to track. Default is 50,000.
        """
        self.max_investors = max_investors
        self.investors = {}  # Dictionary to store investor data by ID

    def add_investor(self, investor_id, name, email, amount_invested):
        """
        Adds a new investor to the tracker.
        
        :param investor_id: Unique ID for the investor.
        :param name: Name of the investor.
        :param email: Email address of the investor.
        :param amount_invested: Amount the investor has invested.
        :raises ValueError: If the maximum number of investors is reached.
        :raises ValueError: If the investor ID is already in use.
        """
        if len(self.investors) >= self.max_investors:
            raise ValueError("Maximum number of investors reached. Cannot add more investors.")
        
        if investor_id in self.investors:
            raise ValueError(f"Investor ID '{investor_id}' is already in use.")
        
        self.investors[investor_id] = {
            'name': name,
            'email': email,
            'amount_invested': amount_invested
        }

    def remove_investor(self, investor_id):
        """
        Removes an investor from the tracker.
        
        :param investor_id: Unique ID of the investor to remove.
        :raises KeyError: If the investor ID does not exist.
        """
        if investor_id not in self.investors:
            raise KeyError(f"Investor ID '{investor_id}' not found.")
        
        del self.investors[investor_id]

    def export_to_csv(self, filename):
        """
        Exports the investor data to a CSV file.
        
        :param filename: Name of the CSV file to export to.
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Investor ID', 'Name', 'Email', 'Amount Invested'])  # Header row
                
                for investor_id, data in self.investors.items():
                    writer.writerow([investor_id, data['name'], data['email'], data['amount_invested']])
                
            print(f"Investor data successfully exported to '{filename}'.")
        except Exception as e:
            print(f"Failed to export investor data: {e}")

    def get_investor(self, investor_id):
        """
        Retrieves an investor's details by their unique ID.
        
        :param investor_id: Unique ID of the investor.
        :return: A dictionary containing the investor's details.
        :raises KeyError: If the investor ID does not exist.
        """
        if investor_id not in self.investors:
            raise KeyError(f"Investor ID '{investor_id}' not found.")
        
        return self.investors[investor_id]

# Example usage
if __name__ == "__main__":
    tracker = InvestorTracker()

    try:
        # Adding investors
        tracker.add_investor(1, "Alice", "alice@example.com", 500.0)
        tracker.add_investor(2, "Bob", "bob@example.com", 1000.0)
        
        # Retrieve investor data
        alice_data = tracker.get_investor(1)
        print("Alice's Data:", alice_data)

        # Export data to CSV
        tracker.export_to_csv("investors.csv")
        
        # Remove an investor
        tracker.remove_investor(1)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
