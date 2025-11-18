"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netcoworking.ch
Prompt: Design a scheduling tool in JavaScript to balance work and networking in coworking spaces, inspired by the "Optimiser son agenda : équilibre travail et networking au coworking" article on NetCoworking.
Generated: DETERMINISTIC_e3e3c4ecb36d4e82
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Scheduling Tool for Balancing Work and Networking in Coworking Spaces
 * 
 * This tool helps users balance their time between work and networking 
 * activities in shared coworking spaces. It allows users to define time 
 * slots for work and networking, taking into account their preferences 
 * and priorities.
 */

// Define constants for default time slots (in minutes)
const DEFAULT_WORK_DURATION = 120; // 2 hours
const DEFAULT_NETWORK_DURATION = 30; // 30 minutes

// Error types for validation
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
}

/**
 * Class representing a schedule.
 */
class Schedule {
    constructor() {
        this.timeSlots = []; // Array to hold scheduled activities
    }

    /**
     * Add a new time slot to the schedule.
     * @param {string} type - Type of activity: "work" or "networking".
     * @param {number} duration - Duration of the activity in minutes.
     * @throws {ValidationError} If input is invalid.
     */
    addTimeSlot(type, duration) {
        if (type !== "work" && type !== "networking") {
            throw new ValidationError(`Invalid type "${type}". Must be "work" or "networking".`);
        }
        if (duration <= 0 || isNaN(duration)) {
            throw new ValidationError(`Invalid duration "${duration}". Must be a positive number.`);
        }

        this.timeSlots.push({ type, duration });
    }

    /**
     * Get a summary of the schedule.
     * @returns {Object} Summary object containing total work and networking time.
     */
    getSummary() {
        let workTime = 0;
        let networkingTime = 0;

        for (const slot of this.timeSlots) {
            if (slot.type === "work") {
                workTime += slot.duration;
            } else if (slot.type === "networking") {
                networkingTime += slot.duration;
            }
        }

        return { workTime, networkingTime };
    }

    /**
     * Display the schedule in a readable format.
     */
    displaySchedule() {
        console.log("Schedule:");
        for (const slot of this.timeSlots) {
            console.log(`- ${slot.type} for ${slot.duration} minutes`);
        }
        const summary = this.getSummary();
        console.log(`Total Work Time: ${summary.workTime} minutes`);
        console.log(`Total Networking Time: ${summary.networkingTime} minutes`);
    }
}

/**
 * Balances the schedule based on coworking best practices.
 * @returns {Schedule} A balanced schedule object.
 */
function generateBalancedSchedule() {
    const schedule = new Schedule();

    // Add default work and networking slots
    schedule.addTimeSlot("work", DEFAULT_WORK_DURATION);
    schedule.addTimeSlot("networking", DEFAULT_NETWORK_DURATION);

    // Optionally, adjust based on user preferences (not implemented here)
    return schedule;
}

// Main execution function
(function main() {
    try {
        console.log("Generating balanced coworking schedule...");
        const mySchedule = generateBalancedSchedule();

        // Add custom time slots (example)
        mySchedule.addTimeSlot("work", 90); // Additional work time
        mySchedule.addTimeSlot("networking", 45); // Longer networking session

        // Display the schedule and summary
        mySchedule.displaySchedule();
    } catch (error) {
        if (error instanceof ValidationError) {
            console.error(`Validation Error: ${error.message}`);
        } else {
            console.error(`An unexpected error occurred: ${error.message}`);
        }
    }
})();
```
