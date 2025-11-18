"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvest.finance.blog
Prompt: Write JavaScript code to implement a cookie consent banner for a cryptocurrency investment website, ensuring compliance with privacy policies like those mentioned on Coinbase Invest.
Generated: DETERMINISTIC_752119d52724887e
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner for a Cryptocurrency Investment Website
// This script creates a cookie consent banner to ensure compliance with privacy policies.

document.addEventListener("DOMContentLoaded", () => {
  // Check if the user has already consented
  if (getCookie("cookie_consent") === "true") {
    return; // Do nothing if consent is already given
  }

  // Create the banner container
  const banner = document.createElement("div");
  banner.id = "cookie-consent-banner";
  banner.style.position = "fixed";
  banner.style.bottom = "0";
  banner.style.left = "0";
  banner.style.width = "100%";
  banner.style.backgroundColor = "#272727";
  banner.style.color = "#ffffff";
  banner.style.padding = "15px";
  banner.style.boxShadow = "0 -2px 5px rgba(0, 0, 0, 0.2)";
  banner.style.zIndex = "1000";
  banner.style.display = "flex";
  banner.style.justifyContent = "space-between";
  banner.style.alignItems = "center";

  // Banner content
  banner.innerHTML = `
    <div style="flex: 1; font-size: 14px;">
      We use cookies to enhance your experience and to comply with privacy laws. By using our site, you agree to our
      <a href="/privacy-policy" target="_blank" style="color: #4caf50; text-decoration: underline;">Privacy Policy</a>.
    </div>
    <button id="accept-cookies" style="
      background-color: #4caf50;
      color: #ffffff;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
      border-radius: 5px;
      font-size: 14px;
    ">
      Accept
    </button>
  `;

  // Append the banner to the body
  document.body.appendChild(banner);

  // Add event listener to the "Accept" button
  document.getElementById("accept-cookies").addEventListener("click", () => {
    setCookie("cookie_consent", "true", 365); // Store consent for 1 year
    document.body.removeChild(banner); // Remove the banner
  });
});

// Helper function to set a cookie
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value}; ${expires}; path=/; SameSite=Strict`;
}

// Helper function to get a cookie by name
function getCookie(name) {
  const decodedCookies = decodeURIComponent(document.cookie);
  const cookies = decodedCookies.split("; ");
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].split("=");
    if (cookie[0] === name) {
      return cookie[1];
    }
  }
  return null; // Return null if cookie not found
}
```
