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
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Turbocharger Repair Management System
 * Tracks customer information, vehicle details, and repair history
 */
public class TurbochargerRepairSystem {
    private static Scanner scanner = new Scanner(System.in);
    private static Map<String, Customer> customers = new HashMap<>();
    private static Map<String, Vehicle> vehicles = new HashMap<>();
    private static List<RepairRecord> repairRecords = new ArrayList<>();

    public static void main(String[] args) {
        boolean running = true;
        while (running) {
            displayMenu();
            int choice = getIntInput("Enter your choice: ");
            
            switch (choice) {
                case 1:
                    addCustomer();
                    break;
                case 2:
                    addVehicle();
                    break;
                case 3:
                    addRepairRecord();
                    break;
                case 4:
                    viewCustomerDetails();
                    break;
                case 5:
                    viewVehicleDetails();
                    break;
                case 6:
                    viewRepairHistory();
                    break;
                case 7:
                    running = false;
                    System.out.println("Exiting system...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }

    private static void displayMenu() {
        System.out.println("\nTurbocharger Repair Management System");
        System.out.println("1. Add New Customer");
        System.out.println("2. Add New Vehicle");
        System.out.println("3. Add Repair Record");
        System.out.println("4. View Customer Details");
        System.out.println("5. View Vehicle Details");
        System.out.println("6. View Repair History");
        System.out.println("7. Exit");
    }

    private static void addCustomer() {
        System.out.println("\nAdd New Customer");
        String customerId = getStringInput("Customer ID: ");
        if (customers.containsKey(customerId)) {
            System.out.println("Customer ID already exists.");
            return;
        }

        String name = getStringInput("Name: ");
        String phone = getStringInput("Phone: ");
        String email = getStringInput("Email: ");
        String address = getStringInput("Address: ");

        Customer customer = new Customer(customerId, name, phone, email, address);
        customers.put(customerId, customer);
        System.out.println("Customer added successfully.");
    }

    private static void addVehicle() {
        System.out.println("\nAdd New Vehicle");
        String vin = getStringInput("VIN: ");
        if (vehicles.containsKey(vin)) {
            System.out.println("Vehicle already exists.");
            return;
        }

        String customerId = getStringInput("Customer ID: ");
        if (!customers.containsKey(customerId)) {
            System.out.println("Customer not found.");
            return;
        }

        String make = getStringInput("Make: ");
        String model = getStringInput("Model: ");
        int year = getIntInput("Year: ");
        String engineType = getStringInput("Engine Type: ");

        Vehicle vehicle = new Vehicle(vin, customerId, make, model, year, engineType);
        vehicles.put(vin, vehicle);
        System.out.println("Vehicle added successfully.");
    }

    private static void addRepairRecord() {
        System.out.println("\nAdd Repair Record");
        String vin = getStringInput("VIN: ");
        if (!vehicles.containsKey(vin)) {
            System.out.println("Vehicle not found.");
            return;
        }

        String repairId = getStringInput("Repair ID: ");
        Date repairDate = new Date(); // Current date
        String description = getStringInput("Description: ");
        double cost = getDoubleInput("Cost: ");
        String technician = getStringInput("Technician: ");
        String status = getStringInput("Status (Completed/In Progress): ");

        RepairRecord record = new RepairRecord(repairId, vin, repairDate, description, cost, technician, status);
        repairRecords.add(record);
        System.out.println("Repair record added successfully.");
    }

    private static void viewCustomerDetails() {
        String customerId = getStringInput("Enter Customer ID: ");
        Customer customer = customers.get(customerId);
        if (customer == null) {
            System.out.println("Customer not found.");
            return;
        }

        System.out.println("\nCustomer Details:");
        System.out.println(customer);
    }

    private static void viewVehicleDetails() {
        String vin = getStringInput("Enter VIN: ");
        Vehicle vehicle = vehicles.get(vin);
        if (vehicle == null) {
            System.out.println("Vehicle not found.");
            return;
        }

        System.out.println("\nVehicle Details:");
        System.out.println(vehicle);
    }

    private static void viewRepairHistory() {
        String vin = getStringInput("Enter VIN: ");
        if (!vehicles.containsKey(vin)) {
            System.out.println("Vehicle not found.");
            return;
        }

        System.out.println("\nRepair History for VIN: " + vin);
        boolean found = false;
        for (RepairRecord record : repairRecords) {
            if (record.getVin().equals(vin)) {
                System.out.println(record);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No repair records found for this vehicle.");
        }
    }

    private static String getStringInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine();
    }

    private static int getIntInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static double getDoubleInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a decimal number.");
            }
        }
    }
}

class Customer {
    private String customerId;
    private String name;
    private String phone;
    private String email;
    private String address;

    public Customer(String customerId, String name, String phone, String email, String address) {
        this.customerId = customerId;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.address = address;
    }

    public String getCustomerId() {
        return customerId;
    }

    @Override
    public String toString() {
        return "Customer ID: " + customerId + "\n" +
               "Name: " + name + "\n" +
               "Phone: " + phone + "\n" +
               "Email: " + email + "\n" +
               "Address: " + address;
    }
}

class Vehicle {
    private String vin;
    private String customerId;
    private String make;
    private String model;
    private int year;
    private String engineType;

    public Vehicle(String vin, String customerId, String make, String model, int year, String engineType) {
        this.vin = vin;
        this.customerId = customerId;
        this.make = make;
        this.model = model;
        this.year = year;
        this.engineType = engineType;
    }

    public String getVin() {
        return vin;
    }

    public String getCustomerId() {
        return customerId;
    }

    @Override
    public String toString() {
        return "VIN: " + vin + "\n" +
               "Customer ID: " + customerId + "\n" +
               "Make: " + make + "\n" +
               "Model: " + model + "\n" +
               "Year: " + year + "\n" +
               "Engine Type: " + engineType;
    }
}

class RepairRecord {
    private String repairId;
    private String vin;
    private Date repairDate;
    private String description;
    private double cost;
    private String technician;
    private String status;

    public RepairRecord(String repairId, String vin, Date repairDate, String description, double cost, String technician, String status) {
        this.repairId = repairId;
        this.vin = vin;
        this.repairDate = repairDate;
        this.description = description;
        this.cost = cost;
        this.technician = technician;
        this.status = status;
    }

    public String getVin() {
        return vin;
    }

    @Override
    public String toString() {
        return "Repair ID: " + repairId + "\n" +
               "VIN: " + vin + "\n" +
               "Date: " + repairDate + "\n" +
               "Description: " + description + "\n" +
               "Cost: $" + String.format("%.2f", cost) + "\n" +
               "Technician: " + technician + "\n" +
               "Status: " + status + "\n";
    }
}
```
