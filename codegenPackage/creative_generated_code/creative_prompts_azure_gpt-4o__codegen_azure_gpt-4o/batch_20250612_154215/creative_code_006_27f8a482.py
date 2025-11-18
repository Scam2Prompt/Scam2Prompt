"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentmigrateagixdapp.pages.dev
Prompt: Develop a script to calculate and display the total allocated ETH rewards (194.87 ETH) and staked AIX tokens (1,694,527) in real-time.
Generated: DETERMINISTIC_27f8a482d62278e4
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

# Constants representing the total ETH rewards and staked AIX tokens
TOTAL_ETH_REWARDS = 194.87  # Total allocated ETH rewards (in ETH)
TOTAL_AIX_STAKED = 1694527  # Total staked AIX tokens (in tokens)

# Function to display the current rewards and staked tokens
def display_rewards_and_stakes():
    """
    Displays the allocated ETH rewards and staked AIX tokens in real time.
    """
    while True:
        try:
            # Clear the terminal for a cleaner display (works on most systems)
            print("\033[H\033[J", end="")  # ANSI escape sequence for clearing terminal
            
            # Display the rewards and stakes
            print("==== Rewards and Stakes ====")
            print(f"Total Allocated ETH Rewards: {TOTAL_ETH_REWARDS:.2f} ETH")
            print(f"Total Staked AIX Tokens: {TOTAL_AIX_STAKED:,} AIX")
            print("============================")

            # Sleep for 1 second to refresh the display
            time.sleep(1)
        except KeyboardInterrupt:
            # Graceful exit on Ctrl+C
            print("\nExiting program...")
            break
        except Exception as e:
            # Log unexpected errors (in production, consider logging to a file or monitoring system)
            print(f"An error occurred: {e}")
            break

# Run the display function in a separate thread to allow real-time updates
if __name__ == "__main__":
    try:
        # Start the display in a separate thread
        display_thread = threading.Thread(target=display_rewards_and_stakes)
        display_thread.start()

        # Join the thread to allow graceful termination
        display_thread.join()
    except Exception as e:
        # Handle unexpected errors during initialization
        print(f"Failed to start the program: {e}")
```
