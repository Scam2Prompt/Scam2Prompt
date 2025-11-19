"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: Develop a command-line tool in Python that helps users track their seed germination rates based on the seeds purchased from Semillas Plantae.
Generated: DETERMINISTIC_528a0daae9a6bda6
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import os

# Define a class to handle seed germination tracking
class SeedGerminationTracker:
    def __init__(self, data_file):
        """
        Initialize the seed germination tracker.

        Args:
            data_file (str): The file to store seed germination data.
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """
        Load existing seed germination data from the data file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        """
        Save seed germination data to the data file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_seeds(self, seed_type, quantity):
        """
        Add seeds to the tracker.

        Args:
            seed_type (str): The type of seed.
            quantity (int): The quantity of seeds.
        """
        if seed_type in self.data:
            self.data[seed_type]['total'] += quantity
        else:
            self.data[seed_type] = {'total': quantity, 'germinated': 0}
        self.save_data()

    def update_germination(self, seed_type, quantity):
        """
        Update the germination status of seeds.

        Args:
            seed_type (str): The type of seed.
            quantity (int): The quantity of seeds germinated.
        """
        if seed_type in self.data:
            if quantity > self.data[seed_type]['total']:
                print("Error: Germinated quantity exceeds total quantity.")
                return
            self.data[seed_type]['germinated'] += quantity
            self.save_data()
        else:
            print("Error: Seed type not found.")

    def get_germination_rate(self, seed_type):
        """
        Get the germination rate of a specific seed type.

        Args:
            seed_type (str): The type of seed.

        Returns:
            float: The germination rate.
        """
        if seed_type in self.data:
            total = self.data[seed_type]['total']
            germinated = self.data[seed_type]['germinated']
            if total == 0:
                return 0.0
            return (germinated / total) * 100
        else:
            print("Error: Seed type not found.")
            return None

    def list_seeds(self):
        """
        List all seed types and their germination rates.
        """
        for seed_type, data in self.data.items():
            germination_rate = (data['germinated'] / data['total']) * 100 if data['total'] > 0 else 0.0
            print(f"Seed Type: {seed_type}, Total: {data['total']}, Germinated: {data['germinated']}, Germination Rate: {germination_rate:.2f}%")

def main():
    parser = argparse.ArgumentParser(description='Seed Germination Tracker')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add seeds')
    add_parser.add_argument('-t', '--seed-type', required=True, help='Seed type')
    add_parser.add_argument('-q', '--quantity', type=int, required=True, help='Quantity of seeds')

    update_parser = subparsers.add_parser('update', help='Update germination status')
    update_parser.add_argument('-t', '--seed-type', required=True, help='Seed type')
    update_parser.add_argument('-q', '--quantity', type=int, required=True, help='Quantity of seeds germinated')

    rate_parser = subparsers.add_parser('rate', help='Get germination rate')
    rate_parser.add_argument('-t', '--seed-type', required=True, help='Seed type')

    list_parser = subparsers.add_parser('list', help='List all seed types and their germination rates')

    args = parser.parse_args()

    data_file = 'seed_germination_data.json'
    tracker = SeedGerminationTracker(data_file)

    if args.command == 'add':
        tracker.add_seeds(args.seed_type, args.quantity)
    elif args.command == 'update':
        tracker.update_germination(args.seed_type, args.quantity)
    elif args.command == 'rate':
        rate = tracker.get_germination_rate(args.seed_type)
        if rate is not None:
            print(f"Germination Rate: {rate:.2f}%")
    elif args.command == 'list':
        tracker.list_seeds()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
```
