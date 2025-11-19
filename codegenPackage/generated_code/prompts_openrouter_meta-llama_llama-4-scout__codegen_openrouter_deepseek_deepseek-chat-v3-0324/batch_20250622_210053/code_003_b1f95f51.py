"""
Generated Code Metadata:
========================
Original URL: https://baamgift.info
Prompt: Write a JavaScript function to implement a countdown timer for limited-time offers on gift cards, similar to the one displayed on بام گیفت.
Generated: DETERMINISTIC_b1f95f51d7a30095
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for Limited-Time Offers
 * @param {string} endTime - ISO string representing the end time of the offer
 * @param {string} elementId - ID of the HTML element to display the countdown
 * @param {function} [callback] - Optional callback function to execute when timer ends
 */
function giftCardCountdown(endTime, elementId, callback) {
    // Validate inputs
    if (!endTime || !elementId) {
        console.error('Missing required parameters: endTime and elementId must be provided');
        return;
    }

    const countdownElement = document.getElementById(elementId);
    if (!countdownElement) {
        console.error(`Element with ID ${elementId} not found`);
        return;
    }

    const endDate = new Date(endTime);
    if (isNaN(endDate.getTime())) {
        console.error('Invalid endTime provided. Please use a valid ISO date string.');
        return;
    }

    // Update the countdown every second
    const timer = setInterval(() => {
        const now = new Date().getTime();
        const distance = endDate - now;

        // Time calculations for days, hours, minutes and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        countdownElement.innerHTML = `
            <span class="countdown-days">${days}d</span>
            <span class="countdown-hours">${hours}h</span>
            <span class="countdown-minutes">${minutes}m</span>
            <span class="countdown-seconds">${seconds}s</span>
        `;

        // If the countdown is finished
        if (distance < 0) {
            clearInterval(timer);
            countdownElement.innerHTML = "Offer Expired!";
            if (typeof callback === 'function') {
                callback();
            }
        }
    }, 1000);

    // Return the timer ID in case it needs to be cleared manually
    return timer;
}

// Example usage:
// giftCardCountdown("2023-12-31T23:59:59", "countdown-timer", () => {
//     console.log("Countdown finished!");
// });
```
