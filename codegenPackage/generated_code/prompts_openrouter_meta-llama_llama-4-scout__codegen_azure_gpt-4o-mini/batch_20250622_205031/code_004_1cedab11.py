"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Develop a JavaScript function that formats and displays date and time information in a specific format, such as `{{Utility.BSPHPrintGlobal.CreatedDate | date : 'dd/MM/yyyy HH:MM'}}`.
Generated: DETERMINISTIC_1cedab1134ae3e4c
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Formats a given date object into a specified string format.
 * 
 * @param {Date} date - The date object to format.
 * @param {string} format - The format string, using 'dd', 'MM', 'yyyy', 'HH', and 'MM' as placeholders.
 * @returns {string} The formatted date string.
 * @throws {TypeError} Throws an error if the input is not a valid Date object.
 */
function formatDate(date, format) {
    // Validate input
    if (!(date instanceof Date) || isNaN(date)) {
        throw new TypeError('Invalid date object provided.');
    }

    // Define format replacements
    const replacements = {
        'dd': String(date.getDate()).padStart(2, '0'), // Day of the month (2 digits)
        'MM': String(date.getMonth() + 1).padStart(2, '0'), // Month (1-12, 2 digits)
        'yyyy': date.getFullYear(), // Full year (4 digits)
        'HH': String(date.getHours()).padStart(2, '0'), // Hours (0-23, 2 digits)
        'mm': String(date.getMinutes()).padStart(2, '0') // Minutes (0-59, 2 digits)
    };

    // Replace format placeholders with actual values
    return format.replace(/dd|MM|yyyy|HH|mm/g, match => replacements[match]);
}

// Example usage
try {
    const createdDate = new Date(); // Replace with actual date as needed
    const formattedDate = formatDate(createdDate, 'dd/MM/yyyy HH:mm');
    console.log(formattedDate); // Output the formatted date
} catch (error) {
    console.error('Error formatting date:', error.message);
}
```
