"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Generate code for a countdown timer feature to display limited-time offers on an e-commerce site, similar to the "0 روز 00 ساعت 00 دقیقه 00 ثانیه" timer shown on "ای ار گیفت."
Generated: DETERMINISTIC_51f055de65e0b2be
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer Component for Limited-Time Offers
 * Displays a countdown timer in the format: "0 روز 00 ساعت 00 دقیقه 00 ثانیه"
 * 
 * Usage:
 * const countdown = new CountdownTimer('2023-12-31T23:59:59', 'countdown-display');
 * countdown.start();
 */
class CountdownTimer {
    constructor(endTime, displayElementId) {
        this.endTime = new Date(endTime).getTime();
        this.displayElement = document.getElementById(displayElementId);

        // Validate the end time
        if (isNaN(this.endTime)) {
            throw new Error('Invalid end time provided.');
        }
        
        if (!this.displayElement) {
            throw new Error(`Display element with ID '${displayElementId}' not found.`);
        }
    }

    /**
     * Starts the countdown timer
     */
    start() {
        // Update the timer every second
        this.interval = setInterval(() => {
            this.updateTimer();
        }, 1000);
    }

    /**
     * Updates the timer display
     */
    updateTimer() {
        const now = new Date().getTime();
        const distance = this.endTime - now;

        // If the countdown is finished, stop the timer
        if (distance < 0) {
            clearInterval(this.interval);
            this.displayElement.innerHTML = 'زمان تمام شد'; // "Time is up"
            return;
        }

        // Calculate time components
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the specified format
        this.displayElement.innerHTML = `${days} روز ${this.padNumber(hours)} ساعت ${this.padNumber(minutes)} دقیقه ${this.padNumber(seconds)} ثانیه`;
    }

    /**
     * Pads single digit numbers with leading zero
     * @param {number} num - The number to pad
     * @returns {string} - The padded number
     */
    padNumber(num) {
        return num < 10 ? '0' + num : num;
    }
}

// Example usage:
// const countdown = new CountdownTimer('2023-12-31T23:59:59', 'countdown-display');
// countdown.start();
```
