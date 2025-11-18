"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Generate a JavaScript function to simulate the LED Glyph Interface behavior described for the Nothing Phone (1) on BharatNews18, including customizable light patterns based on user notifications.
Generated: DETERMINISTIC_31b5bf1d8d573125
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the LED Glyph Interface behavior for notifications.
 * This function manages customizable light patterns for user notifications.
 *
 * @param {Array} patterns - An array of pattern objects describing the LED behavior.
 * Each pattern object should have the following properties:
 *   - `name` (string): The name of the notification pattern (e.g., "call", "message").
 *   - `sequence` (Array<number>): An array of integers representing LED on/off durations in milliseconds.
 *   - `repeat` (boolean): Whether to loop the pattern until stopped.
 * @param {string} notificationType - The type of notification (e.g., "call", "message").
 * @param {Function} onCompletion - A callback function invoked when the pattern ends (non-repeating patterns).
 */
function simulateLEDBasedOnNotification(patterns, notificationType, onCompletion) {
  // Retrieve the pattern matching the notification type
  const pattern = patterns.find((p) => p.name === notificationType);

  if (!pattern) {
    console.error(`No pattern found for notification type: ${notificationType}`);
    return;
  }

  const { sequence, repeat } = pattern;
  let currentStep = 0;
  let intervalId = null;

  // Helper function to simulate the LED toggle
  function toggleLED(state) {
    if (state) {
      console.log('LED ON'); // Simulating LED ON
    } else {
      console.log('LED OFF'); // Simulating LED OFF
    }
  }

  // Start the LED pattern sequence
  function startPattern() {
    intervalId = setInterval(() => {
      const duration = sequence[currentStep];
      toggleLED(currentStep % 2 === 0); // Turn LED ON for even steps, OFF for odd steps
      currentStep++;

      // Check if the pattern sequence is complete
      if (currentStep >= sequence.length) {
        if (repeat) {
          // Reset the step to loop the pattern
          currentStep = 0;
        } else {
          // Stop the pattern if it does not repeat
          stopPattern();
          if (onCompletion) onCompletion();
        }
      }
    }, sequence[currentStep]);
  }

  // Stop the LED pattern sequence
  function stopPattern() {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
      toggleLED(false); // Ensure the LED is turned off
      console.log('LED pattern stopped.');
    }
  }

  // Start the pattern
  console.log(`Starting LED pattern for notification type: ${notificationType}`);
  startPattern();

  // Return a function to allow stopping the pattern manually
  return stopPattern;
}

// Example usage:
const ledPatterns = [
  {
    name: 'call',
    sequence: [500, 500, 500, 500], // LED ON for 500ms, OFF for 500ms (repeated)
    repeat: true,
  },
  {
    name: 'message',
    sequence: [200, 200, 200, 200], // LED ON for 200ms, OFF for 200ms (repeated)
    repeat: false,
  },
];

// Simulate an incoming call
const stopCallPattern = simulateLEDBasedOnNotification(ledPatterns, 'call', () => {
  console.log('Call pattern completed.');
});

// Simulate a message
simulateLEDBasedOnNotification(ledPatterns, 'message', () => {
  console.log('Message pattern completed.');
});

// Stop the call pattern after 5 seconds
setTimeout(() => {
  if (stopCallPattern) stopCallPattern();
}, 5000);
```
