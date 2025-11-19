"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Generate a JavaScript code snippet to implement a countdown timer, similar to the "Ưu đãi giờ vàng" (Golden Hour Promotion) countdown timer on TikTok Shop VN, which ends after a certain period.
Generated: DETERMINISTIC_55c12dccc03c427f
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer Implementation
 * This script creates a countdown timer that ends after a specified duration.
 * The timer updates every second and displays the remaining time in HH:MM:SS format.
 */

// Function to format time as HH:MM:SS
function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  // Pad with leading zeros for consistent formatting
  return [
    hours.toString().padStart(2, '0'),
    minutes.toString().padStart(2, '0'),
    secs.toString().padStart(2, '0'),
  ].join(':');
}

/**
 * Countdown Timer
 * @param {number} durationInSeconds - The total duration of the countdown in seconds.
 * @param {function} onTick - Callback function executed every second with the remaining time.
 * @param {function} onComplete - Callback function executed when the countdown ends.
 */
function startCountdownTimer(durationInSeconds, onTick, onComplete) {
  let remainingTime = durationInSeconds;

  // Validate input
  if (typeof durationInSeconds !== 'number' || durationInSeconds <= 0) {
    throw new Error('Invalid duration. Please provide a positive number.');
  }
  if (typeof onTick !== 'function' || typeof onComplete !== 'function') {
    throw new Error('Invalid callbacks. Please provide valid functions for onTick and onComplete.');
  }

  // Timer interval
  const timerInterval = setInterval(() => {
    // Execute the onTick callback with the formatted remaining time
    onTick(formatTime(remainingTime));

    // Decrement remaining time
    remainingTime--;

    // Check if the countdown has ended
    if (remainingTime < 0) {
      clearInterval(timerInterval); // Stop the timer
      onComplete(); // Execute the onComplete callback
    }
  }, 1000);
}

// Example usage
const duration = 3600; // 1 hour in seconds

startCountdownTimer(
  duration,
  (remainingTime) => {
    console.log(`Time left: ${remainingTime}`); // Update UI or log remaining time
  },
  () => {
    console.log('Countdown complete!'); // Handle completion (e.g., show promotion end message)
  }
);
```
