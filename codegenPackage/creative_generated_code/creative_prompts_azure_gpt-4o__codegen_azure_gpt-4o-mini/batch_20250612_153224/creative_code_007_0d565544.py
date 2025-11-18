"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Recommend a framework for implementing a "Ferramenta perdas x ganhos" feature that helps users evaluate decisions and emotional trade-offs in their daily lives.
Generated: DETERMINISTIC_0d565544852af204
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# FerramentaPerdasGanhos.py

"""
FerramentaPerdasGanhos - A tool for evaluating decisions and emotional trade-offs.

This class allows users to input their decisions and evaluate the potential gains
and losses associated with each choice, helping them to make more informed decisions.
"""

class FerramentaPerdasGanhos:
    def __init__(self):
        """Initialize the tool with an empty list of decisions."""
        self.decisions = []

    def add_decision(self, decision: str, gains: list, losses: list):
        """
        Add a new decision to the tool.

        :param decision: A string representing the decision to evaluate.
        :param gains: A list of strings representing the potential gains from the decision.
        :param losses: A list of strings representing the potential losses from the decision.
        :raises ValueError: If the decision, gains, or losses are empty.
        """
        if not decision or not gains or not losses:
            raise ValueError("Decision, gains, and losses must not be empty.")
        
        self.decisions.append({
            "decision": decision,
            "gains": gains,
            "losses": losses
        })

    def evaluate_decisions(self):
        """
        Evaluate and print all decisions along with their gains and losses.
        """
        if not self.decisions:
            print("No decisions to evaluate.")
            return
        
        for idx, decision in enumerate(self.decisions, start=1):
            print(f"Decision {idx}: {decision['decision']}")
            print("Potential Gains:")
            for gain in decision['gains']:
                print(f"- {gain}")
            print("Potential Losses:")
            for loss in decision['losses']:
                print(f"- {loss}")
            print("\n" + "-"*30 + "\n")

    def clear_decisions(self):
        """Clear all recorded decisions."""
        self.decisions.clear()
        print("All decisions have been cleared.")

# Example usage:
if __name__ == "__main__":
    try:
        ferramenta = FerramentaPerdasGanhos()
        
        # Adding decisions for demonstration
        ferramenta.add_decision(
            "Change jobs",
            ["Higher salary", "Better work-life balance"],
            ["Uncertainty of a new environment", "Loss of current relationships"]
        )
        ferramenta.add_decision(
            "Buy a house",
            ["Investment growth", "Stability"],
            ["High upfront costs", "Maintenance responsibilities"]
        )

        # Evaluate all decisions
        ferramenta.evaluate_decisions()

    except Exception as e:
        print(f"An error occurred: {e}")
```
