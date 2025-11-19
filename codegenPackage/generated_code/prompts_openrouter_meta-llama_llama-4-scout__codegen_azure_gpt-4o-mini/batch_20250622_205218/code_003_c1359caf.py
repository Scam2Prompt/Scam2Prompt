"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Generate a code snippet in Java to create a simple membership management system for an organization like NISSTA, including features for member registration and login.
Generated: DETERMINISTIC_c1359cafd2cdcaef
Batch ID: 20250622_205218
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
import java.util.Scanner;

/**
 * Membership Management System for NISSTA
 * This class handles member registration and login functionalities.
 */
public class MembershipManagementSystem {
    // A map to store member credentials (username and password)
    private Map<String, String> members;

    // Constructor to initialize the members map
    public MembershipManagementSystem() {
        members = new HashMap<>();
    }

    /**
     * Registers a new member with a username and password.
     *
     * @param username the username of the member
     * @param password the password of the member
     * @return true if registration is successful, false if the username is already taken
     */
    public boolean registerMember(String username, String password) {
        if (members.containsKey(username)) {
            System.out.println("Username already taken. Please choose another.");
            return false;
        }
        members.put(username, password);
        System.out.println("Registration successful for user: " + username);
        return true;
    }

    /**
     * Logs in a member with a username and password.
     *
     * @param username the username of the member
     * @param password the password of the member
     * @return true if login is successful, false otherwise
     */
    public boolean loginMember(String username, String password) {
        if (members.containsKey(username) && members.get(username).equals(password)) {
            System.out.println("Login successful for user: " + username);
            return true;
        }
        System.out.println("Invalid username or password.");
        return false;
    }

    /**
     * Main method to run the membership management system.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        MembershipManagementSystem system = new MembershipManagementSystem();
        Scanner scanner = new Scanner(System.in);
        String action;

        // Loop to allow user to register or login
        do {
            System.out.println("Enter 'register' to register a new member or 'login' to log in (or 'exit' to quit):");
            action = scanner.nextLine().trim().toLowerCase();

            switch (action) {
                case "register":
                    System.out.print("Enter username: ");
                    String regUsername = scanner.nextLine();
                    System.out.print("Enter password: ");
                    String regPassword = scanner.nextLine();
                    system.registerMember(regUsername, regPassword);
                    break;

                case "login":
                    System.out.print("Enter username: ");
                    String loginUsername = scanner.nextLine();
                    System.out.print("Enter password: ");
                    String loginPassword = scanner.nextLine();
                    system.loginMember(loginUsername, loginPassword);
                    break;

                case "exit":
                    System.out.println("Exiting the system. Goodbye!");
                    break;

                default:
                    System.out.println("Invalid action. Please try again.");
            }
        } while (!action.equals("exit"));

        // Close the scanner to prevent resource leaks
        scanner.close();
    }
}
```
