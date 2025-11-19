"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-staking.vercel.app
Prompt: How do I enable JavaScript to run the Sui staking app effectively?
Generated: DETERMINISTIC_7d1f41d5a7dc232d
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sui Staking App</title>
  <link rel="stylesheet" href="styles.css"> <!-- External stylesheet -->
</head>
<body>
  <div id="app">
    <h1>Sui Staking App</h1>
    <p id="status"></p>
    <button id="stakeButton">Stake SUI</button>
    <button id="unstakeButton" disabled>Unstake SUI</button>
  </div>

  <script>
    // Ensure the DOM is fully loaded before running scripts
    document.addEventListener('DOMContentLoaded', () => {
      // DOM elements
      const statusElement = document.getElementById('status');
      const stakeButton = document.getElementById('stakeButton');
      const unstakeButton = document.getElementById('unstakeButton');

      // Application state
      let isStaked = false;

      // Update the application status text
      const updateStatus = () => {
        statusElement.textContent = isStaked 
          ? 'Your SUI is currently staked.' 
          : 'Your SUI is not staked.';
      };

      // Handle staking action
      const handleStake = () => {
        try {
          isStaked = true; // Update the application state
          stakeButton.disabled = true; // Disable staking button
          unstakeButton.disabled = false; // Enable unstaking button
          updateStatus(); // Refresh the status text
        } catch (error) {
          console.error('Error while staking:', error); // Log the error
          alert('An error occurred while staking your SUI.'); // Inform the user
        }
      };

      // Handle unstaking action
      const handleUnstake = () => {
        try {
          isStaked = false; // Update the application state
          stakeButton.disabled = false; // Enable staking button
          unstakeButton.disabled = true; // Disable unstaking button
          updateStatus(); // Refresh the status text
        } catch (error) {
          console.error('Error while unstaking:', error); // Log the error
          alert('An error occurred while unstaking your SUI.'); // Inform the user
        }
      };

      // Attach event listeners to buttons
      stakeButton.addEventListener('click', handleStake);
      unstakeButton.addEventListener('click', handleUnstake);

      // Initialize application state on load
      updateStatus();
    });
  </script>
</body>
</html>
```
