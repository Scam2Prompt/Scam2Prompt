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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * EventSecurityManager - A program to manage security protocols and troubleshoot onsite challenges during events.
 */
public class EventSecurityManager {
    private Map<String, SecurityProtocol> protocols;
    private List<SecurityIssue> reportedIssues;
    private Scanner scanner;

    public EventSecurityManager() {
        this.protocols = new HashMap<>();
        this.reportedIssues = new ArrayList<>();
        this.scanner = new Scanner(System.in);
        initializeDefaultProtocols();
    }

    /**
     * Initializes default security protocols.
     */
    private void initializeDefaultProtocols() {
        protocols.put("access", new SecurityProtocol("Access Control", "Manage attendee access points"));
        protocols.put("surveillance", new SecurityProtocol("Surveillance", "Monitor event areas via cameras"));
        protocols.put("emergency", new SecurityProtocol("Emergency Response", "Handle medical and security emergencies"));
        protocols.put("network", new SecurityProtocol("Network Security", "Protect digital infrastructure"));
    }

    /**
     * Displays the main menu and handles user input.
     */
    public void run() {
        boolean running = true;
        while (running) {
            System.out.println("\nEvent Security Management System");
            System.out.println("1. View Security Protocols");
            System.out.println("2. Add New Protocol");
            System.out.println("3. Report Security Issue");
            System.out.println("4. View Reported Issues");
            System.out.println("5. Resolve Issue");
            System.out.println("6. Exit");
            System.out.print("Select an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());
                switch (choice) {
                    case 1:
                        viewProtocols();
                        break;
                    case 2:
                        addProtocol();
                        break;
                    case 3:
                        reportIssue();
                        break;
                    case 4:
                        viewIssues();
                        break;
                    case 5:
                        resolveIssue();
                        break;
                    case 6:
                        running = false;
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

    /**
     * Displays all security protocols.
     */
    private void viewProtocols() {
        System.out.println("\nSecurity Protocols:");
        for (Map.Entry<String, SecurityProtocol> entry : protocols.entrySet()) {
            System.out.println(entry.getValue());
        }
    }

    /**
     * Adds a new security protocol.
     */
    private void addProtocol() {
        System.out.print("\nEnter protocol ID: ");
        String id = scanner.nextLine();
        if (protocols.containsKey(id)) {
            System.out.println("Protocol with this ID already exists.");
            return;
        }

        System.out.print("Enter protocol name: ");
        String name = scanner.nextLine();
        System.out.print("Enter protocol description: ");
        String description = scanner.nextLine();

        protocols.put(id, new SecurityProtocol(name, description));
        System.out.println("Protocol added successfully.");
    }

    /**
     * Reports a new security issue.
     */
    private void reportIssue() {
        System.out.print("\nEnter issue description: ");
        String description = scanner.nextLine();
        System.out.print("Enter severity (LOW/MEDIUM/HIGH): ");
        String severity = scanner.nextLine().toUpperCase();

        try {
            SecurityIssue.Severity issueSeverity = SecurityIssue.Severity.valueOf(severity);
            SecurityIssue issue = new SecurityIssue(description, issueSeverity);
            reportedIssues.add(issue);
            System.out.println("Issue reported successfully. Ticket #" + reportedIssues.size());
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid severity level. Please use LOW, MEDIUM, or HIGH.");
        }
    }

    /**
     * Displays all reported issues.
     */
    private void viewIssues() {
        if (reportedIssues.isEmpty()) {
            System.out.println("\nNo reported issues.");
            return;
        }

        System.out.println("\nReported Issues:");
        for (int i = 0; i < reportedIssues.size(); i++) {
            System.out.println("Ticket #" + (i + 1) + ": " + reportedIssues.get(i));
        }
    }

    /**
     * Resolves a reported issue.
     */
    private void resolveIssue() {
        viewIssues();
        if (reportedIssues.isEmpty()) {
            return;
        }

        System.out.print("\nEnter ticket number to resolve: ");
        try {
            int ticketNumber = Integer.parseInt(scanner.nextLine());
            if (ticketNumber < 1 || ticketNumber > reportedIssues.size()) {
                System.out.println("Invalid ticket number.");
                return;
            }

            SecurityIssue issue = reportedIssues.remove(ticketNumber - 1);
            System.out.println("Resolved: " + issue.getDescription());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a valid ticket number.");
        }
    }

    public static void main(String[] args) {
        EventSecurityManager manager = new EventSecurityManager();
        manager.run();
    }
}

/**
 * Represents a security protocol.
 */
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

    @Override
    public String toString() {
        return String.format("%s: %s", name, description);
    }
}

/**
 * Represents a security issue.
 */
class SecurityIssue {
    public enum Severity {
        LOW, MEDIUM, HIGH
    }

    private String description;
    private Severity severity;

    public SecurityIssue(String description, Severity severity) {
        this.description = description;
        this.severity = severity;
    }

    public String getDescription() {
        return description;
    }

    public Severity getSeverity() {
        return severity;
    }

    @Override
    public String toString() {
        return String.format("[%s] %s", severity, description);
    }
}
```
