"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Create JavaScript code to display a countdown timer for a "limited-time discount" offer, as seen on the Depanten webpage.
Generated: DETERMINISTIC_4f5ba83af95dd784
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Limited-Time Discount Offer
 * This script displays a countdown timer on a webpage. When the countdown reaches zero,
 * it displays a message indicating the offer has expired.
 */

// Function to initialize the countdown timer
function startCountdown(durationInSeconds, displayElementId) {
  // Validate input parameters
  if (typeof durationInSeconds !== 'number' || durationInSeconds <= 0) {
    console.error('Invalid duration. Please provide a positive number.');
    return;
  }
  if (!document.getElementById(displayElementId)) {
    console.error('Invalid display element ID. Element does not exist.');
    return;
  }

  // Calculate hours, minutes, and seconds from the remaining time
  function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
    return {
      hours: hours.toString().padStart(2, '0'),
      minutes: minutes.toString().padStart(2, '0'),
      seconds: remainingSeconds.toString().padStart(2, '0'),
    };
  }

  // Update the countdown timer on the webpage
  function updateDisplay(time) {
    const displayElement = document.getElementById(displayElementId);
    displayElement.textContent = `${time.hours}:${time.minutes}:${time.seconds}`;
  }

  // Display "Offer Expired" message when countdown ends
  function showExpirationMessage() {
    const displayElement = document.getElementById(displayElementId);
    displayElement.textContent = 'Offer Expired';
    displayElement.style.color = 'red'; // Optional: Change text color to red
  }

  let remainingTime = durationInSeconds;
  const intervalId = setInterval(() => {
    if (remainingTime <= 0) {
      clearInterval(intervalId); // Stop the timer
      showExpirationMessage(); // Show expiration message
    } else {
      const formattedTime = formatTime(remainingTime);
      updateDisplay(formattedTime);
      remainingTime -= 1; // Decrease the remaining time by 1 second
    }
  }, 1000); // Update every second
}

// Example Usage:
// Add a <div> with id="countdown-timer" to your HTML to display the timer.
// Call the function with the desired duration (e.g., 3600 seconds for 1 hour).
document.addEventListener('DOMContentLoaded', () => {
  startCountdown(3600, 'countdown-timer'); // Set a 1-hour countdown
});
```
