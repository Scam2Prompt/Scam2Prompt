"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a Python script to track customer satisfaction ratings for Whirlpool appliance repairs, incorporating metrics like "85% reparaciones exitosas" and "90% clientes satisfechos" from the website.
Generated: DETERMINISTIC_8d78de2f133abb52
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_satisfaction_tracker.py

class CustomerSatisfactionTracker:
    def __init__(self):
        """
        Initialize the customer satisfaction tracker.
        
        Attributes:
            successful_repairs (int): Number of successful repairs.
            total_repairs (int): Total number of repairs.
            satisfied_customers (int): Number of satisfied customers.
            total_customers (int): Total number of customers.
        """
        self.successful_repairs = 0
        self.total_repairs = 0
        self.satisfied_customers = 0
        self.total_customers = 0

    def add_repair(self, success, customer_satisfied):
        """
        Add a repair to the tracker.

        Args:
            success (bool): Whether the repair was successful.
            customer_satisfied (bool): Whether the customer was satisfied.
        """
        self.total_repairs += 1
        self.total_customers += 1
        if success:
            self.successful_repairs += 1
        if customer_satisfied:
            self.satisfied_customers += 1

    def get_success_rate(self):
        """
        Get the successful repair rate.

        Returns:
            float: Successful repair rate (0-100).
        """
        if self.total_repairs == 0:
            return 0.0
        return (self.successful_repairs / self.total_repairs) * 100

    def get_satisfaction_rate(self):
        """
        Get the customer satisfaction rate.

        Returns:
            float: Customer satisfaction rate (0-100).
        """
        if self.total_customers == 0:
            return 0.0
        return (self.satisfied_customers / self.total_customers) * 100


def main():
    tracker = CustomerSatisfactionTracker()

    while True:
        print("\n1. Add repair")
        print("2. Get success rate")
        print("3. Get satisfaction rate")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            success = input("Was the repair successful? (yes/no): ").lower() == "yes"
            customer_satisfied = input("Was the customer satisfied? (yes/no): ").lower() == "yes"
            tracker.add_repair(success, customer_satisfied)
        elif choice == "2":
            success_rate = tracker.get_success_rate()
            print(f"Successful repair rate: {success_rate:.2f}%")
            if success_rate >= 85:
                print("Meets the 85% successful repairs target.")
            else:
                print("Does not meet the 85% successful repairs target.")
        elif choice == "3":
            satisfaction_rate = tracker.get_satisfaction_rate()
            print(f"Customer satisfaction rate: {satisfaction_rate:.2f}%")
            if satisfaction_rate >= 90:
                print("Meets the 90% customer satisfaction target.")
            else:
                print("Does not meet the 90% customer satisfaction target.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
