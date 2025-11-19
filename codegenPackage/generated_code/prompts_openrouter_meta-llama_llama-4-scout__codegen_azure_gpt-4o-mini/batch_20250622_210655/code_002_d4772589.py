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

// Class representing a tank cleaning and maintenance service
class TankService {
    private String serviceId;
    private String customerName;
    private String tankType;
    private String serviceDate;
    private String status;

    // Constructor to initialize the service details
    public TankService(String serviceId, String customerName, String tankType, String serviceDate) {
        this.serviceId = serviceId;
        this.customerName = customerName;
        this.tankType = tankType;
        this.serviceDate = serviceDate;
        this.status = "Scheduled"; // Default status
    }

    // Getters and Setters
    public String getServiceId() {
        return serviceId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public String getTankType() {
        return tankType;
    }

    public String getServiceDate() {
        return serviceDate;
    }

    public String getStatus() {
        return status;
    }

    public void completeService() {
        this.status = "Completed"; // Update status to completed
    }

    @Override
    public String toString() {
        return "Service ID: " + serviceId + ", Customer: " + customerName + ", Tank Type: " + tankType +
               ", Service Date: " + serviceDate + ", Status: " + status;
    }
}

// Main class to manage tank services
public class TankCleaningServiceManager {
    private List<TankService> services; // List to store tank services

    // Constructor to initialize the service manager
    public TankCleaningServiceManager() {
        services = new ArrayList<>();
    }

    // Method to add a new service
    public void addService(String serviceId, String customerName, String tankType, String serviceDate) {
        TankService newService = new TankService(serviceId, customerName, tankType, serviceDate);
        services.add(newService);
        System.out.println("Service added successfully: " + newService);
    }

    // Method to complete a service by service ID
    public void completeService(String serviceId) {
        for (TankService service : services) {
            if (service.getServiceId().equals(serviceId)) {
                service.completeService();
                System.out.println("Service completed: " + service);
                return;
            }
        }
        System.out.println("Service ID not found: " + serviceId);
    }

    // Method to display all services
    public void displayServices() {
        if (services.isEmpty()) {
            System.out.println("No services available.");
            return;
        }
        System.out.println("Current Tank Services:");
        for (TankService service : services) {
            System.out.println(service);
        }
    }

    // Main method to run the service manager
    public static void main(String[] args) {
        TankCleaningServiceManager manager = new TankCleaningServiceManager();
        Scanner scanner = new Scanner(System.in);
        String command;

        // Command loop for user interaction
        do {
            System.out.println("Enter command (add, complete, display, exit): ");
            command = scanner.nextLine().toLowerCase();

            switch (command) {
                case "add":
                    System.out.print("Enter Service ID: ");
                    String serviceId = scanner.nextLine();
                    System.out.print("Enter Customer Name: ");
                    String customerName = scanner.nextLine();
                    System.out.print("Enter Tank Type: ");
                    String tankType = scanner.nextLine();
                    System.out.print("Enter Service Date (YYYY-MM-DD): ");
                    String serviceDate = scanner.nextLine();
                    manager.addService(serviceId, customerName, tankType, serviceDate);
                    break;

                case "complete":
                    System.out.print("Enter Service ID to complete: ");
                    String completeServiceId = scanner.nextLine();
                    manager.completeService(completeServiceId);
                    break;

                case "display":
                    manager.displayServices();
                    break;

                case "exit":
                    System.out.println("Exiting the service manager.");
                    break;

                default:
                    System.out.println("Invalid command. Please try again.");
            }
        } while (!command.equals("exit"));

        scanner.close(); // Close the scanner resource
    }
}
```
