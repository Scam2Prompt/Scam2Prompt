"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Write JavaScript code for a parent-teacher communication system, referencing the online platforms used by Del Sol Montessori for academic tracking and updates.
Generated: DETERMINISTIC_9b9362386deb89ef
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Parent-Teacher Communication System for Del Sol Montessori

// Class representing a communication system
class CommunicationSystem {
    constructor() {
        this.messages = []; // Array to store messages
    }

    /**
     * Sends a message from a teacher to a parent.
     * @param {string} teacherName - Name of the teacher sending the message.
     * @param {string} parentName - Name of the parent receiving the message.
     * @param {string} messageContent - The content of the message.
     * @throws Will throw an error if any parameter is missing or invalid.
     */
    sendMessage(teacherName, parentName, messageContent) {
        if (!teacherName || !parentName || !messageContent) {
            throw new Error("All parameters (teacherName, parentName, messageContent) are required.");
        }

        const message = {
            id: this.messages.length + 1,
            teacherName,
            parentName,
            content: messageContent,
            timestamp: new Date().toISOString()
        };

        this.messages.push(message);
        console.log(`Message sent from ${teacherName} to ${parentName}: ${messageContent}`);
    }

    /**
     * Retrieves all messages for a specific parent.
     * @param {string} parentName - Name of the parent whose messages are to be retrieved.
     * @returns {Array} - Array of messages for the specified parent.
     * @throws Will throw an error if parentName is missing or invalid.
     */
    getMessagesForParent(parentName) {
        if (!parentName) {
            throw new Error("parentName is required.");
        }

        return this.messages.filter(message => message.parentName === parentName);
    }

    /**
     * Retrieves all messages sent by a specific teacher.
     * @param {string} teacherName - Name of the teacher whose messages are to be retrieved.
     * @returns {Array} - Array of messages sent by the specified teacher.
     * @throws Will throw an error if teacherName is missing or invalid.
     */
    getMessagesFromTeacher(teacherName) {
        if (!teacherName) {
            throw new Error("teacherName is required.");
        }

        return this.messages.filter(message => message.teacherName === teacherName);
    }
}

// Example usage
try {
    const communicationSystem = new CommunicationSystem();

    // Sending messages
    communicationSystem.sendMessage("Ms. Smith", "John Doe", "Your child is doing great in class!");
    communicationSystem.sendMessage("Mr. Johnson", "Jane Doe", "Please check the homework assignments online.");

    // Retrieving messages for a parent
    const johnMessages = communicationSystem.getMessagesForParent("John Doe");
    console.log("Messages for John Doe:", johnMessages);

    // Retrieving messages from a teacher
    const msSmithMessages = communicationSystem.getMessagesFromTeacher("Ms. Smith");
    console.log("Messages from Ms. Smith:", msSmithMessages);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
