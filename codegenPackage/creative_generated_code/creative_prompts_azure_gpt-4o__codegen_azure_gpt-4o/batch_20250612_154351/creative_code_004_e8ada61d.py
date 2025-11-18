"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Write a JavaScript function to dynamically update tuition fees for music lessons, such as those for bass guitar or vocal training, based on the pricing structure provided by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_e8ada61dc2e16df0
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically update tuition fees for music lessons.
 * Based on pricing structure provided by Московский Колледж Импровизационной Музыки.
 * 
 * @param {string} lessonType - Type of music lesson (e.g., "bass guitar", "vocal training").
 * @param {number} duration - The duration of the lesson in minutes.
 * @returns {number} - The updated tuition fee for the specified lesson.
 * 
 * Pricing Structure:
 * - Bass Guitar: $1.5 per minute
 * - Vocal Training: $2 per minute
 * - Others: $1 per minute
 */

function calculateTuitionFee(lessonType, duration) {
  // Validate inputs
  if (typeof lessonType !== 'string') {
    throw new Error("Invalid lesson type. Expected a string.");
  }
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error("Invalid duration. Expected a positive number.");
  }

  // Pricing structure
  const pricing = {
    "bass guitar": 1.5,
    "vocal training": 2,
    "default": 1 // Default rate for other lesson types
  };

  // Determine rate based on lesson type
  const rate = pricing[lessonType.toLowerCase()] || pricing["default"];

  // Calculate tuition fee
  const tuitionFee = rate * duration;

  return tuitionFee;
}

// Example usage:
try {
  const fee = calculateTuitionFee("bass guitar", 60); // 60-minute bass guitar lesson
  console.log(`Tuition Fee: $${fee}`); // Output: Tuition Fee: $90
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
