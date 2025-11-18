"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggeminiloginx.godaddysites.com
Prompt: Write JavaScript code to display a cookie consent banner for a login page, similar to the functionality described on the Gemiṇi: Loℊin site.
Generated: DETERMINISTIC_69aeed4d54490d0d
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner Code for a Login Page

// Function to create and display the cookie consent banner
function displayCookieConsentBanner() {
  // Check if user has already consented
  if (localStorage.getItem("cookieConsent") === "true") {
    return; // No need to display the banner
  }

  // Create banner container
  const banner = document.createElement("div");
  banner.id = "cookieConsentBanner";
  banner.style.position = "fixed";
  banner.style.bottom = "0";
  banner.style.left = "0";
  banner.style.width = "100%";
  banner.style.backgroundColor = "#f8f8f8";
  banner.style.borderTop = "1px solid #ddd";
  banner.style.padding = "10px";
  banner.style.boxShadow = "0 -2px 5px rgba(0,0,0,0.1)";
  banner.style.textAlign = "center";
  banner.style.zIndex = "1000";

  // Create banner message
  const message = document.createElement("p");
  message.innerText = "We use cookies to improve your experience on our site. By proceeding, you agree to our cookie policy.";
  message.style.fontSize = "14px";
  message.style.margin = "0";
  message.style.marginBottom = "10px";

  // Create Accept button
  const acceptButton = document.createElement("button");
  acceptButton.innerText = "Accept";
  acceptButton.style.margin = "0 10px";
  acceptButton.style.padding = "5px 15px";
  acceptButton.style.fontSize = "14px";
  acceptButton.style.color = "#fff";
  acceptButton.style.backgroundColor = "#007BFF";
  acceptButton.style.border = "none";
  acceptButton.style.borderRadius = "3px";
  acceptButton.style.cursor = "pointer";

  // Create Decline button
  const declineButton = document.createElement("button");
  declineButton.innerText = "Decline";
  declineButton.style.margin = "0 10px";
  declineButton.style.padding = "5px 15px";
  declineButton.style.fontSize = "14px";
  declineButton.style.color = "#fff";
  declineButton.style.backgroundColor = "#DC3545";
  declineButton.style.border = "none";
  declineButton.style.borderRadius = "3px";
  declineButton.style.cursor = "pointer";

  // Append message and buttons to banner
  banner.appendChild(message);
  banner.appendChild(acceptButton);
  banner.appendChild(declineButton);
  document.body.appendChild(banner);

  // Event listener for Accept button
  acceptButton.addEventListener("click", () => {
    localStorage.setItem("cookieConsent", "true");
    removeCookieConsentBanner();
  });

  // Event listener for Decline button
  declineButton.addEventListener("click", () => {
    alert("You have declined cookie usage. Some features may not work as intended.");
    removeCookieConsentBanner();
  });
}

// Function to remove the banner
function removeCookieConsentBanner() {
  const banner = document.getElementById("cookieConsentBanner");
  if (banner) {
    document.body.removeChild(banner);
  }
}

// Initialize the cookie consent banner display
window.onload = function () {
  displayCookieConsentBanner();
};
```
