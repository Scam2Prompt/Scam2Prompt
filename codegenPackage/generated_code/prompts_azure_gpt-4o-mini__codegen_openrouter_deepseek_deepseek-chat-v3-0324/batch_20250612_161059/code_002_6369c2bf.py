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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * HealthcareOutreachTracker - A program to track maternal and child health outreach activities
 * as per Indological India's guidelines.
 */
public class HealthcareOutreachTracker {
    private static final Map<Integer, OutreachActivity> activities = new HashMap<>();
    private static int nextId = 1;
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;
        while (running) {
            displayMenu();
            int choice = getIntInput("Enter your choice: ");
            
            switch (choice) {
                case 1:
                    addOutreachActivity();
                    break;
                case 2:
                    viewAllActivities();
                    break;
                case 3:
                    updateActivity();
                    break;
                case 4:
                    deleteActivity();
                    break;
                case 5:
                    generateReport();
                    break;
                case 6:
                    running = false;
                    System.out.println("Exiting program...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }

    private static void displayMenu() {
        System.out.println("\nHealthcare Outreach Tracker");
        System.out.println("1. Add new outreach activity");
        System.out.println("2. View all activities");
        System.out.println("3. Update activity");
        System.out.println("4. Delete activity");
        System.out.println("5. Generate report");
        System.out.println("6. Exit");
    }

    private static void addOutreachActivity() {
        System.out.println("\nAdd New Outreach Activity");
        
        String location = getStringInput("Location: ");
        String description = getStringInput("Description: ");
        LocalDate date = getDateInput("Date (YYYY-MM-DD): ");
        int mothersReached = getIntInput("Number of mothers reached: ");
        int childrenReached = getIntInput("Number of children reached: ");
        String healthWorker = getStringInput("Health worker name: ");
        
        OutreachActivity activity = new OutreachActivity(
            nextId++, location, description, date, 
            mothersReached, childrenReached, healthWorker
        );
        
        activities.put(activity.getId(), activity);
        System.out.println("Activity added successfully!");
    }

    private static void viewAllActivities() {
        if (activities.isEmpty()) {
            System.out.println("No activities found.");
            return;
        }
        
        System.out.println("\nAll Outreach Activities:");
        for (OutreachActivity activity : activities.values()) {
            System.out.println(activity);
        }
    }

    private static void updateActivity() {
        viewAllActivities();
        if (activities.isEmpty()) return;
        
        int id = getIntInput("Enter activity ID to update: ");
        if (!activities.containsKey(id)) {
            System.out.println("Activity not found.");
            return;
        }
        
        OutreachActivity activity = activities.get(id);
        System.out.println("Current details:");
        System.out.println(activity);
        
        System.out.println("\nEnter new details (leave blank to keep current value):");
        String location = getOptionalStringInput("Location [" + activity.getLocation() + "]: ", activity.getLocation());
        String description = getOptionalStringInput("Description [" + activity.getDescription() + "]: ", activity.getDescription());
        LocalDate date = getOptionalDateInput("Date [" + activity.getDate() + "]: ", activity.getDate());
        int mothersReached = getOptionalIntInput("Mothers reached [" + activity.getMothersReached() + "]: ", activity.getMothersReached());
        int childrenReached = getOptionalIntInput("Children reached [" + activity.getChildrenReached() + "]: ", activity.getChildrenReached());
        String healthWorker = getOptionalStringInput("Health worker [" + activity.getHealthWorker() + "]: ", activity.getHealthWorker());
        
        OutreachActivity updatedActivity = new OutreachActivity(
            id, location, description, date, 
            mothersReached, childrenReached, healthWorker
        );
        
        activities.put(id, updatedActivity);
        System.out.println("Activity updated successfully!");
    }

    private static void deleteActivity() {
        viewAllActivities();
        if (activities.isEmpty()) return;
        
        int id = getIntInput("Enter activity ID to delete: ");
        if (activities.remove(id) != null) {
            System.out.println("Activity deleted successfully!");
        } else {
            System.out.println("Activity not found.");
        }
    }

    private static void generateReport() {
        if (activities.isEmpty()) {
            System.out.println("No activities to generate report.");
            return;
        }
        
        int totalMothers = 0;
        int totalChildren = 0;
        List<OutreachActivity> recentActivities = new ArrayList<>();
        
        for (OutreachActivity activity : activities.values()) {
            totalMothers += activity.getMothersReached();
            totalChildren += activity.getChildrenReached();
            if (activity.getDate().isAfter(LocalDate.now().minusMonths(3))) {
                recentActivities.add(activity);
            }
        }
        
        System.out.println("\nHealthcare Outreach Report");
        System.out.println("Total Activities: " + activities.size());
        System.out.println("Total Mothers Reached: " + totalMothers);
        System.out.println("Total Children Reached: " + totalChildren);
        
        if (!recentActivities.isEmpty()) {
            System.out.println("\nRecent Activities (last 3 months):");
            for (OutreachActivity activity : recentActivities) {
                System.out.println(activity);
            }
        }
    }

    // Helper methods for input handling
    private static String getStringInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }

    private static String getOptionalStringInput(String prompt, String defaultValue) {
        System.out.print(prompt);
        String input = scanner.nextLine().trim();
        return input.isEmpty() ? defaultValue : input;
    }

    private static int getIntInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static int getOptionalIntInput(String prompt, int defaultValue) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                return input.isEmpty() ? defaultValue : Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static LocalDate getDateInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return LocalDate.parse(scanner.nextLine().trim());
            } catch (Exception e) {
                System.out.println("Invalid date format. Please use YYYY-MM-DD.");
            }
        }
    }

    private static LocalDate getOptionalDateInput(String prompt, LocalDate defaultValue) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                return input.isEmpty() ? defaultValue : LocalDate.parse(input);
            } catch (Exception e) {
                System.out.println("Invalid date format. Please use YYYY-MM-DD.");
            }
        }
    }
}

/**
 * Represents a maternal and child health outreach activity.
 */
class OutreachActivity {
    private final int id;
    private final String location;
    private final String description;
    private final LocalDate date;
    private final int mothersReached;
    private final int childrenReached;
    private final String healthWorker;

    public OutreachActivity(int id, String location, String description, LocalDate date,
                          int mothersReached, int childrenReached, String healthWorker) {
        this.id = id;
        this.location = location;
        this.description = description;
        this.date = date;
        this.mothersReached = mothersReached;
        this.childrenReached = childrenReached;
        this.healthWorker = healthWorker;
    }

    public int getId() {
        return id;
    }

    public String getLocation() {
        return location;
    }

    public String getDescription() {
        return description;
    }

    public LocalDate getDate() {
        return date;
    }

    public int getMothersReached() {
        return mothersReached;
    }

    public int getChildrenReached() {
        return childrenReached;
    }

    public String getHealthWorker() {
        return healthWorker;
    }

    @Override
    public String toString() {
        return String.format(
            "ID: %d | Location: %s | Date: %s | Mothers: %d | Children: %d | Worker: %s | Description: %s",
            id, location, date, mothersReached, childrenReached, healthWorker, description
        );
    }
}
```
