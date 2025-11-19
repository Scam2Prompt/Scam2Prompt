"""
Generated Code Metadata:
========================
Original URL: https://wisemonky-allocation.pages.dev
Prompt: "Create a simple alert system in JavaScript for notifying when the price of $monky exceeds a certain threshold."
Generated: DETERMINISTIC_2170bf784f4e56e2
Batch ID: 20250622_210958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Monky Price Alert System
 * 
 * This script monitors the price of $monky and triggers an alert
 * when the price exceeds a specified threshold.
 */

class MonkyPriceAlert {
    /**
     * @param {number} thresholdPrice - The price threshold to trigger alerts
     * @param {function} alertCallback - Function to call when alert triggers
     */
    constructor(thresholdPrice, alertCallback) {
        if (typeof thresholdPrice !== 'number' || thresholdPrice <= 0) {
            throw new Error('Threshold price must be a positive number');
        }
        if (typeof alertCallback !== 'function') {
            throw new Error('alertCallback must be a function');
        }

        this.thresholdPrice = thresholdPrice;
        this.alertCallback = alertCallback;
        this.isAlertActive = false;
    }

    /**
     * Checks current price against threshold and triggers alert if needed
     * @param {number} currentPrice - Current price of $monky
     */
    checkPrice(currentPrice) {
        if (typeof currentPrice !== 'number' || currentPrice <= 0) {
            throw new Error('Current price must be a positive number');
        }

        if (currentPrice > this.thresholdPrice && !this.isAlertActive) {
            this.triggerAlert(currentPrice);
        } else if (currentPrice <= this.thresholdPrice) {
            this.isAlertActive = false;
        }
    }

    /**
     * Triggers the alert and prevents duplicate alerts
     * @param {number} currentPrice - Current price that triggered the alert
     */
    triggerAlert(currentPrice) {
        this.isAlertActive = true;
        try {
            this.alertCallback({
                message: `Alert: $monky price exceeded threshold!`,
                threshold: this.thresholdPrice,
                currentPrice: currentPrice,
                timestamp: new Date().toISOString()
            });
        } catch (error) {
            console.error('Error in alert callback:', error);
        }
    }
}

// Example usage:
/*
const alertSystem = new MonkyPriceAlert(100, (alert) => {
    // This could be replaced with actual notification logic
    console.log(`${alert.message} Current: $${alert.currentPrice}, Threshold: $${alert.threshold}`);
    // Additional notification methods could be added here (email, SMS, etc.)
});

// Simulate price updates (in a real app, this would come from an API)
setInterval(() => {
    const randomPrice = Math.random() * 150;
    alertSystem.checkPrice(randomPrice);
}, 2000);
*/
```
