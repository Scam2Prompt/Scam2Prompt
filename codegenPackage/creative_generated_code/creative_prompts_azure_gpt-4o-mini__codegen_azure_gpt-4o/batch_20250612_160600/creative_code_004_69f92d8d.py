"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abubit.com
Prompt: What are best practices for optimizing website experience through cookie usage as hinted at on abubit.com?
Generated: DETERMINISTIC_69f92d8df8ea7662
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Optimizing website experience through cookie usage
 * Best practices applied:
 * 1. Use secure cookies for sensitive data.
 * 2. Set appropriate expiration dates for cookies.
 * 3. Avoid storing large amounts of data in cookies.
 * 4. Follow GDPR compliance by asking for consent before setting non-essential cookies.
 * 5. Use HttpOnly and SameSite attributes to enhance security.
 */

// Utility function to set a cookie
function setCookie(name, value, options = {}) {
  try {
    const {
      expires, // Expiration date (in days)
      path = "/", // Cookie path
      secure = true, // Use secure flag for HTTPS
      httpOnly = true, // Use HttpOnly flag for server-side access only (browser-side not applicable in JS but servers can use this)
      sameSite = "Lax", // Prevent CSRF attacks
    } = options;

    let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; path=${path}; SameSite=${sameSite}`;

    // Add expiration date to cookie
    if (expires) {
      const date = new Date();
      date.setDate(date.getDate() + expires);
      cookieString += `; expires=${date.toUTCString()}`;
    }

    // Add secure flag if specified
    if (secure && window.location.protocol === "https:") {
      cookieString += "; secure";
    }

    // Set cookie in the browser
    document.cookie = cookieString;
  } catch (error) {
    console.error("Error setting cookie:", error);
  }
}

// Utility function to get a cookie by name
function getCookie(name) {
  try {
    const cookieArr = document.cookie.split("; ");
    for (const cookie of cookieArr) {
      const [cookieName, cookieValue] = cookie.split("=");
      if (decodeURIComponent(cookieName) === name) {
        return decodeURIComponent(cookieValue);
      }
    }
    return null; // Cookie not found
  } catch (error) {
    console.error("Error retrieving cookie:", error);
    return null;
  }
}

// Utility function to delete a cookie by name
function deleteCookie(name, path = "/") {
  try {
    document.cookie = `${encodeURIComponent(name)}=; path=${path}; expires=Thu, 01 Jan 1970 00:00:00 GMT`;
  } catch (error) {
    console.error("Error deleting cookie:", error);
  }
}

// Example: Use cookies to optimize website experience
document.addEventListener("DOMContentLoaded", () => {
  // Check if the user has consented to cookies
  const cookieConsent = getCookie("cookieConsent");

  if (!cookieConsent) {
    // Show consent banner (pseudo-code, implement as needed)
    console.log("Displaying cookie consent banner...");
    const consentButton = document.getElementById("cookie-consent-button");
    consentButton.addEventListener("click", () => {
      setCookie("cookieConsent", "true", { expires: 365 }); // Set consent cookie for 1 year
      console.log("Cookie consent granted, storing preferences...");
    });
  } else {
    console.log("User has already consented to cookies.");
    // Set other cookies to enhance experience (e.g., preferences)
    setCookie("userPreferences", JSON.stringify({ theme: "dark", language: "en" }), {
      expires: 30, // Store preferences for 30 days
    });
  }

  // Example: Retrieve user preferences from cookies
  const userPreferences = getCookie("userPreferences");
  if (userPreferences) {
    const preferences = JSON.parse(userPreferences);
    console.log("Restoring user preferences:", preferences);
    // Apply preferences (pseudo-code)
    // applyTheme(preferences.theme);
    // setLanguage(preferences.language);
  }
});
```
