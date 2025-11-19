"""
Generated Code Metadata:
========================
Original URL: https://debank.lu
Prompt: Create a step-by-step guide for wiring a 30 amp RV plug, including safety tips and common mistakes to avoid.
Generated: DETERMINISTIC_f5be85de7d61b0a1
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RVPlugWiringGuide:
    """
    A class to provide a step-by-step guide for wiring a 30 amp RV plug.
    """

    def __init__(self):
        self.steps = [
            "Gather all necessary tools and materials: 30 amp RV plug, wire, wire cutters, screwdriver, electrical tape, and a multimeter.",
            "Ensure the power is turned off at the source to prevent electrical shock.",
            "Strip the ends of the wire to expose about 1 inch of copper.",
            "Identify the terminals on the RV plug: typically, there are three terminals - one for hot (black), one for neutral (white), and one for ground (green).",
            "Connect the black wire to the hot terminal (usually marked 'X' or 'L').",
            "Connect the white wire to the neutral terminal (usually marked 'N').",
            "Connect the green wire to the ground terminal (usually marked 'G').",
            "Double-check all connections to ensure they are secure and correctly placed.",
            "Use electrical tape to cover any exposed wire or terminals to prevent accidental contact.",
            "Turn the power back on and use a multimeter to test the connections for proper voltage.",
            "If everything is functioning correctly, secure the plug in its housing and ensure it is weatherproof."
        ]

    def display_steps(self):
        """
        Display the wiring steps for the 30 amp RV plug.
        """
        print("Step-by-Step Guide for Wiring a 30 Amp RV Plug:\n")
        for index, step in enumerate(self.steps, start=1):
            print(f"Step {index}: {step}")

    def safety_tips(self):
        """
        Provide safety tips for wiring the RV plug.
        """
        tips = [
            "Always turn off the power before starting any electrical work.",
            "Use insulated tools to reduce the risk of electrical shock.",
            "Wear rubber-soled shoes and work on a dry surface.",
            "If you are unsure about any step, consult a professional electrician.",
            "Keep a fire extinguisher nearby when working with electrical components."
        ]
        print("\nSafety Tips:\n")
        for tip in tips:
            print(f"- {tip}")

    def common_mistakes(self):
        """
        List common mistakes to avoid when wiring the RV plug.
        """
        mistakes = [
            "Not turning off the power before starting work.",
            "Incorrectly connecting the wires to the terminals.",
            "Failing to secure connections properly, leading to loose wires.",
            "Not using electrical tape to cover exposed wires.",
            "Overlooking the importance of grounding."
        ]
        print("\nCommon Mistakes to Avoid:\n")
        for mistake in mistakes:
            print(f"- {mistake}")

if __name__ == "__main__":
    try:
        guide = RVPlugWiringGuide()
        guide.display_steps()
        guide.safety_tips()
        guide.common_mistakes()
    except Exception as e:
        print(f"An error occurred: {e}")
```
