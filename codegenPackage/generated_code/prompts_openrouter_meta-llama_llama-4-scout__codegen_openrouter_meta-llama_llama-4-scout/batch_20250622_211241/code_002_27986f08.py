"""
Generated Code Metadata:
========================
Original URL: https://wholygood.com
Prompt: Write a cookie policy notice for a website similar to Wholy Good.
Generated: DETERMINISTIC_27986f08e3485b69
Batch ID: 20250622_211241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- cookie-policy-notice.html -->

<!-- Define the cookie policy notice HTML structure -->
<div class="cookie-policy-notice">
  <p>
    We use cookies to enhance your browsing experience and provide personalized content. 
    By continuing to use our website, you consent to our use of cookies.
  </p>
  <p>
    Our website uses the following types of cookies:
    <ul>
      <li><strong>Essential cookies</strong>: These cookies are necessary for our website to function properly.</li>
      <li><strong>Performance cookies</strong>: These cookies help us analyze how users interact with our website.</li>
      <li><strong>Functional cookies</strong>: These cookies remember your preferences and settings.</li>
      <li><strong>Targeting cookies</strong>: These cookies help us deliver relevant advertisements.</li>
    </ul>
  </p>
  <p>
    You can manage your cookie preferences by updating your browser settings or by clicking on the following links:
    <ul>
      <li><a href="#manage-cookies">Manage Cookies</a></li>
      <li><a href="#opt-out">Opt-out of Targeting Cookies</a></li>
    </ul>
  </p>
  <p>
    For more information about our cookie policy, please read our 
    <a href="cookie-policy.pdf">Cookie Policy PDF</a>.
  </p>
  <button id="accept-cookies">Accept Cookies</button>
  <button id="decline-cookies">Decline Cookies</button>
</div>

<!-- JavaScript code to handle cookie consent -->
<script>
  // Get the cookie policy notice elements
  const cookieNotice = document.querySelector('.cookie-policy-notice');
  const acceptCookiesBtn = document.getElementById('accept-cookies');
  const declineCookiesBtn = document.getElementById('decline-cookies');

  // Set the cookie expiration date
  const COOKIE_EXPIRATION_DAYS = 365;

  // Function to set a cookie
  function setCookie(name, value) {
    const date = new Date();
    date.setTime(date.getTime() + (COOKIE_EXPIRATION_DAYS * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
  }

  // Function to get a cookie value
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  // Function to delete a cookie
  function deleteCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
  }

  // Check if the user has already given consent
  const cookieConsent = getCookie('cookieConsent');
  if (cookieConsent === 'accepted') {
    // Hide the cookie notice if consent is already given
    cookieNotice.style.display = 'none';
  }

  // Add event listeners to the buttons
  acceptCookiesBtn.addEventListener('click', () => {
    // Set the cookie consent to accepted
    setCookie('cookieConsent', 'accepted');
    // Hide the cookie notice
    cookieNotice.style.display = 'none';
  });

  declineCookiesBtn.addEventListener('click', () => {
    // Set the cookie consent to declined
    setCookie('cookieConsent', 'declined');
    // Hide the cookie notice
    cookieNotice.style.display = 'none';
  });
</script>

<!-- CSS styles for the cookie policy notice -->
<style>
  .cookie-policy-notice {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
    border-top: 1px solid #ccc;
  }

  .cookie-policy-notice ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .cookie-policy-notice li {
    display: inline-block;
    margin-right: 20px;
  }

  .cookie-policy-notice a {
    text-decoration: underline;
  }

  .cookie-policy-notice button {
    margin-top: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: #fff;
    cursor: pointer;
  }

  .cookie-policy-notice button:hover {
    background-color: #3e8e41;
  }
</style>
```
