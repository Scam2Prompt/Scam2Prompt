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
# rv_plug_wiring_guide.py

class RVPlugWiringGuide:
    def __init__(self):
        self.wiring_steps = [
            self.step_1_gather_materials,
            self.step_2_turn_off_power,
            self.step_3_prepare_wires,
            self.step_4_connect_wires,
            self.step_5_test_connection
        ]
        self.safety_tips = [
            "Always turn off power before starting work",
            "Use proper gauge wire for 30 amp application",
            "Ensure all connections are secure and not loose"
        ]
        self.common_mistakes = [
            "Using incorrect gauge wire",
            "Not turning off power before starting work",
            "Not testing connection after completion"
        ]

    def step_1_gather_materials(self):
        # Gather necessary materials
        # - 30 amp RV plug
        # - 10 gauge wire (or larger)
        # - Wire strippers
        # - Pliers
        # - Screwdriver
        print("Step 1: Gather materials")
        print("  - 30 amp RV plug")
        print("  - 10 gauge wire (or larger)")
        print("  - Wire strippers")
        print("  - Pliers")
        print("  - Screwdriver")

    def step_2_turn_off_power(self):
        # Turn off power to the circuit
        try:
            print("Step 2: Turn off power to the circuit")
            # Assume a function to turn off power exists
            # turn_off_power()
        except Exception as e:
            print(f"Error turning off power: {e}")

    def step_3_prepare_wires(self):
        # Prepare wires for connection
        print("Step 3: Prepare wires")
        print("  - Strip insulation from wire ends")
        print("  - Cut wires to correct length")

    def step_4_connect_wires(self):
        # Connect wires to the RV plug
        try:
            print("Step 4: Connect wires to the RV plug")
            print("  - Connect black (hot) wire to brass terminal")
            print("  - Connect white (neutral) wire to silver terminal")
            print("  - Connect green (ground) wire to green terminal")
        except Exception as e:
            print(f"Error connecting wires: {e}")

    def step_5_test_connection(self):
        # Test the connection
        try:
            print("Step 5: Test the connection")
            # Assume a function to test connection exists
            # test_connection()
        except Exception as e:
            print(f"Error testing connection: {e}")

    def display_safety_tips(self):
        print("Safety Tips:")
        for tip in self.safety_tips:
            print(f"  - {tip}")

    def display_common_mistakes(self):
        print("Common Mistakes to Avoid:")
        for mistake in self.common_mistakes:
            print(f"  - {mistake}")

    def run_guide(self):
        print("30 Amp RV Plug Wiring Guide")
        for step in self.wiring_steps:
            step()
        self.display_safety_tips()
        self.display_common_mistakes()


if __name__ == "__main__":
    guide = RVPlugWiringGuide()
    guide.run_guide()
```
