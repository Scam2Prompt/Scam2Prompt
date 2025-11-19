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

/**
 * EligibilityChecker class to determine if an individual is eligible for a Nassau County CCW permit.
 */
public class EligibilityChecker {

    // Constants for eligibility criteria
    private static final int MIN_AGE = 21;

    /**
     * Main method to run the eligibility checker.
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Gather user information
            System.out.print("Enter your age: ");
            int age = Integer.parseInt(scanner.nextLine());

            System.out.print("Are you a resident of Nassau County? (yes/no): ");
            String residency = scanner.nextLine().trim().toLowerCase();

            System.out.print("Do you have any past arrests? (yes/no): ");
            String pastArrests = scanner.nextLine().trim().toLowerCase();

            // Check eligibility
            boolean isEligible = checkEligibility(age, residency, pastArrests);
            if (isEligible) {
                System.out.println("You are eligible for a Nassau County CCW permit.");
            } else {
                System.out.println("You are not eligible for a Nassau County CCW permit.");
            }

        } catch (NumberFormatException e) {
            System.err.println("Invalid input for age. Please enter a valid number.");
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Checks the eligibility for a Nassau County CCW permit based on age, residency, and past arrests.
     *
     * @param age          The age of the applicant
     * @param residency    The residency status of the applicant
     * @param pastArrests  The past arrest status of the applicant
     * @return true if eligible, false otherwise
     */
    private static boolean checkEligibility(int age, String residency, String pastArrests) {
        // Check if the applicant meets the minimum age requirement
        if (age < MIN_AGE) {
            return false;
        }

        // Check residency requirement
        if (!residency.equals("yes")) {
            return false;
        }

        // Check past arrest status
        if (pastArrests.equals("yes")) {
            return false;
        }

        // If all checks pass, the applicant is eligible
        return true;
    }
}
```
