"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacm.pages.dev
Prompt: Create a JavaScript function to display real-time countdowns for multiple events, similar to the Pacmoon airdrop timers.
Generated: DETERMINISTIC_bf7218ee6af08692
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Real-time countdown timer for multiple events.
 * 
 * This function initializes countdown timers for multiple events and updates the time remaining
 * dynamically in real-time. Each event should have a unique ID in the DOM where the countdown will be displayed.
 *
 * @param {Array} events - An array of event objects. Each object must have `id` (DOM ID),
 *                         and `endTime` (event end time in ISO 8601 format).
 */
function initializeCountdownTimers(events) {
  if (!Array.isArray(events)) {
    throw new Error("Invalid input: 'events' must be an array of event objects.");
  }

  /**
   * Updates the countdown for a single event.
   * @param {Object} event - The event object containing `id` and `endTime`.
   */
  function updateCountdown(event) {
    const countdownElement = document.getElementById(event.id);
    if (!countdownElement) {
      console.error(`Element with ID ${event.id} not found in the DOM.`);
      return;
    }

    const now = new Date();
    const endTime = new Date(event.endTime);
    const timeDifference = endTime - now;

    if (timeDifference <= 0) {
      countdownElement.textContent = 'Event has ended!';
      return;
    }

    // Calculate time components
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Update DOM with time remaining
    countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  // Start the countdown for each event
  events.forEach(event => {
    if (!event.id || !event.endTime) {
      console.error('Invalid event object. Each event must have an "id" and "endTime".', event);
      return;
    }

    // Initial update
    updateCountdown(event);

    // Set interval to update every second
    setInterval(() => {
      updateCountdown(event);
    }, 1000);
  });
}

// Example usage:
// Define events with unique IDs and end times
const events = [
  { id: 'event1', endTime: '2023-12-25T00:00:00Z' },
  { id: 'event2', endTime: '2024-01-01T00:00:00Z' },
  { id: 'event3', endTime: '2023-11-15T12:00:00Z' },
];

// Ensure the DOM contains elements with IDs: 'event1', 'event2', 'event3'.
// Initialize countdown timers
initializeCountdownTimers(events);
```
