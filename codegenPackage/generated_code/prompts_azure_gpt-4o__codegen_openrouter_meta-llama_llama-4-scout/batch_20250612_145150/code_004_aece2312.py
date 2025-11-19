"""
Generated Code Metadata:
========================
Original URL: https://changemypin.com.au
Prompt: Write a Java program that simulates the user flow for changing a card PIN, including input validation for the PIN Change Number, OTP, and new PIN, as described on the Heritage Bank "Change My PIN" page.
Generated: DETERMINISTIC_aece2312c145c1c2
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Simulates the user flow for changing a card PIN.
 */
public class PinChanger {

    private static final int PIN_CHANGE_NUMBER_LENGTH = 6;
    private static final int OTP_LENGTH = 6;
    private static final int NEW_PIN_LENGTH = 4;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get PIN Change Number
        String pinChangeNumber = getPinChangeNumber(scanner);

        // Get OTP
        String otp = getOtp(scanner);

        // Get new PIN
        String newPin = getNewPin(scanner);

        // Get confirm new PIN
        String confirmNewPin = getConfirmNewPin(scanner, newPin);

        // Validate and change PIN
        if (validatePinChange(pinChangeNumber, otp, newPin, confirmNewPin)) {
            System.out.println("PIN changed successfully!");
        } else {
            System.out.println("PIN change failed. Please try again.");
        }
    }

    /**
     * Gets the PIN Change Number from the user.
     *
     * @param scanner the Scanner object to read user input
     * @return the PIN Change Number
     */
    private static String getPinChangeNumber(Scanner scanner) {
        while (true) {
            try {
                System.out.print("Enter your 6-digit PIN Change Number: ");
                String pinChangeNumber = scanner.nextLine().trim();
                if (pinChangeNumber.length() == PIN_CHANGE_NUMBER_LENGTH && pinChangeNumber.matches("\\d+")) {
                    return pinChangeNumber;
                } else {
                    System.out.println("Invalid PIN Change Number. Please enter 6 digits.");
                }
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }

    /**
     * Gets the OTP from the user.
     *
     * @param scanner the Scanner object to read user input
     * @return the OTP
     */
    private static String getOtp(Scanner scanner) {
        while (true) {
            try {
                System.out.print("Enter your 6-digit OTP: ");
                String otp = scanner.nextLine().trim();
                if (otp.length() == OTP_LENGTH && otp.matches("\\d+")) {
                    return otp;
                } else {
                    System.out.println("Invalid OTP. Please enter 6 digits.");
                }
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }

    /**
     * Gets the new PIN from the user.
     *
     * @param scanner the Scanner object to read user input
     * @return the new PIN
     */
    private static String getNewPin(Scanner scanner) {
        while (true) {
            try {
                System.out.print("Enter your new 4-digit PIN: ");
                String newPin = scanner.nextLine().trim();
                if (newPin.length() == NEW_PIN_LENGTH && newPin.matches("\\d+")) {
                    return newPin;
                } else {
                    System.out.println("Invalid new PIN. Please enter 4 digits.");
                }
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }

    /**
     * Gets the confirm new PIN from the user.
     *
     * @param scanner  the Scanner object to read user input
     * @param newPin the new PIN
     * @return the confirm new PIN
     */
    private static String getConfirmNewPin(Scanner scanner, String newPin) {
        while (true) {
            try {
                System.out.print("Confirm your new 4-digit PIN: ");
                String confirmNewPin = scanner.nextLine().trim();
                if (confirmNewPin.equals(newPin)) {
                    return confirmNewPin;
                } else {
                    System.out.println("PINs do not match. Please try again.");
                }
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }

    /**
     * Validates the PIN change.
     *
     * @param pinChangeNumber the PIN Change Number
     * @param otp             the OTP
     * @param newPin          the new PIN
     * @param confirmNewPin   the confirm new PIN
     * @return true if valid, false otherwise
     */
    private static boolean validatePinChange(String pinChangeNumber, String otp, String newPin, String confirmNewPin) {
        // Simulate validation logic (replace with actual validation)
        return true;
    }
}
```
