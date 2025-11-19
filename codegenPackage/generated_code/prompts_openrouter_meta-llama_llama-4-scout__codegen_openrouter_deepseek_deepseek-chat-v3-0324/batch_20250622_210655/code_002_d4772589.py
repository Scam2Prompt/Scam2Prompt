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
import java.util.Date;
import java.util.List;
import java.util.Scanner;

/**
 * Tank Maintenance Management System
 * Manages cleaning and maintenance services for water tanks
 */
public class TankMaintenanceSystem {
    private List<Tank> tanks;
    private List<MaintenanceRecord> maintenanceRecords;
    private Scanner scanner;

    public TankMaintenanceSystem() {
        this.tanks = new ArrayList<>();
        this.maintenanceRecords = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    public static void main(String[] args) {
        TankMaintenanceSystem system = new TankMaintenanceSystem();
        system.run();
    }

    public void run() {
        while (true) {
            displayMenu();
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    addTank();
                    break;
                case 2:
                    scheduleMaintenance();
                    break;
                case 3:
                    viewMaintenanceHistory();
                    break;
                case 4:
                    markMaintenanceCompleted();
                    break;
                case 5:
                    listAllTanks();
                    break;
                case 6:
                    System.out.println("Exiting system...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private void displayMenu() {
        System.out.println("\nTank Maintenance Management System");
        System.out.println("1. Add New Tank");
        System.out.println("2. Schedule Maintenance");
        System.out.println("3. View Maintenance History");
        System.out.println("4. Mark Maintenance as Completed");
        System.out.println("5. List All Tanks");
        System.out.println("6. Exit");
        System.out.print("Enter your choice: ");
    }

    private void addTank() {
        System.out.println("\nAdd New Tank");
        System.out.print("Enter tank ID: ");
        String id = scanner.nextLine();

        System.out.print("Enter tank location: ");
        String location = scanner.nextLine();

        System.out.print("Enter tank capacity (liters): ");
        double capacity = scanner.nextDouble();
        scanner.nextLine(); // Consume newline

        System.out.print("Enter tank type (UNDERGROUND/OVERHEAD): ");
        String typeStr = scanner.nextLine().toUpperCase();
        TankType type;
        try {
            type = TankType.valueOf(typeStr);
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid tank type. Defaulting to OVERHEAD.");
            type = TankType.OVERHEAD;
        }

        Tank tank = new Tank(id, location, capacity, type);
        tanks.add(tank);
        System.out.println("Tank added successfully!");
    }

    private void scheduleMaintenance() {
        if (tanks.isEmpty()) {
            System.out.println("No tanks available. Please add a tank first.");
            return;
        }

        System.out.println("\nSchedule Maintenance");
        listAllTanks();

        System.out.print("Enter tank ID for maintenance: ");
        String tankId = scanner.nextLine();

        Tank tank = findTankById(tankId);
        if (tank == null) {
            System.out.println("Tank not found.");
            return;
        }

        System.out.print("Enter scheduled date (YYYY-MM-DD): ");
        String dateStr = scanner.nextLine();
        Date scheduledDate = parseDate(dateStr);

        if (scheduledDate == null) {
            System.out.println("Invalid date format. Use YYYY-MM-DD.");
            return;
        }

        MaintenanceRecord record = new MaintenanceRecord(tank, scheduledDate);
        maintenanceRecords.add(record);
        System.out.println("Maintenance scheduled successfully!");
    }

    private void viewMaintenanceHistory() {
        if (maintenanceRecords.isEmpty()) {
            System.out.println("No maintenance records found.");
            return;
        }

        System.out.println("\nMaintenance History");
        for (MaintenanceRecord record : maintenanceRecords) {
            System.out.println(record);
        }
    }

    private void markMaintenanceCompleted() {
        if (maintenanceRecords.isEmpty()) {
            System.out.println("No maintenance records found.");
            return;
        }

        System.out.println("\nMark Maintenance as Completed");
        for (int i = 0; i < maintenanceRecords.size(); i++) {
            MaintenanceRecord record = maintenanceRecords.get(i);
            if (!record.isCompleted()) {
                System.out.println(i + ". " + record);
            }
        }

        System.out.print("Enter record number to mark as completed: ");
        int recordNumber = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        if (recordNumber < 0 || recordNumber >= maintenanceRecords.size()) {
            System.out.println("Invalid record number.");
            return;
        }

        MaintenanceRecord record = maintenanceRecords.get(recordNumber);
        if (record.isCompleted()) {
            System.out.println("This maintenance is already completed.");
            return;
        }

        record.setCompleted(true);
        record.setCompletionDate(new Date());
        System.out.println("Maintenance marked as completed.");
    }

    private void listAllTanks() {
        if (tanks.isEmpty()) {
            System.out.println("No tanks registered.");
            return;
        }

        System.out.println("\nList of All Tanks");
        for (Tank tank : tanks) {
            System.out.println(tank);
        }
    }

    private Tank findTankById(String id) {
        for (Tank tank : tanks) {
            if (tank.getId().equals(id)) {
                return tank;
            }
        }
        return null;
    }

    private Date parseDate(String dateStr) {
        try {
            return java.sql.Date.valueOf(dateStr);
        } catch (IllegalArgumentException e) {
            return null;
        }
    }
}

enum TankType {
    UNDERGROUND, OVERHEAD
}

class Tank {
    private String id;
    private String location;
    private double capacity; // in liters
    private TankType type;

    public Tank(String id, String location, double capacity, TankType type) {
        this.id = id;
        this.location = location;
        this.capacity = capacity;
        this.type = type;
    }

    public String getId() {
        return id;
    }

    public String getLocation() {
        return location;
    }

    public double getCapacity() {
        return capacity;
    }

    public TankType getType() {
        return type;
    }

    @Override
    public String toString() {
        return String.format("Tank ID: %s, Location: %s, Capacity: %.2fL, Type: %s",
                id, location, capacity, type);
    }
}

class MaintenanceRecord {
    private Tank tank;
    private Date scheduledDate;
    private Date completionDate;
    private boolean completed;

    public MaintenanceRecord(Tank tank, Date scheduledDate) {
        this.tank = tank;
        this.scheduledDate = scheduledDate;
        this.completed = false;
    }

    public Tank getTank() {
        return tank;
    }

    public Date getScheduledDate() {
        return scheduledDate;
    }

    public Date getCompletionDate() {
        return completionDate;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public void setCompletionDate(Date completionDate) {
        this.completionDate = completionDate;
    }

    @Override
    public String toString() {
        String status = completed ? "Completed" : "Pending";
        String completionInfo = completed ? 
            String.format(", Completed on: %s", completionDate) : "";
        return String.format("Tank: %s, Scheduled: %s, Status: %s%s",
                tank.getId(), scheduledDate, status, completionInfo);
    }
}
```
