"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Create a Java program to handle event planning for weddings at White Pines Lodge, including features like ceremony settings and reception management.
Generated: DETERMINISTIC_617828b6ce61c48f
Batch ID: 20250622_204559
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
 * Represents a wedding event at White Pines Lodge.
 */
class WeddingEvent {
    private String coupleName;
    private String ceremonySetting;
    private List<String> receptionDetails;

    public WeddingEvent(String coupleName) {
        this.coupleName = coupleName;
        this.ceremonySetting = "";
        this.receptionDetails = new ArrayList<>();
    }

    public String getCoupleName() {
        return coupleName;
    }

    public String getCeremonySetting() {
        return ceremonySetting;
    }

    public void setCeremonySetting(String ceremonySetting) {
        this.ceremonySetting = ceremonySetting;
    }

    public List<String> getReceptionDetails() {
        return receptionDetails;
    }

    public void addReceptionDetail(String detail) {
        receptionDetails.add(detail);
    }

    @Override
    public String toString() {
        return "WeddingEvent{" +
                "coupleName='" + coupleName + '\'' +
                ", ceremonySetting='" + ceremonySetting + '\'' +
                ", receptionDetails=" + receptionDetails +
                '}';
    }
}

/**
 * Manages the wedding events at White Pines Lodge.
 */
class WeddingPlanner {
    private List<WeddingEvent> events;

    public WeddingPlanner() {
        events = new ArrayList<>();
    }

    public void addEvent(WeddingEvent event) {
        events.add(event);
    }

    public void displayEvents() {
        if (events.isEmpty()) {
            System.out.println("No wedding events scheduled.");
            return;
        }
        for (WeddingEvent event : events) {
            System.out.println(event);
        }
    }
}

/**
 * Main class to run the wedding planning application.
 */
public class WeddingPlanningApp {
    private static final Scanner scanner = new Scanner(System.in);
    private static final WeddingPlanner weddingPlanner = new WeddingPlanner();

    public static void main(String[] args) {
        while (true) {
            System.out.println("Welcome to White Pines Lodge Wedding Planner!");
            System.out.println("1. Add Wedding Event");
            System.out.println("2. Display All Events");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");

            int choice = getUserChoice();
            switch (choice) {
                case 1:
                    addWeddingEvent();
                    break;
                case 2:
                    weddingPlanner.displayEvents();
                    break;
                case 3:
                    System.out.println("Exiting the application. Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static int getUserChoice() {
        while (true) {
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static void addWeddingEvent() {
        System.out.print("Enter couple's name: ");
        String coupleName = scanner.nextLine();

        WeddingEvent event = new WeddingEvent(coupleName);

        System.out.print("Enter ceremony setting: ");
        String ceremonySetting = scanner.nextLine();
        event.setCeremonySetting(ceremonySetting);

        System.out.print("Enter reception details (type 'done' to finish): ");
        while (true) {
            String detail = scanner.nextLine();
            if (detail.equalsIgnoreCase("done")) {
                break;
            }
            event.addReceptionDetail(detail);
        }

        weddingPlanner.addEvent(event);
        System.out.println("Wedding event added successfully!");
    }
}
```
