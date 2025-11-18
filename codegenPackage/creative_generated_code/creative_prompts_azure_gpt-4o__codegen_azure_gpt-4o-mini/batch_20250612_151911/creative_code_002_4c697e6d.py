"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the effects of grassroots campaigning strategies, such as door-to-door canvassing, in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_4c697e6dcd0dda0b
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import matplotlib.pyplot as plt
from collections import namedtuple

# Define a namedtuple to represent a campaign strategy
CampaignStrategy = namedtuple('CampaignStrategy', ['name', 'effectiveness', 'cost_per_contact'])

# Define a class to simulate the grassroots campaign
class GrassrootsCampaign:
    def __init__(self, strategies):
        """
        Initialize the GrassrootsCampaign with a list of strategies.

        :param strategies: List of CampaignStrategy tuples representing the available strategies.
        """
        self.strategies = strategies
        self.total_cost = 0
        self.contacts_made = 0

    def simulate_campaign(self, budget):
        """
        Simulates the campaign based on the available budget and chosen strategies.

        :param budget: The total budget allocated for the campaign.
        :return: A dictionary with results of the simulation.
        """
        results = {}

        for strategy in self.strategies:
            # Calculate the number of contacts that can be made with the current strategy within the budget
            max_contacts = budget // strategy.cost_per_contact
            self.total_cost += max_contacts * strategy.cost_per_contact
            self.contacts_made += max_contacts
            
            # Calculate the effectiveness of the contacts made
            effectiveness_score = random.uniform(0, strategy.effectiveness) * max_contacts
            results[strategy.name] = {
                'contacts_made': max_contacts,
                'effectiveness_score': effectiveness_score
            }

        return results

    def plot_results(self, results):
        """
        Plots the results of the campaign simulation.

        :param results: A dictionary containing the results of the campaign.
        """
        strategies = list(results.keys())
        contacts = [result['contacts_made'] for result in results.values()]
        effectiveness_scores = [result['effectiveness_score'] for result in results.values()]

        # Create a bar plot for contacts made
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))

        ax[0].bar(strategies, contacts, color='blue', alpha=0.7)
        ax[0].set_title('Contacts Made per Strategy')
        ax[0].set_xlabel('Strategies')
        ax[0].set_ylabel('Number of Contacts')

        # Create a bar plot for effectiveness scores
        ax[1].bar(strategies, effectiveness_scores, color='green', alpha=0.7)
        ax[1].set_title('Effectiveness Scores per Strategy')
        ax[1].set_xlabel('Strategies')
        ax[1].set_ylabel('Effectiveness Score')

        plt.tight_layout()
        plt.show()

# Define the strategies for the campaign
strategies = [
    CampaignStrategy(name='Door-to-Door Canvassing', effectiveness=0.8, cost_per_contact=5),
    CampaignStrategy(name='Phone Banking', effectiveness=0.6, cost_per_contact=2),
    CampaignStrategy(name='Community Events', effectiveness=0.9, cost_per_contact=50)
]

# Create the campaign with defined strategies
campaign = GrassrootsCampaign(strategies)

# Simulate the campaign with a budget of $5000
budget = 5000

try:
    results = campaign.simulate_campaign(budget)
    campaign.plot_results(results)

except Exception as e:
    print(f"An error occurred during the simulation: {e}")
```
