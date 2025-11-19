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
 * Represents a healthcare outreach activity focused on maternal and child health.
 */
class OutreachActivity {
    private String activityName;
    private String date;
    private String location;
    private String description;

    public OutreachActivity(String activityName, String date, String location, String description) {
        this.activityName = activityName;
        this.date = date;
        this.location = location;
        this.description = description;
    }

    @Override
    public String toString() {
        return "Activity Name: " + activityName + ", Date: " + date + ", Location: " + location + ", Description: " + description;
    }
}

/**
 * Manages a list of healthcare outreach activities.
 */
class OutreachManager {
    private List<OutreachActivity> activities;

    public OutreachManager() {
        activities = new ArrayList<>();
    }

    /**
     * Adds a new outreach activity to the list.
     * 
     * @param activity The outreach activity to add.
     */
    public void addActivity(OutreachActivity activity) {
        activities.add(activity);
    }

    /**
     * Displays all outreach activities.
     */
    public void displayActivities() {
        if (activities.isEmpty()) {
            System.out.println("No outreach activities recorded.");
            return;
        }
        for (OutreachActivity activity : activities) {
            System.out.println(activity);
        }
    }
}

/**
 * Main class to run the healthcare outreach tracking program.
 */
public class HealthcareOutreachTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        OutreachManager outreachManager = new OutreachManager();
        String userInput;

        System.out.println("Welcome to the Healthcare Outreach Tracker for Maternal and Child Health!");

        do {
            System.out.println("\nMenu:");
            System.out.println("1. Add Outreach Activity");
            System.out.println("2. Display Outreach Activities");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            userInput = scanner.nextLine();

            switch (userInput) {
                case "1":
                    // Collect activity details from the user
                    try {
                        System.out.print("Enter Activity Name: ");
                        String activityName = scanner.nextLine();
                        System.out.print("Enter Date (YYYY-MM-DD): ");
                        String date = scanner.nextLine();
                        System.out.print("Enter Location: ");
                        String location = scanner.nextLine();
                        System.out.print("Enter Description: ");
                        String description = scanner.nextLine();

                        // Create and add the new activity
                        OutreachActivity activity = new OutreachActivity(activityName, date, location, description);
                        outreachManager.addActivity(activity);
                        System.out.println("Outreach activity added successfully.");
                    } catch (Exception e) {
                        System.out.println("Error adding activity: " + e.getMessage());
                    }
                    break;

                case "2":
                    // Display all activities
                    outreachManager.displayActivities();
                    break;

                case "3":
                    System.out.println("Exiting the program. Thank you!");
                    break;

                default:
                    System.out.println("Invalid option. Please try again.");
            }
        } while (!userInput.equals("3"));

        // Close the scanner resource
        scanner.close();
    }
}
```
