"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a JavaScript function to enhance the school’s online communication platform, ensuring it aligns with the transparency goals of SMKN 1 Kadipaten.
Generated: DETERMINISTIC_61b7bcaf2a443d8b
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Enhances the school's online communication platform by 
 * providing a transparent messaging system for students, 
 * teachers, and parents.
 *
 * @class CommunicationPlatform
 */
class CommunicationPlatform {
    constructor() {
        this.messages = [];
    }

    /**
     * Sends a message to the communication platform.
     * 
     * @param {string} sender - The name of the sender (student, teacher, or parent).
     * @param {string} content - The content of the message.
     * @throws {Error} Throws an error if the sender or content is invalid.
     */
    sendMessage(sender, content) {
        if (!sender || typeof sender !== 'string') {
            throw new Error('Invalid sender. Sender must be a non-empty string.');
        }
        if (!content || typeof content !== 'string') {
            throw new Error('Invalid content. Content must be a non-empty string.');
        }

        const timestamp = new Date().toISOString();
        const message = { sender, content, timestamp };

        this.messages.push(message);
        console.log('Message sent successfully:', message);
    }

    /**
     * Retrieves all messages from the platform.
     * 
     * @returns {Array} An array of messages.
     */
    getAllMessages() {
        return this.messages;
    }

    /**
     * Filters messages by sender.
     * 
     * @param {string} sender - The name of the sender to filter messages by.
     * @returns {Array} An array of messages sent by the specified sender.
     * @throws {Error} Throws an error if the sender is invalid.
     */
    getMessagesBySender(sender) {
        if (!sender || typeof sender !== 'string') {
            throw new Error('Invalid sender. Sender must be a non-empty string.');
        }

        return this.messages.filter(message => message.sender === sender);
    }
}

// Example usage:
try {
    const platform = new CommunicationPlatform();
    platform.sendMessage('John Doe', 'Hello, this is a test message.');
    platform.sendMessage('Jane Smith', 'Good morning everyone!');

    console.log('All Messages:', platform.getAllMessages());
    console.log('Messages from John Doe:', platform.getMessagesBySender('John Doe'));
} catch (error) {
    console.error('Error:', error.message);
}
```
