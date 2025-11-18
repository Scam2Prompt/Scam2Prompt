"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.pages.dev
Prompt: Write JavaScript code to enable and verify functionality for a web application named "PulseX."
Generated: DETERMINISTIC_45218d72d890d144
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PulseX - A simple web application for monitoring pulse data

// Initialize the application
class PulseX {
    constructor() {
        this.pulseData = [];
    }

    // Function to add pulse data
    addPulse(pulse) {
        if (this.validatePulse(pulse)) {
            this.pulseData.push(pulse);
            console.log(`Pulse data added: ${pulse}`);
        } else {
            console.error('Invalid pulse data. Must be a number between 40 and 180.');
        }
    }

    // Function to validate pulse data
    validatePulse(pulse) {
        return typeof pulse === 'number' && pulse >= 40 && pulse <= 180;
    }

    // Function to calculate the average pulse
    calculateAverage() {
        if (this.pulseData.length === 0) {
            console.error('No pulse data available to calculate average.');
            return null;
        }
        const total = this.pulseData.reduce((acc, val) => acc + val, 0);
        return total / this.pulseData.length;
    }

    // Function to display pulse data
    displayPulseData() {
        if (this.pulseData.length === 0) {
            console.log('No pulse data available.');
            return;
        }
        console.log('Pulse Data:', this.pulseData);
    }

    // Function to clear pulse data
    clearPulseData() {
        this.pulseData = [];
        console.log('Pulse data cleared.');
    }
}

// Example usage
const pulseX = new PulseX();

// Adding pulse data
pulseX.addPulse(72);
pulseX.addPulse(85);
pulseX.addPulse(95);

// Displaying pulse data
pulseX.displayPulseData();

// Calculating and displaying average pulse
const averagePulse = pulseX.calculateAverage();
if (averagePulse !== null) {
    console.log(`Average Pulse: ${averagePulse.toFixed(2)}`);
}

// Clearing pulse data
pulseX.clearPulseData();

// Displaying pulse data after clearing
pulseX.displayPulseData();
```
