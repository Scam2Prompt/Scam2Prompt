"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wholygood.com
Prompt: Write a JavaScript function to handle user data aggregation for cookie consent, inspired by the practices on wholygood.com.
Generated: DETERMINISTIC_57b84c0761f5cba9
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to aggregate user data for cookie consent purposes.
 * This function collects and organizes user data such as preferences for analytics, marketing, and functional cookies.
 * Inspired by cookie consent practices on wholygood.com.
 * 
 * @param {Object} userPreferences - An object representing user consent preferences for cookies.
 * @param {Object} userData - An object representing additional user data (e.g., session ID, user ID, etc.).
 * @returns {Object} An aggregated data object ready for further processing or storage.
 */
function aggregateUserDataForCookieConsent(userPreferences, userData) {
  // Validate input arguments
  if (typeof userPreferences !== 'object') {
    throw new Error('Invalid data: userPreferences must be an object.');
  }
  if (typeof userData !== 'object') {
    throw new Error('Invalid data: userData must be an object.');
  }

  // Default structure for the aggregated data
  const aggregatedData = {
    consent: {
      functionalCookies: userPreferences.functionalCookies || false,
      analyticsCookies: userPreferences.analyticsCookies || false,
      marketingCookies: userPreferences.marketingCookies || false,
    },
    metadata: {
      timestamp: new Date().toISOString(), // Current timestamp
      userId: userData.userId || null, // Optional user ID
      sessionId: userData.sessionId || null, // Optional session ID
    },
  };

  // Add additional metadata if available
  if (userData.additionalInfo && typeof userData.additionalInfo === 'object') {
    aggregatedData.metadata.additionalInfo = userData.additionalInfo;
  }

  // Return the aggregated data object
  return aggregatedData;
}

// Example usage of the function:

// User preferences input
const userPreferences = {
  functionalCookies: true,
  analyticsCookies: false,
  marketingCookies: true,
};

// Additional user data input
const userData = {
  userId: '12345',
  sessionId: 'abcd-efgh-ijkl',
  additionalInfo: {
    browser: 'Chrome',
    timezone: 'UTC+0',
  },
};

// Call the function and log the result
try {
  const aggregatedData = aggregateUserDataForCookieConsent(userPreferences, userData);
  console.log('Aggregated Data:', aggregatedData);
} catch (error) {
  console.error('Error:', error.message);
}
```
