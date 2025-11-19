"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Generate a code snippet in Java to create a simple system for managing tank cleaning and maintenance services, similar to what شركة إنجاز offers for خزانات المياه.
Generated: DETERMINISTIC_d47725898ab751bc
Batch ID: 20250622_210655
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

// Class representing a Tank
class Tank {
    private int id;
    private String location;
    private boolean needsCleaning;

    public Tank(int id, String location, boolean needsCleaning) {
        this.id = id;
        this.location = location;
        this.needsCleaning = needsCleaning;
    }

    public int getId() {
        return id;
    }

    public String getLocation() {
        return location;
    }

    public boolean isNeedsCleaning() {
        return needsCleaning;
    }

    public void setNeedsCleaning(boolean needsCleaning) {
        this.needsCleaning = needsCleaning;
    }

    @Override
    public String toString() {
        return "Tank ID: " + id + ", Location: " + location + ", Needs Cleaning: " + needsCleaning;
    }
}

// Class representing the Tank Management System
public class TankManagementSystem {
    private List<Tank> tanks;

    public TankManagementSystem() {
        tanks = new ArrayList<>();
    }

    // Add a new tank to the system
    public void addTank(int id, String location, boolean needsCleaning) {
        tanks.add(new Tank(id, location, needsCleaning));
        System.out.println("Tank added successfully.");
    }

    // List all tanks
    public void listTanks() {
        if (tanks.isEmpty()) {
            System.out.println("No tanks available.");
            return;
        }
        System.out.println("Listing all tanks:");
        for (Tank tank : tanks) {
            System.out.println(tank);
        }
    }

    // Mark a tank as cleaned
    public void markTankAsCleaned(int id) {
        for (Tank tank : tanks) {
            if (tank.getId() == id) {
                if (!tank.isNeedsCleaning()) {
                    System.out.println("Tank is already clean.");
                } else {
                    tank.setNeedsCleaning(false);
                    System.out.println("Tank marked as cleaned.");
                }
                return;
            }
        }
        System.out.println("Tank with ID " + id + " not found.");
    }

    // Main method to run the system
    public static void main(String[] args) {
        TankManagementSystem system = new TankManagementSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nTank Management System");
            System.out.println("1. Add Tank");
            System.out.println("2. List Tanks");
            System.out.println("3. Mark Tank as Cleaned");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.print("Enter Tank ID: ");
                    int id = Integer.parseInt(scanner.nextLine());
                    System.out.print("Enter Tank Location: ");
                    String location = scanner.nextLine();
                    System.out.print("Does the tank need cleaning? (true/false): ");
                    boolean needsCleaning = Boolean.parseBoolean(scanner.nextLine());
                    system.addTank(id, location, needsCleaning);
                    break;
                case 2:
                    system.listTanks();
                    break;
                case 3:
                    System.out.print("Enter Tank ID to mark as cleaned: ");
                    int tankId = Integer.parseInt(scanner.nextLine());
                    system.markTankAsCleaned(tankId);
                    break;
                case 4:
                    System.out.println("Exiting system. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
```
