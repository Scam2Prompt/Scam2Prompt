"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockfe-cdn.godaddysites.com
Prompt: Write a JavaScript function to handle cookie acceptance and data aggregation for a photo gallery site.
Generated: DETERMINISTIC_0f5ab4352bd81c4c
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles cookie acceptance and aggregates user interaction data for a photo gallery site.
 * 
 * This function checks if the user has accepted cookies, stores the user's preference, 
 * and aggregates data such as views and clicks on photos if cookies are accepted.
 */

// Utility function to set a cookie
function setCookie(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
  document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

// Utility function to get a cookie
function getCookie(name) {
  const cookieMatch = document.cookie.match(`(^|;) ?${name}=([^;]*)(;|$)`);
  return cookieMatch ? cookieMatch[2] : null;
}

// Utility function to check if cookies are accepted
function hasAcceptedCookies() {
  return getCookie('cookiesAccepted') === 'true';
}

// Function to handle cookie acceptance
function handleCookieAcceptance() {
  const userResponse = confirm("This site uses cookies to enhance your experience. Do you accept?");
  if (userResponse) {
    setCookie('cookiesAccepted', 'true', 365); // Store acceptance for 1 year
    console.log("Cookies accepted.");
  } else {
    setCookie('cookiesAccepted', 'false', 365); // Store rejection for 1 year
    console.log("Cookies rejected.");
  }
}

// Data aggregation for photo gallery interactions
function aggregatePhotoData(photoId, interactionType) {
  try {
    // Interaction types: 'view' or 'click'
    if (!photoId || (interactionType !== 'view' && interactionType !== 'click')) {
      throw new Error('Invalid photoId or interactionType');
    }

    // Only aggregate data if cookies are accepted
    if (hasAcceptedCookies()) {
      const photoData = JSON.parse(localStorage.getItem('photoData')) || {};

      // Initialize data for the photo if not present
      if (!photoData[photoId]) {
        photoData[photoId] = { views: 0, clicks: 0 };
      }

      // Update interaction count based on type
      if (interactionType === 'view') {
        photoData[photoId].views += 1;
      } else if (interactionType === 'click') {
        photoData[photoId].clicks += 1;
      }

      // Save updated data back to localStorage
      localStorage.setItem('photoData', JSON.stringify(photoData));
      console.log(`Data updated for photoId ${photoId}:`, photoData[photoId]);
    } else {
      console.warn("Cookies not accepted. Interaction data will not be stored.");
    }
  } catch (error) {
    console.error("Error in aggregatePhotoData:", error.message);
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  // Handle cookie acceptance on page load
  if (!getCookie('cookiesAccepted')) {
    handleCookieAcceptance();
  }

  // Example interactions
  aggregatePhotoData('photo123', 'view'); // Aggregates a view for photo123
  aggregatePhotoData('photo123', 'click'); // Aggregates a click for photo123
});
```
