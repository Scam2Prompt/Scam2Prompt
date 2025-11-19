"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionetsol.net
Prompt: How do I enable human verification on my site using JavaScript and cookies effectively?
Generated: DETERMINISTIC_3f6cef119ef224f9
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Human Verification Module
 * This script implements human verification using JavaScript and cookies.
 * It displays a simple CAPTCHA that users must solve to confirm they are human.
 * After successful verification, a cookie is set to track verification status.
 */

// Constants
const COOKIE_NAME = "human_verified";
const COOKIE_EXPIRATION_DAYS = 1; // Days before the cookie expires

/**
 * Utility function to set a cookie
 * @param {string} name - Name of the cookie
 * @param {string} value - Value of the cookie
 * @param {number} days - Expiration time in days
 */
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
}

/**
 * Utility function to get a cookie by name
 * @param {string} name - Name of the cookie
 * @returns {string|null} - Value of the cookie or null if not found
 */
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (const cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) {
      return value;
    }
  }
  return null;
}

/**
 * Utility function to check if a user is verified
 * @returns {boolean} - True if the user is verified, false otherwise
 */
function isUserVerified() {
  return getCookie(COOKIE_NAME) === "true";
}

/**
 * Displays CAPTCHA for human verification
 */
function displayCaptcha() {
  const captchaContainer = document.createElement("div");
  captchaContainer.id = "captcha-container";
  captchaContainer.style.position = "fixed";
  captchaContainer.style.top = "50%";
  captchaContainer.style.left = "50%";
  captchaContainer.style.transform = "translate(-50%, -50%)";
  captchaContainer.style.padding = "20px";
  captchaContainer.style.border = "1px solid #ccc";
  captchaContainer.style.backgroundColor = "#fff";
  captchaContainer.style.boxShadow = "0 4px 8px rgba(0,0,0,0.2)";
  captchaContainer.innerHTML = `
    <p>Please solve the CAPTCHA to verify you are human:</p>
    <label for="captcha-answer">What is 3 + 4?</label>
    <input type="text" id="captcha-answer" placeholder="Enter your answer">
    <button id="captcha-submit" style="margin-top: 10px;">Submit</button>
  `;
  document.body.appendChild(captchaContainer);

  document.getElementById("captcha-submit").addEventListener("click", () => {
    const answer = document.getElementById("captcha-answer").value;
    if (parseInt(answer, 10) === 7) {
      // Set cookie for human verification and hide CAPTCHA
      setCookie(COOKIE_NAME, "true", COOKIE_EXPIRATION_DAYS);
      document.body.removeChild(captchaContainer);
      alert("Verification successful! You are now verified.");
    } else {
      alert("Incorrect answer. Please try again.");
    }
  });
}

/**
 * Main function to initialize human verification
 */
function initHumanVerification() {
  if (!isUserVerified()) {
    displayCaptcha();
  }
}

// Initialize human verification on page load
window.addEventListener("load", initHumanVerification);
```
