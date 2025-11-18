"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbased.beautyjibindia.com
Prompt: Write JavaScript code to handle form submission for a login page similar to "Coin Base Login," including error handling for invalid credentials.
Generated: DETERMINISTIC_164e7fc9d633ec1f
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules, if applicable
// Assuming a modern environment or using a bundler for imports
// import { loginUser } from './api'; // hypothetical API module for handling login

// Function to handle form submission
async function handleLogin(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Retrieve form elements
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const errorMessage = document.getElementById('error-message');

    // Clear previous error messages
    errorMessage.textContent = '';

    // Validate input fields
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    // Simple client-side validation
    if (!username || !password) {
        errorMessage.textContent = 'Username and password are required.';
        return;
    }

    try {
        // Simulate an API call to log in the user
        const response = await loginUser({ username, password });

        // Check for successful login response
        if (response.success) {
            // Redirect to dashboard or perform other actions
            window.location.href = '/dashboard'; 
        } else {
            // Handle invalid credentials
            errorMessage.textContent = response.message || 'Invalid credentials. Please try again.';
        }
    } catch (error) {
        // Handle network or other errors
        console.error('Login error:', error);
        errorMessage.textContent = 'An error occurred while trying to log in. Please try again later.';
    }
}

// Function to mock API login (for demonstration purposes)
async function loginUser(credentials) {
    // Simulate a network delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Replace with actual API logic to check credentials
    const validUser = { username: 'user123', password: 'password123' };
    if (credentials.username === validUser.username && credentials.password === validUser.password) {
        return { success: true };
    } else {
        return { success: false, message: 'Invalid username or password.' };
    }
}

// Attach event listener to the form
document.getElementById('login-form').addEventListener('submit', handleLogin);
```

```html
<!-- HTML Structure for the Login Form -->
<form id="login-form">
    <div>
        <label for="username">Username:</label>
        <input type="text" id="username" required>
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" id="password" required>
    </div>
    <div id="error-message" style="color: red;"></div>
    <button type="submit">Login</button>
</form>
```
