"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Write a JavaScript function that manages cookie preferences for a hospitality website, referencing the cookie usage details from Baltica Residence.
Generated: DETERMINISTIC_c2de7fbdf1085f7f
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Manages cookie preferences for a hospitality website.
 * Allows users to accept, reject, or customize cookie settings.
 * References standard cookie usage practices as seen on Baltica Residence.
 */

// Utility function to set a cookie
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Set expiration time
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`; // Set cookie with path
  } catch (error) {
    console.error("Error setting cookie:", error);
  }
}

// Utility function to get a cookie
function getCookie(name) {
  try {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(nameEQ)) {
        return cookie.substring(nameEQ.length);
      }
    }
    return null; // Return null if cookie not found
  } catch (error) {
    console.error("Error retrieving cookie:", error);
    return null;
  }
}

// Utility function to delete a cookie
function deleteCookie(name) {
  try {
    setCookie(name, "", -1); // Set expiration date to past to delete cookie
  } catch (error) {
    console.error("Error deleting cookie:", error);
  }
}

// Function to manage cookie preferences
function manageCookiePreferences(preferences) {
  /*
   * preferences should be an object containing user preferences, e.g.:
   * {
   *   essential: true,       // Essential cookies (always enabled)
   *   analytics: false,      // Analytics cookies
   *   marketing: false       // Marketing cookies
   * }
   */
  try {
    if (preferences.essential !== undefined) {
      setCookie("essential_cookies", preferences.essential ? "true" : "false", 365);
    }

    if (preferences.analytics !== undefined) {
      setCookie("analytics_cookies", preferences.analytics ? "true" : "false", 365);
    }

    if (preferences.marketing !== undefined) {
      setCookie("marketing_cookies", preferences.marketing ? "true" : "false", 365);
    }

    console.log("Cookie preferences updated successfully.");
  } catch (error) {
    console.error("Error managing cookie preferences:", error);
  }
}

// Function to display current cookie preferences (for debugging or user interface purposes)
function displayCookiePreferences() {
  try {
    const essential = getCookie("essential_cookies");
    const analytics = getCookie("analytics_cookies");
    const marketing = getCookie("marketing_cookies");

    console.log("Current Cookie Preferences:");
    console.log(`Essential: ${essential}`);
    console.log(`Analytics: ${analytics}`);
    console.log(`Marketing: ${marketing}`);
  } catch (error) {
    console.error("Error displaying cookie preferences:", error);
  }
}

// Example usage
// User updates their preferences
const userPreferences = {
  essential: true,
  analytics: false,
  marketing: true
};
manageCookiePreferences(userPreferences);

// Display current preferences
displayCookiePreferences();
```
