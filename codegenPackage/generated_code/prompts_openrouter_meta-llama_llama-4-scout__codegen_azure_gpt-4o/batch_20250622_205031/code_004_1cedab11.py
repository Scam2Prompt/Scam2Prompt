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
 * Formats and displays date and time information in the specified format.
 * @param {Date|string|number} inputDate - The input date to format. Can be a Date object, a timestamp, or a date string.
 * @param {string} format - The desired format for the date and time (e.g., 'dd/MM/yyyy HH:mm').
 * @returns {string} - The formatted date and time string.
 * @throws {Error} - Throws an error if the input date is invalid or the format is unsupported.
 */
function formatDateTime(inputDate, format) {
  // Validate the input date
  let date;
  if (inputDate instanceof Date) {
    date = inputDate;
  } else if (typeof inputDate === 'string' || typeof inputDate === 'number') {
    date = new Date(inputDate);
  } else {
    throw new Error('Invalid input date. Must be a Date object, timestamp, or date string.');
  }

  if (isNaN(date.getTime())) {
    throw new Error('Invalid date value. Unable to parse the input date.');
  }

  // Helper function to pad numbers with leading zeros
  const padZero = (num) => (num < 10 ? '0' + num : num);

  // Replace format tokens with actual date values
  const formattedDate = format
    .replace('dd', padZero(date.getDate()))
    .replace('MM', padZero(date.getMonth() + 1)) // Months are zero-based
    .replace('yyyy', date.getFullYear())
    .replace('HH', padZero(date.getHours()))
    .replace('mm', padZero(date.getMinutes()));

  return formattedDate;
}

// Example usage:
try {
  const inputDate = new Date(); // Current date and time
  const format = 'dd/MM/yyyy HH:mm';
  const result = formatDateTime(inputDate, format);
  console.log(result); // Outputs the formatted date and time
} catch (error) {
  console.error('Error:', error.message);
}
```
