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
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * HealthcareOutreachTracker
 * A program to track healthcare outreach activities focusing on maternal and child health.
 * This program allows users to add, view, and search outreach activities.
 */
public class HealthcareOutreachTracker {

    // Class to represent an outreach activity
    static class OutreachActivity {
        private String activityName;
        private String targetGroup;
        private String location;
        private String date;
        private String description;

        // Constructor
        public OutreachActivity(String activityName, String targetGroup, String location, String date, String description) {
            this.activityName = activityName;
            this.targetGroup = targetGroup;
            this.location = location;
            this.date = date;
            this.description = description;
        }

        // Getters
        public String getActivityName() {
            return activityName;
        }

        public String getTargetGroup() {
            return targetGroup;
        }

        public String getLocation() {
            return location;
        }

        public String getDate() {
            return date;
        }

        public String getDescription() {
            return description;
        }

        // Override toString for easy display
        @Override
        public String toString() {
            return "Activity Name: " + activityName + "\n" +
                   "Target Group: " + targetGroup + "\n" +
                   "Location: " + location + "\n" +
                   "Date: " + date + "\n" +
                   "Description: " + description + "\n";
        }
    }

    // List to store outreach activities
    private static List<OutreachActivity> activities = new ArrayList<>();

    // Main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("Welcome to the Healthcare Outreach Tracker!");

        while (running) {
            // Display menu
            System.out.println("\nMenu:");
            System.out.println("1. Add Outreach Activity");
            System.out.println("2. View All Activities");
            System.out.println("3. Search Activities by Target Group");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            // Get user choice
            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
                continue;
            }

            switch (choice) {
                case 1:
                    // Add Outreach Activity
                    addActivity(scanner);
                    break;
                case 2:
                    // View All Activities
                    viewActivities();
                    break;
                case 3:
                    // Search Activities by Target Group
                    searchActivities(scanner);
                    break;
                case 4:
                    // Exit
                    running = false;
                    System.out.println("Exiting the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }

        scanner.close();
    }

    /**
     * Adds a new outreach activity to the list.
     * @param scanner Scanner object for user input
     */
    private static void addActivity(Scanner scanner) {
        System.out.println("\nAdd Outreach Activity:");

        // Get activity details from user
        System.out.print("Enter Activity Name: ");
        String activityName = scanner.nextLine();

        System.out.print("Enter Target Group (e.g., Maternal, Child): ");
        String targetGroup = scanner.nextLine();

        System.out.print("Enter Location: ");
        String location = scanner.nextLine();

        System.out.print("Enter Date (YYYY-MM-DD): ");
        String date = scanner.nextLine();

        System.out.print("Enter Description: ");
        String description = scanner.nextLine();

        // Create and add activity to the list
        OutreachActivity activity = new OutreachActivity(activityName, targetGroup, location, date, description);
        activities.add(activity);

        System.out.println("Activity added successfully!");
    }

    /**
     * Displays all outreach activities.
     */
    private static void viewActivities() {
        System.out.println("\nAll Outreach Activities:");

        if (activities.isEmpty()) {
            System.out.println("No activities found.");
        } else {
            for (OutreachActivity activity : activities) {
                System.out.println(activity);
                System.out.println("----------------------------");
            }
        }
    }

    /**
     * Searches for activities by target group.
     * @param scanner Scanner object for user input
     */
    private static void searchActivities(Scanner scanner) {
        System.out.print("\nEnter Target Group to Search (e.g., Maternal, Child): ");
        String targetGroup = scanner.nextLine();

        System.out.println("\nSearch Results:");

        boolean found = false;
        for (OutreachActivity activity : activities) {
            if (activity.getTargetGroup().equalsIgnoreCase(targetGroup)) {
                System.out.println(activity);
                System.out.println("----------------------------");
                found = true;
            }
        }

        if (!found) {
            System.out.println("No activities found for the target group: " + targetGroup);
        }
    }
}
```
