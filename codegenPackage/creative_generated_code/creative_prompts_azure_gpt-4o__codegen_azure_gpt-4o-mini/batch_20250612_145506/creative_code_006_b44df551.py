"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indexapplc.rf.gd
Prompt: Create a step-by-step tutorial for selecting a hosting plan that includes unlimited disk space, multiple PHP versions, and free transfer from existing hosting providers.
Generated: DETERMINISTIC_b44df551f9129c4f
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPlan:
    def __init__(self, name, disk_space, php_versions, free_transfer):
        """
        Initialize a HostingPlan instance.

        Parameters:
        - name (str): The name of the hosting plan.
        - disk_space (str): Description of disk space offered.
        - php_versions (list): List of PHP versions supported.
        - free_transfer (bool): Indicates if free transfer is provided.
        """
        self.name = name
        self.disk_space = disk_space
        self.php_versions = php_versions
        self.free_transfer = free_transfer

    def display_details(self):
        """
        Display the details of the hosting plan.
        """
        print(f"Hosting Plan: {self.name}")
        print(f"Disk Space: {self.disk_space}")
        print(f"Supported PHP Versions: {', '.join(self.php_versions)}")
        print(f"Free Transfer: {'Yes' if self.free_transfer else 'No'}")


def select_hosting_plan(plans):
    """
    Select a hosting plan based on user criteria.

    Parameters:
    - plans (list): List of available hosting plans.

    Returns:
    - HostingPlan: The selected hosting plan.
    """
    print("Available Hosting Plans:")
    for index, plan in enumerate(plans):
        print(f"{index + 1}. {plan.name}")

    try:
        choice = int(input("Select a plan by number: ")) - 1
        if choice < 0 or choice >= len(plans):
            raise IndexError("Invalid selection. Please choose a valid plan number.")

        selected_plan = plans[choice]
        print("\nYou selected:")
        selected_plan.display_details()
        return selected_plan

    except ValueError:
        print("Error: Please enter a valid number.")
    except IndexError as e:
        print(f"Error: {e}")


def main():
    """
    Main function to run the hosting plan selection process.
    """
    # Sample hosting plans
    plans = [
        HostingPlan("Basic Plan", "Unlimited", ["7.4", "8.0"], True),
        HostingPlan("Pro Plan", "Unlimited", ["7.4", "8.0", "8.1"], True),
        HostingPlan("Business Plan", "Unlimited", ["7.4", "8.0", "8.1", "8.2"], True),
    ]

    # Select a hosting plan
    select_hosting_plan(plans)


if __name__ == "__main__":
    main()
```
