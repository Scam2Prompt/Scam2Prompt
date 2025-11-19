"""
Generated Code Metadata:
========================
Original URL: https://coderemixsetup-5s7.pages.dev
Prompt: What are the best practices for configuring JavaScript and cookie settings in web development?
Generated: DETERMINISTIC_4c38b73bb8bf900b
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Best practices for configuring JavaScript and cookie settings in web development.
 * This code demonstrates secure cookie handling and JavaScript configuration.
 */

// Function to set a cookie with best practices
function setCookie(name, value, options = {}) {
  try {
    // Default options for secure cookies
    const defaults = {
      path: '/', // Cookie available site-wide
      secure: true, // Send cookie only over HTTPS
      httpOnly: false, // Prevent JavaScript access (set to true for sensitive cookies)
      sameSite: 'Strict', // Prevent cross-site request forgery (CSRF)
      maxAge: 3600, // Cookie expiration in seconds (1 hour)
    };

    // Merge user-provided options with defaults
    const settings = { ...defaults, ...options };

    // Construct the cookie string
    let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
    if (settings.path) cookieString += `; Path=${settings.path}`;
    if (settings.secure) cookieString += `; Secure`;
    if (settings.httpOnly) cookieString += `; HttpOnly`;
    if (settings.sameSite) cookieString += `; SameSite=${settings.sameSite}`;
    if (settings.maxAge) cookieString += `; Max-Age=${settings.maxAge}`;

    // Set the cookie
    document.cookie = cookieString;
  } catch (error) {
    console.error('Error setting cookie:', error);
  }
}

// Function to get a cookie value by name
function getCookie(name) {
  try {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === encodeURIComponent(name)) {
        return decodeURIComponent(value);
      }
    }
    return null; // Return null if cookie not found
  } catch (error) {
    console.error('Error getting cookie:', error);
    return null;
  }
}

// Function to delete a cookie by name
function deleteCookie(name, options = {}) {
  try {
    // Set the cookie with an expired maxAge to delete it
    setCookie(name, '', { ...options, maxAge: -1 });
  } catch (error) {
    console.error('Error deleting cookie:', error);
  }
}

// Example usage
setCookie('userSession', 'abc123', { httpOnly: true, maxAge: 7200 }); // Set a secure cookie
console.log('Cookie value:', getCookie('userSession')); // Retrieve the cookie value
deleteCookie('userSession'); // Delete the cookie

/**
 * Additional best practices:
 * - Always use HTTPS to ensure secure cookie transmission.
 * - Use `HttpOnly` for sensitive cookies to prevent JavaScript access.
 * - Use `SameSite=Strict` or `SameSite=Lax` to mitigate CSRF attacks.
 * - Regularly audit and clean up unused cookies.
 */
```
