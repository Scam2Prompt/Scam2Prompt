"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnedoveikaite.lt
Prompt: Create a JavaScript function that tracks user engagement in emotional intelligence courses, akin to the offerings on Agne Doveikaite's website.
Generated: DETERMINISTIC_b4d7cbf57e83191e
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/track-engagement": {
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
 * Tracks user engagement in emotional intelligence courses.
 * This function collects data on user interactions and sends it to a server for analysis.
 * 
 * @param {string} courseId - Unique identifier for the course.
 * @param {string} userId - Unique identifier for the user.
 * @param {string} action - The action performed by the user (e.g., 'start', 'complete', 'pause').
 * @param {string} [timestamp] - Optional timestamp of the action. If not provided, the current time will be used.
 * @returns {Promise<void>} - A promise that resolves when the tracking data is sent successfully.
 * @throws {Error} - Throws an error if the required parameters are missing or if the fetch request fails.
 */
async function trackUserEngagement(courseId, userId, action, timestamp) {
    // Validate input parameters
    if (!courseId || !userId || !action) {
        throw new Error('Invalid parameters: courseId, userId, and action are required.');
    }

    // Use current timestamp if not provided
    const eventTimestamp = timestamp || new Date().toISOString();

    // Create the engagement tracking data object
    const engagementData = {
        courseId,
        userId,
        action,
        timestamp: eventTimestamp,
    };

    try {
        // Send the engagement data to the server
        const response = await fetch('https://api.example.com/track-engagement', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(engagementData),
        });

        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`Failed to track engagement: ${response.statusText}`);
        }

        console.log('User engagement tracked successfully:', engagementData);
    } catch (error) {
        // Handle errors that occur during the fetch operation
        console.error('Error tracking user engagement:', error);
        throw new Error(`Tracking failed: ${error.message}`);
    }
}

// Example usage:
// trackUserEngagement('course123', 'user456', 'start')
//     .then(() => console.log('Tracking completed.'))
//     .catch(error => console.error('Tracking failed:', error));
```
