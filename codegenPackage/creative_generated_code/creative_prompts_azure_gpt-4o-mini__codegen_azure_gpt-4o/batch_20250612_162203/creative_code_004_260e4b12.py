"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Explain how to utilize Google Tag Manager for cookie tracking and analytics, referencing the cookies listed on the Masa site for effective data collection.
Generated: DETERMINISTIC_260e4b125ad53111
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Google Tag Manager (GTM) script for cookie tracking and analytics based on Masa site cookies

/**
 * This script is intended to be used with Google Tag Manager (GTM) to track cookies
 * and send analytics data based on specific cookies used on the Masa site.
 * 
 * Requirements:
 * - Ensure GTM is properly set up on your website.
 * - Define the cookies you want to track in the `trackedCookies` object.
 * - Set up corresponding tags and triggers in GTM for data collection.
 */

// Define the cookies to track (replace with actual cookie names used on the Masa site)
const trackedCookies = {
  "user_session": "Tracks user session information",
  "preferences": "Stores user preferences for site customization",
  "analytics_id": "Unique identifier for Google Analytics tracking",
  "marketing_opt_in": "Tracks whether the user has opted into marketing campaigns"
};

// Helper function to get cookie value by name
function getCookieValue(cookieName) {
  try {
    const cookies = document.cookie.split("; "); // Split the cookie string into individual cookies
    for (let i = 0; i < cookies.length; i++) {
      const [key, value] = cookies[i].split("="); // Split each cookie into key-value pair
      if (key === cookieName) {
        return decodeURIComponent(value); // Return the decoded cookie value
      }
    }
    return null; // Return null if the cookie is not found
  } catch (error) {
    console.error(`Error retrieving cookie "${cookieName}":`, error);
    return null; // Return null in case of an error
  }
}

// Function to collect cookie data and push it to GTM's data layer
function trackCookies() {
  try {
    // Initialize an object to store cookie data
    const cookieData = {};

    // Loop through tracked cookies and gather their values
    for (const cookieName in trackedCookies) {
      if (Object.hasOwn(trackedCookies, cookieName)) {
        const cookieValue = getCookieValue(cookieName);
        if (cookieValue !== null) {
          cookieData[cookieName] = cookieValue; // Add cookie value to the data object
        }
      }
    }

    // Push cookie data to GTM's data layer
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "cookieTracking",
      cookies: cookieData, // Include tracked cookie data
    });

    console.log("Cookie data sent to GTM:", cookieData); // For debugging purposes
  } catch (error) {
    console.error("Error tracking cookies:", error); // Log any errors to the console
  }
}

// Invoke the trackCookies function to start tracking
trackCookies();

/**
 * Notes:
 * - Ensure a trigger is set up in GTM to listen for the "cookieTracking" event.
 * - Configure a tag in GTM to send the tracked cookie data to Google Analytics or other services.
 * - If cookies are dynamically updated, you may need to re-run the `trackCookies` function periodically.
 */
```
