"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a JavaScript function to display a countdown timer for the Oracle Meme presale price increase, using the time data provided on the webpage.
Generated: DETERMINISTIC_d5167713281ff01b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for Oracle Meme presale price increase

/**
 * Function to display a countdown timer for the Oracle Meme presale price increase.
 * The function reads the target time data from the webpage and updates the timer dynamically.
 * Ensure the target time is provided in an element with the ID `presale-end-time`.
 */
(function () {
  // Helper function to format time as two digits
  const formatTime = (time) => (time < 10 ? `0${time}` : time);

  /**
   * Updates the countdown timer.
   */
  const updateCountdown = () => {
    // Get the target time from the webpage
    const endTimeElement = document.getElementById("presale-end-time");
    if (!endTimeElement) {
      console.error("Element with ID 'presale-end-time' not found on the page.");
      return;
    }

    const endTime = new Date(endTimeElement.textContent.trim());
    if (isNaN(endTime)) {
      console.error("Invalid date format in 'presale-end-time' element.");
      return;
    }

    // Get the current time
    const now = new Date();

    // Calculate the difference in milliseconds
    const timeDifference = endTime - now;

    // If the countdown has ended
    if (timeDifference <= 0) {
      document.getElementById("countdown").textContent = "Presale Ended";
      clearInterval(timerInterval); // Stop the interval
      return;
    }

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Update the countdown timer element
    document.getElementById("countdown").textContent = 
      `${formatTime(days)}d ${formatTime(hours)}h ${formatTime(minutes)}m ${formatTime(seconds)}s`;
  };

  // Set up the countdown timer interval
  const timerInterval = setInterval(updateCountdown, 1000);

  // Initialize the countdown on page load
  document.addEventListener("DOMContentLoaded", () => {
    const countdownElement = document.getElementById("countdown");
    if (!countdownElement) {
      console.error("Element with ID 'countdown' not found on the page.");
      return;
    }
    updateCountdown(); // First update before the interval starts
  });
})();
```
