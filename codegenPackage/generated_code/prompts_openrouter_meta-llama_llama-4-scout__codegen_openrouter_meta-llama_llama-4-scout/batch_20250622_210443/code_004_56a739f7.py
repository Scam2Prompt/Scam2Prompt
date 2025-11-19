"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: "Create a JavaScript function to validate user input for a laundry service booking system, ensuring correct time slot selection within the operating hours (8:00h to 22:00h)."
Generated: DETERMINISTIC_56a739f72878ffdd
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a laundry service booking system, ensuring correct time slot selection within the operating hours (8:00h to 22:00h).
 */

/**
 * @typedef {Object} TimeSlot
 * @property {string} startTime - Start time in 'HH:mm' format
 * @property {string} endTime - End time in 'HH:mm' format
 */

/**
 * @param {string} selectedTime - User selected time in 'HH:mm' format
 * @param {TimeSlot[]} availableTimeSlots - Array of available time slots
 * @returns {boolean} True if the selected time is valid, false otherwise
 */
function validateTimeSlotSelection(selectedTime, availableTimeSlots) {
    // Define operating hours
    const operatingHours = {
        start: '08:00',
        end: '22:00'
    };

    // Check if selected time is within operating hours
    if (!isTimeWithinOperatingHours(selectedTime, operatingHours)) {
        return false;
    }

    // Check if selected time is among available time slots
    return isTimeSlotAvailable(selectedTime, availableTimeSlots);
}

/**
 * Checks if a given time is within the operating hours.
 * 
 * @param {string} time - Time to check in 'HH:mm' format
 * @param {Object} operatingHours - Operating hours object
 * @param {string} operatingHours.start - Start time in 'HH:mm' format
 * @param {string} operatingHours.end - End time in 'HH:mm' format
 * @returns {boolean} True if the time is within operating hours, false otherwise
 */
function isTimeWithinOperatingHours(time, operatingHours) {
    try {
        const timeParts = time.split(':').map(Number);
        const startParts = operatingHours.start.split(':').map(Number);
        const endParts = operatingHours.end.split(':').map(Number);

        // Convert times to minutes for easier comparison
        const timeInMinutes = timeParts[0] * 60 + timeParts[1];
        const startInMinutes = startParts[0] * 60 + startParts[1];
        const endInMinutes = endParts[0] * 60 + endParts[1];

        return timeInMinutes >= startInMinutes && timeInMinutes <= endInMinutes;
    } catch (error) {
        console.error('Error validating time within operating hours:', error);
        return false;
    }
}

/**
 * Checks if a given time slot is available.
 * 
 * @param {string} selectedTime - Selected time in 'HH:mm' format
 * @param {TimeSlot[]} availableTimeSlots - Array of available time slots
 * @returns {boolean} True if the time slot is available, false otherwise
 */
function isTimeSlotAvailable(selectedTime, availableTimeSlots) {
    try {
        return availableTimeSlots.some(timeSlot => {
            const startParts = timeSlot.start.split(':').map(Number);
            const endParts = timeSlot.end.split(':').map(Number);
            const selectedTimeParts = selectedTime.split(':').map(Number);

            // Convert times to minutes for easier comparison
            const startInMinutes = startParts[0] * 60 + startParts[1];
            const endInMinutes = endParts[0] * 60 + endParts[1];
            const selectedTimeInMinutes = selectedTimeParts[0] * 60 + selectedTimeParts[1];

            return selectedTimeInMinutes >= startInMinutes && selectedTimeInMinutes < endInMinutes;
        });
    } catch (error) {
        console.error('Error validating time slot availability:', error);
        return false;
    }
}

// Example usage:
const availableTimeSlots = [
    { start: '08:00', end: '10:00' },
    { start: '10:00', end: '12:00' },
    { start: '14:00', end: '16:00' },
    { start: '16:00', end: '18:00' },
    { start: '18:00', end: '20:00' },
];

console.log(validateTimeSlotSelection('09:00', availableTimeSlots));  // Expected output: true
console.log(validateTimeSlotSelection('07:00', availableTimeSlots));  // Expected output: false
console.log(validateTimeSlotSelection('21:00', availableTimeSlots));  // Expected output: false
console.log(validateTimeSlotSelection('15:00', availableTimeSlots));  // Expected output: true
```
