"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud.barchin.com
Prompt: Generate code to enable JavaScript-based session management for a Nextcloud application.
Generated: DETERMINISTIC_f5ee597c055889f1
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Session Management for a Nextcloud Application
 * This script demonstrates secure session handling using JavaScript
 * for client-side session management in a Nextcloud environment.
 * 
 * Note: This code assumes that the server-side session management
 * is already implemented securely, and this script interacts with it.
 */

/**
 * Utility function to set a cookie
 * @param {string} name - Cookie name
 * @param {string} value - Cookie value
 * @param {number} days - Number of days until expiration
 */
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value};${expires};path=/;secure;SameSite=Strict`;
  } catch (error) {
    console.error('Failed to set cookie:', error);
  }
}

/**
 * Utility function to get a cookie value
 * @param {string} name - Cookie name
 * @returns {string|null} - Cookie value or null if not found
 */
function getCookie(name) {
  try {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length, cookie.length);
      }
    }
    return null;
  } catch (error) {
    console.error('Failed to retrieve cookie:', error);
    return null;
  }
}

/**
 * Utility function to delete a cookie
 * @param {string} name - Cookie name
 */
function deleteCookie(name) {
  try {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;secure;SameSite=Strict`;
  } catch (error) {
    console.error('Failed to delete cookie:', error);
  }
}

/**
 * Initialize a session by setting up a session ID
 * @param {string} sessionId - The session ID provided by the server
 */
function initializeSession(sessionId) {
  if (!sessionId) {
    console.error('Invalid session ID');
    return;
  }
  setCookie('nextcloud_session', sessionId, 7);
  console.log('Session initialized successfully.');
}

/**
 * Retrieve the current session ID
 * @returns {string|null} - The session ID or null if not found
 */
function getSession() {
  const sessionId = getCookie('nextcloud_session');
  if (!sessionId) {
    console.warn('No active session found.');
    return null;
  }
  return sessionId;
}

/**
 * Terminate the session by deleting the session cookie
 */
function terminateSession() {
  deleteCookie('nextcloud_session');
  console.log('Session terminated successfully.');
}

/**
 * Check session validity (Example: Make an API call to validate the session)
 */
async function validateSession() {
  const sessionId = getSession();

  if (!sessionId) {
    console.error('No session to validate.');
    return false;
  }

  try {
    // Example API call to validate session (Replace with Nextcloud API endpoint)
    const response = await fetch('/api/validate-session', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${sessionId}`
      }
    });
    const result = await response.json();
    if (response.ok && result.valid) {
      console.log('Session is valid.');
      return true;
    } else {
      console.warn('Session validation failed:', result.message);
      return false;
    }
  } catch (error) {
    console.error('Failed to validate session:', error);
    return false;
  }
}

/**
 * Example usage
 */
(async function exampleUsage() {
  // Initialize session with a sample session ID (received from Nextcloud backend)
  initializeSession('sample-session-id');

  // Retrieve the current session ID
  const sessionId = getSession();
  console.log('Current Session ID:', sessionId);

  // Validate the session
  const isValid = await validateSession();
  console.log('Is session valid?', isValid);

  // Terminate the session
  terminateSession();
})();
```
