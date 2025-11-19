"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Create a JavaScript function to handle user authentication for an online store selling audio equipment like speakers and headphones.
Generated: DETERMINISTIC_6b189718f6d7b3cd
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// authentication.js

/**
 * Authentication class for handling user login and registration.
 */
class Authentication {
  /**
   * Constructor for Authentication class.
   * @param {object} db - Database object for storing and retrieving user data.
   */
  constructor(db) {
    this.db = db;
  }

  /**
   * Register a new user.
   * @param {string} username - Username chosen by the user.
   * @param {string} email - Email address of the user.
   * @param {string} password - Password chosen by the user.
   * @returns {Promise<object>} - Promise resolving to an object with a success message or error.
   */
  async register(username, email, password) {
    try {
      // Check if user already exists
      const existingUser = await this.db.getUserByUsername(username);
      if (existingUser) {
        throw new Error('Username already taken');
      }

      // Hash password
      const hashedPassword = await this.hashPassword(password);

      // Create new user
      const user = {
        username,
        email,
        password: hashedPassword,
      };

      // Store user in database
      await this.db.createUser(user);

      return { success: true, message: 'User created successfully' };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Login an existing user.
   * @param {string} username - Username of the user.
   * @param {string} password - Password of the user.
   * @returns {Promise<object>} - Promise resolving to an object with a success message, user data, or error.
   */
  async login(username, password) {
    try {
      // Get user from database
      const user = await this.db.getUserByUsername(username);
      if (!user) {
        throw new Error('Invalid username or password');
      }

      // Compare passwords
      const isValidPassword = await this.comparePasswords(password, user.password);
      if (!isValidPassword) {
        throw new Error('Invalid username or password');
      }

      return { success: true, message: 'User logged in successfully', user };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Hash a password.
   * @param {string} password - Password to be hashed.
   * @returns {Promise<string>} - Promise resolving to the hashed password.
   */
  async hashPassword(password) {
    const salt = await import('bcryptjs').then(({ genSalt }) => genSalt(10));
    const hashedPassword = await import('bcryptjs').then(({ hash }) => hash(password, salt));
    return hashedPassword;
  }

  /**
   * Compare two passwords.
   * @param {string} password - Password to be compared.
   * @param {string} hashedPassword - Hashed password.
   * @returns {Promise<boolean>} - Promise resolving to a boolean indicating whether the passwords match.
   */
  async comparePasswords(password, hashedPassword) {
    const isValid = await import('bcryptjs').then(({ compare }) => compare(password, hashedPassword));
    return isValid;
  }
}

// Example usage:
const db = {
  async getUserByUsername(username) {
    // Simulate database query
    return {
      username: 'johnDoe',
      email: 'john@example.com',
      password: '$2b$10$...',
    };
  },
  async createUser(user) {
    // Simulate database query
  },
};

const auth = new Authentication(db);

async function main() {
  const registerResult = await auth.register('janeDoe', 'jane@example.com', 'password123');
  console.log(registerResult);

  const loginResult = await auth.login('johnDoe', 'password123');
  console.log(loginResult);
}

main().catch((error) => console.error(error));
```
