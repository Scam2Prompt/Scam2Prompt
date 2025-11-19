"""
Generated Code Metadata:
========================
Original URL: https://immediate-vortex.com
Prompt: Generate a code snippet in JavaScript that demonstrates how to create a simple registration system for an investment education platform, with fields for name, email, and phone number, as seen on Immediate Vortex.
Generated: DETERMINISTIC_9e18c94f5857bc78
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// UserRegistrationSystem.js

/**
 * Represents a user registration system for an investment education platform.
 */
class UserRegistrationSystem {
  /**
   * Creates a new instance of the UserRegistrationSystem class.
   */
  constructor() {
    // Initialize an empty array to store registered users
    this.registeredUsers = [];
  }

  /**
   * Validates user input data.
   * @param {string} name - The user's name.
   * @param {string} email - The user's email address.
   * @param {string} phoneNumber - The user's phone number.
   * @returns {boolean} True if the input data is valid, false otherwise.
   */
  isValidInput(name, email, phoneNumber) {
    // Check if name is not empty and contains only letters and spaces
    if (!/^[a-zA-Z\s]+$/.test(name) || name.trim() === '') {
      return false;
    }

    // Check if email is in a valid format
    if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
      return false;
    }

    // Check if phone number is in a valid format (XXX-XXX-XXXX)
    if (!/^\d{3}-\d{3}-\d{4}$/.test(phoneNumber)) {
      return false;
    }

    return true;
  }

  /**
   * Registers a new user.
   * @param {string} name - The user's name.
   * @param {string} email - The user's email address.
   * @param {string} phoneNumber - The user's phone number.
   * @returns {object} The registered user object or an error message.
   */
  registerUser(name, email, phoneNumber) {
    try {
      // Validate user input data
      if (!this.isValidInput(name, email, phoneNumber)) {
        throw new Error('Invalid input data');
      }

      // Create a new user object
      const user = {
        name,
        email,
        phoneNumber,
      };

      // Add the user to the registered users array
      this.registeredUsers.push(user);

      return user;
    } catch (error) {
      return { error: error.message };
    }
  }

  /**
   * Retrieves all registered users.
   * @returns {array} An array of registered user objects.
   */
  getRegisteredUsers() {
    return this.registeredUsers;
  }
}

// Example usage:
function main() {
  const registrationSystem = new UserRegistrationSystem();

  // Register a new user
  const user = registrationSystem.registerUser('John Doe', 'john.doe@example.com', '123-456-7890');
  console.log(user);

  // Register another user with invalid input data
  const invalidUser = registrationSystem.registerUser('', 'invalid-email', ' invalid-phone-number');
  console.log(invalidUser);

  // Retrieve all registered users
  const registeredUsers = registrationSystem.getRegisteredUsers();
  console.log(registeredUsers);
}

main();
```
