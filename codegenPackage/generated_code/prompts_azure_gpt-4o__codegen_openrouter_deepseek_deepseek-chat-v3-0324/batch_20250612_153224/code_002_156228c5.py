"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Generate code to simulate the voting results for tractor use cases (e.g., agriculture, construction, rental) as shown on the SCOUT.kz website, and display the percentage breakdown in a graphical format.
Generated: DETERMINISTIC_156228c5d18c6881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def simulate_voting_data(num_votes=1000):
    """
    Simulate voting data for tractor use cases.
    Returns a dictionary with use cases and their vote percentages.
    """
    # Possible tractor use cases
    use_cases = ['Agriculture', 'Construction', 'Rental', 'Landscaping', 'Transport']
    
    # Generate random votes following a normal distribution
    np.random.seed(42)  # For reproducibility
    votes = np.random.normal(loc=50, scale=20, size=len(use_cases))
    votes = np.abs(votes)  # Ensure no negative votes
    total = np.sum(votes)
    
    # Calculate percentages and create result dictionary
    results = {case: (vote/total)*100 for case, vote in zip(use_cases, votes)}
    return results

def display_voting_results(results):
    """
    Display voting results in a graphical format using matplotlib.
    """
    try:
        # Prepare data for plotting
        labels = list(results.keys())
        sizes = list(results.values())
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
        
        # Create figure and axis
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle('Tractor Use Case Voting Results', fontsize=16)
        
        # Pie chart
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', 
                startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
        ax1.set_title('Percentage Breakdown')
        
        # Bar chart
        y_pos = np.arange(len(labels))
        ax2.bar(y_pos, sizes, color=colors)
        ax2.set_xticks(y_pos)
        ax2.set_xticklabels(labels, rotation=45)
        ax2.set_ylabel('Percentage (%)')
        ax2.set_title('Voting Distribution')
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error displaying results: {e}")

def main():
    """
    Main function to simulate and display voting results.
    """
    try:
        print("Simulating tractor use case voting results...")
        voting_results = simulate_voting_data()
        
        print("\nVoting Results:")
        for use_case, percentage in voting_results.items():
            print(f"{use_case}: {percentage:.1f}%")
            
        display_voting_results(voting_results)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
