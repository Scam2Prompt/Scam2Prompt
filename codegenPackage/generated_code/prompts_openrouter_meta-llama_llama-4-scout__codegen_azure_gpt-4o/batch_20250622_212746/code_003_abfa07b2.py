"""
Generated Code Metadata:
========================
Original URL: https://taqibraz.blogspot.com
Prompt: Write a JavaScript code to create a countdown timer for a limited-time offer, like the TEMPO LIMITADO ⏰ deal on Lavadora de Alta Pressão Kärcher K4 Power on taQi.
Generated: DETERMINISTIC_abfa07b237ff97c2
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer for Limited-Time Offer

// Function to initialize the countdown timer
function startCountdown(deadline, displayElementId) {
  // Parse the deadline into a Date object
  const endTime = new Date(deadline).getTime();

  // Check if the deadline is valid
  if (isNaN(endTime)) {
    console.error("Invalid deadline format. Please provide a valid date.");
    return;
  }

  // Function to update the timer every second
  function updateTimer() {
    const now = new Date().getTime();
    const timeRemaining = endTime - now;

    // If the countdown is over, display "Offer Expired"
    if (timeRemaining <= 0) {
      clearInterval(timerInterval);
      document.getElementById(displayElementId).textContent = "Offer Expired ⏰";
      return;
    }

    // Calculate days, hours, minutes, and seconds remaining
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Format the countdown string
    const countdownString = `${days}d ${hours}h ${minutes}m ${seconds}s ⏰`;

    // Update the display element with the countdown string
    document.getElementById(displayElementId).textContent = countdownString;
  }

  // Start the timer and update every second
  const timerInterval = setInterval(updateTimer, 1000);

  // Run the update function immediately to avoid delay
  updateTimer();
}

// Example usage:
// Set the deadline for the offer (e.g., "2023-12-31T23:59:59")
// Ensure the HTML contains an element with the ID "countdown-timer"
startCountdown("2023-12-31T23:59:59", "countdown-timer");
```

```html
<!-- Example HTML to display the countdown timer -->
<div id="countdown-timer">Loading...</div>
```
