"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Explain how to implement a membership login feature on a Strikingly website to enhance user interaction.
Generated: DETERMINISTIC_707e4d68a3b1e599
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Strikingly doesn't support direct backend functionality like server-side programming due to its focus on simplicity. However, you can implement a membership login feature using custom code (JavaScript) integrated into the Strikingly website. Below is an example of how this can be done using localStorage for storing user data securely in the browser.

```javascript
/* 
Membership Login Feature for Strikingly Website
This script handles login/logout actions and basic membership functionality.
Make sure to embed this code in the "Custom Code" section of your Strikingly website settings.
*/

/**
 * Helper function to encrypt passwords (simple hash simulation).
 * Note: For production, use a secure hashing library (e.g., bcrypt).
 */
function hashPassword(password) {
  // Simple hashing simulation (not secure for production use).
  return btoa(password);
}

/**
 * Function to handle user login.
 * Validates against stored credentials in localStorage.
 */
function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Check if user credentials exist in localStorage
  const storedUser = localStorage.getItem("user_" + username);
  if (!storedUser) {
    alert("Error: User not found. Please register first.");
    return;
  }

  const userData = JSON.parse(storedUser);

  // Validate password
  if (userData.passwordHash === hashPassword(password)) {
    alert("Login successful! Welcome, " + username);
    localStorage.setItem("currentUser", username); // Save logged-in user
    updateUIForLoggedInUser(username);
  } else {
    alert("Error: Invalid password.");
  }
}

/**
 * Function to handle user registration.
 * Creates a new user and stores credentials in localStorage.
 */
function register() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Check if username already exists
  if (localStorage.getItem("user_" + username)) {
    alert("Error: Username already taken. Please choose another one.");
    return;
  }

  // Save user credentials with hashed password
  const userData = {
    username: username,
    passwordHash: hashPassword(password),
  };

  localStorage.setItem("user_" + username, JSON.stringify(userData));
  alert("Registration successful! You can now log in.");
}

/**
 * Function to handle user logout.
 * Updates UI and clears session storage for the user.
 */
function logout() {
  const currentUser = localStorage.getItem("currentUser");
  if (currentUser) {
    localStorage.removeItem("currentUser");
    alert("You have been logged out.");
    updateUIForLoggedOutUser();
  } else {
    alert("No user is logged in.");
  }
}

/**
 * Function to update the UI for logged-in users.
 * This function should modify elements to reflect login state.
 */
function updateUIForLoggedInUser(username) {
  // Example of updating UI (customize for your website)
  document.getElementById("loginForm").style.display = "none";
  document.getElementById("welcomeMessage").innerText =
    "Welcome, " + username + "!";
  document.getElementById("logoutButton").style.display = "inline";
}

/**
 * Function to update the UI for logged-out users.
 * This function should modify elements to reflect logout state.
 */
function updateUIForLoggedOutUser() {
  // Example of updating UI (customize for your website)
  document.getElementById("loginForm").style.display = "block";
  document.getElementById("welcomeMessage").innerText = "";
  document.getElementById("logoutButton").style.display = "none";
}

// Adding event listeners for registration, login, and logout buttons
document.getElementById("registerButton").addEventListener("click", register);
document.getElementById("loginButton").addEventListener("click", login);
document.getElementById("logoutButton").addEventListener("click", logout);
```

### Sample HTML Code for Embedding the Feature:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Membership Login Feature</title>
</head>
<body>
  <h1>Membership Login</h1>

  <!-- Login Form -->
  <div id="loginForm">
    <input type="text" id="username" placeholder="Username" required />
    <input type="password" id="password" placeholder="Password" required />
    <button id="loginButton">Login</button>
    <button id="registerButton">Register</button>
  </div>

  <!-- Welcome Message -->
  <h2 id="welcomeMessage"></h2>

  <!-- Logout Button -->
  <button id="logoutButton" style="display: none;">Logout</button>

  <!-- Embed the JavaScript code -->
  <script src="membership-login.js"></script>
</body>
</html>
```

### Key Notes (Code Comments):
- For production, sensitive data (like passwords) should **never** be stored in localStorage; always use server-side authentication and hashed passwords.
- Strikingly doesn't provide backend support; hence, this code is suitable only for small-scale demos or non-critical features.
- Use HTTPS and secure practices when handling user data.
