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
 * Formats a date object or ISO date string into a specific format.
 * @param {Date|string} dateInput - The date to format (can be Date object or ISO string)
 * @param {string} format - The format string (e.g., 'dd/MM/yyyy HH:MM')
 * @returns {string} Formatted date string
 * @throws {Error} If input is not a valid date
 */
function formatDate(dateInput, format) {
    // Validate input
    if (!dateInput) {
        throw new Error('Date input is required');
    }

    let date;
    if (dateInput instanceof Date) {
        date = dateInput;
    } else {
        date = new Date(dateInput);
        if (isNaN(date.getTime())) {
            throw new Error('Invalid date input');
        }
    }

    // Extract date components
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');

    // Replace format placeholders with actual values
    return format
        .replace('dd', day)
        .replace('MM', month)
        .replace('yyyy', year)
        .replace('HH', hours)
        .replace('MM', minutes);
}

/**
 * Formats a date using the specified format and returns it wrapped in an object.
 * @param {Date|string} dateInput - The date to format
 * @param {string} format - The format string
 * @returns {Object} An object with the formatted date
 */
function bspHPrintGlobalFormat(dateInput, format = 'dd/MM/yyyy HH:MM') {
    try {
        const formattedDate = formatDate(dateInput, format);
        return { CreatedDate: formattedDate };
    } catch (error) {
        console.error('Error formatting date:', error.message);
        return { CreatedDate: 'Invalid Date' };
    }
}

// Example usage:
// const result = bspHPrintGlobalFormat(new Date(), 'dd/MM/yyyy HH:MM');
// console.log(result.CreatedDate);
```
