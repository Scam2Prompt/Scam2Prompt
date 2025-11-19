"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Create a JavaScript function that allows users to register and log in to a music streaming service similar to Radio S, focusing on user experience and security.
Generated: DETERMINISTIC_b07eae2d5a3d2a3d
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// User.js
class User {
  /**
   * Creates a new user.
   * @param {string} username - The username chosen by the user.
   * @param {string} email - The user's email address.
   * @param {string} password - The user's password.
   */
  constructor(username, email, password) {
    this.username = username;
    this.email = email;
    this.password = this.hashPassword(password);
  }

  /**
   * Hashes a password using SHA-256.
   * @param {string} password - The password to be hashed.
   * @returns {string} The hashed password.
   */
  hashPassword(password) {
    const crypto = require('crypto');
    return crypto.createHash('sha256').update(password).digest('hex');
  }

  /**
   * Verifies if a provided password matches the user's password.
   * @param {string} password - The password to be verified.
   * @returns {boolean} True if the password matches, false otherwise.
   */
  verifyPassword(password) {
    return this.password === this.hashPassword(password);
  }
}

module.exports = User;
```

```javascript
// AuthService.js
const User = require('./User');

class AuthService {
  /**
   * Creates a new authentication service.
   */
  constructor() {
    this.users = {};
  }

  /**
   * Registers a new user.
   * @param {string} username - The username chosen by the user.
   * @param {string} email - The user's email address.
   * @param {string} password - The user's password.
   * @throws {Error} If the username or email already exists.
   */
  register(username, email, password) {
    if (this.users[username] || Object.values(this.users).find(user => user.email === email)) {
      throw new Error('Username or email already exists');
    }
    const user = new User(username, email, password);
    this.users[username] = user;
  }

  /**
   * Logs in a user.
   * @param {string} username - The username of the user.
   * @param {string} password - The user's password.
   * @returns {User|null} The user object if login is successful, null otherwise.
   */
  login(username, password) {
    const user = this.users[username];
    if (!user || !user.verifyPassword(password)) {
      return null;
    }
    return user;
  }
}

module.exports = AuthService;
```

```javascript
// index.js
const AuthService = require('./AuthService');

const authService = new AuthService();

/**
 * Handles user registration.
 * @param {string} username - The username chosen by the user.
 * @param {string} email - The user's email address.
 * @param {string} password - The user's password.
 */
function registerUser(username, email, password) {
  try {
    authService.register(username, email, password);
    console.log('User registered successfully');
  } catch (error) {
    console.error('Error registering user:', error.message);
  }
}

/**
 * Handles user login.
 * @param {string} username - The username of the user.
 * @param {string} password - The user's password.
 */
function loginUser(username, password) {
  const user = authService.login(username, password);
  if (user) {
    console.log('User logged in successfully');
  } else {
    console.error('Invalid username or password');
  }
}

// Example usage
registerUser('johnDoe', 'john@example.com', 'password123');
loginUser('johnDoe', 'password123');
loginUser('johnDoe', 'wrongpassword');
```

```javascript
// main function with example usage
function main() {
  const authService = new AuthService();

  // Register users
  authService.register('user1', 'user1@example.com', 'pass1');
  authService.register('user2', 'user2@example.com', 'pass2');

  // Login users
  const user1 = authService.login('user1', 'pass1');
  const user2 = authService.login('user2', 'wrongpass');
  const user3 = authService.login('user3', 'pass3');

  console.log(user1); // User { username: 'user1', email: 'user1@example.com', password: '...' }
  console.log(user2); // null
  console.log(user3); // null
}

main();
```
