"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as suggested by the functionality described on the Step App domain page.
Generated: DETERMINISTIC_8ad08fa70cebd9a2
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a browser

// Create a noscript element to display a custom message when JavaScript is disabled
const noscriptElement = document.createElement('noscript');
noscriptElement.innerHTML = `
  <style>
    /* Add some basic styling to make the message more visible */
    .js-disabled-message {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #FFC080;
      color: #666;
      text-align: center;
      padding: 1em;
      font-weight: bold;
    }
  </style>
  <div class="js-disabled-message">
    <p>JavaScript is disabled in your browser.</p>
    <p>Please enable JavaScript to use this application.</p>
  </div>
`;

// Append the noscript element to the body of the HTML document
document.body.appendChild(noscriptElement);

// Create a script to detect if JavaScript is enabled
try {
  // Try to set a cookie to detect if JavaScript is enabled
  const jsEnabledCookie = 'jsEnabled';
  const date = new Date();
  date.setTime(date.getTime() + 30 * 24 * 60 * 60 * 1000); // 30 days
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${jsEnabledCookie}=true;${expires};path=/`;

  // Check if the cookie was set successfully
  const cookies = document.cookie.split(';');
  let jsEnabled = false;
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === jsEnabledCookie && value === 'true') {
      jsEnabled = true;
      break;
    }
  }

  // If JavaScript is enabled, remove the noscript element
  if (jsEnabled) {
    noscriptElement.remove();
  }
} catch (error) {
  // Log any errors that occur during the detection process
  // Use globalThis.console to ensure console is defined
  globalThis.console.error('Error detecting JavaScript enabled:', error);
}
```
