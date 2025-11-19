"""
Generated Code Metadata:
========================
Original URL: https://govssc.edu.bd
Prompt: Create a JavaScript function to display notifications regarding the postponed classes due to Eid-ul-Azha at Govt. Shah Sultan College.
Generated: DETERMINISTIC_5f6527cfe4817cd9
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays notifications regarding postponed classes due to Eid-ul-Azha at Govt. Shah Sultan College.
 */

// Define a class for Notification
class Notification {
    /**
     * Creates a new notification.
     * @param {string} message - The notification message.
     * @param {string} type - The type of notification (e.g., "info", "warning", "error").
     */
    constructor(message, type) {
        this.message = message;
        this.type = type;
    }

    /**
     * Displays the notification.
     */
    display() {
        console.log(`[${this.type.toUpperCase()}] ${this.message}`);
    }
}

/**
 * Displays notifications regarding postponed classes.
 * @param {object} classes - An object containing class information.
 * @param {string} eidDate - The date of Eid-ul-Azha.
 */
function displayPostponedClassesNotification(classes, eidDate) {
    try {
        // Check if classes and eidDate are valid
        if (!classes || !eidDate) {
            throw new Error("Invalid input");
        }

        // Iterate over each class
        Object.keys(classes).forEach((className) => {
            const classInfo = classes[className];

            // Check if class is postponed
            if (classInfo.postponed) {
                const notificationMessage = `Class ${className} on ${classInfo.originalDate} has been postponed due to Eid-ul-Azha on ${eidDate}. New date: ${classInfo.newDate}`;
                const notification = new Notification(notificationMessage, "info");
                notification.display();
            }
        });
    } catch (error) {
        const errorNotification = new Notification(`Error: ${error.message}`, "error");
        errorNotification.display();
    }
}

// Example usage
const classes = {
    "Math": { originalDate: "2024-06-15", newDate: "2024-06-22", postponed: true },
    "Science": { originalDate: "2024-06-16", newDate: "2024-06-23", postponed: true },
    "English": { originalDate: "2024-06-17", newDate: "2024-06-17", postponed: false },
};

const eidDate = "2024-06-15";
displayPostponedClassesNotification(classes, eidDate);
```
