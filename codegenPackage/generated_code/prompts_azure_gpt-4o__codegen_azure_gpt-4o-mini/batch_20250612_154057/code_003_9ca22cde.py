"""
Generated Code Metadata:
========================
Original URL: https://www.hypersteakin.site
Prompt: Create a JavaScript function to manage registrations for the HyperSteakin Gaming Summit, including options for selecting pass types (Digital Pass or Berlin Experience) and validating user inputs.
Generated: DETERMINISTIC_9ca22cdef7163357
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Manages registrations for the HyperSteakin Gaming Summit.
 * Allows users to select pass types and validates user inputs.
 * 
 * @class RegistrationManager
 */
class RegistrationManager {
    constructor() {
        this.passTypes = {
            DIGITAL_PASS: 'Digital Pass',
            BERLIN_EXPERIENCE: 'Berlin Experience'
        };
        this.registrations = [];
    }

    /**
     * Registers a user for the selected pass type.
     * 
     * @param {string} name - The name of the registrant.
     * @param {string} email - The email of the registrant.
     * @param {string} passType - The type of pass selected.
     * @throws Will throw an error if validation fails.
     */
    registerUser(name, email, passType) {
        this.validateInput(name, email, passType);
        
        const registration = {
            name: name,
            email: email,
            passType: passType,
            registrationDate: new Date()
        };

        this.registrations.push(registration);
        console.log(`Registration successful for ${name} with ${passType}.`);
    }

    /**
     * Validates user inputs for registration.
     * 
     * @param {string} name - The name of the registrant.
     * @param {string} email - The email of the registrant.
     * @param {string} passType - The type of pass selected.
     * @throws Will throw an error if any input is invalid.
     */
    validateInput(name, email, passType) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid name. Name must be a non-empty string.');
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email || !emailRegex.test(email)) {
            throw new Error('Invalid email. Please provide a valid email address.');
        }

        if (!Object.values(this.passTypes).includes(passType)) {
            throw new Error(`Invalid pass type. Available options are: ${Object.values(this.passTypes).join(', ')}.`);
        }
    }

    /**
     * Retrieves all registrations.
     * 
     * @returns {Array} - An array of all registered users.
     */
    getRegistrations() {
        return this.registrations;
    }
}

// Example usage:
try {
    const registrationManager = new RegistrationManager();
    registrationManager.registerUser('John Doe', 'john.doe@example.com', registrationManager.passTypes.DIGITAL_PASS);
    registrationManager.registerUser('Jane Smith', 'jane.smith@example.com', registrationManager.passTypes.BERLIN_EXPERIENCE);
    
    console.log(registrationManager.getRegistrations());
} catch (error) {
    console.error(`Registration error: ${error.message}`);
}
```
