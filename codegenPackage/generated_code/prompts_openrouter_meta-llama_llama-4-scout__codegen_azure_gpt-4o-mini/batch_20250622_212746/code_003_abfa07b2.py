"""
Generated Code Metadata:
========================
Original URL: https://taqibraz.blogspot.com
Prompt: Write a JavaScript code to create a countdown timer for a limited-time offer, like the TEMPO LIMITADO ⏰ deal on Lavadora de Alta Pressão Kärcher K4 Power on taQi.
Generated: DETERMINISTIC_abfa07b237ff97c2
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer for Limited-Time Offer
// This script creates a countdown timer that displays the time remaining for a limited-time offer.

class CountdownTimer {
    constructor(endTime) {
        this.endTime = new Date(endTime).getTime();
        this.timerId = null;
        this.init();
    }

    // Initialize the countdown timer
    init() {
        this.updateTimer(); // Update the timer immediately
        this.startTimer();  // Start the countdown
    }

    // Start the countdown timer
    startTimer() {
        this.timerId = setInterval(() => {
            this.updateTimer();
        }, 1000);
    }

    // Update the timer display
    updateTimer() {
        const now = new Date().getTime();
        const timeLeft = this.endTime - now;

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        // Display the result in the element with id="countdown"
        const countdownElement = document.getElementById("countdown");
        if (countdownElement) {
            countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        } else {
            console.error("Countdown element not found.");
        }

        // If the countdown is finished, display a message and clear the timer
        if (timeLeft < 0) {
            clearInterval(this.timerId);
            if (countdownElement) {
                countdownElement.innerHTML = "Offer has ended!";
            }
        }
    }
}

// Example usage: Set the countdown to end in 1 hour from now
const offerEndTime = new Date(Date.now() + 60 * 60 * 1000); // 1 hour from now
const countdownTimer = new CountdownTimer(offerEndTime);

// HTML structure for the countdown timer
document.body.innerHTML += '<div id="countdown" style="font-size: 24px; font-weight: bold;"></div>';
```

Make sure to include this script in an HTML file to see the countdown timer in action.
