"""
Generated Code Metadata:
========================
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Generate a script in JavaScript to display the countdown timer for the $MGMES token presale price increase, as shown on The Meme Games Token website.
Generated: DETERMINISTIC_03da281a54ca0c6b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Get the presale end time from the server or a reliable source
// For demonstration purposes, let's assume the presale ends in 2 hours from now
const PRESALE_END_TIME = new Date().getTime() + 2 * 60 * 60 * 1000;

// Function to format time
function formatTime(time) {
    return Math.floor(time / 1000);
}

// Function to update the countdown timer
function updateCountdown() {
    const now = new Date().getTime();
    const distance = PRESALE_END_TIME - now;

    if (distance < 0) {
        // Presale has ended
        document.getElementById('countdown').innerHTML = 'Presale has ended';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {
        countdownElement.innerHTML = `
            <span id="days">${days.toString().padStart(2, '0')}</span>:
            <span id="hours">${hours.toString().padStart(2, '0')}</span>:
            <span id="minutes">${minutes.toString().padStart(2, '0')}</span>:
            <span id="seconds">${seconds.toString().padStart(2, '0')}</span>
        `;
    } else {
        console.error('Countdown element not found');
    }

    // Update every second
    setTimeout(updateCountdown, 1000);
}

// Initialize the countdown
try {
    updateCountdown();
} catch (error) {
    console.error('Error initializing countdown:', error);
}

// Optional: fetch PRESALE_END_TIME from server
// fetch('/api/presale-end-time')
//     .then(response => response.json())
//     .then(data => {
//         PRESALE_END_TIME = data.presaleEndTime;
//         updateCountdown();
//     })
//     .catch(error => console.error('Error fetching presale end time:', error));
```
