"""
Generated Code Metadata:
========================
Original URL: https://polymarketscanner.com
Prompt: "Generate JavaScript code to create a real-time update of the next fetch and flush intervals for Polymarket polls as shown on https://polymarketscanner.com."
Generated: DETERMINISTIC_e8b5caff66b09b89
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Real-time update of next fetch and flush intervals for Polymarket polls.
 * This code calculates and updates the intervals dynamically based on the current time.
 */

// Configuration constants
const FETCH_INTERVAL_MINUTES = 5; // Polymarket polls are fetched every 5 minutes
const FLUSH_INTERVAL_HOURS = 24; // Polymarket polls are flushed every 24 hours

/**
 * Calculates the time remaining until the next interval.
 * @param {number} intervalDuration - Duration of the interval in milliseconds
 * @param {number} offset - Optional offset in milliseconds (default: 0)
 * @returns {Object} An object containing minutes and seconds remaining
 */
function getTimeUntilNextInterval(intervalDuration, offset = 0) {
    const now = new Date();
    const currentTime = now.getTime();
    const nextInterval = Math.ceil((currentTime - offset) / intervalDuration) * intervalDuration + offset;
    const timeRemaining = nextInterval - currentTime;

    const minutes = Math.floor(timeRemaining / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    return { minutes, seconds };
}

/**
 * Updates the UI with the next fetch and flush times.
 */
function updateIntervalsDisplay() {
    try {
        // Calculate next fetch time (aligned to 5-minute intervals)
        const fetchIntervalMs = FETCH_INTERVAL_MINUTES * 60 * 1000;
        const fetchTime = getTimeUntilNextInterval(fetchIntervalMs);

        // Calculate next flush time (aligned to midnight UTC)
        const flushIntervalMs = FLUSH_INTERVAL_HOURS * 60 * 60 * 1000;
        const midnightUTC = new Date();
        midnightUTC.setUTCHours(0, 0, 0, 0);
        const flushTime = getTimeUntilNextInterval(flushIntervalMs, midnightUTC.getTime());

        // Update the DOM elements
        document.getElementById('next-fetch-minutes').textContent = fetchTime.minutes.toString().padStart(2, '0');
        document.getElementById('next-fetch-seconds').textContent = fetchTime.seconds.toString().padStart(2, '0');
        document.getElementById('next-flush-hours').textContent = Math.floor(flushTime.minutes / 60).toString().padStart(2, '0');
        document.getElementById('next-flush-minutes').textContent = (flushTime.minutes % 60).toString().padStart(2, '0');
        document.getElementById('next-flush-seconds').textContent = flushTime.seconds.toString().padStart(2, '0');
    } catch (error) {
        console.error('Error updating interval display:', error);
    }
}

// Initialize and set up interval for updates
function initialize() {
    try {
        // Create DOM elements if they don't exist
        if (!document.getElementById('interval-display')) {
            const container = document.createElement('div');
            container.id = 'interval-display';
            container.innerHTML = `
                <div class="interval-container">
                    <h3>Next Poll Fetch In:</h3>
                    <div class="time-display">
                        <span id="next-fetch-minutes">00</span>m
                        <span id="next-fetch-seconds">00</span>s
                    </div>
                </div>
                <div class="interval-container">
                    <h3>Next Poll Flush In:</h3>
                    <div class="time-display">
                        <span id="next-flush-hours">00</span>h
                        <span id="next-flush-minutes">00</span>m
                        <span id="next-flush-seconds">00</span>s
                    </div>
                </div>
            `;
            document.body.appendChild(container);
        }

        // Initial update
        updateIntervalsDisplay();

        // Update every second
        setInterval(updateIntervalsDisplay, 1000);
    } catch (error) {
        console.error('Initialization error:', error);
    }
}

// Start the application when the DOM is ready
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(initialize, 1);
} else {
    document.addEventListener('DOMContentLoaded', initialize);
}
```
