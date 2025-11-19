"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Create a Java program that tracks healthcare outreach activities, focusing on maternal and child health, as outlined by Indological India.
Generated: DETERMINISTIC_6369c2bfbbc69eb2
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Healthcare Outreach Activity Tracker for Maternal and Child Health
 */

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Enum for activity types
enum ActivityType {
    MATERNAL_HEALTH_CHECKUP,
    CHILD_VACCINATION,
    HEALTH_EDUCATION_SESSION
}

// Class representing a healthcare outreach activity
class OutreachActivity {
    private String date;
    private ActivityType type;
    private String location;
    private int attendees;

    public OutreachActivity(String date, ActivityType type, String location, int attendees) {
        this.date = date;
        this.type = type;
        this.location = location;
        this.attendees = attendees;
    }

    // Getters and setters
    public String getDate() { return date; }
    public ActivityType getType() { return type; }
    public String getLocation() { return location; }
    public int getAttendees() { return attendees; }
}

public class HealthcareOutreachTracker {
    private List<OutreachActivity> activities;
    private Scanner scanner;

    public HealthcareOutreachTracker() {
        this.activities = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    // Method to add a new outreach activity
    public void addActivity() {
        try {
            System.out.print("Enter date (yyyy-MM-dd): ");
            String date = scanner.nextLine();
            LocalDate.parse(date, DateTimeFormatter.ISO_DATE);

            System.out.print("Enter activity type (1 for Maternal Health Checkup, 2 for Child Vaccination, 3 for Health Education Session): ");
            int typeChoice = Integer.parseInt(scanner.nextLine());
            ActivityType type = getActivityType(typeChoice);

            System.out.print("Enter location: ");
            String location = scanner.nextLine();

            System.out.print("Enter number of attendees: ");
            int attendees = Integer.parseInt(scanner.nextLine());

            OutreachActivity activity = new OutreachActivity(date, type, location, attendees);
            activities.add(activity);
            System.out.println("Activity added successfully!");
        } catch (DateTimeParseException e) {
            System.out.println("Invalid date format. Please use yyyy-MM-dd.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to view all outreach activities
    public void viewActivities() {
        if (activities.isEmpty()) {
            System.out.println("No activities recorded.");
        } else {
            System.out.println("Outreach Activities:");
            for (OutreachActivity activity : activities) {
                System.out.println("Date: " + activity.getDate());
                System.out.println("Type: " + activity.getType());
                System.out.println("Location: " + activity.getLocation());
                System.out.println("Attendees: " + activity.getAttendees());
                System.out.println();
            }
        }
    }

    // Helper method to get activity type from user input
    private ActivityType getActivityType(int choice) {
        switch (choice) {
            case 1:
                return ActivityType.MATERNAL_HEALTH_CHECKUP;
            case 2:
                return ActivityType.CHILD_VACCINATION;
            case 3:
                return ActivityType.HEALTH_EDUCATION_SESSION;
            default:
                System.out.println("Invalid choice. Defaulting to Maternal Health Checkup.");
                return ActivityType.MATERNAL_HEALTH_CHECKUP;
        }
    }

    // Main method to run the program
    public static void main(String[] args) {
        HealthcareOutreachTracker tracker = new HealthcareOutreachTracker();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Healthcare Outreach Activity Tracker");
            System.out.println("1. Add Outreach Activity");
            System.out.println("2. View Outreach Activities");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = Integer.parseInt(scanner.nextLine());

            switch (option) {
                case 1:
                    tracker.addActivity();
                    break;
                case 2:
                    tracker.viewActivities();
                    break;
                case 3:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
