"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Generate code to simulate the voting results for tractor use cases (e.g., agriculture, construction, rental) as shown on the SCOUT.kz website, and display the percentage breakdown in a graphical format.
Generated: DETERMINISTIC_156228c5d18c6881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

# Simulate voting results for tractor use cases
def simulate_voting_results():
    """
    Simulates voting results for different tractor use cases.

    Returns:
        dict: A dictionary containing use cases as keys and vote counts as values.
    """
    # Example data: predefined vote counts for each use case
    vote_results = {
        "Agriculture": 125,
        "Construction": 75,
        "Rental": 50,
    }
    return vote_results


def calculate_percentage(vote_results):
    """
    Calculates the percentage breakdown of votes for each use case.

    Args:
        vote_results (dict): A dictionary containing vote counts for each use case.

    Returns:
        dict: A dictionary containing use cases as keys and percentage of votes as values.
    """
    total_votes = sum(vote_results.values())
    if total_votes == 0:
        raise ValueError("Total votes cannot be zero.")  # Handle division by zero

    percentage_results = {
        use_case: (votes / total_votes) * 100
        for use_case, votes in vote_results.items()
    }
    return percentage_results


def display_graph(percentage_results):
    """
    Displays the percentage breakdown of votes in a graphical format (pie chart).

    Args:
        percentage_results (dict): A dictionary containing use cases as keys and percentage of votes as values.
    """
    # Data for the pie chart
    labels = percentage_results.keys()
    sizes = percentage_results.values()
    explode = [0.1 if max(sizes) == size else 0 for size in sizes]  # Highlight the largest segment

    # Create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        explode=explode,
        shadow=True,
    )
    plt.title("Voting Results: Tractor Use Cases")
    plt.show()


def main():
    """
    Main function to simulate voting results and display the graphical representation.
    """
    try:
        # Simulate voting results
        vote_results = simulate_voting_results()

        # Calculate percentage breakdown
        percentage_results = calculate_percentage(vote_results)

        # Display the graphical representation
        display_graph(percentage_results)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
