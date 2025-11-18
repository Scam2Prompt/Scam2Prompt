"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Generate code to track and manage user data metrics, such as total users and daily unique IPs, using Particle Network's SDK.
Generated: DETERMINISTIC_d64d78ce39d0597f
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from particle_network.sdk import ParticleNetwork

# Set up Particle Network SDK
# Replace "your_project_id" and "your_api_key" with appropriate credentials
PROJECT_ID = "your_project_id"
API_KEY = "your_api_key"
particle = ParticleNetwork(project_id=PROJECT_ID, api_key=API_KEY)

# Initialize metrics tracking
user_metrics = {
    "total_users": 0,
    "daily_unique_ips": {},
}

def register_user(user_id, ip_address):
    """
    Register a new user and track unique IPs for the day.
    
    :param user_id: Unique identifier for the user
    :param ip_address: IP address of the user
    """
    try:
        # Add user to Particle Network
        response = particle.add_user(user_id)
        if response["success"]:
            user_metrics["total_users"] += 1
            print(f"User {user_id} added successfully.")
        else:
            print(f"Failed to add user {user_id}. Error: {response['message']}")

        # Track unique IPs for the day
        today = datetime.date.today()
        if today not in user_metrics["daily_unique_ips"]:
            user_metrics["daily_unique_ips"][today] = set()

        user_metrics["daily_unique_ips"][today].add(ip_address)

    except Exception as e:
        print(f"Error registering user {user_id} with IP {ip_address}: {e}")

def get_metrics():
    """
    Retrieve current metrics.
    
    :return: Dictionary containing total users and daily unique IP counts
    """
    try:
        today = datetime.date.today()
        unique_ip_count = len(user_metrics["daily_unique_ips"].get(today, set()))
        return {
            "total_users": user_metrics["total_users"],
            "daily_unique_ips": unique_ip_count,
        }
    except Exception as e:
        print(f"Error retrieving metrics: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Register example users
    register_user("user1", "192.168.1.1")
    register_user("user2", "192.168.1.2")
    register_user("user3", "192.168.1.1")  # Duplicate IP for the day

    # Get metrics
    metrics = get_metrics()
    print(f"Total Users: {metrics['total_users']}")
    print(f"Daily Unique IPs: {metrics['daily_unique_ips']}")
```
