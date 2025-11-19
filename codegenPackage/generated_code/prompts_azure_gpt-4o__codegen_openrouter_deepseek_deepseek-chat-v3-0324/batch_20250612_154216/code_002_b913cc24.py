"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: Generate a troubleshooting guide in Python for diagnosing issues with proportioning valves in brake systems, incorporating information from The Ram Man's troubleshooting videos.
Generated: DETERMINISTIC_b913cc24ecbc407a
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brake Proportioning Valve Troubleshooting Guide
This script provides a step-by-step guide to diagnose issues with proportioning valves in brake systems,
based on The Ram Man's troubleshooting videos.
"""

import sys
from enum import Enum, auto

class BrakeIssue(Enum):
    """Enumeration of common brake proportioning valve issues"""
    FRONT_BRAKES_LOCKING = auto()
    REAR_BRAKES_LOCKING = auto()
    BRAKE_PEDAL_SPONGY = auto()
    BRAKE_PEDAL_HARD = auto()
    BRAKE_FLUID_LEAK = auto()
    BRAKE_LIGHT_ON = auto()
    UNEVEN_BRAKING = auto()

class TroubleshootingGuide:
    """Main class for the troubleshooting guide"""
    
    def __init__(self):
        self.issues = {
            BrakeIssue.FRONT_BRAKES_LOCKING: self._front_brakes_locking,
            BrakeIssue.REAR_BRAKES_LOCKING: self._rear_brakes_locking,
            BrakeIssue.BRAKE_PEDAL_SPONGY: self._brake_pedal_spongy,
            BrakeIssue.BRAKE_PEDAL_HARD: self._brake_pedal_hard,
            BrakeIssue.BRAKE_FLUID_LEAK: self._brake_fluid_leak,
            BrakeIssue.BRAKE_LIGHT_ON: self._brake_light_on,
            BrakeIssue.UNEVEN_BRAKING: self._uneven_braking
        }
    
    def start_diagnosis(self):
        """Main entry point for the troubleshooting guide"""
        print("Brake Proportioning Valve Troubleshooting Guide")
        print("Based on The Ram Man's troubleshooting videos\n")
        
        try:
            self._display_menu()
            issue = self._get_user_choice()
            self.issues[issue]()
        except KeyboardInterrupt:
            print("\n\nDiagnosis cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            sys.exit(1)
    
    def _display_menu(self):
        """Display the menu of common issues"""
        print("Select the issue you're experiencing:")
        for i, issue in enumerate(BrakeIssue, 1):
            print(f"{i}. {issue.name.replace('_', ' ').title()}")
        print("0. Exit\n")
    
    def _get_user_choice(self) -> BrakeIssue:
        """Get and validate user input"""
        while True:
            try:
                choice = int(input("Enter your choice (0 to exit): "))
                if choice == 0:
                    print("Exiting troubleshooting guide.")
                    sys.exit(0)
                if 1 <= choice <= len(BrakeIssue):
                    return list(BrakeIssue)[choice - 1]
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _front_brakes_locking(self):
        """Diagnose front brakes locking issues"""
        print("\n--- Front Brakes Locking Diagnosis ---")
        print("1. Check proportioning valve adjustment")
        print("2. Inspect front brake calipers for sticking")
        print("3. Verify front brake hose condition (no restrictions)")
        print("4. Check master cylinder pushrod adjustment")
        print("5. Test proportioning valve pressure (front circuit)")
        print("\nRecommended action: Adjust or replace proportioning valve if front pressure is too high")
    
    def _rear_brakes_locking(self):
        """Diagnose rear brakes locking issues"""
        print("\n--- Rear Brakes Locking Diagnosis ---")
        print("1. Verify proportioning valve is properly adjusted")
        print("2. Check rear brake shoe adjustment")
        print("3. Inspect rear wheel cylinders for proper operation")
        print("4. Test proportioning valve pressure (rear circuit)")
        print("5. Check for contaminated brake linings")
        print("\nRecommended action: Adjust proportioning valve or replace if rear pressure is too high")
    
    def _brake_pedal_spongy(self):
        """Diagnose spongy brake pedal issues"""
        print("\n--- Spongy Brake Pedal Diagnosis ---")
        print("1. Bleed brake system to remove air")
        print("2. Check for leaks in hydraulic system")
        print("3. Inspect proportioning valve for internal leaks")
        print("4. Verify master cylinder operation")
        print("5. Check brake hose condition (no bulging)")
        print("\nRecommended action: Replace proportioning valve if internal leaks are found")
    
    def _brake_pedal_hard(self):
        """Diagnose hard brake pedal issues"""
        print("\n--- Hard Brake Pedal Diagnosis ---")
        print("1. Check power brake booster operation")
        print("2. Inspect brake pedal linkage")
        print("3. Verify proportioning valve isn't stuck")
        print("4. Check for restrictions in brake lines")
        print("5. Test master cylinder operation")
        print("\nRecommended action: Replace proportioning valve if stuck or malfunctioning")
    
    def _brake_fluid_leak(self):
        """Diagnose brake fluid leak issues"""
        print("\n--- Brake Fluid Leak Diagnosis ---")
        print("1. Visually inspect all brake lines and connections")
        print("2. Check proportioning valve for external leaks")
        print("3. Inspect wheel cylinders and calipers")
        print("4. Verify master cylinder reservoir and connections")
        print("5. Check brake hose condition")
        print("\nRecommended action: Replace proportioning valve if leaking at body or connections")
    
    def _brake_light_on(self):
        """Diagnose brake warning light issues"""
        print("\n--- Brake Warning Light Diagnosis ---")
        print("1. Check parking brake switch")
        print("2. Verify brake fluid level")
        print("3. Test proportioning valve pressure differential switch")
        print("4. Inspect wiring to warning light")
        print("5. Check for pressure imbalance between circuits")
        print("\nRecommended action: Replace proportioning valve if differential switch is faulty")
    
    def _uneven_braking(self):
        """Diagnose uneven braking issues"""
        print("\n--- Uneven Braking Diagnosis ---")
        print("1. Check tire pressure and condition")
        print("2. Inspect brake pad/shoe wear patterns")
        print("3. Verify proportioning valve pressure balance")
        print("4. Check for sticking calipers or wheel cylinders")
        print("5. Test front-to-rear brake balance")
        print("\nRecommended action: Adjust or replace proportioning valve if pressure balance is incorrect")

if __name__ == "__main__":
    guide = TroubleshootingGuide()
    guide.start_diagnosis()
```
