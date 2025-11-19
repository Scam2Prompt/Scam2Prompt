"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft4.web.app
Prompt: Create a code snippet to display the countdown timer for the $LOYAL airdrop closing time on a webpage.
Generated: DETERMINISTIC_960b6ad6832d21db
Batch ID: 20250612_162521
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
  <title>$LOYAL Airdrop Countdown</title>
  <style>
    /* Style for the countdown timer */
    #countdown {
      font-family: Arial, sans-serif;
      font-size: 2rem;
      color: #333;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div id="countdown">
    <!-- Placeholder for the countdown timer -->
    Loading countdown...
  </div>

  <script>
    /**
     * Function to update the countdown timer on the webpage
     */
    function updateCountdown(endTime) {
      const countdownElement = document.getElementById('countdown');
      
      // Update the timer every second
      const interval = setInterval(() => {
        const now = new Date().getTime(); // Current time in milliseconds
        const timeRemaining = endTime - now; // Calculate time remaining
        
        // If the countdown has ended, stop the timer and display message
        if (timeRemaining <= 0) {
          clearInterval(interval);
          countdownElement.textContent = "The $LOYAL airdrop has closed!";
          return;
        }

        // Calculate remaining days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Display the countdown timer
        countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
      }, 1000);
    }

    /**
     * Entry point: Initialize the countdown timer
     */
    (function initializeCountdown() {
      try {
        // Define the closing time for the $LOYAL airdrop (update as necessary)
        const closingTime = new Date('2023-12-31T23:59:59Z').getTime(); // UTC time
        
        // Validate the closing time
        if (isNaN(closingTime)) {
          throw new Error("Invalid closing time for the $LOYAL airdrop.");
        }
        
        // Start the countdown
        updateCountdown(closingTime);
      } catch (error) {
        console.error("Error initializing countdown timer:", error.message);
        document.getElementById('countdown').textContent = "Error loading countdown timer. Please try again later.";
      }
    })();
  </script>
</body>
</html>
```
