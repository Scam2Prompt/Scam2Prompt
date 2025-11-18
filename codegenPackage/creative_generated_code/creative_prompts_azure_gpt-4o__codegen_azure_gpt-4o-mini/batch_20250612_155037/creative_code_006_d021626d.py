"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eiizaos-ai.com
Prompt: Create a script to monitor and log AI agent activity on ElizaOS using Eliza Labs tools.
Generated: DETERMINISTIC_d021626d3c542e01
Batch ID: 20250612_155037
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
from eliza_labs import ElizaOSAgent, ElizaOSMonitor  # Assume these are provided by Eliza Labs

# Configure logging
logging.basicConfig(
    filename='ai_agent_activity.log',  # Log file
    level=logging.INFO,                 # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def monitor_agent_activity(agent_name: str, monitor_duration: int):
    """
    Monitors the activity of a specified AI agent on ElizaOS.

    Args:
        agent_name (str): The name of the AI agent to monitor.
        monitor_duration (int): The duration in seconds for monitoring.

    Raises:
        ValueError: If monitor_duration is not a positive integer.
        Exception: For any unexpected errors during monitoring.
    """
    if monitor_duration <= 0:
        raise ValueError("monitor_duration must be a positive integer.")

    # Initialize the agent and monitor
    agent = ElizaOSAgent(name=agent_name)
    monitor = ElizaOSMonitor(agent)

    # Start monitoring
    logging.info(f"Starting to monitor agent: {agent_name} for {monitor_duration} seconds.")
    start_time = time.time()

    try:
        while time.time() - start_time < monitor_duration:
            activity = monitor.get_activity()  # Fetch the current activity of the agent
            logging.info(f"Agent Activity - {activity}")
            time.sleep(5)  # Log activity every 5 seconds

    except Exception as e:
        logging.error(f"Error monitoring agent activity: {str(e)}")
    finally:
        logging.info(f"Finished monitoring agent: {agent_name}.")

if __name__ == "__main__":
    # Example usage: Monitor the agent 'ElizaBot' for 60 seconds
    try:
        monitor_agent_activity('ElizaBot', 60)
    except ValueError as ve:
        logging.error(f"Value Error: {str(ve)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
```
