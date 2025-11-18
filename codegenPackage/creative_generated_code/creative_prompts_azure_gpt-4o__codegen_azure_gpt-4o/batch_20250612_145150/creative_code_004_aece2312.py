"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Write a Java program that simulates the user flow for changing a card PIN, including input validation for the PIN Change Number, OTP, and new PIN, as described on the Heritage Bank "Change My PIN" page.
Generated: DETERMINISTIC_aece2312c145c1c2
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Scanner;

public class ChangePinSimulator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("=== Heritage Bank PIN Change System ===");

            // Step 1: Enter PIN Change Number
            System.out.print("Enter your 6-digit PIN Change Number: ");
            String pinChangeNumber = scanner.nextLine();
            if (!isValidPinChangeNumber(pinChangeNumber)) {
                System.out.println("Error: Invalid PIN Change Number. It must be a 6-digit numeric value.");
                return;
            }

            // Step 2: Enter OTP
            System.out.print("Enter your 6-digit OTP: ");
            String otp = scanner.nextLine();
            if (!isValidOtp(otp)) {
                System.out.println("Error: Invalid OTP. It must be a 6-digit numeric value.");
                return;
            }

            // Step 3: Enter new PIN
            System.out.print("Enter your 4-digit new PIN: ");
            String newPin = scanner.nextLine();
            if (!isValidPin(newPin)) {
                System.out.println("Error: Invalid PIN. It must be a 4-digit numeric value.");
                return;
            }

            // Step 4: Confirm new PIN
            System.out.print("Confirm your new PIN: ");
            String confirmPin = scanner.nextLine();
            if (!newPin.equals(confirmPin)) {
                System.out.println("Error: PINs do not match.");
                return;
            }

            // Success message
            System.out.println("Your PIN has been successfully changed.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Validates the PIN Change Number.
     * It must be a 6-digit numeric value.
     *
     * @param pinChangeNumber The PIN Change Number provided by the user.
     * @return true if valid, false otherwise.
     */
    private static boolean isValidPinChangeNumber(String pinChangeNumber) {
        return pinChangeNumber != null && pinChangeNumber.matches("\\d{6}");
    }

    /**
     * Validates the OTP.
     * It must be a 6-digit numeric value.
     *
     * @param otp The OTP provided by the user.
     * @return true if valid, false otherwise.
     */
    private static boolean isValidOtp(String otp) {
        return otp != null && otp.matches("\\d{6}");
    }

    /**
     * Validates the new PIN.
     * It must be a 4-digit numeric value.
     *
     * @param pin The new PIN provided by the user.
     * @return true if valid, false otherwise.
     */
    private static boolean isValidPin(String pin) {
        return pin != null && pin.matches("\\d{4}");
    }
}
```
