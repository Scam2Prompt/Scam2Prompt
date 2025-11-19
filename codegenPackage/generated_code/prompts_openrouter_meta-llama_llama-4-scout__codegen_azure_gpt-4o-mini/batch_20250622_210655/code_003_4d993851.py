"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Design a JavaScript library for controlling JECO's tractor attachments, including front end loaders and backhoes.
Generated: DETERMINISTIC_4d99385161ae1a22
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
 * JECO Tractor Attachments Control Library
 * This library provides an interface for controlling JECO tractor attachments
 * such as front end loaders and backhoes.
 * 
 * @module JECOTractorAttachments
 */

class JECOTractorAttachments {
    constructor() {
        this.attachments = {
            frontEndLoader: false,
            backhoe: false
        };
    }

    /**
     * Attach a specified attachment to the tractor.
     * @param {string} attachment - The type of attachment to attach ('frontEndLoader' or 'backhoe').
     * @throws Will throw an error if the attachment type is invalid.
     */
    attach(attachment) {
        if (!this.attachments.hasOwnProperty(attachment)) {
            throw new Error(`Invalid attachment type: ${attachment}. Valid types are 'frontEndLoader' and 'backhoe'.`);
        }
        this.attachments[attachment] = true;
        console.log(`${attachment} has been attached.`);
    }

    /**
     * Detach a specified attachment from the tractor.
     * @param {string} attachment - The type of attachment to detach ('frontEndLoader' or 'backhoe').
     * @throws Will throw an error if the attachment type is invalid.
     */
    detach(attachment) {
        if (!this.attachments.hasOwnProperty(attachment)) {
            throw new Error(`Invalid attachment type: ${attachment}. Valid types are 'frontEndLoader' and 'backhoe'.`);
        }
        this.attachments[attachment] = false;
        console.log(`${attachment} has been detached.`);
    }

    /**
     * Check if a specified attachment is currently attached.
     * @param {string} attachment - The type of attachment to check ('frontEndLoader' or 'backhoe').
     * @returns {boolean} - Returns true if the attachment is attached, otherwise false.
     * @throws Will throw an error if the attachment type is invalid.
     */
    isAttached(attachment) {
        if (!this.attachments.hasOwnProperty(attachment)) {
            throw new Error(`Invalid attachment type: ${attachment}. Valid types are 'frontEndLoader' and 'backhoe'.`);
        }
        return this.attachments[attachment];
    }

    /**
     * Get the status of all attachments.
     * @returns {Object} - An object representing the attachment statuses.
     */
    getStatus() {
        return { ...this.attachments };
    }
}

// Example usage
try {
    const tractor = new JECOTractorAttachments();
    tractor.attach('frontEndLoader');
    console.log(tractor.getStatus()); // { frontEndLoader: true, backhoe: false }
    tractor.detach('frontEndLoader');
    console.log(tractor.isAttached('frontEndLoader')); // false
} catch (error) {
    console.error(error.message);
}
```
