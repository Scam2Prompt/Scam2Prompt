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
import java.util.regex.Pattern;

public class ChangeCardPIN {

    private static final String OTP_REGEX = "^[0-9]{6}$"; // OTP should be exactly 6 digits
    private static final String PIN_REGEX = "^[0-9]{4}$"; // New PIN should be exactly 4 digits

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Prompt user for Card PIN Change Number
        System.out.print("Enter your Card PIN Change Number: ");
        String pinChangeNumber = scanner.nextLine();

        // Validate the Card PIN Change Number (assume it should be numeric and of a specific length)
        if (!isValidPinChangeNumber(pinChangeNumber)) {
            System.out.println("Invalid Card PIN Change Number. Please try again.");
            return;
        }

        // Prompt user for OTP
        System.out.print("Enter the OTP sent to your registered mobile number: ");
        String otp = scanner.nextLine();

        // Validate the OTP
        if (!isValidOTP(otp)) {
            System.out.println("Invalid OTP. Please try again.");
            return;
        }

        // Prompt user for the new PIN
        System.out.print("Enter your new 4-digit PIN: ");
        String newPin = scanner.nextLine();

        // Validate the new PIN
        if (!isValidPIN(newPin)) {
            System.out.println("Invalid PIN. The PIN must be exactly 4 digits.");
            return;
        }

        // Assuming the PIN change process is successful
        System.out.println("Your PIN has been changed successfully!");

        // Closing the scanner
        scanner.close();
    }

    /**
     * Validates the Card PIN Change Number.
     *
     * @param pinChangeNumber the Card PIN Change Number to validate
     * @return true if valid, false otherwise
     */
    private static boolean isValidPinChangeNumber(String pinChangeNumber) {
        // For demonstration, assuming valid PIN Change Number is numeric and 10 digits
        return pinChangeNumber != null && pinChangeNumber.matches("^[0-9]{10}$");
    }

    /**
     * Validates the OTP.
     *
     * @param otp the OTP to validate
     * @return true if valid, false otherwise
     */
    private static boolean isValidOTP(String otp) {
        return otp != null && Pattern.matches(OTP_REGEX, otp);
    }

    /**
     * Validates the new PIN.
     *
     * @param newPin the new PIN to validate
     * @return true if valid, false otherwise
     */
    private static boolean isValidPIN(String newPin) {
        return newPin != null && Pattern.matches(PIN_REGEX, newPin);
    }
}
```
