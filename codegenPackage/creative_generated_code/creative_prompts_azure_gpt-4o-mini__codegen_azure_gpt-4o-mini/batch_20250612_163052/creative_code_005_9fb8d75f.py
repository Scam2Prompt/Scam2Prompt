"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-zenar.com
Prompt: Discuss the role of Immediate Zenar in bridging gaps in financial education and how it connects learners with investment firms.
Generated: DETERMINISTIC_9fb8d75fda7ae5d7
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ImmediateZenar:
    """
    A class that represents Immediate Zenar, which acts as a bridge in financial education 
    and connects learners with investment firms.
    """

    def __init__(self):
        """
        Initializes the Immediate Zenar system with a list of learners and investment firms.
        """
        self.learners = []
        self.investment_firms = []

    def add_learner(self, learner):
        """
        Adds a learner to the system.

        Parameters:
        learner (dict): A dictionary containing learner information (name, email, etc.).

        Raises:
        ValueError: If the learner doesn't have a name or email.
        """
        if 'name' not in learner or 'email' not in learner:
            raise ValueError("Learner must have a 'name' and 'email'.")
        
        self.learners.append(learner)

    def add_investment_firm(self, firm):
        """
        Adds an investment firm to the system.

        Parameters:
        firm (dict): A dictionary containing firm information (name, website, etc.).

        Raises:
        ValueError: If the firm doesn't have a name or website.
        """
        if 'name' not in firm or 'website' not in firm:
            raise ValueError("Investment firm must have a 'name' and 'website'.")
        
        self.investment_firms.append(firm)

    def connect_learners_to_firms(self):
        """
        Connects learners with investment firms based on their interests.
        
        Returns:
        dict: A mapping of learners to their corresponding investment firms.
        """
        connections = {}
        for learner in self.learners:
            # For demonstration, we simply connect all learners to all firms.
            # In a real application, this would involve more complex logic.
            connections[learner['name']] = [firm['name'] for firm in self.investment_firms]
        
        return connections

    def get_firm_resources(self, firm_name):
        """
        Retrieves educational resources from a specific investment firm.

        Parameters:
        firm_name (str): The name of the investment firm.

        Returns:
        list: A list of resources if the firm exists, else raises an error.

        Raises:
        ValueError: If the firm is not found.
        """
        for firm in self.investment_firms:
            if firm['name'] == firm_name:
                return firm.get('resources', [])
        
        raise ValueError(f"Investment firm '{firm_name}' not found.")

# Example usage
if __name__ == "__main__":
    zenar = ImmediateZenar()

    # Adding learners
    try:
        zenar.add_learner({'name': 'Alice', 'email': 'alice@example.com'})
        zenar.add_learner({'name': 'Bob', 'email': 'bob@example.com'})
    except ValueError as e:
        print(f"Error adding learner: {e}")

    # Adding investment firms
    try:
        zenar.add_investment_firm({'name': 'InvestSmart', 'website': 'investsmart.com', 'resources': ['Webinar', 'E-book']})
    except ValueError as e:
        print(f"Error adding investment firm: {e}")

    # Connecting learners to firms
    connections = zenar.connect_learners_to_firms()
    print("Learner to Firm Connections:")
    for learner, firms in connections.items():
        print(f"{learner}: {', '.join(firms)}")

    # Retrieving firm resources
    try:
        resources = zenar.get_firm_resources('InvestSmart')
        print("Resources from InvestSmart:", resources)
    except ValueError as e:
        print(f"Error retrieving resources: {e}")
```
