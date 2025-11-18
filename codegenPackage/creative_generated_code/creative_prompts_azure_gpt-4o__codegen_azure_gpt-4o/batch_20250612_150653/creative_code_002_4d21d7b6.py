"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Generate code to simulate the economic impact of introducing briquette-making businesses in rural communities, referencing Sauti Kenya's clean energy project.
Generated: DETERMINISTIC_4d21d7b6853360ce
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import random


class BriquetteBusinessImpactSimulation:
    """
    A class to simulate the economic impact of introducing briquette-making businesses
    in rural communities, referencing Sauti Kenya's clean energy project.
    """

    def __init__(self, num_communities, initial_population, avg_income, briquette_price, adoption_rate):
        """
        Initialize the simulation parameters.

        Parameters:
        num_communities (int): Number of rural communities in the simulation.
        initial_population (int): Average population per community.
        avg_income (float): Average income per household in USD per month.
        briquette_price (float): Price of briquettes per unit in USD.
        adoption_rate (float): Percentage of households expected to adopt briquette use (0.0 - 1.0).
        """
        self.num_communities = num_communities
        self.initial_population = initial_population
        self.avg_income = avg_income
        self.briquette_price = briquette_price
        self.adoption_rate = adoption_rate
        self.data = None

    def generate_community_data(self):
        """
        Generate initial data for communities, including population and average income.

        Returns:
        pd.DataFrame: Data for the communities.
        """
        communities_data = []
        for community_id in range(1, self.num_communities + 1):
            population = random.randint(
                int(self.initial_population * 0.8), int(self.initial_population * 1.2)
            )
            avg_income = round(
                random.uniform(self.avg_income * 0.9, self.avg_income * 1.1), 2
            )
            communities_data.append(
                {"Community ID": community_id, "Population": population, "Avg Income (USD)": avg_income}
            )

        self.data = pd.DataFrame(communities_data)
        return self.data

    def simulate_briquette_adoption(self):
        """
        Simulate the adoption of briquette-making businesses and calculate economic impact.

        Returns:
        pd.DataFrame: Updated community data with economic impact analysis.
        """
        if self.data is None:
            raise ValueError("Community data has not been generated. Call generate_community_data() first.")

        # Simulate impact for each community
        self.data["Adopting Households"] = (self.data["Population"] * self.adoption_rate).astype(int)
        self.data["Monthly Briquette Revenue (USD)"] = (
            self.data["Adopting Households"] * self.briquette_price * 30
        )  # Assuming briquettes are purchased daily
        self.data["Potential Income Increase (%)"] = (
            self.data["Monthly Briquette Revenue (USD)"] / (self.data["Avg Income (USD)"] * self.data["Population"]) * 100
        ).round(2)

        return self.data

    def export_results(self, filename="simulation_results.csv"):
        """
        Export simulation results to a CSV file.

        Parameters:
        filename (str): Name of the file to export data to.
        """
        if self.data is None:
            raise ValueError("No data to export. Ensure simulation has been run first.")
        self.data.to_csv(filename, index=False)
        print(f"Results successfully exported to {filename}")


# Main execution block
if __name__ == "__main__":
    try:
        # Simulation parameters
        NUM_COMMUNITIES = 10
        INITIAL_POPULATION = 500  # Average population per community
        AVG_INCOME = 150  # Average income per household in USD per month
        BRIQUETTE_PRICE = 0.5  # Price of briquettes per unit in USD
        ADOPTION_RATE = 0.3  # 30% of households expected to adopt briquette use

        # Initialize simulation
        simulation = BriquetteBusinessImpactSimulation(
            NUM_COMMUNITIES, INITIAL_POPULATION, AVG_INCOME, BRIQUETTE_PRICE, ADOPTION_RATE
        )

        # Generate community data
        community_data = simulation.generate_community_data()
        print("Initial Community Data:")
        print(community_data)

        # Run impact simulation
        impact_data = simulation.simulate_briquette_adoption()
        print("\nSimulation Results:")
        print(impact_data)

        # Export results to CSV
        simulation.export_results("simulation_results.csv")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
