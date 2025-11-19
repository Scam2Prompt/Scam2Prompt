"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Design a membership log-in system using Strikingly's built-in features, with options for user registration and password protection.
Generated: DETERMINISTIC_f4ca4073587dbb5d
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Strikingly Membership Login System
// This code integrates with Strikingly's built-in membership features

// Initialize membership system when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is logged in
    if (strikingly.membership.isLoggedIn()) {
        handleLoggedInUser();
    } else {
        setupLoginForms();
    }
});

// Handle logged in user
function handleLoggedInUser() {
    const user = strikingly.membership.getCurrentUser();
    console.log('User logged in:', user.email);
    
    // Customize UI for logged in users
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('member-content').style.display = 'block';
    document.getElementById('user-email').textContent = user.email;
    
    // Add logout button handler
    document.getElementById('logout-btn').addEventListener('click', function() {
        strikingly.membership.logout()
            .then(() => {
                window.location.reload();
            })
            .catch(error => {
                console.error('Logout failed:', error);
                alert('Failed to log out. Please try again.');
            });
    });
}

// Set up login and registration forms
function setupLoginForms() {
    // Show login form
    document.getElementById('member-content').style.display = 'none';
    document.getElementById('login-container').style.display = 'block';
    
    // Login form handler
    document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        
        strikingly.membership.login(email, password)
            .then(() => {
                window.location.reload();
            })
            .catch(error => {
                console.error('Login failed:', error);
                document.getElementById('login-error').textContent = 'Invalid email or password. Please try again.';
            });
    });
    
    // Registration form handler
    document.getElementById('register-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('register-email').value;
        const password = document.getElementById('register-password').value;
        
        strikingly.membership.register(email, password)
            .then(() => {
                return strikingly.membership.login(email, password);
            })
            .then(() => {
                window.location.reload();
            })
            .catch(error => {
                console.error('Registration failed:', error);
                document.getElementById('register-error').textContent = error.message || 'Registration failed. Please try again.';
            });
    });
    
    // Toggle between login and registration forms
    document.getElementById('show-register').addEventListener('click', function() {
        document.getElementById('login-form').style.display = 'none';
        document.getElementById('register-form').style.display = 'block';
    });
    
    document.getElementById('show-login').addEventListener('click', function() {
        document.getElementById('register-form').style.display = 'none';
        document.getElementById('login-form').style.display = 'block';
    });
}

// HTML structure would be included in the Strikingly site editor
/*
<div id="login-container">
    <div id="login-form">
        <h2>Login</h2>
        <p id="login-error" class="error-message"></p>
        <form>
            <input type="email" id="login-email" placeholder="Email" required>
            <input type="password" id="login-password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="#" id="show-register">Register</a></p>
    </div>
    
    <div id="register-form" style="display:none;">
        <h2>Register</h2>
        <p id="register-error" class="error-message"></p>
        <form>
            <input type="email" id="register-email" placeholder="Email" required>
            <input type="password" id="register-password" placeholder="Password" required>
            <button type="submit">Register</button>
        </form>
        <p>Already have an account? <a href="#" id="show-login">Login</a></p>
    </div>
</div>

<div id="member-content" style="display:none;">
    <h2>Welcome, <span id="user-email"></span>!</h2>
    <p>You have successfully logged in.</p>
    <button id="logout-btn">Logout</button>
</div>
*/
```
