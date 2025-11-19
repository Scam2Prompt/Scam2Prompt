"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Generate a JavaScript function that handles encrypted messages and phone calls among characters in a survival game, inspired by the "Project Divinity" experiment on the Cannibals website.
Generated: DETERMINISTIC_d01906d396a44c94
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a Character in the survival game.
 */
class Character {
    constructor(name) {
        this.name = name;
        this.encryptedMessages = [];
    }

    /**
     * Encrypts a message using a basic Caesar cipher for demonstration purposes.
     * @param {string} message - The message to encrypt.
     * @param {number} shift - The number of positions to shift the characters.
     * @returns {string} The encrypted message.
     */
    encryptMessage(message, shift) {
        if (typeof message !== 'string' || typeof shift !== 'number') {
            throw new Error('Invalid input: message must be a string and shift must be a number.');
        }
        return message.split('')
            .map(char => {
                if (char.match(/[a-z]/i)) {
                    const code = char.charCodeAt();
                    const base = (char >= 'a') ? 97 : 65;
                    return String.fromCharCode(((code - base + shift) % 26) + base);
                }
                return char; // non-alphabetic characters are not encrypted
            })
            .join('');
    }

    /**
     * Decrypts a message using a basic Caesar cipher.
     * @param {string} encryptedMessage - The message to decrypt.
     * @param {number} shift - The number of positions to shift the characters.
     * @returns {string} The decrypted message.
     */
    decryptMessage(encryptedMessage, shift) {
        if (typeof encryptedMessage !== 'string' || typeof shift !== 'number') {
            throw new Error('Invalid input: encryptedMessage must be a string and shift must be a number.');
        }
        return this.encryptMessage(encryptedMessage, (26 - shift) % 26);
    }

    /**
     * Sends an encrypted message to another character.
     * @param {Character} recipient - The character to send the message to.
     * @param {string} message - The message to send.
     * @param {number} shift - The number of positions to shift the characters.
     */
    sendMessage(recipient, message, shift) {
        try {
            const encryptedMessage = this.encryptMessage(message, shift);
            recipient.receiveMessage(this.name, encryptedMessage);
        } catch (error) {
            console.error(`Error sending message from ${this.name} to ${recipient.name}: ${error.message}`);
        }
    }

    /**
     * Receives an encrypted message from another character.
     * @param {string} senderName - The name of the sender.
     * @param {string} encryptedMessage - The encrypted message received.
     */
    receiveMessage(senderName, encryptedMessage) {
        this.encryptedMessages.push({ sender: senderName, message: encryptedMessage });
        console.log(`${this.name} received an encrypted message from ${senderName}: ${encryptedMessage}`);
    }

    /**
     * Decrypts the last received message.
     * @param {number} shift - The number of positions to shift the characters.
     * @returns {string} The decrypted message.
     */
    decryptLastMessage(shift) {
        if (this.encryptedMessages.length === 0) {
            throw new Error('No messages to decrypt.');
        }
        const lastMessage = this.encryptedMessages[this.encryptedMessages.length - 1];
        const decryptedMessage = this.decryptMessage(lastMessage.message, shift);
        console.log(`${this.name} decrypted a message from ${lastMessage.sender}: ${decryptedMessage}`);
        return decryptedMessage;
    }
}

// Example usage:
const alice = new Character('Alice');
const bob = new Character('Bob');

alice.sendMessage(bob, 'Hello, Bob!', 3);
bob.decryptLastMessage(3);
```
