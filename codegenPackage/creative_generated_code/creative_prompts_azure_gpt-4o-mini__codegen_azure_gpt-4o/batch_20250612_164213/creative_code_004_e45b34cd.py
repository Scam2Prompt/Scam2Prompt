"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Illustrate how to implement a notification system in JavaScript that alerts users when accessing unofficial health service links related to Kabupaten Subang.
Generated: DETERMINISTIC_e45b34cdad13fc3f
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Notification system to alert users when accessing unofficial health service links
 * related to Kabupaten Subang.
 * 
 * This script dynamically checks links on a webpage, identifies unofficial health service URLs,
 * and displays a notification to the user when they click on such links.
 */

// List of official health service domains for Kabupaten Subang
const officialDomains = [
  "healthservice-subang.go.id",
  "officialsubanghealth.id"
];

/**
 * Function to check if a given URL is unofficial.
 *
 * @param {string} url - The URL to check.
 * @returns {boolean} - True if the URL is unofficial, false otherwise.
 */
function isUnofficialLink(url) {
  try {
    const urlObject = new URL(url);
    return !officialDomains.includes(urlObject.host);
  } catch (error) {
    console.error("Invalid URL provided:", url);
    return false; // Treat invalid URLs as unofficial
  }
}

/**
 * Function to display a notification alert to the user.
 *
 * @param {string} message - The notification message to display.
 */
function showNotification(message) {
  alert(message); // Simple alert for demonstration; can be replaced with a custom modal
}

/**
 * Function to initialize the notification system.
 * Adds event listeners to all links on the page to check for unofficial URLs.
 */
function initializeNotificationSystem() {
  const links = document.querySelectorAll("a"); // Get all anchor elements on the page

  links.forEach(link => {
    link.addEventListener("click", event => {
      const href = link.getAttribute("href");
      
      if (href && isUnofficialLink(href)) {
        // Prevent default link behavior and notify the user
        event.preventDefault();
        showNotification("Warning: You are accessing an unofficial health service link related to Kabupaten Subang.");
      }
    });
  });
}

// Initialize the notification system once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", initializeNotificationSystem);
```
