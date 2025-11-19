"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Generate a JavaScript function that handles encrypted messages and phone calls among characters in a survival game, inspired by the "Project Divinity" experiment on the Cannibals website.
Generated: DETERMINISTIC_d01906d396a44c94
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
 * Handles encrypted messages and phone calls for a survival game.
 * Inspired by the "Project Divinity" experiment.
 * 
 * @class CommunicationHandler
 */
class CommunicationHandler {
    /**
     * Creates an instance of CommunicationHandler.
     * @param {Object} config - Configuration object
     * @param {string} config.encryptionKey - Key for message encryption/decryption
     * @param {number} [config.callDurationLimit=300] - Max call duration in seconds
     */
    constructor(config) {
        if (!config || !config.encryptionKey) {
            throw new Error('Encryption key is required');
        }

        this.encryptionKey = config.encryptionKey;
        this.callDurationLimit = config.callDurationLimit || 300; // 5 minutes default
        this.activeCalls = new Map();
        this.messageQueue = [];
    }

    /**
     * Encrypts a message using a simple XOR cipher
     * @param {string} message - Message to encrypt
     * @returns {string} Encrypted message
     */
    encryptMessage(message) {
        if (typeof message !== 'string') {
            throw new Error('Message must be a string');
        }

        let encrypted = '';
        for (let i = 0; i < message.length; i++) {
            const keyChar = this.encryptionKey.charCodeAt(i % this.encryptionKey.length);
            const msgChar = message.charCodeAt(i);
            encrypted += String.fromCharCode(msgChar ^ keyChar);
        }
        return btoa(encrypted); // Base64 encode
    }

    /**
     * Decrypts a message
     * @param {string} encryptedMessage - Message to decrypt
     * @returns {string} Decrypted message
     */
    decryptMessage(encryptedMessage) {
        if (typeof encryptedMessage !== 'string') {
            throw new Error('Encrypted message must be a string');
        }

        try {
            const decoded = atob(encryptedMessage);
            let decrypted = '';
            for (let i = 0; i < decoded.length; i++) {
                const keyChar = this.encryptionKey.charCodeAt(i % this.encryptionKey.length);
                const msgChar = decoded.charCodeAt(i);
                decrypted += String.fromCharCode(msgChar ^ keyChar);
            }
            return decrypted;
        } catch (error) {
            throw new Error('Failed to decrypt message: invalid format');
        }
    }

    /**
     * Sends an encrypted message to a recipient
     * @param {string} recipientId - ID of the recipient
     * @param {string} message - Message to send
     * @returns {string} Encrypted message that was sent
     */
    sendMessage(recipientId, message) {
        if (!recipientId || typeof recipientId !== 'string') {
            throw new Error('Invalid recipient ID');
        }

        const encrypted = this.encryptMessage(message);
        this.messageQueue.push({
            recipientId,
            message: encrypted,
            timestamp: Date.now()
        });
        return encrypted;
    }

    /**
     * Retrieves messages for a recipient
     * @param {string} recipientId - ID of the recipient
     * @returns {Array} Array of decrypted messages
     */
    retrieveMessages(recipientId) {
        if (!recipientId || typeof recipientId !== 'string') {
            throw new Error('Invalid recipient ID');
        }

        const messages = this.messageQueue.filter(msg => msg.recipientId === recipientId);
        this.messageQueue = this.messageQueue.filter(msg => msg.recipientId !== recipientId);

        return messages.map(msg => ({
            ...msg,
            message: this.decryptMessage(msg.message)
        }));
    }

    /**
     * Initiates a phone call between two characters
     * @param {string} callerId - ID of the caller
     * @param {string} receiverId - ID of the receiver
     * @returns {string} Call ID
     */
    initiateCall(callerId, receiverId) {
        if (!callerId || !receiverId) {
            throw new Error('Both caller and receiver IDs are required');
        }

        const callId = `call_${Date.now()}`;
        this.activeCalls.set(callId, {
            callerId,
            receiverId,
            startTime: Date.now(),
            endTime: null,
            isActive: true
        });

        return callId;
    }

    /**
     * Ends a phone call
     * @param {string} callId - ID of the call to end
     * @returns {Object} Call details
     */
    endCall(callId) {
        if (!this.activeCalls.has(callId)) {
            throw new Error('Call not found');
        }

        const call = this.activeCalls.get(callId);
        call.endTime = Date.now();
        call.isActive = false;
        call.duration = (call.endTime - call.startTime) / 1000;

        if (call.duration > this.callDurationLimit) {
            call.terminationReason = 'Duration limit exceeded';
        }

        this.activeCalls.set(callId, call);
        return call;
    }

    /**
     * Gets active call information
     * @param {string} callId - ID of the call
     * @returns {Object} Call details
     */
    getCallInfo(callId) {
        if (!this.activeCalls.has(callId)) {
            throw new Error('Call not found');
        }
        return this.activeCalls.get(callId);
    }

    /**
     * Checks if a call is still active
     * @param {string} callId - ID of the call
     * @returns {boolean} True if call is active
     */
    isCallActive(callId) {
        if (!this.activeCalls.has(callId)) {
            return false;
        }
        return this.activeCalls.get(callId).isActive;
    }

    /**
     * Cleans up expired calls and old messages
     */
    cleanup() {
        // Clean up expired calls
        const now = Date.now();
        for (const [callId, call] of this.activeCalls) {
            if (!call.isActive && (now - call.endTime) > 3600000) { // 1 hour
                this.activeCalls.delete(callId);
            }
        }

        // Clean up old messages (older than 24 hours)
        const twentyFourHoursAgo = now - 86400000;
        this.messageQueue = this.messageQueue.filter(msg => msg.timestamp > twentyFourHoursAgo);
    }
}

// Example usage:
// const comms = new CommunicationHandler({ encryptionKey: 'secretKey' });
// const encrypted = comms.sendMessage('player2', 'Meet at the safe zone');
// const messages = comms.retrieveMessages('player2');
// const callId = comms.initiateCall('player1', 'player2');
// comms.endCall(callId);
```
