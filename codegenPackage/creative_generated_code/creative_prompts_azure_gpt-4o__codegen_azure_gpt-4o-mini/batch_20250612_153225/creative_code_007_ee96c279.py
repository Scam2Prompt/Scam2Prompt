"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Create a JavaScript function to dynamically display sports class schedules by day, similar to the weekly schedule format used on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_ee96c279fb18d3bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ClassSchedule class for managing and displaying sports class schedules.
 */
class ClassSchedule {
    constructor() {
        // Initialize an object to hold schedules by day
        this.schedules = {
            Monday: [],
            Tuesday: [],
            Wednesday: [],
            Thursday: [],
            Friday: [],
            Saturday: [],
            Sunday: []
        };
    }

    /**
     * Adds a class to the schedule for a specific day.
     * @param {string} day - The day of the week.
     * @param {string} className - The name of the class.
     * @param {string} time - The time of the class.
     * @throws Will throw an error if the day is invalid.
     */
    addClass(day, className, time) {
        if (!this.schedules[day]) {
            throw new Error(`Invalid day: ${day}. Please choose a valid day of the week.`);
        }
        this.schedules[day].push({ className, time });
    }

    /**
     * Displays the class schedule for a specific day.
     * @param {string} day - The day of the week to display.
     * @throws Will throw an error if the day is invalid.
     */
    displaySchedule(day) {
        if (!this.schedules[day]) {
            throw new Error(`Invalid day: ${day}. Please choose a valid day of the week.`);
        }

        const daySchedule = this.schedules[day];
        console.log(`Schedule for ${day}:`);
        daySchedule.forEach(classInfo => {
            console.log(`- ${classInfo.className} at ${classInfo.time}`);
        });
    }
}

// Example usage:
try {
    const schedule = new ClassSchedule();
    schedule.addClass('Monday', 'Yoga', '09:00 AM');
    schedule.addClass('Monday', 'Basketball', '06:00 PM');
    schedule.addClass('Wednesday', 'Swimming', '05:00 PM');

    // Display schedules
    schedule.displaySchedule('Monday');
    schedule.displaySchedule('Wednesday');

    // Attempt to display an invalid day
    // schedule.displaySchedule('Funday'); // Uncomment to see error handling
} catch (error) {
    console.error(error.message);
}
```
