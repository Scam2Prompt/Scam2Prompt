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
/**
 * This program handles event planning for weddings at White Pines Lodge.
 * It includes features like ceremony settings and reception management.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Enum for ceremony settings
enum CeremonySetting {
    OUTDOOR,
    INDOOR,
    BEACH
}

// Class for Ceremony
class Ceremony {
    private CeremonySetting setting;
    private int guestCount;
    private String ceremonyTime;

    public Ceremony(CeremonySetting setting, int guestCount, String ceremonyTime) {
        this.setting = setting;
        this.guestCount = guestCount;
        this.ceremonyTime = ceremonyTime;
    }

    // Getters and setters
    public CeremonySetting getSetting() { return setting; }
    public int getGuestCount() { return guestCount; }
    public String getCeremonyTime() { return ceremonyTime; }
}

// Class for Reception
class Reception {
    private int guestCount;
    private String receptionTime;
    private String menu;

    public Reception(int guestCount, String receptionTime, String menu) {
        this.guestCount = guestCount;
        this.receptionTime = receptionTime;
        this.menu = menu;
    }

    // Getters and setters
    public int getGuestCount() { return guestCount; }
    public String getReceptionTime() { return receptionTime; }
    public String getMenu() { return menu; }
}

// Class for WeddingEvent
class WeddingEvent {
    private Ceremony ceremony;
    private Reception reception;

    public WeddingEvent(Ceremony ceremony, Reception reception) {
        this.ceremony = ceremony;
        this.reception = reception;
    }

    // Getters
    public Ceremony getCeremony() { return ceremony; }
    public Reception getReception() { return reception; }
}

public class WeddingPlanner {
    private List<WeddingEvent> events;
    private Scanner scanner;

    public WeddingPlanner() {
        this.events = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    // Method to create a new ceremony
    public Ceremony createCeremony() {
        System.out.println("Enter ceremony setting (OUTDOOR, INDOOR, BEACH):");
        String settingInput = scanner.nextLine();
        CeremonySetting setting = CeremonySetting.valueOf(settingInput.toUpperCase());

        System.out.println("Enter guest count:");
        int guestCount = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        System.out.println("Enter ceremony time:");
        String ceremonyTime = scanner.nextLine();

        return new Ceremony(setting, guestCount, ceremonyTime);
    }

    // Method to create a new reception
    public Reception createReception() {
        System.out.println("Enter guest count:");
        int guestCount = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        System.out.println("Enter reception time:");
        String receptionTime = scanner.nextLine();

        System.out.println("Enter menu:");
        String menu = scanner.nextLine();

        return new Reception(guestCount, receptionTime, menu);
    }

    // Method to plan a wedding event
    public void planWeddingEvent() {
        Ceremony ceremony = createCeremony();
        Reception reception = createReception();

        WeddingEvent event = new WeddingEvent(ceremony, reception);
        events.add(event);

        System.out.println("Wedding event planned successfully!");
        System.out.println("Ceremony Setting: " + ceremony.getSetting());
        System.out.println("Ceremony Guest Count: " + ceremony.getGuestCount());
        System.out.println("Ceremony Time: " + ceremony.getCeremonyTime());
        System.out.println("Reception Guest Count: " + reception.getGuestCount());
        System.out.println("Reception Time: " + reception.getReceptionTime());
        System.out.println("Reception Menu: " + reception.getMenu());
    }

    // Method to display all wedding events
    public void displayEvents() {
        if (events.isEmpty()) {
            System.out.println("No wedding events planned.");
        } else {
            for (int i = 0; i < events.size(); i++) {
                WeddingEvent event = events.get(i);
                System.out.println("Event " + (i + 1));
                System.out.println("Ceremony Setting: " + event.getCeremony().getSetting());
                System.out.println("Ceremony Guest Count: " + event.getCeremony().getGuestCount());
                System.out.println("Ceremony Time: " + event.getCeremony().getCeremonyTime());
                System.out.println("Reception Guest Count: " + event.getReception().getGuestCount());
                System.out.println("Reception Time: " + event.getReception().getReceptionTime());
                System.out.println("Reception Menu: " + event.getReception().getMenu());
                System.out.println();
            }
        }
    }

    public void run() {
        while (true) {
            System.out.println("Wedding Planner");
            System.out.println("1. Plan a wedding event");
            System.out.println("2. Display all wedding events");
            System.out.println("3. Exit");
            System.out.println("Enter your choice:");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (choice) {
                case 1:
                    planWeddingEvent();
                    break;
                case 2:
                    displayEvents();
                    break;
                case 3:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    public static void main(String[] args) {
        WeddingPlanner planner = new WeddingPlanner();
        planner.run();
    }
}
```
