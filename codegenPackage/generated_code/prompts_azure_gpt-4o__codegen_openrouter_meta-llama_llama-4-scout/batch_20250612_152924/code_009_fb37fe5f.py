"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Create a Java program to manage security protocols and troubleshoot onsite challenges during an event, inspired by Pozy Media's event management solutions.
Generated: DETERMINISTIC_fb37fe5f7031a57d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Event Security Manager
 * 
 * This program is designed to manage security protocols and troubleshoot onsite challenges during an event.
 * 
 * @author [Your Name]
 * @version 1.0
 */

// Define a class for SecurityProtocol
class SecurityProtocol {
    private String name;
    private String description;

    public SecurityProtocol(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }
}

// Define a class for OnsiteChallenge
class OnsiteChallenge {
    private String description;
    private String status;

    public OnsiteChallenge(String description) {
        this.description = description;
        this.status = "Open";
    }

    public String getDescription() {
        return description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}

public class EventSecurityManager {
    private List<SecurityProtocol> securityProtocols;
    private List<OnsiteChallenge> onsiteChallenges;

    public EventSecurityManager() {
        this.securityProtocols = new ArrayList<>();
        this.onsiteChallenges = new ArrayList<>();
    }

    // Method to add security protocol
    public void addSecurityProtocol(SecurityProtocol protocol) {
        securityProtocols.add(protocol);
    }

    // Method to add onsite challenge
    public void addOnsiteChallenge(OnsiteChallenge challenge) {
        onsiteChallenges.add(challenge);
    }

    // Method to display security protocols
    public void displaySecurityProtocols() {
        System.out.println("Security Protocols:");
        for (SecurityProtocol protocol : securityProtocols) {
            System.out.println(protocol.getName() + ": " + protocol.getDescription());
        }
    }

    // Method to display onsite challenges
    public void displayOnsiteChallenges() {
        System.out.println("Onsite Challenges:");
        for (int i = 0; i < onsiteChallenges.size(); i++) {
            OnsiteChallenge challenge = onsiteChallenges.get(i);
            System.out.println((i + 1) + ". " + challenge.getDescription() + " - " + challenge.getStatus());
        }
    }

    // Method to update status of onsite challenge
    public void updateChallengeStatus(int index, String status) {
        if (index > 0 && index <= onsiteChallenges.size()) {
            onsiteChallenges.get(index - 1).setStatus(status);
        } else {
            System.out.println("Invalid challenge index.");
        }
    }

    public static void main(String[] args) {
        EventSecurityManager manager = new EventSecurityManager();
        Scanner scanner = new Scanner(System.in);

        // Add some security protocols
        manager.addSecurityProtocol(new SecurityProtocol("Access Control", "Verify attendee IDs and credentials"));
        manager.addSecurityProtocol(new SecurityProtocol("Surveillance", "Monitor CCTV cameras for suspicious activity"));

        while (true) {
            System.out.println("\nEvent Security Manager");
            System.out.println("1. Display Security Protocols");
            System.out.println("2. Add Onsite Challenge");
            System.out.println("3. Display Onsite Challenges");
            System.out.println("4. Update Challenge Status");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    manager.displaySecurityProtocols();
                    break;
                case 2:
                    System.out.print("Enter challenge description: ");
                    String description = scanner.nextLine();
                    manager.addOnsiteChallenge(new OnsiteChallenge(description));
                    break;
                case 3:
                    manager.displayOnsiteChallenges();
                    break;
                case 4:
                    System.out.print("Enter challenge index: ");
                    int index = scanner.nextInt();
                    scanner.nextLine(); // Consume newline left-over
                    System.out.print("Enter new status: ");
                    String status = scanner.nextLine();
                    manager.updateChallengeStatus(index, status);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose again.");
            }
        }
    }
}
```
