"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.ca
Prompt: Generate a tutorial script for setting up a parked domain with Hostinger, including steps to activate nameservers.
Generated: DETERMINISTIC_74c8bdb818602440
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Hostinger Parked Domain Setup Tutorial Script

This script provides a step-by-step guide for setting up a parked domain with Hostinger,
including activating nameservers. It simulates the process with user interaction.
"""

import sys
import time
from typing import Optional

class HostingerTutorial:
    def __init__(self):
        self.domain_name: Optional[str] = None
        self.steps_completed = 0
        self.total_steps = 6

    def display_header(self) -> None:
        """Display the tutorial header."""
        print("\n" + "="*50)
        print("Hostinger Parked Domain Setup Tutorial".center(50))
        print("="*50 + "\n")

    def get_domain_name(self) -> None:
        """Prompt user for domain name."""
        while True:
            self.domain_name = input("Enter the domain name you want to park (e.g., example.com): ").strip()
            if self.domain_name and "." in self.domain_name:
                break
            print("Error: Please enter a valid domain name (e.g., example.com)")
        self.steps_completed += 1

    def login_to_hostinger(self) -> None:
        """Simulate login to Hostinger."""
        print(f"\nStep {self.steps_completed}/{self.total_steps}: Log in to your Hostinger account")
        input("Press Enter after you've logged in to your Hostinger account...")
        self.steps_completed += 1

    def navigate_to_domains_section(self) -> None:
        """Guide to domains section."""
        print(f"\nStep {self.steps_completed}/{self.total_steps}: Navigate to 'Domains' section")
        print("1. Click on 'Hosting' in the top menu")
        print("2. Select 'Domains' from the dropdown")
        input("Press Enter when you're in the Domains section...")
        self.steps_completed += 1

    def add_parked_domain(self) -> None:
        """Guide through adding parked domain."""
        print(f"\nStep {self.steps_completed}/{self.total_steps}: Add parked domain")
        print(f"1. Click 'Add Domain' button")
        print(f"2. Select 'Park Domain' option")
        print(f"3. Enter '{self.domain_name}' in the domain field")
        print("4. Click 'Add' button")
        input("Press Enter after adding the parked domain...")
        self.steps_completed += 1

    def configure_nameservers(self) -> None:
        """Guide through nameserver configuration."""
        print(f"\nStep {self.steps_completed}/{self.total_steps}: Configure nameservers")
        print("1. Go to your domain registrar's website (where you purchased the domain)")
        print("2. Find the DNS or Nameserver settings")
        print("3. Replace existing nameservers with Hostinger's:")
        print("   - ns1.hostinger.com")
        print("   - ns2.hostinger.com")
        print("   - ns3.hostinger.com")
        print("   - ns4.hostinger.com")
        print("4. Save changes")
        input("Press Enter after updating nameservers...")
        self.steps_completed += 1

    def verify_setup(self) -> None:
        """Guide through verification process."""
        print(f"\nStep {self.steps_completed}/{self.total_steps}: Verify setup")
        print("1. Wait 24-48 hours for DNS propagation")
        print("2. Visit your domain in a browser to verify it's parked")
        print(f"3. You should see a default Hostinger parked page for {self.domain_name}")
        self.steps_completed += 1

    def run_tutorial(self) -> None:
        """Run the complete tutorial."""
        try:
            self.display_header()
            self.get_domain_name()
            self.login_to_hostinger()
            self.navigate_to_domains_section()
            self.add_parked_domain()
            self.configure_nameservers()
            self.verify_setup()

            print("\n" + "="*50)
            print("Tutorial Completed Successfully!".center(50))
            print("="*50)
            print(f"\nYour domain {self.domain_name} is now parked with Hostinger.")
            print("Note: DNS changes may take up to 48 hours to propagate globally.")

        except KeyboardInterrupt:
            print("\n\nTutorial was interrupted. You can restart it anytime.")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    tutorial = HostingerTutorial()
    tutorial.run_tutorial()
```
