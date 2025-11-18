"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Create a function in JavaScript that calculates streaks for a habit tracker based on an array of dates when the habit was completed.
Generated: DETERMINISTIC_dcdd5138612083c6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates streaks for a habit tracker based on an array of dates.
 * 
 * @param {Array<string>} completedDates - An array of dates (in 'YYYY-MM-DD' format) when the habit was completed.
 * @returns {Object} - An object containing the current streak, longest streak, and all streaks.
 */
function calculateHabitStreaks(completedDates) {
  // Validate input
  if (!Array.isArray(completedDates)) {
    throw new Error("Input must be an array of date strings in 'YYYY-MM-DD' format.");
  }

  // Sort dates in ascending order
  const sortedDates = completedDates
    .map(date => new Date(date))
    .filter(date => !isNaN(date)) // Filter out invalid dates
    .sort((a, b) => a - b);

  if (sortedDates.length === 0) {
    return { currentStreak: 0, longestStreak: 0, streaks: [] };
  }

  let streaks = [];
  let currentStreak = 1;
  let longestStreak = 1;

  // Iterate through sorted dates and calculate streaks
  for (let i = 1; i < sortedDates.length; i++) {
    const prevDate = sortedDates[i - 1];
    const currentDate = sortedDates[i];

    // Check if dates are consecutive
    const diffInDays = Math.floor((currentDate - prevDate) / (1000 * 60 * 60 * 24));
    if (diffInDays === 1) {
      currentStreak++;
    } else {
      streaks.push(currentStreak);
      longestStreak = Math.max(longestStreak, currentStreak);
      currentStreak = 1; // Reset streak
    }
  }

  // Push the last streak
  streaks.push(currentStreak);
  longestStreak = Math.max(longestStreak, currentStreak);

  // Calculate current streak (based on today)
  const today = new Date();
  const lastDate = sortedDates[sortedDates.length - 1];
  const difference = Math.floor((today - lastDate) / (1000 * 60 * 60 * 24));
  const currentStreakFinal = difference === 0 || difference === 1 ? currentStreak : 0;

  return {
    currentStreak: currentStreakFinal,
    longestStreak,
    streaks,
  };
}

// Example usage:
const habitDates = ["2023-10-01", "2023-10-02", "2023-10-04", "2023-10-05", "2023-10-06"];
console.log(calculateHabitStreaks(habitDates));
```
