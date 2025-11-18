"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verified.myclickfunnels.com
Prompt: Provide an example of JavaScript code to implement a countdown timer for a limited-time offer on a ClickFunnels product page.
Generated: DETERMINISTIC_b875c41c7d0fe5d7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Limited-Time Offers
 * This script initializes a countdown timer that counts down from a specified duration.
 * When the timer reaches zero, an alert is displayed and the timer stops.
 */

// Function to start the countdown timer
function startCountdown(duration, display) {
    let timer = duration, minutes, seconds;

    // Update the countdown every second
    const interval = setInterval(() => {
        // Calculate minutes and seconds from the timer
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        // Format the time display
        display.textContent = minutes + "m " + seconds + "s";

        // If the timer reaches zero, stop the countdown
        if (--timer < 0) {
            clearInterval(interval);
            display.textContent = "EXPIRED";
            alert("The limited-time offer has expired!");
            // Additional logic can be added here (e.g., redirecting or disabling buy button)
        }
    }, 1000);
}

// Function to initialize the countdown
function initializeCountdown() {
    // Set the countdown duration in seconds (e.g., 5 minutes)
    const countdownDuration = 60 * 5; // 5 minutes in seconds
    const display = document.getElementById('countdown-display');

    // Check if the display element exists
    if (display) {
        // Start the countdown
        startCountdown(countdownDuration, display);
    } else {
        console.error("Countdown display element not found. Please check your HTML.");
    }
}

// Run the countdown timer on page load
window.onload = initializeCountdown;
```

<!-- HTML to include in your ClickFunnels page -->
<!-- 
<div id="countdown-display"></div>
-->
