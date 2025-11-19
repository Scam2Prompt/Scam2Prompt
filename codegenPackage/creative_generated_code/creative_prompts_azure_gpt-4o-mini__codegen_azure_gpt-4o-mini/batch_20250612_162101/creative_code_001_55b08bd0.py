"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: Recommend an API for creating customizable countdown timers for web applications.
Generated: DETERMINISTIC_55b08bd0033d5b39
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CountdownTimer.js
class CountdownTimer {
    constructor(duration, onTick, onComplete) {
        // Validate input parameters
        if (typeof duration !== 'number' || duration <= 0) {
            throw new Error('Duration must be a positive number');
        }
        if (typeof onTick !== 'function') {
            throw new Error('onTick must be a function');
        }
        if (typeof onComplete !== 'function') {
            throw new Error('onComplete must be a function');
        }

        this.duration = duration; // Duration in seconds
        this.onTick = onTick;     // Callback for each tick
        this.onComplete = onComplete; // Callback when countdown completes
        this.remainingTime = duration; // Time left in countdown
        this.intervalId = null;    // Store interval ID for cleanup
    }

    // Start the countdown timer
    start() {
        if (this.intervalId) {
            throw new Error('Timer is already running');
        }

        this.intervalId = setInterval(() => {
            this.remainingTime--;
            this.onTick(this.remainingTime);

            if (this.remainingTime <= 0) {
                this.stop();
                this.onComplete();
            }
        }, 1000); // Tick every second
    }

    // Stop the countdown timer
    stop() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    // Reset the countdown timer
    reset(newDuration) {
        this.stop(); // Stop any existing timer
        if (newDuration) {
            if (typeof newDuration !== 'number' || newDuration <= 0) {
                throw new Error('New duration must be a positive number');
            }
            this.duration = newDuration;
        }
        this.remainingTime = this.duration;
        this.onTick(this.remainingTime); // Update the tick with the new duration
    }
}

// Usage example:
const timer = new CountdownTimer(
    10, // Duration in seconds
    (remainingTime) => {
        console.log(`Time remaining: ${remainingTime} seconds`);
    },
    () => {
        console.log('Countdown complete!');
    }
);

// Start the countdown
timer.start();

// To reset the timer after 5 seconds
setTimeout(() => {
    timer.reset(15); // Reset to 15 seconds
    timer.start();   // Start the new countdown
}, 5000);
```
