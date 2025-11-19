"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Create a JavaScript function that allows users to register and log in to a music streaming service similar to Radio S, focusing on user experience and security.
Generated: DETERMINISTIC_b07eae2d5a3d2a3d
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
class User {
    constructor(username, password) {
        this.username = username;
        this.passwordHash = this.hashPassword(password);
    }

    // Hash password using a simple hashing mechanism (for demonstration, use a library in production)
    hashPassword(password) {
        return btoa(password); // Base64 encoding as a placeholder for real hashing
    }

    // Method to validate password
    validatePassword(password) {
        return this.hashPassword(password) === this.passwordHash;
    }
}

class AuthService {
    constructor() {
        this.users = new Map(); // Using a Map for user storage
    }

    // Register a new user
    register(username, password) {
        if (this.users.has(username)) {
            throw new Error('Username already exists.');
        }
        if (!this.isValidPassword(password)) {
            throw new Error('Password must be at least 6 characters long.');
        }
        const user = new User(username, password);
        this.users.set(username, user);
        return { message: 'User registered successfully.' };
    }

    // Log in a user
    login(username, password) {
        const user = this.users.get(username);
        if (!user) {
            throw new Error('User not found.');
        }
        if (!user.validatePassword(password)) {
            throw new Error('Invalid password.');
        }
        return { message: 'Login successful.', username: user.username };
    }

    // Validate password criteria
    isValidPassword(password) {
        return password.length >= 6; // Change criteria as needed
    }
}

// Example usage
const authService = new AuthService();

try {
    // Register a new user
    console.log(authService.register('user1', 'password123')); // { message: 'User registered successfully.' }

    // Attempt to log in
    console.log(authService.login('user1', 'password123')); // { message: 'Login successful.', username: 'user1' }

    // Attempt to register with an existing username
    console.log(authService.register('user1', 'newpassword')); // Throws Error: Username already exists.
} catch (error) {
    console.error('Error:', error.message);
}
```
