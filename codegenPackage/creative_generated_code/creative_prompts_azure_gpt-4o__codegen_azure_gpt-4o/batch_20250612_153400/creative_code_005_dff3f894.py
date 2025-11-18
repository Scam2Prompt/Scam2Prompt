"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Create a countdown timer in JavaScript that displays the remaining time for users to register within the next 48 hours for a PWA event.
Generated: DETERMINISTIC_dff3f894f943aceb
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
 * Countdown Timer for PWA Event Registration
 * This script creates a countdown timer that displays the remaining time 
 * for users to register within the next 48 hours.
 */

// Set the deadline for the countdown (current time + 48 hours)
const deadline = new Date(Date.now() + 48 * 60 * 60 * 1000); // 48 hours from now

/**
 * Formats a number to always display two digits.
 * @param {number} num - The number to format.
 * @returns {string} - Formatted number as a string (e.g., 04, 12, etc.).
 */
const formatNumber = (num) => (num < 10 ? '0' + num : num);

/**
 * Updates the countdown timer and displays remaining time.
 */
function updateCountdown() {
  const now = new Date(); // Current time
  const timeRemaining = deadline - now; // Time remaining in milliseconds

  if (timeRemaining <= 0) {
    // If the countdown ends
    clearInterval(timerInterval); // Stop the interval timer
    document.getElementById('countdown').textContent = "Registration has ended!";
    return;
  }

  // Calculate remaining time components
  const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

  // Display the countdown in a readable format
  const formattedTime = `${formatNumber(days)}d ${formatNumber(hours)}h ${formatNumber(minutes)}m ${formatNumber(seconds)}s`;
  document.getElementById('countdown').textContent = formattedTime;
}

// Start updating the countdown timer every second
const timerInterval = setInterval(updateCountdown, 1000);

// Initial call to display the correct time immediately
updateCountdown();

/**
 * HTML snippet for reference:
 * <div id="countdown"></div>
 */
```
