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
 * Simple Membership Management System for NISSTA
 * Features: Member registration and login
 */
public class MembershipSystem {
    private static Map<String, Member> members = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;
        
        while (running) {
            System.out.println("\nNISSTA Membership System");
            System.out.println("1. Register");
            System.out.println("2. Login");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");
            
            try {
                int choice = Integer.parseInt(scanner.nextLine());
                
                switch (choice) {
                    case 1:
                        registerMember();
                        break;
                    case 2:
                        loginMember();
                        break;
                    case 3:
                        running = false;
                        System.out.println("Exiting system...");
                        break;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number.");
            }
        }
        scanner.close();
    }

    private static void registerMember() {
        System.out.println("\nMember Registration");
        
        try {
            System.out.print("Enter username: ");
            String username = scanner.nextLine();
            
            if (members.containsKey(username)) {
                System.out.println("Username already exists.");
                return;
            }
            
            System.out.print("Enter password: ");
            String password = scanner.nextLine();
            
            System.out.print("Enter full name: ");
            String fullName = scanner.nextLine();
            
            System.out.print("Enter email: ");
            String email = scanner.nextLine();
            
            Member newMember = new Member(username, password, fullName, email);
            members.put(username, newMember);
            
            System.out.println("Registration successful!");
        } catch (Exception e) {
            System.out.println("Error during registration: " + e.getMessage());
        }
    }

    private static void loginMember() {
        System.out.println("\nMember Login");
        
        try {
            System.out.print("Enter username: ");
            String username = scanner.nextLine();
            
            System.out.print("Enter password: ");
            String password = scanner.nextLine();
            
            if (!members.containsKey(username)) {
                System.out.println("Username not found.");
                return;
            }
            
            Member member = members.get(username);
            
            if (member.getPassword().equals(password)) {
                System.out.println("Login successful!");
                System.out.println("Welcome, " + member.getFullName());
                System.out.println("Email: " + member.getEmail());
            } else {
                System.out.println("Incorrect password.");
            }
        } catch (Exception e) {
            System.out.println("Error during login: " + e.getMessage());
        }
    }

    static class Member {
        private String username;
        private String password;
        private String fullName;
        private String email;

        public Member(String username, String password, String fullName, String email) {
            this.username = username;
            this.password = password;
            this.fullName = fullName;
            this.email = email;
        }

        public String getUsername() {
            return username;
        }

        public String getPassword() {
            return password;
        }

        public String getFullName() {
            return fullName;
        }

        public String getEmail() {
            return email;
        }
    }
}
```
