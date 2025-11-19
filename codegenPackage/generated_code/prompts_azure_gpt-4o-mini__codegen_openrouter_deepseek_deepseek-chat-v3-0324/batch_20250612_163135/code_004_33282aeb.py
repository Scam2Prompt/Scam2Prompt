"""
Generated Code Metadata:
========================
Original URL: https://debank.lu
Prompt: Explain how to troubleshoot electrical issues using a Honda Fourtrax 300 wiring diagram. What key areas should I check?
Generated: DETERMINISTIC_33282aeb37615fb5
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the user request is about troubleshooting electrical issues using a wiring diagram (not a programming task), there isn't actual code to generate. However, I can provide a Python script that could serve as a basic wiring diagram analyzer or troubleshooting guide helper:

```python
"""
Honda Fourtrax 300 Electrical Troubleshooting Tool
This script provides guidance for checking key areas in the ATV's electrical system.
"""

class ElectricalTroubleshooter:
    """Helper class for troubleshooting Honda Fourtrax 300 electrical issues."""
    
    def __init__(self):
        self.common_issues = {
            'no_power': [
                "1. Check main fuse (usually 30A)",
                "2. Inspect battery connections for corrosion",
                "3. Verify battery voltage (should be ~12.6V)",
                "4. Check ignition switch connections"
            ],
            'no_spark': [
                "1. Inspect spark plug and wire",
                "2. Check pulse generator resistance (should be 400-600 ohms)",
                "3. Test ignition coil primary/secondary windings",
                "4. Verify CDI unit connections"
            ],
            'lighting_issues': [
                "1. Check bulb condition",
                "2. Inspect lighting circuit fuses",
                "3. Verify voltage at light connector",
                "4. Check handlebar switch contacts"
            ],
            'starting_problems': [
                "1. Verify starter relay operation",
                "2. Check starter button contacts",
                "3. Inspect starter motor connections",
                "4. Test neutral safety switch"
            ]
        }
        
        self.key_checkpoints = [
            "Battery and connections",
            "Main fuse",
            "Ignition switch",
            "Ground connections",
            "Wiring harness for damage",
            "Connectors for corrosion",
            "Fuse box",
            "Voltage regulator",
            "Starter relay",
            "CDI unit"
        ]

    def get_troubleshooting_steps(self, issue):
        """Returns troubleshooting steps for common electrical issues."""
        return self.common_issues.get(issue.lower(), ["Unknown issue. Please consult the wiring diagram."])

    def get_key_checkpoints(self):
        """Returns key areas to inspect in the electrical system."""
        return self.key_checkpoints

    def print_system_check(self):
        """Prints a systematic check of the electrical system."""
        print("\nSystematic Electrical Check:")
        for i, checkpoint in enumerate(self.key_checkpoints, 1):
            print(f"{i}. {checkpoint}")


if __name__ == "__main__":
    troubleshooter = ElectricalTroubleshooter()
    
    print("Honda Fourtrax 300 Electrical Troubleshooting Guide")
    print("Common issues: no_power, no_spark, lighting_issues, starting_problems")
    
    issue = input("\nEnter your electrical issue (or 'system_check' for full system check): ")
    
    if issue.lower() == 'system_check':
        troubleshooter.print_system_check()
    else:
        steps = troubleshooter.get_troubleshooting_steps(issue)
        print(f"\nTroubleshooting steps for {issue}:")
        for step in steps:
            print(f"- {step}")
```
