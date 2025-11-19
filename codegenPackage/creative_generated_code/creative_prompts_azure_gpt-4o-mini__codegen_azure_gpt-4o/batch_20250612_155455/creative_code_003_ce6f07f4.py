"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestai.xyz
Prompt: What are the steps to monitor AI agent performance in real-time using the advanced performance analytics features of Celest AI?
Generated: DETERMINISTIC_ce6f07f493b158ed
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import celest_ai
import time

# Initialize Celest AI's performance monitoring system
def initialize_monitoring(api_key):
    """
    Initialize the Celest AI monitoring system using the provided API key.

    Args:
        api_key (str): API key for authentication with Celest AI.

    Returns:
        monitoring_session (object): Instance of Celest AI monitoring session.
    """
    try:
        # Authenticate with Celest AI
        monitoring_session = celest_ai.Monitor(api_key=api_key)
        print("Successfully connected to Celest AI performance monitoring system.")
        return monitoring_session
    except Exception as e:
        print(f"Error initializing monitoring session: {e}")
        raise

# Function to monitor AI agent performance in real-time
def monitor_agent_performance(monitoring_session, agent_id, duration=60, frequency=5):
    """
    Monitor AI agent performance in real-time using Celest AI.

    Args:
        monitoring_session (object): Authenticated Celest AI monitoring session.
        agent_id (str): Unique identifier of the AI agent to be monitored.
        duration (int): Total monitoring duration in seconds (default=60).
        frequency (int): Frequency of data collection in seconds (default=5).
    """
    try:
        print(f"Starting real-time monitoring for agent '{agent_id}'...")
        start_time = time.time()
        while time.time() - start_time < duration:
            # Fetch performance metrics for the agent
            metrics = monitoring_session.get_agent_metrics(agent_id=agent_id)
            
            # Log or process the metrics (for demonstration, print them)
            print(f"Real-time metrics for agent '{agent_id}': {metrics}")
            
            # Wait for the specified frequency before fetching metrics again
            time.sleep(frequency)
        print(f"Completed monitoring for agent '{agent_id}'.")
    except Exception as e:
        print(f"Error during monitoring: {e}")
        raise

# Main function to set up and run the monitoring process
def main():
    """
    Main function to execute the AI agent performance monitoring workflow.
    """
    # Replace 'your_api_key_here' with your actual Celest AI API key
    API_KEY = "your_api_key_here"

    # Replace 'your_agent_id_here' with the AI agent's unique identifier
    AGENT_ID = "your_agent_id_here"
    
    # Create an authenticated session with Celest AI
    monitoring_session = initialize_monitoring(api_key=API_KEY)
    
    # Monitor the agent's performance for 60 seconds, collecting data every 5 seconds
    monitor_agent_performance(monitoring_session, agent_id=AGENT_ID, duration=60, frequency=5)

# Entry point for the script
if __name__ == "__main__":
    main()
```
