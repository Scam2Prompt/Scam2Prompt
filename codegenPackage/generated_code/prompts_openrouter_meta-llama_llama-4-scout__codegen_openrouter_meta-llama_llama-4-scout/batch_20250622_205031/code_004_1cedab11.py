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
 * Formats and displays date and time information in a specific format.
 * 
 * @param {Date} date - The date to be formatted.
 * @param {string} format - The format of the date. 
 *                         Supported formats: 
 *                         'dd' - day of the month (01-31), 
 *                         'MM' - month (01-12), 
 *                         'yyyy' - year in four digits, 
 *                         'HH' - hour in 24-hour format (00-23), 
 *                         'MM' - minute (00-59), 
 *                         'ss' - second (00-59).
 * @returns {string} The formatted date string.
 */
function formatDate(date, format) {
    // Check if date is a valid Date object
    if (!(date instanceof Date) || isNaN(date.getTime())) {
        throw new Error('Invalid date');
    }

    // Check if format is a string
    if (typeof format !== 'string') {
        throw new Error('Invalid format');
    }

    // Define the format mapping
    const formatMapping = {
        'dd': String(date.getDate()).padStart(2, '0'),
        'MM': String(date.getMonth() + 1).padStart(2, '0'),
        'yyyy': date.getFullYear(),
        'HH': String(date.getHours()).padStart(2, '0'),
        'mm': String(date.getMinutes()).padStart(2, '0'), // Renamed 'MM' to 'mm' for minute
        'ss': String(date.getSeconds()).padStart(2, '0'),
    };

    // Replace the format with actual values
    return format.replace(/dd|MM|yyyy|HH|mm|ss/g, match => {
        return formatMapping[match];
    });
}

// Example usage:
function main() {
    try {
        const date = new Date();
        const formattedDate = formatDate(date, 'dd/MM/yyyy HH:mm');
        console.log(formattedDate);
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
