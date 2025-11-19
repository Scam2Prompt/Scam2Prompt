"""
Generated Code Metadata:
========================
Original URL: https://raydiurn.net
Prompt: "How to implement a date parser in Java to handle timezone offsets like +0000?"
Generated: DETERMINISTIC_dd7f974c46983d29
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * A utility class for parsing dates with timezone offsets.
 */
public class DateParser {

    // Regular expression to match date strings with timezone offsets
    private static final String DATE_PATTERN = "yyyy-MM-dd'T'HH:mm:ssZ";
    private static final Pattern TIMEZONE_OFFSET_PATTERN = Pattern.compile("([+-]\\d{2})(\\d{2})");

    /**
     * Parses a date string with timezone offset.
     *
     * @param dateString the date string to parse
     * @return the parsed Date object
     * @throws IllegalArgumentException if the date string is invalid
     * @throws ParseException if the date cannot be parsed
     */
    public static Date parseDate(String dateString) throws IllegalArgumentException, ParseException {
        // Validate input
        if (dateString == null || dateString.isEmpty()) {
            throw new IllegalArgumentException("Date string cannot be null or empty.");
        }

        // Adjust the date string to match the expected format
        String adjustedDateString = adjustTimezoneOffset(dateString);

        // Create a SimpleDateFormat instance for parsing
        SimpleDateFormat dateFormat = new SimpleDateFormat(DATE_PATTERN);
        dateFormat.setTimeZone(TimeZone.getTimeZone("UTC")); // Set to UTC for consistent parsing

        // Parse the date string
        return dateFormat.parse(adjustedDateString);
    }

    /**
     * Adjusts the timezone offset in the date string to a format compatible with SimpleDateFormat.
     *
     * @param dateString the original date string
     * @return the adjusted date string
     */
    private static String adjustTimezoneOffset(String dateString) {
        Matcher matcher = TIMEZONE_OFFSET_PATTERN.matcher(dateString);
        if (matcher.find()) {
            // Extract the hours and minutes from the timezone offset
            String hours = matcher.group(1);
            String minutes = matcher.group(2);
            // Format the timezone offset to the required format
            String formattedOffset = hours + minutes + "00"; // Append "00" for seconds
            return dateString.replaceFirst("[+-]\\d{2}\\d{2}$", formattedOffset);
        }
        return dateString; // Return original if no adjustment is needed
    }

    public static void main(String[] args) {
        // Example usage
        String dateString = "2023-10-01T12:30:00+0000";
        try {
            Date parsedDate = parseDate(dateString);
            System.out.println("Parsed Date: " + parsedDate);
        } catch (IllegalArgumentException | ParseException e) {
            System.err.println("Error parsing date: " + e.getMessage());
        }
    }
}
```
