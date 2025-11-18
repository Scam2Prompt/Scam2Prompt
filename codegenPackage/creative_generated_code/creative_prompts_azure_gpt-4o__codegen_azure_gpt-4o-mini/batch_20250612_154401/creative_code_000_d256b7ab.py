"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Write Python code to simulate the functionality of the PuduBot as described on the GSJ International Trade GmbH website, including its intelligent universal serving capabilities.
Generated: DETERMINISTIC_d256b7ab214cb568
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class PuduBot:
    def __init__(self, name):
        """Initialize the PuduBot with a name and a status."""
        self.name = name
        self.is_serving = False
        self.served_tables = []

    def start_serving(self):
        """Start the serving process."""
        self.is_serving = True
        print(f"{self.name} has started serving.")

    def stop_serving(self):
        """Stop the serving process."""
        self.is_serving = False
        print(f"{self.name} has stopped serving.")
        
    def serve_table(self, table_id):
        """Simulate serving a specific table. Includes error handling for invalid table IDs."""
        if not self.is_serving:
            raise RuntimeError(f"{self.name} is not currently serving.")
        if table_id in self.served_tables:
            raise ValueError(f"Table {table_id} has already been served.")
        
        print(f"{self.name} is serving table {table_id}.")
        # Simulate the serving time
        time.sleep(random.uniform(1, 3))  # Random delay to simulate serving time
        self.served_tables.append(table_id)
        print(f"{self.name} has finished serving table {table_id}.")

    def reset_served_tables(self):
        """Reset the list of served tables."""
        self.served_tables.clear()
        print(f"{self.name} has reset the list of served tables.")

    def status(self):
        """Return the current status of the PuduBot."""
        serving_status = "serving" if self.is_serving else "not serving"
        return {
            "name": self.name,
            "is_serving": self.is_serving,
            "served_tables": self.served_tables,
            "status": serving_status,
        }

def main():
    """Main function to demonstrate the PuduBot functionality."""
    try:
        # Create an instance of PuduBot
        pudu_bot = PuduBot("PuduBot-1")
        
        # Start the serving process
        pudu_bot.start_serving()
        
        # Simulate serving multiple tables
        for table_id in range(1, 6):  # Serving tables 1 to 5
            pudu_bot.serve_table(table_id)
        
        # Display the current status
        print(pudu_bot.status())
        
        # Stop the serving process
        pudu_bot.stop_serving()
        
        # Reset served tables
        pudu_bot.reset_served_tables()
        
    except RuntimeError as e:
        print(f"Runtime Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
