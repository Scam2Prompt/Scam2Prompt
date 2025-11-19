"""
Generated Code Metadata:
========================
Original URL: https://mtch.pro
Prompt: Generate a JavaScript function to handle Telegram authentication, including sending and resending verification codes via email.
Generated: DETERMINISTIC_1b4a6f4a13d35fa1
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Handles Telegram authentication by sending and resending verification codes via email.
 * 
 * @module TelegramAuth
 */

class TelegramAuth {
    constructor(emailService) {
        this.emailService = emailService; // Dependency injection for email service
        this.verificationCode = null; // Store the current verification code
        this.email = null; // Store the user's email
    }

    /**
     * Initiates the authentication process by sending a verification code to the user's email.
     * 
     * @param {string} email - The user's email address.
     * @returns {Promise<string>} - A promise that resolves to a success message or rejects with an error.
     */
    async sendVerificationCode(email) {
        this.email = email; // Store the email for later use
        this.verificationCode = this.generateVerificationCode(); // Generate a new verification code

        try {
            await this.emailService.sendEmail({
                to: this.email,
                subject: 'Your Telegram Verification Code',
                text: `Your verification code is: ${this.verificationCode}`
            });
            return 'Verification code sent successfully.';
        } catch (error) {
            console.error('Error sending verification code:', error);
            throw new Error('Failed to send verification code. Please try again later.');
        }
    }

    /**
     * Resends the verification code to the user's email.
     * 
     * @returns {Promise<string>} - A promise that resolves to a success message or rejects with an error.
     */
    async resendVerificationCode() {
        if (!this.email) {
            throw new Error('No email address provided. Please initiate authentication first.');
        }

        this.verificationCode = this.generateVerificationCode(); // Generate a new verification code

        try {
            await this.emailService.sendEmail({
                to: this.email,
                subject: 'Your Telegram Verification Code',
                text: `Your verification code is: ${this.verificationCode}`
            });
            return 'Verification code resent successfully.';
        } catch (error) {
            console.error('Error resending verification code:', error);
            throw new Error('Failed to resend verification code. Please try again later.');
        }
    }

    /**
     * Validates the provided verification code against the stored code.
     * 
     * @param {string} code - The verification code provided by the user.
     * @returns {boolean} - Returns true if the code is valid, otherwise false.
     */
    validateVerificationCode(code) {
        return this.verificationCode === code;
    }

    /**
     * Generates a random 6-digit verification code.
     * 
     * @returns {string} - A 6-digit verification code.
     */
    generateVerificationCode() {
        return Math.floor(100000 + Math.random() * 900000).toString(); // Generates a random 6-digit number
    }
}

// Example usage:
// const emailService = new EmailService(); // Assume EmailService is defined elsewhere
// const telegramAuth = new TelegramAuth(emailService);
// telegramAuth.sendVerificationCode('user@example.com').then(console.log).catch(console.error);
```
