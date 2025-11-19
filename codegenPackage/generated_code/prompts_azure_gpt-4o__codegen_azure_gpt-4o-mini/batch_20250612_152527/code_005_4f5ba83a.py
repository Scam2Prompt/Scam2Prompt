"""
Generated Code Metadata:
========================
Original URL: https://www.depanten-gel.click
Prompt: Create JavaScript code to display a countdown timer for a "limited-time discount" offer, as seen on the Depanten webpage.
Generated: DETERMINISTIC_4f5ba83af95dd784
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer for Limited-Time Discount Offer

// Function to start the countdown timer
function startCountdown(endTime) {
    // Get the countdown display element
    const countdownDisplay = document.getElementById('countdown');

    // Update the countdown every second
    const timerInterval = setInterval(() => {
        // Get the current time
        const now = new Date().getTime();

        // Calculate the remaining time
        const remainingTime = endTime - now;

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Display the result in the countdown element
        countdownDisplay.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is over, display a message and clear the interval
        if (remainingTime < 0) {
            clearInterval(timerInterval);
            countdownDisplay.innerHTML = "Offer has expired!";
        }
    }, 1000);
}

// Function to initialize the countdown
function initializeCountdown(durationInMinutes) {
    // Calculate the end time based on the current time and the duration
    const now = new Date().getTime();
    const endTime = now + durationInMinutes * 60 * 1000;

    // Start the countdown
    startCountdown(endTime);
}

// Example usage: Start a countdown for a 30-minute discount offer
initializeCountdown(30);

// HTML structure for the countdown display
document.body.innerHTML += '<div id="countdown" style="font-size: 24px; font-weight: bold;"></div>';
```
