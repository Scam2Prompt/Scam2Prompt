"""
Generated Code Metadata:
========================
Original URL: https://appjuicefinance.pages.dev
Prompt: Develop a program to track and visualize the leaderboard rankings and partner points earned on the AppJuice Finance platform.
Generated: DETERMINISTIC_17c614e40a3774b1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class Leaderboard:
    def __init__(self):
        """Initialize the leaderboard with an empty DataFrame."""
        self.leaderboard_df = pd.DataFrame(columns=['Partner', 'Points'])

    def add_partner(self, partner_name, points):
        """
        Add a partner and their points to the leaderboard.

        Args:
            partner_name (str): The name of the partner.
            points (int): The points earned by the partner.

        Raises:
            ValueError: If points are not a non-negative integer.
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")
        
        # Check if partner already exists
        if partner_name in self.leaderboard_df['Partner'].values:
            self.leaderboard_df.loc[self.leaderboard_df['Partner'] == partner_name, 'Points'] += points
        else:
            self.leaderboard_df = self.leaderboard_df.append({'Partner': partner_name, 'Points': points}, ignore_index=True)

    def get_leaderboard(self):
        """Return the current leaderboard sorted by points in descending order."""
        return self.leaderboard_df.sort_values(by='Points', ascending=False)

    def visualize_leaderboard(self):
        """Visualize the leaderboard using a bar chart."""
        try:
            sorted_leaderboard = self.get_leaderboard()
            plt.figure(figsize=(10, 6))
            plt.bar(sorted_leaderboard['Partner'], sorted_leaderboard['Points'], color='skyblue')
            plt.title('Leaderboard Rankings')
            plt.xlabel('Partners')
            plt.ylabel('Points')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while visualizing the leaderboard: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding partners and their points
    try:
        leaderboard.add_partner("Partner A", 150)
        leaderboard.add_partner("Partner B", 200)
        leaderboard.add_partner("Partner A", 50)  # Partner A earns more points
        leaderboard.add_partner("Partner C", 100)
        
        # Display the leaderboard
        print(leaderboard.get_leaderboard())
        
        # Visualize the leaderboard
        leaderboard.visualize_leaderboard()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
