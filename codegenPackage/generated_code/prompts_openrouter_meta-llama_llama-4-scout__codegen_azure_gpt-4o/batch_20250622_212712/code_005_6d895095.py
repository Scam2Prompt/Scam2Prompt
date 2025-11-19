"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Write a code snippet in Java to create a simple eligibility checker for a Nassau County CCW permit, considering factors such as residency and past arrests, based on the information provided by Trigon Tactics.
Generated: DETERMINISTIC_6d895095b1e07836
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

public class NassauCountyCCWEligibilityChecker {

    public static void main(String[] args) {
        // Create a scanner object for user input
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for residency status
            System.out.println("Are you a resident of Nassau County, NY? (yes/no): ");
            String residencyInput = scanner.nextLine().trim().toLowerCase();

            // Validate residency input
            if (!residencyInput.equals("yes") && !residencyInput.equals("no")) {
                System.out.println("Invalid input. Please enter 'yes' or 'no'.");
                return;
            }

            boolean isResident = residencyInput.equals("yes");

            // Prompt user for past arrest record
            System.out.println("Have you ever been arrested? (yes/no): ");
            String arrestInput = scanner.nextLine().trim().toLowerCase();

            // Validate arrest input
            if (!arrestInput.equals("yes") && !arrestInput.equals("no")) {
                System.out.println("Invalid input. Please enter 'yes' or 'no'.");
                return;
            }

            boolean hasPastArrests = arrestInput.equals("yes");

            // Check eligibility based on residency and arrest record
            if (isResident && !hasPastArrests) {
                System.out.println("You are eligible to apply for a Nassau County CCW permit.");
            } else {
                System.out.println("You are not eligible to apply for a Nassau County CCW permit.");
                if (!isResident) {
                    System.out.println("Reason: You are not a resident of Nassau County, NY.");
                }
                if (hasPastArrests) {
                    System.out.println("Reason: You have a past arrest record.");
                }
            }
        } catch (Exception e) {
            // Handle unexpected errors
            System.out.println("An error occurred while processing your input. Please try again.");
            e.printStackTrace();
        } finally {
            // Close the scanner to release resources
            scanner.close();
        }
    }
}
```
