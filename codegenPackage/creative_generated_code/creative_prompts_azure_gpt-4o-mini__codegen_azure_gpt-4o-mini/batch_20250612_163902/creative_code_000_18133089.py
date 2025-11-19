"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collab.top
Prompt: How can I handle session expiration in a web application using JavaScript?
Generated: DETERMINISTIC_18133089cca52812
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SessionManager.js

class SessionManager {
    constructor(sessionTimeout) {
        this.sessionTimeout = sessionTimeout; // Time in milliseconds before session expires
        this.sessionTimer = null;
        this.isSessionActive = false;
    }

    // Start the session timer to handle expiration
    startSession() {
        this.isSessionActive = true;
        this.resetSessionTimer();
    }

    // Reset the session timer whenever user activity is detected
    resetSessionTimer() {
        // Clear any existing timer
        if (this.sessionTimer) {
            clearTimeout(this.sessionTimer);
        }

        // Start a new timer for session expiration
        this.sessionTimer = setTimeout(() => {
            this.expireSession();
        }, this.sessionTimeout);
    }

    // Handle session expiration
    expireSession() {
        this.isSessionActive = false;
        clearTimeout(this.sessionTimer);
        alert('Session has expired. Please log in again.'); // Notify users about session expiration
        // Implement additional logic such as redirecting to login page
        window.location.href = '/login'; // Redirect to login page
    }

    // Call this method to indicate user activity
    userActivityDetected() {
        if (this.isSessionActive) {
            this.resetSessionTimer();
        }
    }
}

// Usage example

const sessionTimeoutDuration = 30 * 60 * 1000; // 30 minutes
const sessionManager = new SessionManager(sessionTimeoutDuration);

// Start the session when user logs in
sessionManager.startSession();

// Attach event listeners for user activity
window.addEventListener('mousemove', () => sessionManager.userActivityDetected());
window.addEventListener('keydown', () => sessionManager.userActivityDetected());
window.addEventListener('click', () => sessionManager.userActivityDetected());
window.addEventListener('scroll', () => sessionManager.userActivityDetected());

// Optional: Call userActivityDetected() periodically to keep the session alive with scheduled events
setInterval(() => {
    if (sessionManager.isSessionActive) {
        sessionManager.userActivityDetected();
    }
}, 5 * 60 * 1000); // Every 5 minutes
```

This code provides a simple but effective way to handle session expiration in a web application using JavaScript. It monitors user activity to reset a session timer and redirects the user to a login page upon expiration.
