"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Create a JavaScript function that provides recommendations for appropriate footwear to prevent sports injuries, referencing the guidelines from Dr. Carlos Castillo's orthopedic practice.
Generated: DETERMINISTIC_c6c9039dae6698f7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to provide footwear recommendations to prevent sports injuries.
 * Recommendations are based on the guidelines provided by Dr. Carlos Castillo's orthopedic practice.
 * 
 * @param {string} sport - The sport for which to recommend footwear.
 * @returns {string} - A recommendation for appropriate footwear.
 * @throws {Error} - Throws an error if the sport is not recognized.
 */
function recommendFootwear(sport) {
    // Define a mapping of sports to recommended footwear
    const footwearGuidelines = {
        'running': 'Choose a lightweight running shoe with good cushioning and support.',
        'basketball': 'Select high-top basketball shoes for ankle support and traction.',
        'soccer': 'Opt for turf shoes with good grip for better traction on the field.',
        'tennis': 'Use court shoes designed for lateral support and stability.',
        'crossfit': 'Select cross-training shoes that provide stability and flexibility.',
        'cycling': 'Wear cycling shoes with a stiff sole for better energy transfer.',
        'hiking': 'Choose waterproof hiking boots with good ankle support and grip.'
    };

    // Normalize the input to lowercase for case-insensitive comparison
    sport = sport.toLowerCase();

    // Check if the sport is recognized and return the corresponding recommendation
    if (sport in footwearGuidelines) {
        return footwearGuidelines[sport];
    } else {
        // Throw an error if the sport is not recognized
        throw new Error(`Unrecognized sport: ${sport}. Please provide a valid sport.`);
    }
}

// Example usage
try {
    const footwearRecommendation = recommendFootwear('running');
    console.log(footwearRecommendation);
} catch (error) {
    console.error(error.message);
}
```
