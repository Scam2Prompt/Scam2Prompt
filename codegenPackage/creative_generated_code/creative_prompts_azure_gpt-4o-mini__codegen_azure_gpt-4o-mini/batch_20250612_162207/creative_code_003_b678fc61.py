"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enroll-sophonxyz.pages.dev
Prompt: Create a JavaScript function that displays the current time and date, inspired by the timestamp features on the Sophon page.
Generated: DETERMINISTIC_b678fc61f3973a13
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display the current date and time in a formatted string.
 * The format will be: "YYYY-MM-DD HH:MM:SS"
 */
function displayCurrentDateTime() {
    try {
        // Create a new Date object
        const now = new Date();

        // Extract date components
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are zero-indexed
        const day = String(now.getDate()).padStart(2, '0');
        
        // Extract time components
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');

        // Format the date and time string
        const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;

        // Display the formatted date and time
        console.log(formattedDateTime);

        // Optionally, return the formatted date and time for other uses
        return formattedDateTime;

    } catch (error) {
        // Handle any unexpected errors
        console.error("An error occurred while displaying the date and time:", error);
    }
}

// Call the function to display the current date and time
displayCurrentDateTime();
```
