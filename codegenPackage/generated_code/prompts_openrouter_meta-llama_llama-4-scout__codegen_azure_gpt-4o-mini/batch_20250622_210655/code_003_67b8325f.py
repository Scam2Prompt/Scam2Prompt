"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Develop a JavaScript function to implement a simple availability calendar for a villa or hotel, reflecting the type of accommodations offered by Vila Vračar.
Generated: DETERMINISTIC_67b8325f04174727
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * AvailabilityCalendar class to manage the availability of accommodations.
 */
class AvailabilityCalendar {
    constructor() {
        // Initialize the calendar with an empty availability map
        this.availability = new Map();
    }

    /**
     * Adds availability for a specific date and accommodation type.
     * @param {string} date - The date in 'YYYY-MM-DD' format.
     * @param {string} accommodationType - The type of accommodation (e.g., 'single', 'double', 'suite').
     * @param {boolean} isAvailable - Availability status (true for available, false for not available).
     */
    addAvailability(date, accommodationType, isAvailable) {
        if (!this.isValidDate(date)) {
            throw new Error('Invalid date format. Please use YYYY-MM-DD.');
        }

        if (!this.availability.has(date)) {
            this.availability.set(date, {});
        }

        this.availability.get(date)[accommodationType] = isAvailable;
    }

    /**
     * Checks availability for a specific date and accommodation type.
     * @param {string} date - The date in 'YYYY-MM-DD' format.
     * @param {string} accommodationType - The type of accommodation.
     * @returns {boolean} - Returns true if available, false otherwise.
     */
    checkAvailability(date, accommodationType) {
        if (!this.isValidDate(date)) {
            throw new Error('Invalid date format. Please use YYYY-MM-DD.');
        }

        const dateAvailability = this.availability.get(date);
        return dateAvailability ? dateAvailability[accommodationType] || false : false;
    }

    /**
     * Validates the date format.
     * @param {string} date - The date to validate.
     * @returns {boolean} - Returns true if the date is valid, false otherwise.
     */
    isValidDate(date) {
        const regex = /^\d{4}-\d{2}-\d{2}$/;
        return regex.test(date);
    }

    /**
     * Retrieves the availability for a specific date.
     * @param {string} date - The date in 'YYYY-MM-DD' format.
     * @returns {object|null} - Returns an object with accommodation types and their availability or null if no data.
     */
    getAvailabilityForDate(date) {
        if (!this.isValidDate(date)) {
            throw new Error('Invalid date format. Please use YYYY-MM-DD.');
        }

        return this.availability.get(date) || null;
    }
}

// Example usage:
try {
    const calendar = new AvailabilityCalendar();
    calendar.addAvailability('2023-10-01', 'single', true);
    calendar.addAvailability('2023-10-01', 'double', false);
    console.log(calendar.checkAvailability('2023-10-01', 'single')); // true
    console.log(calendar.getAvailabilityForDate('2023-10-01')); // { single: true, double: false }
} catch (error) {
    console.error(error.message);
}
```
