"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Generate a JavaScript function that schedules OSHA safety training sessions for employees, incorporating the training options provided by iSi Environmental.
Generated: DETERMINISTIC_67a8cb992e047575
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * OSHA Safety Training Scheduler
 * 
 * This module provides functionality to schedule OSHA safety training sessions for employees.
 * It incorporates training options provided by iSi Environmental.
 */

// Define the TrainingSession class
class TrainingSession {
    /**
     * Creates a new TrainingSession
     * @param {string} topic - The topic of the training session
     * @param {Date} date - The date of the training session
     * @param {string} time - The time of the training session
     * @param {string[]} attendees - The list of employee attendees
     */
    constructor(topic, date, time, attendees) {
        this.topic = topic;
        this.date = date;
        this.time = time;
        this.attendees = attendees;
    }
}

// Define the TrainingScheduler class
class TrainingScheduler {
    /**
     * Creates a new TrainingScheduler
     */
    constructor() {
        this.trainingSessions = [];
        this.trainingOptions = [
            "Hazmat Operations",
            "Confined Space Entry",
            "Fall Protection",
            "Respiratory Protection",
            "Hazard Communication"
        ];
    }

    /**
     * Schedules a new training session
     * @param {string} topic - The topic of the training session
     * @param {Date} date - The date of the training session
     * @param {string} time - The time of the training session
     * @param {string[]} attendees - The list of employee attendees
     * @throws {Error} If the topic is not a valid training option
     */
    scheduleTrainingSession(topic, date, time, attendees) {
        if (!this.trainingOptions.includes(topic)) {
            throw new Error(`Invalid training topic: ${topic}`);
        }

        const session = new TrainingSession(topic, date, time, attendees);
        this.trainingSessions.push(session);
        return session;
    }

    /**
     * Cancels a training session by index
     * @param {number} index - The index of the training session to cancel
     * @throws {Error} If the index is out of range
     */
    cancelTrainingSession(index) {
        if (index < 0 || index >= this.trainingSessions.length) {
            throw new Error(`Invalid session index: ${index}`);
        }

        this.trainingSessions.splice(index, 1);
    }

    /**
     * Prints a list of all scheduled training sessions
     */
    printTrainingSessions() {
        console.log("Scheduled Training Sessions:");
        this.trainingSessions.forEach((session, index) => {
            console.log(`Session ${index + 1}:`);
            console.log(`Topic: ${session.topic}`);
            console.log(`Date: ${session.date.toLocaleDateString()}`);
            console.log(`Time: ${session.time}`);
            console.log(`Attendees: ${session.attendees.join(", ")}`);
            console.log();
        });
    }
}

// Example usage:
function main() {
    const scheduler = new TrainingScheduler();

    try {
        const session1 = scheduler.scheduleTrainingSession(
            "Hazmat Operations",
            new Date("2024-09-20"),
            "9:00 AM",
            ["John Doe", "Jane Smith"]
        );

        const session2 = scheduler.scheduleTrainingSession(
            "Fall Protection",
            new Date("2024-09-22"),
            "1:00 PM",
            ["Bob Johnson", "Alice Brown"]
        );

        scheduler.printTrainingSessions();

        scheduler.cancelTrainingSession(0);

        scheduler.printTrainingSessions();
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
