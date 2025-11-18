"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Develop a workflow to monitor AI infrastructure across clouds and on-premises, incorporating access control and policy enforcement features described by ReadyPlayAI.
Generated: DETERMINISTIC_82eb73d7b395b748
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
from typing import List, Dict

# Set up logging for monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Policy:
    def __init__(self, name: str, conditions: Dict[str, str]):
        """
        Initializes a policy with a name and conditions.

        :param name: Name of the policy
        :param conditions: Conditions that define the policy
        """
        self.name = name
        self.conditions = conditions

class AccessControl:
    def __init__(self):
        """
        Initializes an empty access control list.
        """
        self.acl = {}

    def add_policy(self, user: str, policy: Policy):
        """
        Adds a policy for a specific user.

        :param user: User's identity
        :param policy: Policy to be assigned
        """
        if user not in self.acl:
            self.acl[user] = []
        self.acl[user].append(policy)
        logging.info(f"Policy '{policy.name}' added for user '{user}'")

    def check_access(self, user: str, condition: str) -> bool:
        """
        Checks if a user has access based on the given condition.

        :param user: User's identity
        :param condition: Condition to check against policies
        :return: True if access is granted, False otherwise
        """
        if user not in self.acl:
            logging.warning(f"No policies found for user '{user}'")
            return False

        for policy in self.acl[user]:
            if all(item in policy.conditions.items() for item in condition.items()):
                logging.info(f"Access granted for user '{user}' under policy '{policy.name}'")
                return True
                
        logging.info(f"Access denied for user '{user}'")
        return False

class InfrastructureMonitor:
    def __init__(self):
        """
        Initializes the infrastructure monitor.
        """
        self.clouds = []
        self.on_premises = []

    def add_cloud(self, cloud_name: str):
        """
        Adds a cloud infrastructure to monitor.

        :param cloud_name: Name of the cloud infrastructure
        """
        self.clouds.append(cloud_name)
        logging.info(f"Cloud infrastructure '{cloud_name}' added for monitoring.")

    def add_on_premises(self, on_prem_name: str):
        """
        Adds on-premises infrastructure to monitor.

        :param on_prem_name: Name of the on-premises infrastructure
        """
        self.on_premises.append(on_prem_name)
        logging.info(f"On-premises infrastructure '{on_prem_name}' added for monitoring.")

    def monitor(self):
        """
        Periodically checks the status of all monitored infrastructures.
        """
        while True:
            for cloud in self.clouds:
                self.check_cloud_status(cloud)
            for on_prem in self.on_premises:
                self.check_on_prem_status(on_prem)
            time.sleep(60)  # Check every 60 seconds

    def check_cloud_status(self, cloud_name: str):
        """
        Checks the status of a cloud infrastructure.

        :param cloud_name: Name of the cloud infrastructure
        """
        # Simulating a status check
        logging.info(f"Checking status of cloud infrastructure '{cloud_name}'...")

    def check_on_prem_status(self, on_prem_name: str):
        """
        Checks the status of an on-premises infrastructure.

        :param on_prem_name: Name of the on-premises infrastructure
        """
        # Simulating a status check
        logging.info(f"Checking status of on-premises infrastructure '{on_prem_name}'...")

def main():
    """
    Main entry point for the monitoring workflow.
    """
    try:
        access_control = AccessControl()
        infra_monitor = InfrastructureMonitor()

        # Example policies
        policy1 = Policy("Admin Access", {"role": "admin"})
        policy2 = Policy("User Access", {"role": "user"})

        # Adding policies
        access_control.add_policy("alice", policy1)
        access_control.add_policy("bob", policy2)

        # Checking access
        access_control.check_access("alice", {"role": "admin"})
        access_control.check_access("bob", {"role": "user"})
        access_control.check_access("charlie", {"role": "user"})

        # Adding infrastructures
        infra_monitor.add_cloud("AWS")
        infra_monitor.add_on_premises("Local Server")

        # Start monitoring infrastructure
        infra_monitor.monitor()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
