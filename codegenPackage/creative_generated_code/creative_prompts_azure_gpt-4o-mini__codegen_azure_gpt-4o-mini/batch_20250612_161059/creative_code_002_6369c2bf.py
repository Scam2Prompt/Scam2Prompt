"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Create a Java program that tracks healthcare outreach activities, focusing on maternal and child health, as outlined by Indological India.
Generated: DETERMINISTIC_6369c2bfbbc69eb2
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents a healthcare outreach activity.
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

    // Getters for activity details
    public String getActivityName() {
        return activityName;
    }

    public String getDate() {
        return date;
    }

    public String getLocation() {
        return location;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return "Activity: " + activityName + ", Date: " + date + 
               ", Location: " + location + ", Description: " + description;
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

    // Adds a new outreach activity
    public void addActivity(OutreachActivity activity) {
        activities.add(activity);
    }

    // Displays all outreach activities
    public void displayActivities() {
        if (activities.isEmpty()) {
            System.out.println("No outreach activities recorded.");
        } else {
            for (OutreachActivity activity : activities) {
                System.out.println(activity);
            }
        }
    }
}

/**
 * Main class for tracking healthcare outreach activities.
 */
public class HealthcareOutreachTracker {
    private static final Scanner scanner = new Scanner(System.in);
    private static final OutreachManager outreachManager = new OutreachManager();

    public static void main(String[] args) {
        int choice;

        do {
            choice = showMenu();
            switch (choice) {
                case 1:
                    addOutreachActivity();
                    break;
                case 2:
                    outreachManager.displayActivities();
                    break;
                case 3:
                    System.out.println("Exiting the program. Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice. Please select again.");
            }
        } while (choice != 3);
    }

    // Displays the menu and returns the user's choice
    private static int showMenu() {
        System.out.println("\nHealthcare Outreach Tracker Menu:");
        System.out.println("1. Add Outreach Activity");
        System.out.println("2. View Outreach Activities");
        System.out.println("3. Exit");
        System.out.print("Enter your choice: ");
        return Integer.parseInt(scanner.nextLine());
    }

    // Collects data for a new outreach activity and adds it to the manager
    private static void addOutreachActivity() {
        try {
            System.out.print("Enter activity name: ");
            String name = scanner.nextLine();
            System.out.print("Enter date (YYYY-MM-DD): ");
            String date = scanner.nextLine();
            System.out.print("Enter location: ");
            String location = scanner.nextLine();
            System.out.print("Enter description: ");
            String description = scanner.nextLine();

            OutreachActivity activity = new OutreachActivity(name, date, location, description);
            outreachManager.addActivity(activity);
            System.out.println("Outreach activity added successfully!");

        } catch (Exception e) {
            System.out.println("An error occurred while adding an activity: " + e.getMessage());
        }
    }
}
```
