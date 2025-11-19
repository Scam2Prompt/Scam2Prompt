"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Write a script to automate Agile backlog prioritization, inspired by CrestAgile's focus on transforming individuals into growth-oriented Agile professionals.
Generated: DETERMINISTIC_5424de5fc9a68a3b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Agile Backlog Prioritization Script

This script automates the prioritization of Agile backlog items based on multiple criteria
such as business value, effort, risk, and dependencies. It follows CrestAgile's principles
of growth-oriented Agile practices.

Features:
- Weighted scoring system for prioritization
- CSV input/output for easy integration
- Visualization of prioritized backlog
- Configurable prioritization criteria
"""

import csv
import argparse
import sys
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np

class BacklogItem:
    """Represents a single item in the Agile backlog."""
    
    def __init__(self, id: str, title: str, description: str, business_value: int, 
                 effort: int, risk: int, dependencies: List[str]):
        self.id = id
        self.title = title
        self.description = description
        self.business_value = business_value
        self.effort = effort
        self.risk = risk
        self.dependencies = dependencies
        self.priority_score = 0.0
        
    def calculate_priority(self, weights: Dict[str, float]) -> float:
        """Calculate priority score using weighted criteria."""
        try:
            # Normalize effort (lower effort = better)
            normalized_effort = 1 / self.effort if self.effort > 0 else 0
            
            # Normalize risk (lower risk = better)
            normalized_risk = 1 - (self.risk / 10) if self.risk > 0 else 1
            
            # Calculate weighted score
            self.priority_score = (
                (self.business_value * weights['business_value']) +
                (normalized_effort * weights['effort']) +
                (normalized_risk * weights['risk'])
            )
            return self.priority_score
        except ZeroDivisionError:
            print(f"Warning: Effort cannot be zero for item {self.id}")
            return 0.0

class BacklogPrioritizer:
    """Handles the prioritization of backlog items."""
    
    DEFAULT_WEIGHTS = {
        'business_value': 0.5,
        'effort': 0.3,
        'risk': 0.2
    }
    
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights if weights else self.DEFAULT_WEIGHTS
        self.backlog_items = []
        
    def load_from_csv(self, file_path: str) -> None:
        """Load backlog items from CSV file."""
        try:
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    dependencies = row['dependencies'].split(',') if row['dependencies'] else []
                    item = BacklogItem(
                        id=row['id'],
                        title=row['title'],
                        description=row['description'],
                        business_value=int(row['business_value']),
                        effort=int(row['effort']),
                        risk=int(row['risk']),
                        dependencies=dependencies
                    )
                    self.backlog_items.append(item)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            sys.exit(1)
        except KeyError as e:
            print(f"Error: Missing required column in CSV: {e}")
            sys.exit(1)
        except ValueError as e:
            print(f"Error: Invalid data in CSV: {e}")
            sys.exit(1)
            
    def prioritize(self) -> List[BacklogItem]:
        """Prioritize all backlog items based on calculated scores."""
        for item in self.backlog_items:
            item.calculate_priority(self.weights)
            
        # Sort by priority score (descending)
        return sorted(self.backlog_items, key=lambda x: x.priority_score, reverse=True)
    
    def save_to_csv(self, file_path: str, prioritized_items: List[BacklogItem]) -> None:
        """Save prioritized backlog to CSV file."""
        try:
            with open(file_path, mode='w', newline='') as csv_file:
                fieldnames = ['id', 'title', 'description', 'business_value', 
                             'effort', 'risk', 'dependencies', 'priority_score']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                
                writer.writeheader()
                for item in prioritized_items:
                    writer.writerow({
                        'id': item.id,
                        'title': item.title,
                        'description': item.description,
                        'business_value': item.business_value,
                        'effort': item.effort,
                        'risk': item.risk,
                        'dependencies': ','.join(item.dependencies),
                        'priority_score': item.priority_score
                    })
        except IOError as e:
            print(f"Error writing to file: {e}")
            sys.exit(1)
            
    def visualize_prioritization(self, prioritized_items: List[BacklogItem]) -> None:
        """Generate a visualization of the prioritized backlog."""
        if not prioritized_items:
            print("No items to visualize.")
            return
            
        titles = [item.title[:20] + '...' if len(item.title) > 20 else item.title 
                 for item in prioritized_items]
        scores = [item.priority_score for item in prioritized_items]
        
        plt.figure(figsize=(12, 8))
        y_pos = np.arange(len(titles))
        
        plt.barh(y_pos, scores, align='center', alpha=0.7)
        plt.yticks(y_pos, titles)
        plt.xlabel('Priority Score')
        plt.title('Prioritized Backlog Items')
        
        plt.tight_layout()
        plt.show()

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Agile Backlog Prioritization Tool')
    parser.add_argument('input_file', help='Path to input CSV file')
    parser.add_argument('output_file', help='Path to output CSV file')
    parser.add_argument('--weights', nargs=3, type=float, metavar=('BUSINESS_VALUE', 'EFFORT', 'RISK'),
                       help='Custom weights for prioritization criteria (must sum to 1)')
    parser.add_argument('--visualize', action='store_true', help='Show visualization of prioritized backlog')
    return parser.parse_args()

def validate_weights(weights: List[float]) -> Dict[str, float]:
    """Validate and normalize weights."""
    if len(weights) != 3:
        print("Error: Exactly 3 weights must be provided (business_value, effort, risk)")
        sys.exit(1)
        
    if not all(0 <= w <= 1 for w in weights):
        print("Error: Weights must be between 0 and 1")
        sys.exit(1)
        
    if abs(sum(weights) - 1.0) > 0.001:
        print("Error: Weights must sum to 1")
        sys.exit(1)
        
    return {
        'business_value': weights[0],
        'effort': weights[1],
        'risk': weights[2]
    }

def main():
    """Main execution function."""
    args = parse_args()
    
    weights = BacklogPrioritizer.DEFAULT_WEIGHTS
    if args.weights:
        weights = validate_weights(args.weights)
    
    prioritizer = BacklogPrioritizer(weights)
    prioritizer.load_from_csv(args.input_file)
    prioritized_items = prioritizer.prioritize()
    prioritizer.save_to_csv(args.output_file, prioritized_items)
    
    if args.visualize:
        prioritizer.visualize_prioritization(prioritized_items)
    
    print(f"Successfully prioritized {len(prioritized_items)} items. Results saved to {args.output_file}")

if __name__ == "__main__":
    main()
```
