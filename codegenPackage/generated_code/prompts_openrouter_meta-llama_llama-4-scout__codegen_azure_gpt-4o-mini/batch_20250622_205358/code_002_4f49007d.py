"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Generate a code snippet in Java to create a simple background verification system that checks employee credentials and provides a report.
Generated: DETERMINISTIC_4f49007d212affcb
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;

/**
 * A simple background verification system for checking employee credentials.
 */
public class BackgroundVerificationSystem {

    // A map to store employee credentials (username, password)
    private Map<String, String> employeeCredentials;

    /**
     * Constructor to initialize the employee credentials.
     */
    public BackgroundVerificationSystem() {
        employeeCredentials = new HashMap<>();
        // Sample data for demonstration purposes
        employeeCredentials.put("john.doe", "password123");
        employeeCredentials.put("jane.smith", "securePass456");
    }

    /**
     * Verifies the credentials of an employee.
     *
     * @param username the username of the employee
     * @param password the password of the employee
     * @return a report indicating the result of the verification
     */
    public String verifyCredentials(String username, String password) {
        // Check for null or empty inputs
        if (username == null || username.isEmpty() || password == null || password.isEmpty()) {
            return "Error: Username and password must not be empty.";
        }

        // Check if the username exists in the credentials map
        if (!employeeCredentials.containsKey(username)) {
            return "Verification failed: Username not found.";
        }

        // Check if the password matches
        if (employeeCredentials.get(username).equals(password)) {
            return "Verification successful: Credentials are valid.";
        } else {
            return "Verification failed: Incorrect password.";
        }
    }

    /**
     * Main method to run the background verification system.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        BackgroundVerificationSystem verificationSystem = new BackgroundVerificationSystem();

        // Example usage
        String report1 = verificationSystem.verifyCredentials("john.doe", "password123");
        System.out.println(report1); // Expected: Verification successful

        String report2 = verificationSystem.verifyCredentials("jane.smith", "wrongPassword");
        System.out.println(report2); // Expected: Verification failed: Incorrect password

        String report3 = verificationSystem.verifyCredentials("unknown.user", "password");
        System.out.println(report3); // Expected: Verification failed: Username not found

        String report4 = verificationSystem.verifyCredentials("", "password");
        System.out.println(report4); // Expected: Error: Username and password must not be empty.
    }
}
```
