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
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents a tank cleaning and maintenance service.
 */
class TankService {
    private String serviceType;
    private LocalDate serviceDate;

    public TankService(String serviceType, LocalDate serviceDate) {
        this.serviceType = serviceType;
        this.serviceDate = serviceDate;
    }

    public String getServiceType() {
        return serviceType;
    }

    public LocalDate getServiceDate() {
        return serviceDate;
    }
}

/**
 * Represents a water tank.
 */
class WaterTank {
    private String tankId;
    private List<TankService> services;

    public WaterTank(String tankId) {
        this.tankId = tankId;
        this.services = new ArrayList<>();
    }

    public String getTankId() {
        return tankId;
    }

    public List<TankService> getServices() {
        return services;
    }

    public void addService(TankService service) {
        services.add(service);
    }
}

/**
 * Manages tank cleaning and maintenance services.
 */
public class TankMaintenanceSystem {
    private List<WaterTank> tanks;
    private Scanner scanner;

    public TankMaintenanceSystem() {
        this.tanks = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Adds a new water tank to the system.
     */
    public void addTank() {
        System.out.print("Enter tank ID: ");
        String tankId = scanner.nextLine();
        WaterTank tank = new WaterTank(tankId);
        tanks.add(tank);
        System.out.println("Tank added successfully!");
    }

    /**
     * Adds a new service to a water tank.
     */
    public void addService() {
        if (tanks.isEmpty()) {
            System.out.println("No tanks available. Please add a tank first.");
            return;
        }

        System.out.println("Available tanks:");
        for (int i = 0; i < tanks.size(); i++) {
            System.out.println((i + 1) + ". Tank ID: " + tanks.get(i).getTankId());
        }

        System.out.print("Enter the tank number: ");
        int tankNumber = Integer.parseInt(scanner.nextLine()) - 1;

        if (tankNumber < 0 || tankNumber >= tanks.size()) {
            System.out.println("Invalid tank number.");
            return;
        }

        System.out.print("Enter service type: ");
        String serviceType = scanner.nextLine();

        System.out.print("Enter service date (yyyy-MM-dd): ");
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate serviceDate = LocalDate.parse(scanner.nextLine(), formatter);

        TankService service = new TankService(serviceType, serviceDate);
        tanks.get(tankNumber).addService(service);
        System.out.println("Service added successfully!");
    }

    /**
     * Displays all tanks and their services.
     */
    public void displayTanks() {
        if (tanks.isEmpty()) {
            System.out.println("No tanks available.");
            return;
        }

        for (WaterTank tank : tanks) {
            System.out.println("Tank ID: " + tank.getTankId());
            for (TankService service : tank.getServices()) {
                System.out.println("Service Type: " + service.getServiceType() + ", Service Date: " + service.getServiceDate());
            }
            System.out.println();
        }
    }

    /**
     * Runs the tank maintenance system.
     */
    public void run() {
        while (true) {
            System.out.println("Tank Maintenance System");
            System.out.println("1. Add Tank");
            System.out.println("2. Add Service");
            System.out.println("3. Display Tanks");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            int choice = Integer.parseInt(scanner.nextLine());

            switch (choice) {
                case 1:
                    addTank();
                    break;
                case 2:
                    addService();
                    break;
                case 3:
                    displayTanks();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    public static void main(String[] args) {
        TankMaintenanceSystem system = new TankMaintenanceSystem();
        system.run();
    }
}
```
