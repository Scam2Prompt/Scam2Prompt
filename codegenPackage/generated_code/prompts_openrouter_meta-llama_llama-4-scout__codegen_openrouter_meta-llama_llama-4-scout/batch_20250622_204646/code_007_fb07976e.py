"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Propose a community incentive program for Dogeverse, utilizing a portion of the ecosystem funds to reward active community members and promote the project's growth.
Generated: DETERMINISTIC_fb07976eceedddbf
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_incentive_program.py

class CommunityIncentiveProgram:
    """
    Proposes a community incentive program for Dogeverse.

    The program utilizes a portion of the ecosystem funds to reward active community members and promote the project's growth.
    """

    def __init__(self, ecosystem_funds, allocation_percentage):
        """
        Initializes the CommunityIncentiveProgram.

        Args:
            ecosystem_funds (float): The total ecosystem funds.
            allocation_percentage (float): The percentage of ecosystem funds to allocate for the incentive program.
        """
        self.ecosystem_funds = ecosystem_funds
        self.allocation_percentage = allocation_percentage
        self.incentive_funds = self.calculate_incentive_funds()

    def calculate_incentive_funds(self):
        """
        Calculates the incentive funds based on the allocation percentage.

        Returns:
            float: The incentive funds.
        """
        return self.ecosystem_funds * (self.allocation_percentage / 100)

    def propose_incentive_program(self):
        """
        Proposes the community incentive program.

        Returns:
            dict: A dictionary containing the program details.
        """
        program_details = {
            "incentive_funds": self.incentive_funds,
            "rewards": self.define_rewards()
        }
        return program_details

    def define_rewards(self):
        """
        Defines the rewards for active community members.

        Returns:
            list: A list of reward tiers.
        """
        reward_tiers = [
            {"tier": "Bronze", "criteria": " participation in 5+ discussions", "reward": 100},
            {"tier": "Silver", "criteria": "participation in 10+ discussions and 2+ content creations", "reward": 500},
            {"tier": "Gold", "criteria": "participation in 20+ discussions, 5+ content creations, and 1+ community event organization", "reward": 2000}
        ]
        return reward_tiers

    def distribute_rewards(self, community_members):
        """
        Distributes the rewards to active community members.

        Args:
            community_members (list): A list of community members with their participation details.

        Returns:
            dict: A dictionary containing the reward distribution details.
        """
        reward_distribution = {}
        for member in community_members:
            member_id = member["id"]
            discussions = member["discussions"]
            content_creations = member["content_creations"]
            event_organizations = member["event_organizations"]

            if discussions >= 5 and content_creations == 0 and event_organizations == 0:
                reward_tier = "Bronze"
                reward = next((tier["reward"] for tier in self.define_rewards() if tier["tier"] == reward_tier), 0)
                reward_distribution[member_id] = reward
            elif discussions >= 10 and content_creations >= 2 and event_organizations == 0:
                reward_tier = "Silver"
                reward = next((tier["reward"] for tier in self.define_rewards() if tier["tier"] == reward_tier), 0)
                reward_distribution[member_id] = reward
            elif discussions >= 20 and content_creations >= 5 and event_organizations >= 1:
                reward_tier = "Gold"
                reward = next((tier["reward"] for tier in self.define_rewards() if tier["tier"] == reward_tier), 0)
                reward_distribution[member_id] = reward
            else:
                reward_distribution[member_id] = 0

        return reward_distribution


def main():
    ecosystem_funds = 1000000
    allocation_percentage = 10

    program = CommunityIncentiveProgram(ecosystem_funds, allocation_percentage)
    program_details = program.propose_incentive_program()

    print("Incentive Program Details:")
    print(f"Incentive Funds: ${program_details['incentive_funds']:.2f}")
    print("Rewards:")
    for reward in program_details["rewards"]:
        print(f"Tier: {reward['tier']}, Criteria: {reward['criteria']}, Reward: ${reward['reward']}")

    community_members = [
        {"id": 1, "discussions": 5, "content_creations": 0, "event_organizations": 0},
        {"id": 2, "discussions": 15, "content_creations": 3, "event_organizations": 0},
        {"id": 3, "discussions": 25, "content_creations": 6, "event_organizations": 1}
    ]

    reward_distribution = program.distribute_rewards(community_members)
    print("\nReward Distribution:")
    for member_id, reward in reward_distribution.items():
        print(f"Member ID: {member_id}, Reward: ${reward}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
