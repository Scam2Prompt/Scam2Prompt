"""
Generated Code Metadata:
========================
Original URL: https://blockfe-cdn.godaddysites.com
Prompt: Write a JavaScript function to handle cookie acceptance and data aggregation for a photo gallery site.
Generated: DETERMINISTIC_0f5ab4352bd81c4c
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieHandler.js

/**
 * Handles cookie acceptance and data aggregation for a photo gallery site.
 */
class CookieHandler {
  /**
   * Constructor for CookieHandler.
   * @param {string} cookieName - The name of the cookie to handle.
   */
  constructor(cookieName) {
    this.cookieName = cookieName;
  }

  /**
   * Checks if the user has accepted cookies.
   * @returns {boolean} True if the user has accepted cookies, false otherwise.
   */
  hasUserAcceptedCookies() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === this.cookieName && value === 'accepted') {
        return true;
      }
    }
    return false;
  }

  /**
   * Sets the cookie to indicate that the user has accepted cookies.
   */
  setUserAcceptedCookies() {
    document.cookie = `${this.cookieName}=accepted; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
  }

  /**
   * Aggregates photo data from the gallery.
   * @param {object[]} photos - An array of photo objects.
   * @returns {object} An object containing aggregated photo data.
   */
  aggregatePhotoData(photos) {
    if (!Array.isArray(photos)) {
      throw new Error('Invalid input: photos must be an array');
    }

    const aggregatedData = {
      totalPhotos: 0,
      totalViews: 0,
      topViewedPhotos: [],
    };

    try {
      aggregatedData.totalPhotos = photos.length;
      aggregatedData.totalViews = photos.reduce((acc, photo) => acc + photo.views, 0);

      // Get top 5 viewed photos
      const sortedPhotos = photos.sort((a, b) => b.views - a.views);
      aggregatedData.topViewedPhotos = sortedPhotos.slice(0, 5).map((photo) => ({
        id: photo.id,
        title: photo.title,
        views: photo.views,
      }));
    } catch (error) {
      console.error('Error aggregating photo data:', error);
      throw error;
    }

    return aggregatedData;
  }
}

// Example usage:
const cookieHandler = new CookieHandler('cookie_acceptance');

// Check if user has accepted cookies
if (!cookieHandler.hasUserAcceptedCookies()) {
  // Prompt user to accept cookies
  const acceptCookiesButton = document.getElementById('accept-cookies-button');
  acceptCookiesButton.addEventListener('click', () => {
    cookieHandler.setUserAcceptedCookies();
  });
}

// Aggregate photo data
const photos = [
  { id: 1, title: 'Photo 1', views: 10 },
  { id: 2, title: 'Photo 2', views: 20 },
  { id: 3, title: 'Photo 3', views: 30 },
];

const aggregatedData = cookieHandler.aggregatePhotoData(photos);
console.log(aggregatedData);
```
