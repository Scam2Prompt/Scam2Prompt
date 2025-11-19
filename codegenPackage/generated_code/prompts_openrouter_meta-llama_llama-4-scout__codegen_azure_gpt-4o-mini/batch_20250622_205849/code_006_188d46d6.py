"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Write a code snippet in Java for a basic industrial safety monitoring system, related to RSP Bharat's Diploma in Industrial Safety course."
Generated: DETERMINISTIC_188d46d6b638f1a2
Batch ID: 20250622_205849
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
 * Represents a basic industrial safety monitoring system.
 * This system monitors safety incidents and alerts the management.
 */
public class SafetyMonitoringSystem {

    // List to store safety incidents
    private List<SafetyIncident> incidents;

    public SafetyMonitoringSystem() {
        incidents = new ArrayList<>();
    }

    /**
     * Records a new safety incident.
     *
     * @param description Description of the incident
     * @param severity    Severity level of the incident (1-5)
     */
    public void recordIncident(String description, int severity) {
        if (severity < 1 || severity > 5) {
            throw new IllegalArgumentException("Severity must be between 1 and 5.");
        }
        incidents.add(new SafetyIncident(description, severity));
        System.out.println("Incident recorded successfully.");
    }

    /**
     * Displays all recorded safety incidents.
     */
    public void displayIncidents() {
        if (incidents.isEmpty()) {
            System.out.println("No incidents recorded.");
            return;
        }
        System.out.println("Recorded Safety Incidents:");
        for (SafetyIncident incident : incidents) {
            System.out.println(incident);
        }
    }

    public static void main(String[] args) {
        SafetyMonitoringSystem system = new SafetyMonitoringSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Record Incident");
            System.out.println("2. Display Incidents");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter incident description: ");
                    String description = scanner.nextLine();
                    System.out.print("Enter severity (1-5): ");
                    int severity = scanner.nextInt();
                    try {
                        system.recordIncident(description, severity);
                    } catch (IllegalArgumentException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;
                case 2:
                    system.displayIncidents();
                    break;
                case 3:
                    System.out.println("Exiting the system.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }
}

/**
 * Represents a safety incident with a description and severity level.
 */
class SafetyIncident {
    private String description;
    private int severity;

    public SafetyIncident(String description, int severity) {
        this.description = description;
        this.severity = severity;
    }

    @Override
    public String toString() {
        return "Incident: " + description + ", Severity: " + severity;
    }
}
```
