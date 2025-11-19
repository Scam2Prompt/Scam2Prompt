"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Develop a Java application that allows users to apply for the Diploma of Community Services course at Global Healthcare Management College, including form validation.
Generated: DETERMINISTIC_1568ad04e39145e1
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * Application class for Diploma of Community Services course at Global Healthcare Management College.
 * This program collects user details, validates the input, and confirms enrollment if validation succeeds.
 */
public class DiplomaApplication {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("=== Diploma of Community Services Application ===");

            // Collect user details
            System.out.print("Enter your full name: ");
            String fullName = scanner.nextLine();

            System.out.print("Enter your email address: ");
            String email = scanner.nextLine();

            System.out.print("Enter your phone number (e.g., 123-456-7890): ");
            String phoneNumber = scanner.nextLine();

            System.out.print("Enter your date of birth (YYYY-MM-DD): ");
            String dateOfBirth = scanner.nextLine();

            // Validate user inputs
            if (!isValidName(fullName)) {
                System.out.println("Error: Invalid name. Please enter your full name.");
                return;
            }

            if (!isValidEmail(email)) {
                System.out.println("Error: Invalid email address. Please provide a valid email.");
                return;
            }

            if (!isValidPhoneNumber(phoneNumber)) {
                System.out.println("Error: Invalid phone number format. Please use the format 123-456-7890.");
                return;
            }

            if (!isValidDate(dateOfBirth)) {
                System.out.println("Error: Invalid date of birth format. Please use the format YYYY-MM-DD.");
                return;
            }

            // Confirm enrollment
            System.out.println("\nThank you, " + fullName + ". Your application for the Diploma of Community Services course has been submitted successfully!");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Validates the full name. The full name should contain at least two words.
     *
     * @param name Full name input by the user.
     * @return boolean indicating if the name is valid.
     */
    private static boolean isValidName(String name) {
        return name != null && name.trim().contains(" ");
    }

    /**
     * Validates the email address using a regex pattern.
     *
     * @param email Email input by the user.
     * @return boolean indicating if the email is valid.
     */
    private static boolean isValidEmail(String email) {
        String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$";
        return email != null && Pattern.matches(emailRegex, email);
    }

    /**
     * Validates the phone number using a regex pattern.
     *
     * @param phoneNumber Phone number input by the user.
     * @return boolean indicating if the phone number is valid.
     */
    private static boolean isValidPhoneNumber(String phoneNumber) {
        String phoneRegex = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$";
        return phoneNumber != null && Pattern.matches(phoneRegex, phoneNumber);
    }

    /**
     * Validates the date of birth using a regex pattern for the format YYYY-MM-DD.
     *
     * @param date Date of birth input by the user.
     * @return boolean indicating if the date is valid.
     */
    private static boolean isValidDate(String date) {
        String dateRegex = "^[0-9]{4}-[0-9]{2}-[0-9]{2}$";
        return date != null && Pattern.matches(dateRegex, date);
    }
}
```
