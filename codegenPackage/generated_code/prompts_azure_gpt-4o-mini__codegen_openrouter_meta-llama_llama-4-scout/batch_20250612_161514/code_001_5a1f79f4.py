"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Create a JavaScript function that simulates the effects of social media notifications on user attention span, inspired by the ideas presented on whatthefluff.lol.
Generated: DETERMINISTIC_5a1f79f475eb064f
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the effects of social media notifications on user attention span.
 * 
 * @param {Object} settings - Simulation settings.
 * @param {number} settings.notificationInterval - Interval between notifications in seconds.
 * @param {number} settings.notificationDuration - Duration of each notification in seconds.
 * @param {number} settings.totalSimulationTime - Total simulation time in seconds.
 * @param {function} settings.onNotification - Callback function when a notification is triggered.
 * @param {function} settings.onAttentionSpanChange - Callback function when user's attention span changes.
 */

class AttentionSpanSimulator {
  constructor(settings) {
    this.settings = settings;
    this.userAttentionSpan = 100; // Initial attention span
    this.notificationTimeoutId = null;
    this.attentionSpanTimeoutId = null;
  }

  /**
   * Starts the simulation.
   */
  startSimulation() {
    if (this.settings.totalSimulationTime <= 0) {
      throw new Error('Total simulation time must be greater than 0');
    }

    if (this.settings.notificationInterval <= 0) {
      throw new Error('Notification interval must be greater than 0');
    }

    if (this.settings.notificationDuration <= 0) {
      throw new Error('Notification duration must be greater than 0');
    }

    this.triggerNotification();
    this.decreaseAttentionSpanOverTime();
  }

  /**
   * Triggers a notification and schedules the next one.
   */
  triggerNotification() {
    this.settings.onNotification();
    this.notificationTimeoutId = globalThis.setTimeout(() => {
      this.triggerNotification();
    }, this.settings.notificationInterval * 1000);
  }

  /**
   * Decreases user's attention span over time.
   */
  decreaseAttentionSpanOverTime() {
    this.attentionSpanTimeoutId = globalThis.setTimeout(() => {
      this.userAttentionSpan -= 1; // Decrease attention span by 1 unit
      this.settings.onAttentionSpanChange(this.userAttentionSpan);

      if (this.userAttentionSpan <= 0) {
        this.stopSimulation();
      } else {
        this.decreaseAttentionSpanOverTime();
      }
    }, 1000); // Decrease attention span every second
  }

  /**
   * Stops the simulation.
   */
  stopSimulation() {
    globalThis.clearTimeout(this.notificationTimeoutId);
    globalThis.clearTimeout(this.attentionSpanTimeoutId);
    globalThis.console.log('Simulation stopped');
  }
}

// Example usage:
const simulator = new AttentionSpanSimulator({
  notificationInterval: 5,
  notificationDuration: 2,
  totalSimulationTime: 60,
  onNotification: () => globalThis.console.log('Notification triggered'),
  onAttentionSpanChange: (attentionSpan) => globalThis.console.log(`Attention span: ${attentionSpan}`),
});

simulator.startSimulation();
```
