"""
Generated Code Metadata:
========================
Original URL: https://donna-lopez-376.pages.dev
Prompt: Write a JavaScript code snippet to create a simple promotional webpage with a countdown timer for a limited-time offer, similar to the one implied on the given website.
Generated: DETERMINISTIC_0d3692beb43b6d55
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HTML structure for the promotional webpage
const htmlContent = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Limited-Time Offer</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      padding: 20px;
    }
    .offer {
      font-size: 24px;
      font-weight: bold;
      margin: 20px 0;
    }
    .countdown {
      font-size: 32px;
      color: #ff0000;
    }
    .expired {
      font-size: 24px;
      color: #888;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Special Limited-Time Offer!</h1>
    <p class="offer">Hurry up! This offer ends in:</p>
    <div id="countdown" class="countdown"></div>
  </div>
  <script>
    // Countdown Timer Logic
    (function() {
      // Set the end date and time for the offer
      const offerEndDate = new Date("2023-12-31T23:59:59").getTime();

      // Function to update the countdown timer
      function updateCountdown() {
        const now = new Date().getTime();
        const timeRemaining = offerEndDate - now;

        if (timeRemaining > 0) {
          // Calculate days, hours, minutes, and seconds
          const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
          const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

          // Display the countdown timer
          document.getElementById("countdown").textContent = 
            `${days}d ${hours}h ${minutes}m ${seconds}s`;
        } else {
          // If the offer has expired, display a message
          document.getElementById("countdown").textContent = "Offer has expired!";
          document.getElementById("countdown").className = "expired";
          clearInterval(timerInterval); // Stop the timer
        }
      }

      // Update the countdown every second
      const timerInterval = setInterval(updateCountdown, 1000);

      // Initial call to display the countdown immediately
      updateCountdown();
    })();
  </script>
</body>
</html>
`;

// Dynamically create and open the promotional webpage
const newWindow = window.open();
newWindow.document.write(htmlContent);
newWindow.document.close();
```
