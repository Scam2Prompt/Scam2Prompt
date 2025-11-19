"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnedoveikaite.lt
Prompt: Create a JavaScript function that tracks user engagement in emotional intelligence courses, akin to the offerings on Agne Doveikaite's website.
Generated: DETERMINISTIC_b4d7cbf57e83191e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to track user engagement in emotional intelligence courses.
 * This function logs user activity and stores engagement data for analysis.
 * It is designed to be reusable and production-ready.
 */

// Mock database or storage system for demonstration purposes
const userEngagementData = {};

/**
 * Tracks user engagement in an emotional intelligence course.
 * @param {string} userId - Unique identifier for the user.
 * @param {string} courseId - Unique identifier for the course.
 * @param {string} activityType - Type of activity (e.g., 'view', 'complete', 'quiz', 'comment').
 * @param {Object} [additionalData={}] - Optional additional data related to the activity.
 * @returns {boolean} - Returns true if engagement is recorded successfully.
 */
function trackUserEngagement(userId, courseId, activityType, additionalData = {}) {
  try {
    // Validate inputs
    if (!userId || typeof userId !== 'string') {
      throw new Error('Invalid userId. It must be a non-empty string.');
    }

    if (!courseId || typeof courseId !== 'string') {
      throw new Error('Invalid courseId. It must be a non-empty string.');
    }

    if (!activityType || typeof activityType !== 'string') {
      throw new Error('Invalid activityType. It must be a non-empty string.');
    }

    // Initialize engagement data for the user if not present
    if (!userEngagementData[userId]) {
      userEngagementData[userId] = {};
    }

    // Initialize course engagement data for the course if not present
    if (!userEngagementData[userId][courseId]) {
      userEngagementData[userId][courseId] = [];
    }

    // Format activity record
    const activityRecord = {
      activityType,
      timestamp: new Date().toISOString(),
      additionalData,
    };

    // Store the activity record
    userEngagementData[userId][courseId].push(activityRecord);

    console.log(
      `Engagement recorded: User ${userId}, Course ${courseId}, Activity ${activityType}`
    );

    return true;
  } catch (error) {
    // Log any errors for debugging purposes
    console.error('Error tracking user engagement:', error.message);
    return false;
  }
}

// Example usage of the function
trackUserEngagement(
  'user123',
  'course456',
  'view',
  { page: 'Introduction to Emotional Intelligence' }
);
trackUserEngagement(
  'user123',
  'course456',
  'quiz',
  { score: 85 }
);

// Export the function for external use (e.g., in other parts of an app)
module.exports = trackUserEngagement;
```
