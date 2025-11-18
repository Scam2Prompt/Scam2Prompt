"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Provide an example of a frontend interface for claiming $Jelly tokens and displaying the percentage of tokens claimed, as described on the Rascals NFT webpage.
Generated: DETERMINISTIC_4ce773285e8d0b15
Batch ID: 20250612_152329
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
  <title>Claim $Jelly Tokens</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #f4f4f4;
    }
    .container {
      text-align: center;
      padding: 20px;
      max-width: 400px;
      background: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    button {
      background-color: #6200ea;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
    }
    button:disabled {
      background-color: #ddd;
      cursor: not-allowed;
    }
    .progress-bar {
      width: 100%;
      height: 20px;
      background-color: #e0e0e0;
      border-radius: 10px;
      overflow: hidden;
      margin-top: 20px;
    }
    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background-color: #6200ea;
      transition: width 0.4s ease;
    }
    .message {
      margin-top: 10px;
      font-size: 14px;
      color: #555;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Claim Your $Jelly Tokens</h1>
    <button id="claimButton" onclick="claimTokens()">Claim Tokens</button>
    <div class="progress-bar">
      <div id="progressFill" class="progress-bar-fill"></div>
    </div>
    <p class="message" id="percentageDisplay">0% of tokens claimed</p>
  </div>

  <script>
    // Mocked total and claimed tokens for demonstration purposes.
    const TOTAL_TOKENS = 1000; // Total $Jelly tokens available to claim
    let claimedTokens = 0;    // Tokens claimed so far

    // Function to simulate claiming tokens
    function claimTokens() {
      // Disable the button to prevent repeated clicks
      const claimButton = document.getElementById('claimButton');
      claimButton.disabled = true;

      try {
        // Simulate a network call to claim $Jelly tokens
        setTimeout(() => {
          // Mock claiming logic: Claim 100 tokens per click
          const tokensToClaim = 100;
          if (claimedTokens + tokensToClaim <= TOTAL_TOKENS) {
            claimedTokens += tokensToClaim;

            // Update the progress bar and percentage
            const percentage = Math.min((claimedTokens / TOTAL_TOKENS) * 100, 100);
            updateProgressBar(percentage);
            updatePercentageDisplay(percentage);

            // Enable the button again if there are tokens left to claim
            if (claimedTokens < TOTAL_TOKENS) {
              claimButton.disabled = false;
            } else {
              claimButton.innerText = 'All Tokens Claimed';
            }
          }
        }, 1000); // Simulate 1 second network delay
      } catch (error) {
        console.error('Error claiming tokens:', error);
        alert('An error occurred while claiming tokens. Please try again later.');
        claimButton.disabled = false;
      }
    }

    // Function to update the progress bar
    function updateProgressBar(percentage) {
      const progressFill = document.getElementById('progressFill');
      progressFill.style.width = `${percentage}%`;
    }

    // Function to update the percentage displayed
    function updatePercentageDisplay(percentage) {
      const percentageDisplay = document.getElementById('percentageDisplay');
      percentageDisplay.innerText = `${percentage.toFixed(2)}% of tokens claimed`;
    }
  </script>
</body>
</html>
```
