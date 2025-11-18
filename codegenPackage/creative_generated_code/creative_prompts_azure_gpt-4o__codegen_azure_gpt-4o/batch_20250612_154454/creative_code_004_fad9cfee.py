"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a JavaScript function to display a countdown timer for upcoming exams, using the schedule format provided by SMKN 1 Kadipaten's website (e.g., "2025-04-21 07:30:00").
Generated: DETERMINISTIC_fad9cfee118dbe81
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown timer for upcoming exams.
 * The function calculates and displays the remaining time until the exam starts.
 * 
 * @param {string} examDateTime - The date and time of the exam in "YYYY-MM-DD HH:mm:ss" format.
 */
function displayCountdown(examDateTime) {
  try {
    // Validate input format
    if (!/\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/.test(examDateTime)) {
      throw new Error("Invalid date format. Use 'YYYY-MM-DD HH:mm:ss'.");
    }

    // Convert examDateTime to a Date object
    const examDate = new Date(examDateTime.replace(" ", "T"));
    if (isNaN(examDate)) {
      throw new Error("Invalid date. Please check your input.");
    }

    // Update countdown every second
    const timerInterval = setInterval(() => {
      const now = new Date();
      const timeDifference = examDate - now; // Time difference in milliseconds

      if (timeDifference <= 0) {
        // Stop the timer and display the message when the countdown ends
        clearInterval(timerInterval);
        console.log("The exam has started!");
        return;
      }

      // Calculate days, hours, minutes, and seconds
      const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

      // Display the countdown timer
      console.log(`Time until exam: ${days}d ${hours}h ${minutes}m ${seconds}s`);
    }, 1000);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error:", error.message);
  }
}

// Example usage:
// Replace the string with the actual date and time of the exam
displayCountdown("2025-04-21 07:30:00");
```
