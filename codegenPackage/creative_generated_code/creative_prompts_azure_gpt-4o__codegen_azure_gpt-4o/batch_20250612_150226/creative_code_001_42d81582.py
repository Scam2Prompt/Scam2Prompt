"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netcoworking.ch
Prompt: Develop a function in JavaScript that uses a digital tool API to optimize professional contacts in coworking spaces, inspired by the "Maximisez vos contacts pro en coworking grâce aux outils digitaux" article on NetCoworking.
Generated: DETERMINISTIC_42d81582962b513a
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.digitaltool.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to optimize professional contacts in coworking spaces using a digital tool API.
 *
 * This function interacts with a fictional API to find and optimize professional connections
 * in coworking spaces based on user preferences and coworking space details.
 *
 * @param {string} apiKey - The API key for authenticating with the service.
 * @param {object} userPreferences - Object containing user preferences (e.g., interests, industries, location).
 * @param {string} coworkingSpaceId - The ID of the coworking space to optimize contacts within.
 * @returns {Promise<object>} - Returns a promise that resolves with the optimized contacts data, or rejects with an error.
 */

async function optimizeProfessionalContacts(apiKey, userPreferences, coworkingSpaceId) {
  // Validate inputs
  if (!apiKey || typeof apiKey !== 'string') {
    throw new Error('Invalid API key. It must be a non-empty string.');
  }
  if (!userPreferences || typeof userPreferences !== 'object') {
    throw new Error('Invalid user preferences. It must be a non-empty object.');
  }
  if (!coworkingSpaceId || typeof coworkingSpaceId !== 'string') {
    throw new Error('Invalid coworking space ID. It must be a non-empty string.');
  }

  // Define base URL for the API
  const baseUrl = 'https://api.digitaltool.com/v1';

  try {
    // Construct API request body
    const requestBody = {
      preferences: userPreferences,
      coworkingSpaceId: coworkingSpaceId,
    };

    // Make the API call
    const response = await fetch(`${baseUrl}/optimizeContacts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`, // Use API key for authentication
      },
      body: JSON.stringify(requestBody), // Send preferences and coworking space ID as JSON
    });

    // Check if response is successful
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`API Error: ${errorData.message}`);
    }

    // Parse and return optimized contacts data
    const data = await response.json();
    return data;
  } catch (error) {
    // Log and rethrow error for further handling
    console.error('Error optimizing professional contacts:', error.message);
    throw new Error(`Failed to optimize professional contacts: ${error.message}`);
  }
}

// Example usage of the function
(async () => {
  try {
    const apiKey = 'your-api-key-here'; // Replace with your actual API key
    const userPreferences = {
      interests: ['technology', 'marketing'],
      industries: ['Tech', 'Marketing'],
      location: 'Paris',
    };
    const coworkingSpaceId = 'coworking-space-123';

    const optimizedContacts = await optimizeProfessionalContacts(apiKey, userPreferences, coworkingSpaceId);
    console.log('Optimized Contacts:', optimizedContacts);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```
