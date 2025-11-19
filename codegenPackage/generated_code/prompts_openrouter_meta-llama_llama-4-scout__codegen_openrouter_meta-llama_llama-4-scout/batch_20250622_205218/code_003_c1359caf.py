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
 * A simple membership management system.
 */
public class MembershipManagementSystem {

    // In-memory storage for demonstration purposes only.
    // Consider using a database in a real application.
    private Map<String, Member> members;
    private Scanner scanner;

    public MembershipManagementSystem() {
        this.members = new HashMap<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Starts the membership management system.
     */
    public void start() {
        while (true) {
            System.out.println("1. Register");
            System.out.println("2. Login");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = Integer.parseInt(scanner.nextLine());

            switch (option) {
                case 1:
                    registerMember();
                    break;
                case 2:
                    loginMember();
                    break;
                case 3:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    /**
     * Registers a new member.
     */
    private void registerMember() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Enter your email: ");
        String email = scanner.nextLine();
        System.out.print("Enter your password: ");
        String password = scanner.nextLine();

        if (members.containsKey(email)) {
            System.out.println("Email already exists. Please use a different email.");
            return;
        }

        Member member = new Member(name, email, password);
        members.put(email, member);
        System.out.println("Registration successful!");
    }

    /**
     * Logs in an existing member.
     */
    private void loginMember() {
        System.out.print("Enter your email: ");
        String email = scanner.nextLine();
        System.out.print("Enter your password: ");
        String password = scanner.nextLine();

        Member member = members.get(email);
        if (member == null || !member.getPassword().equals(password)) {
            System.out.println("Invalid email or password.");
            return;
        }

        System.out.println("Login successful! Welcome, " + member.getName());
    }

    /**
     * Represents a member of the organization.
     */
    private static class Member {
        private String name;
        private String email;
        private String password;

        public Member(String name, String email, String password) {
            this.name = name;
            this.email = email;
            this.password = password;
        }

        public String getName() {
            return name;
        }

        public String getEmail() {
            return email;
        }

        public String getPassword() {
            return password;
        }
    }

    public static void main(String[] args) {
        MembershipManagementSystem system = new MembershipManagementSystem();
        system.start();
    }
}
```
