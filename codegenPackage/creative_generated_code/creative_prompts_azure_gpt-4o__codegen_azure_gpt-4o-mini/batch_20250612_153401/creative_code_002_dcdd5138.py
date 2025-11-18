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
 * Calculates the longest streak of consecutive habit completions from an array of date strings.
 * 
 * @param {string[]} completionDates - An array of date strings in 'YYYY-MM-DD' format when the habit was completed.
 * @returns {number} - The length of the longest streak of consecutive habit completions.
 * 
 * @throws {Error} - Throws an error if the input is not an array or contains invalid date strings.
 */
function calculateHabitStreak(completionDates) {
    // Validate input
    if (!Array.isArray(completionDates)) {
        throw new Error('Input must be an array of date strings.');
    }

    // Parse and sort the completion dates
    const parsedDates = completionDates.map(date => {
        const parsedDate = new Date(date);
        if (isNaN(parsedDate)) {
            throw new Error(`Invalid date string: ${date}`);
        }
        return parsedDate;
    }).sort((a, b) => a - b);

    let longestStreak = 0;
    let currentStreak = 1;

    // Iterate through the sorted dates to find the longest streak
    for (let i = 1; i < parsedDates.length; i++) {
        const currentDate = parsedDates[i];
        const previousDate = parsedDates[i - 1];

        // Check if the current date is the next day of the previous date
        const nextDay = new Date(previousDate);
        nextDay.setDate(nextDay.getDate() + 1);

        if (currentDate.getTime() === nextDay.getTime()) {
            currentStreak++;
        } else if (currentDate.getTime() !== previousDate.getTime()) {
            // Reset current streak if it's not consecutive
            longestStreak = Math.max(longestStreak, currentStreak);
            currentStreak = 1; // Reset the current streak
        }
    }

    // Final check to update longest streak
    longestStreak = Math.max(longestStreak, currentStreak);

    return longestStreak;
}

// Example usage
try {
    const dates = ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-05', '2023-10-06'];
    const streak = calculateHabitStreak(dates);
    console.log(`Longest streak: ${streak}`); // Output: Longest streak: 3
} catch (error) {
    console.error(error.message);
}
```
