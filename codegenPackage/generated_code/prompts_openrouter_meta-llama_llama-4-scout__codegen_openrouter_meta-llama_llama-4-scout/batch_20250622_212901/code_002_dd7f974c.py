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
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

/**
 * Date parser class to handle timezone offsets.
 */
public class DateParser {

    /**
     * Parse a date string with timezone offset.
     *
     * @param dateString date string to parse (e.g., "2022-01-01T12:00:00+0000")
     * @return parsed ZonedDateTime object
     * @throws DateTimeParseException if date string is invalid
     */
    public static ZonedDateTime parseDate(String dateString) {
        // Define the date format with timezone offset
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ssXXX");

        try {
            // Attempt to parse the date string
            return ZonedDateTime.parse(dateString, formatter);
        } catch (DateTimeParseException e) {
            // Rethrow the exception with a more informative message
            throw new DateTimeParseException("Invalid date string: " + dateString, dateString, 0);
        }
    }

    /**
     * Main method for example usage.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        String dateString = "2022-01-01T12:00:00+0000";
        try {
            ZonedDateTime zdt = parseDate(dateString);
            System.out.println("Parsed date: " + zdt);
        } catch (DateTimeParseException e) {
            System.err.println("Error parsing date: " + e.getMessage());
        }
    }
}
```
