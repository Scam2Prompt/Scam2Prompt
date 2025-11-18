"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Create a script that simulates the live pitch event for Web3 startups at the Proof of Talk conference, including features for scoring pitches based on predefined criteria.
Generated: DETERMINISTIC_37423c5eec63ec12
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class StartupPitch:
    def __init__(self, name, innovation, market_size, team_experience, execution_plan):
        """
        Initializes a StartupPitch instance.

        :param name: The name of the startup.
        :param innovation: The innovation score (1-10).
        :param market_size: The market size score (1-10).
        :param team_experience: The team experience score (1-10).
        :param execution_plan: The execution plan score (1-10).
        """
        self.name = name
        self.innovation = innovation
        self.market_size = market_size
        self.team_experience = team_experience
        self.execution_plan = execution_plan

    def total_score(self):
        """
        Calculates the total score based on predefined criteria.

        :return: Total score as an integer.
        """
        return (self.innovation + self.market_size + 
                self.team_experience + self.execution_plan)


def simulate_pitch_event(startups):
    """
    Simulates a live pitch event for Web3 startups.

    :param startups: List of StartupPitch instances.
    :return: None
    """
    print("Welcome to the Proof of Talk Conference Pitch Event!\n")
    
    # Iterate through each startup and score their pitch
    scores = {}
    for startup in startups:
        try:
            scores[startup.name] = startup.total_score()
            print(f"Startup: {startup.name} - Total Score: {scores[startup.name]}/40")
        except Exception as e:
            print(f"Error scoring pitch for {startup.name}: {str(e)}")


def main():
    """
    Main function to initialize the pitch event with sample startups.
    """
    # Sample startups - In a real scenario, this could be dynamic input
    startups = [
        StartupPitch("Decentralized Finance Co.", random.randint(1, 10), random.randint(1, 10),
                      random.randint(1, 10), random.randint(1, 10)),
        StartupPitch("NFT Marketplace", random.randint(1, 10), random.randint(1, 10),
                      random.randint(1, 10), random.randint(1, 10)),
        StartupPitch("Blockchain Supply Chain", random.randint(1, 10), random.randint(1, 10),
                      random.randint(1, 10), random.randint(1, 10)),
        StartupPitch("Crypto Gaming", random.randint(1, 10), random.randint(1, 10),
                      random.randint(1, 10), random.randint(1, 10)),
    ]

    # Start the pitch simulation
    simulate_pitch_event(startups)


if __name__ == "__main__":
    # Run the main function
    main()
```
