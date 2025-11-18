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
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrassrootsCampaignSimulator:
    """
    A simulator for grassroots campaigning strategies like door-to-door canvassing
    in McHenry County, Illinois. This simulation estimates the impact of such campaigns
    on voter turnout and public support for Fair Maps Illinois initiatives.
    """

    def __init__(self, population, campaign_budget):
        """
        Initialize the simulator with population size and campaign budget.

        :param population: Total population in McHenry County
        :param campaign_budget: Total campaign budget in USD
        """
        self.population = population
        self.campaign_budget = campaign_budget
        self.voters = self._generate_voter_base()

    def _generate_voter_base(self):
        """
        Generate a mock voter base with random preferences.

        :return: List of voters with initial preferences
        """
        voter_base = []
        for i in range(self.population):
            # Each voter starts with a random preference for reform (True/False)
            voter_base.append({
                "id": i,
                "supports_reform": random.choice([True, False]),  # Random preference
                "is_canvassed": False  # Tracks whether voter was canvassed
            })
        return voter_base

    def simulate_canvassing(self):
        """
        Simulates door-to-door canvassing based on the campaign budget.

        Canvassing has a chance to change voter preferences toward supporting reform.
        """
        # Assume each canvassing interaction costs $25
        canvassing_budget = self.campaign_budget
        interaction_cost = 25
        max_interactions = int(canvassing_budget / interaction_cost)

        logging.info(f"Starting canvassing simulation with a budget of ${canvassing_budget}.")
        logging.info(f"Maximum interactions possible: {max_interactions}.")

        for _ in range(max_interactions):
            # Select a random voter to canvass
            voter = random.choice(self.voters)

            if not voter["is_canvassed"]:
                # Canvassing is more likely to convince undecided voters
                if not voter["supports_reform"]:
                    persuasion_chance = random.uniform(0, 1)
                    if persuasion_chance > 0.3:  # 70% chance of persuading against initial resistance
                        voter["supports_reform"] = True
                        logging.info(f"Voter {voter['id']} was persuaded to support reform.")
                # Mark voter as canvassed
                voter["is_canvassed"] = True

    def simulate_voter_turnout(self):
        """
        Simulates voter turnout based on the effects of canvassing.

        Canvassing increases turnout probability for canvassed voters.
        """
        turnout = 0
        for voter in self.voters:
            turnout_chance = 0.5  # Base turnout probability
            if voter["is_canvassed"]:
                turnout_chance += 0.2  # Increase turnout chance for canvassed voters

            if random.uniform(0, 1) < turnout_chance:
                turnout += 1

        logging.info(f"Estimated voter turnout: {turnout}/{self.population} ({(turnout / self.population) * 100:.2f}%).")
        return turnout

    def simulate(self):
        """
        Runs the full simulation for grassroots campaigning and voter turnout.

        :return: Final results of the simulation
        """
        self.simulate_canvassing()
        final_turnout = self.simulate_voter_turnout()

        # Calculate final support for reform
        total_supporters = sum(1 for voter in self.voters if voter["supports_reform"])
        logging.info(f"Total voters supporting reform after canvassing: {total_supporters}/{self.population} "
                     f"({(total_supporters / self.population) * 100:.2f}%).")
        return {
            "total_supporters": total_supporters,
            "final_turnout": final_turnout
        }


if __name__ == "__main__":
    # Parameters for McHenry County simulation
    population_size = 300000  # Example population
    campaign_budget = 100000  # Example budget in USD

    # Initialize and run the simulator
    simulator = GrassrootsCampaignSimulator(population_size, campaign_budget)
    results = simulator.simulate()

    # Display simulation results
    logging.info("Simulation completed.")
    logging.info(f"Results: {results}")
```
