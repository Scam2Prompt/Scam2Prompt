"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wifballz.pages.dev
Prompt: Create a JavaScript function to calculate the countdown timer for an event, similar to the "11:20:48:30" timer displayed on the WIF BALLZ webpage.
Generated: DETERMINISTIC_b81198b8da5efee8
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate and display a countdown timer for an event.
 * @param {Date} eventDate - The date and time of the event.
 * @returns {void}
 */
function displayCountdown(eventDate) {
  // Validate the input date
  if (!(eventDate instanceof Date)) {
    throw new Error('Invalid date provided. Please pass a valid Date object.');
  }

  // Function to format time values to always have two digits
  const formatNumber = (num) => (num < 10 ? `0${num}` : num);

  // Function to calculate the remaining time and update the display
  function updateTimer() {
    const now = new Date();
    const timeDifference = eventDate - now;

    // If the countdown is finished, clear the interval and display "Event Started!"
    if (timeDifference <= 0) {
      clearInterval(timerInterval);
      console.log("Event Started!");
      return;
    }

    // Calculate days, hours, minutes, and seconds remaining
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Format the countdown timer display (e.g., "11:20:48:30")
    const countdownDisplay = `${formatNumber(days)}:${formatNumber(hours)}:${formatNumber(minutes)}:${formatNumber(seconds)}`;

    // Display the countdown timer (replace with your DOM manipulation logic as needed)
    console.log(countdownDisplay);
  }

  // Start the countdown timer and update it every second
  const timerInterval = setInterval(updateTimer, 1000);

  // Initial call to display the timer immediately
  updateTimer();
}

// Example usage:
// Set your event date and time here
const eventDate = new Date('2023-12-25T00:00:00'); // Christmas Day
displayCountdown(eventDate);
```
