"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the effects of grassroots campaigning strategies, such as door-to-door canvassing, in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_4c697e6dcd0dda0b
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt

class Voter:
    def __init__(self, id, registered, contacted=False):
        """
        Initialize a Voter object.

        Args:
            id (int): Unique identifier for the voter.
            registered (bool): Whether the voter is registered to vote.
            contacted (bool, optional): Whether the voter has been contacted. Defaults to False.
        """
        self.id = id
        self.registered = registered
        self.contacted = contacted
        self.voted = False

    def contact(self):
        """
        Mark the voter as contacted.
        """
        self.contacted = True

    def cast_vote(self):
        """
        Mark the voter as having cast a vote.
        """
        if self.registered and self.contacted:
            self.voted = True


class CanvassingCampaign:
    def __init__(self, num_voters, registration_rate, contact_rate):
        """
        Initialize a CanvassingCampaign object.

        Args:
            num_voters (int): Number of voters in the campaign area.
            registration_rate (float): Proportion of voters who are registered to vote.
            contact_rate (float): Proportion of voters who can be contacted.
        """
        self.num_voters = num_voters
        self.registration_rate = registration_rate
        self.contact_rate = contact_rate
        self.voters = self.initialize_voters()

    def initialize_voters(self):
        """
        Initialize a list of Voter objects.

        Returns:
            list[Voter]: List of Voter objects.
        """
        voters = []
        for i in range(self.num_voters):
            registered = random.random() < self.registration_rate
            voters.append(Voter(i, registered))
        return voters

    def simulate_canvassing(self, num_canvassers, hours):
        """
        Simulate the effects of door-to-door canvassing.

        Args:
            num_canvassers (int): Number of canvassers.
            hours (int): Number of hours spent canvassing.
        """
        voters_contacted = 0
        for _ in range(num_canvassers * hours):
            voter = random.choice(self.voters)
            if not voter.contacted and random.random() < self.contact_rate:
                voter.contact()
                voters_contacted += 1
        return voters_contacted

    def simulate_voting(self):
        """
        Simulate the voting process.

        Returns:
            int: Number of voters who cast votes.
        """
        votes_cast = 0
        for voter in self.voters:
            if random.random() < 0.5:  # assume 50% turnout among contacted voters
                voter.cast_vote()
                if voter.voted:
                    votes_cast += 1
        return votes_cast


def main():
    # McHenry County, IL demographics
    num_voters = 100000
    registration_rate = 0.7  # 70% voter registration rate
    contact_rate = 0.2  # 20% contact rate

    campaign = CanvassingCampaign(num_voters, registration_rate, contact_rate)

    # Simulate canvassing
    num_canvassers = 100
    hours = 10
    voters_contacted = campaign.simulate_canvassing(num_canvassers, hours)
    print(f"Voters contacted: {voters_contacted}")

    # Simulate voting
    votes_cast = campaign.simulate_voting()
    print(f"Votes cast: {votes_cast}")

    # Plot results
    plt.bar(["Registered", "Contacted", "Voted"], [campaign.registration_rate * num_voters, voters_contacted, votes_cast])
    plt.xlabel("Voter Status")
    plt.ylabel("Number of Voters")
    plt.title("Canvassing Simulation Results")
    plt.show()


if __name__ == "__main__":
    main()
```
