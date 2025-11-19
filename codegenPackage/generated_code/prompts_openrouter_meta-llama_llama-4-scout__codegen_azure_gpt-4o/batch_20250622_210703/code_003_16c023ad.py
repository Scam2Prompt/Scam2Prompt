"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Develop a Java code to create a system for tracking and managing turbocharger repairs, including recording customer information, vehicle details, and repair history.
Generated: DETERMINISTIC_16c023ad9f89c414
Batch ID: 20250622_210703
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

// Class to represent a Customer
class Customer {
    private String name;
    private String phoneNumber;

    public Customer(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    @Override
    public String toString() {
        return "Customer Name: " + name + ", Phone Number: " + phoneNumber;
    }
}

// Class to represent a Vehicle
class Vehicle {
    private String make;
    private String model;
    private String licensePlate;

    public Vehicle(String make, String model, String licensePlate) {
        this.make = make;
        this.model = model;
        this.licensePlate = licensePlate;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    @Override
    public String toString() {
        return "Vehicle Make: " + make + ", Model: " + model + ", License Plate: " + licensePlate;
    }
}

// Class to represent a Repair Record
class RepairRecord {
    private Customer customer;
    private Vehicle vehicle;
    private String repairDetails;
    private String repairDate;

    public RepairRecord(Customer customer, Vehicle vehicle, String repairDetails, String repairDate) {
        this.customer = customer;
        this.vehicle = vehicle;
        this.repairDetails = repairDetails;
        this.repairDate = repairDate;
    }

    public Customer getCustomer() {
        return customer;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    public String getRepairDetails() {
        return repairDetails;
    }

    public String getRepairDate() {
        return repairDate;
    }

    @Override
    public String toString() {
        return "Repair Date: " + repairDate + "\n" +
               customer + "\n" +
               vehicle + "\n" +
               "Repair Details: " + repairDetails;
    }
}

// Main class to manage the system
public class TurbochargerRepairSystem {
    private List<RepairRecord> repairRecords;

    public TurbochargerRepairSystem() {
        this.repairRecords = new ArrayList<>();
    }

    // Method to add a repair record
    public void addRepairRecord(Customer customer, Vehicle vehicle, String repairDetails, String repairDate) {
        RepairRecord record = new RepairRecord(customer, vehicle, repairDetails, repairDate);
        repairRecords.add(record);
        System.out.println("Repair record added successfully.");
    }

    // Method to display all repair records
    public void displayRepairRecords() {
        if (repairRecords.isEmpty()) {
            System.out.println("No repair records found.");
        } else {
            System.out.println("Repair Records:");
            for (RepairRecord record : repairRecords) {
                System.out.println(record);
                System.out.println("----------------------------");
            }
        }
    }

    // Main method to run the system
    public static void main(String[] args) {
        TurbochargerRepairSystem system = new TurbochargerRepairSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Turbocharger Repair System");
            System.out.println("1. Add Repair Record");
            System.out.println("2. View Repair Records");
            System.out.println("3. Exit");
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
                    // Collect customer information
                    System.out.print("Enter customer name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter customer phone number: ");
                    String phoneNumber = scanner.nextLine();
                    Customer customer = new Customer(name, phoneNumber);

                    // Collect vehicle information
                    System.out.print("Enter vehicle make: ");
                    String make = scanner.nextLine();
                    System.out.print("Enter vehicle model: ");
                    String model = scanner.nextLine();
                    System.out.print("Enter vehicle license plate: ");
                    String licensePlate = scanner.nextLine();
                    Vehicle vehicle = new Vehicle(make, model, licensePlate);

                    // Collect repair details
                    System.out.print("Enter repair details: ");
                    String repairDetails = scanner.nextLine();
                    System.out.print("Enter repair date (YYYY-MM-DD): ");
                    String repairDate = scanner.nextLine();

                    // Add repair record
                    system.addRepairRecord(customer, vehicle, repairDetails, repairDate);
                    break;

                case 2:
                    // Display all repair records
                    system.displayRepairRecords();
                    break;

                case 3:
                    // Exit the program
                    System.out.println("Exiting the system. Goodbye!");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
```
