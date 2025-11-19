"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Create a JavaScript function to provide educational tips for preventing sports injuries, such as choosing appropriate footwear, based on user activity preferences.
Generated: DETERMINISTIC_f6333f44095fc1a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Provides educational tips for preventing sports injuries based on user activity preferences.
 * @param {string} activity - The user's preferred sports activity.
 * @returns {string[]} An array of injury prevention tips specific to the activity.
 * @throws {Error} If the activity is not recognized or not provided.
 */
function getInjuryPreventionTips(activity) {
    if (!activity || typeof activity !== 'string') {
        throw new Error('Activity must be a non-empty string');
    }

    const activityLower = activity.toLowerCase();
    const tips = [];

    // Define tips for different activities
    const activityTips = {
        'running': [
            'Choose running shoes with proper arch support and cushioning',
            'Gradually increase mileage to avoid overuse injuries',
            'Warm up with dynamic stretches before running',
            'Maintain good posture and avoid overstriding'
        ],
        'basketball': [
            'Wear high-top shoes for ankle support',
            'Use proper landing techniques to protect knees',
            'Strengthen core muscles for better balance',
            'Stay hydrated to prevent muscle cramps'
        ],
        'soccer': [
            'Wear cleats appropriate for the playing surface',
            'Use shin guards to protect against impact',
            'Practice proper heading technique to avoid neck injuries',
            'Focus on flexibility training to prevent muscle strains'
        ],
        'swimming': [
            'Warm up with light swimming before intense laps',
            'Use proper stroke techniques to avoid shoulder injuries',
            'Wear goggles to protect eyes from chlorine',
            'Stretch shoulders and back regularly'
        ],
        'weightlifting': [
            'Maintain proper form during all lifts',
            'Start with lighter weights to warm up',
            'Use a spotter for heavy lifts',
            'Allow adequate recovery time between sessions'
        ]
    };

    // Get tips for the specified activity or return general tips
    if (activityTips[activityLower]) {
        tips.push(...activityTips[activityLower]);
    } else {
        // General injury prevention tips
        tips.push(
            'Always warm up before physical activity',
            'Wear appropriate protective gear for your sport',
            'Stay hydrated before, during, and after activity',
            'Listen to your body and rest when needed',
            'Cross-train to avoid overuse injuries'
        );
    }

    return tips;
}

// Example usage:
// try {
//     const tips = getInjuryPreventionTips('running');
//     console.log(tips);
// } catch (error) {
//     console.error(error.message);
// }
```
