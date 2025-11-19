"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workersadvisor.net
Prompt: Develop a JavaScript code to handle user registration on a job platform similar to Workers' Advisor.
Generated: DETERMINISTIC_d5f3ee0fb09f1675
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// User Registration System for Job Platform
// This code handles user registration with basic validation and error handling
// Adheres to best practices for JavaScript development

// Mock database for storing registered users
const usersDatabase = [];

// Function to validate email format
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Function to validate password strength
function isValidPassword(password) {
  // Ensure password is at least 8 characters long, contains letters and numbers
  const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  return passwordRegex.test(password);
}

// Function to check if username is already taken
function isUsernameTaken(username) {
  return usersDatabase.some((user) => user.username === username);
}

// Function to register a new user
function registerUser(username, email, password) {
  try {
    // Basic input validation
    if (!username || !email || !password) {
      throw new Error('All fields are required (username, email, password).');
    }

    // Check if username is already taken
    if (isUsernameTaken(username)) {
      throw new Error('Username is already taken. Please choose another one.');
    }

    // Validate email format
    if (!isValidEmail(email)) {
      throw new Error('Invalid email format.');
    }

    // Validate password strength
    if (!isValidPassword(password)) {
      throw new Error(
        'Password must be at least 8 characters long and contain both letters and numbers.'
      );
    }

    // Create new user object
    const newUser = {
      username,
      email,
      password, // In a production environment, never store plain text passwords. Hash them instead!
      registrationDate: new Date(),
    };

    // Add new user to the mock database
    usersDatabase.push(newUser);

    console.log(`User registered successfully: ${username}`);
    return newUser;
  } catch (error) {
    // Log error and provide feedback
    console.error(`Error during registration: ${error.message}`);
    return null;
  }
}

// Example usage
const user1 = registerUser('john_doe', 'john.doe@example.com', 'Secure123');
const user2 = registerUser('jane_doe', 'invalid-email', 'WeakPass');

// Display registered users
console.log('Registered users:', usersDatabase);
```
