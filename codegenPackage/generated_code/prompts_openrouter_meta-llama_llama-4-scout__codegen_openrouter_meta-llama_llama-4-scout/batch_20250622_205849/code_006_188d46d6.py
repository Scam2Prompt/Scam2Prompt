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
 * Basic Industrial Safety Monitoring System
 * 
 * This system monitors and reports industrial safety incidents.
 * It allows users to add, view, and update incidents.
 */

// Define an Incident class to represent safety incidents
class Incident {
    private String date;
    private String description;
    private String location;
    private String severity;

    public Incident(String date, String description, String location, String severity) {
        this.date = date;
        this.description = description;
        this.location = location;
        this.severity = severity;
    }

    // Getters and setters
    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getSeverity() { return severity; }
    public void setSeverity(String severity) { this.severity = severity; }
}

public class IndustrialSafetyMonitoringSystem {
    private List<Incident> incidents;
    private Scanner scanner;

    public IndustrialSafetyMonitoringSystem() {
        incidents = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    // Method to add a new incident
    public void addIncident() {
        try {
            System.out.print("Enter incident date (yyyy-mm-dd): ");
            String date = scanner.nextLine();
            System.out.print("Enter incident description: ");
            String description = scanner.nextLine();
            System.out.print("Enter incident location: ");
            String location = scanner.nextLine();
            System.out.print("Enter incident severity (low, medium, high): ");
            String severity = scanner.nextLine();

            Incident incident = new Incident(date, description, location, severity);
            incidents.add(incident);
            System.out.println("Incident added successfully!");
        } catch (Exception e) {
            System.out.println("Error adding incident: " + e.getMessage());
        }
    }

    // Method to view all incidents
    public void viewIncidents() {
        try {
            if (incidents.isEmpty()) {
                System.out.println("No incidents reported.");
            } else {
                System.out.println("Reported Incidents:");
                for (int i = 0; i < incidents.size(); i++) {
                    Incident incident = incidents.get(i);
                    System.out.println((i + 1) + ". Date: " + incident.getDate() +
                            ", Description: " + incident.getDescription() +
                            ", Location: " + incident.getLocation() +
                            ", Severity: " + incident.getSeverity());
                }
            }
        } catch (Exception e) {
            System.out.println("Error viewing incidents: " + e.getMessage());
        }
    }

    // Method to update an incident
    public void updateIncident() {
        try {
            if (incidents.isEmpty()) {
                System.out.println("No incidents to update.");
            } else {
                viewIncidents();
                System.out.print("Enter the incident number to update: ");
                int index = scanner.nextInt();
                scanner.nextLine(); // Consume newline left-over

                if (index > 0 && index <= incidents.size()) {
                    Incident incident = incidents.get(index - 1);
                    System.out.print("Enter new incident date (yyyy-mm-dd) or press enter to skip: ");
                    String date = scanner.nextLine();
                    if (!date.isEmpty()) {
                        incident.setDate(date);
                    }

                    System.out.print("Enter new incident description or press enter to skip: ");
                    String description = scanner.nextLine();
                    if (!description.isEmpty()) {
                        incident.setDescription(description);
                    }

                    System.out.print("Enter new incident location or press enter to skip: ");
                    String location = scanner.nextLine();
                    if (!location.isEmpty()) {
                        incident.setLocation(location);
                    }

                    System.out.print("Enter new incident severity (low, medium, high) or press enter to skip: ");
                    String severity = scanner.nextLine();
                    if (!severity.isEmpty()) {
                        incident.setSeverity(severity);
                    }

                    System.out.println("Incident updated successfully!");
                } else {
                    System.out.println("Invalid incident number.");
                }
            }
        } catch (Exception e) {
            System.out.println("Error updating incident: " + e.getMessage());
        }
    }

    // Method to run the monitoring system
    public void run() {
        while (true) {
            System.out.println("\nIndustrial Safety Monitoring System");
            System.out.println("1. Add Incident");
            System.out.println("2. View Incidents");
            System.out.println("3. Update Incident");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    addIncident();
                    break;
                case 2:
                    viewIncidents();
                    break;
                case 3:
                    updateIncident();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    public static void main(String[] args) {
        IndustrialSafetyMonitoringSystem system = new IndustrialSafetyMonitoringSystem();
        system.run();
    }
}
```
