"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Write a code snippet in JavaScript to create a scheduling system for classes in a dental education institution, considering a mixed modality schedule with varying class days and times, such as those listed for INESO's specializations."
Generated: DETERMINISTIC_3edd3508e6a62cf1
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ClassScheduleManager: A class to manage the scheduling of classes in a dental education institution
class ClassScheduleManager {
    constructor() {
        // Initialize an empty schedule
        this.schedule = [];
    }

    /**
     * Adds a new class to the schedule.
     * @param {string} className - The name of the class.
     * @param {string} instructor - The name of the instructor.
     * @param {string} modality - The modality of the class (e.g., 'In-Person', 'Online', 'Hybrid').
     * @param {Date} startTime - The start time of the class.
     * @param {number} duration - The duration of the class in hours.
     * @throws Will throw an error if the class time conflicts with an existing class.
     */
    addClass(className, instructor, modality, startTime, duration) {
        // Validate input parameters
        if (!className || !instructor || !modality || !startTime || !duration) {
            throw new Error("All parameters are required to add a class.");
        }

        // Check for time conflicts
        const endTime = new Date(startTime.getTime() + duration * 60 * 60 * 1000);
        for (const scheduledClass of this.schedule) {
            if (this.isTimeConflict(scheduledClass.startTime, scheduledClass.endTime, startTime, endTime)) {
                throw new Error(`Time conflict with existing class: ${scheduledClass.className}`);
            }
        }

        // Add the new class to the schedule
        this.schedule.push({
            className,
            instructor,
            modality,
            startTime,
            endTime,
        });
    }

    /**
     * Checks if two time periods conflict.
     * @param {Date} startA - Start time of the first period.
     * @param {Date} endA - End time of the first period.
     * @param {Date} startB - Start time of the second period.
     * @param {Date} endB - End time of the second period.
     * @returns {boolean} - True if there is a conflict, false otherwise.
     */
    isTimeConflict(startA, endA, startB, endB) {
        return (startA < endB && startB < endA);
    }

    /**
     * Retrieves the current schedule.
     * @returns {Array} - The current class schedule.
     */
    getSchedule() {
        return this.schedule;
    }

    /**
     * Displays the schedule in a readable format.
     */
    displaySchedule() {
        if (this.schedule.length === 0) {
            console.log("No classes scheduled.");
            return;
        }

        console.log("Current Class Schedule:");
        this.schedule.forEach(({ className, instructor, modality, startTime, endTime }) => {
            console.log(`Class: ${className}, Instructor: ${instructor}, Modality: ${modality}, Start: ${startTime.toLocaleString()}, End: ${endTime.toLocaleString()}`);
        });
    }
}

// Example usage
try {
    const scheduleManager = new ClassScheduleManager();
    scheduleManager.addClass("Dental Anatomy", "Dr. Smith", "In-Person", new Date("2023-10-01T09:00:00"), 2);
    scheduleManager.addClass("Oral Pathology", "Dr. Johnson", "Online", new Date("2023-10-01T11:00:00"), 1.5);
    scheduleManager.displaySchedule();
} catch (error) {
    console.error("Error:", error.message);
}
```
