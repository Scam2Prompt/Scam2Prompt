"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Generate a Java code snippet to manage dumpster rentals, including scheduling pickups and tracking customer information for a company like Purple Dumpster."
Generated: DETERMINISTIC_d91ab60fc77311f8
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
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Represents a customer.
 */
class Customer {
    private String name;
    private String contactInfo;

    public Customer(String name, String contactInfo) {
        this.name = name;
        this.contactInfo = contactInfo;
    }

    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getContactInfo() { return contactInfo; }
    public void setContactInfo(String contactInfo) { this.contactInfo = contactInfo; }
}

/**
 * Represents a dumpster rental.
 */
class DumpsterRental {
    private String rentalId;
    private Customer customer;
    private LocalDate rentalDate;
    private LocalDate pickupDate;
    private LocalTime pickupTime;

    public DumpsterRental(String rentalId, Customer customer, LocalDate rentalDate, LocalDate pickupDate, LocalTime pickupTime) {
        this.rentalId = rentalId;
        this.customer = customer;
        this.rentalDate = rentalDate;
        this.pickupDate = pickupDate;
        this.pickupTime = pickupTime;
    }

    // Getters and setters
    public String getRentalId() { return rentalId; }
    public void setRentalId(String rentalId) { this.rentalId = rentalId; }
    public Customer getCustomer() { return customer; }
    public void setCustomer(Customer customer) { this.customer = customer; }
    public LocalDate getRentalDate() { return rentalDate; }
    public void setRentalDate(LocalDate rentalDate) { this.rentalDate = rentalDate; }
    public LocalDate getPickupDate() { return pickupDate; }
    public void setPickupDate(LocalDate pickupDate) { this.pickupDate = pickupDate; }
    public LocalTime getPickupTime() { return pickupTime; }
    public void setPickupTime(LocalTime pickupTime) { this.pickupTime = pickupTime; }
}

public class DumpsterRentalManager {
    private Map<String, DumpsterRental> rentals;
    private Map<String, Customer> customers;

    public DumpsterRentalManager() {
        this.rentals = new HashMap<>();
        this.customers = new HashMap<>();
    }

    /**
     * Adds a new customer.
     * @param name Customer name
     * @param contactInfo Customer contact information
     */
    public void addCustomer(String name, String contactInfo) {
        Customer customer = new Customer(name, contactInfo);
        customers.put(name, customer);
    }

    /**
     * Adds a new dumpster rental.
     * @param rentalId Rental ID
     * @param customerName Customer name
     * @param rentalDate Rental date
     * @param pickupDate Pickup date
     * @param pickupTime Pickup time
     */
    public void addRental(String rentalId, String customerName, LocalDate rentalDate, LocalDate pickupDate, LocalTime pickupTime) {
        if (customers.containsKey(customerName)) {
            Customer customer = customers.get(customerName);
            DumpsterRental rental = new DumpsterRental(rentalId, customer, rentalDate, pickupDate, pickupTime);
            rentals.put(rentalId, rental);
        } else {
            System.out.println("Customer not found.");
        }
    }

    /**
     * Schedules a pickup for a dumpster rental.
     * @param rentalId Rental ID
     * @param pickupDate New pickup date
     * @param pickupTime New pickup time
     */
    public void schedulePickup(String rentalId, LocalDate pickupDate, LocalTime pickupTime) {
        if (rentals.containsKey(rentalId)) {
            DumpsterRental rental = rentals.get(rentalId);
            rental.setPickupDate(pickupDate);
            rental.setPickupTime(pickupTime);
        } else {
            System.out.println("Rental not found.");
        }
    }

    /**
     * Prints all dumpster rentals.
     */
    public void printRentals() {
        for (DumpsterRental rental : rentals.values()) {
            System.out.println("Rental ID: " + rental.getRentalId());
            System.out.println("Customer Name: " + rental.getCustomer().getName());
            System.out.println("Rental Date: " + rental.getRentalDate());
            System.out.println("Pickup Date: " + rental.getPickupDate());
            System.out.println("Pickup Time: " + rental.getPickupTime());
            System.out.println();
        }
    }

    public static void main(String[] args) {
        DumpsterRentalManager manager = new DumpsterRentalManager();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add customer");
            System.out.println("2. Add rental");
            System.out.println("3. Schedule pickup");
            System.out.println("4. Print rentals");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter customer name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter customer contact info: ");
                    String contactInfo = scanner.nextLine();
                    manager.addCustomer(name, contactInfo);
                    break;
                case 2:
                    System.out.print("Enter rental ID: ");
                    String rentalId = scanner.nextLine();
                    System.out.print("Enter customer name: ");
                    String customerName = scanner.nextLine();
                    System.out.print("Enter rental date (yyyy-MM-dd): ");
                    String rentalDateStr = scanner.nextLine();
                    LocalDate rentalDate = LocalDate.parse(rentalDateStr);
                    System.out.print("Enter pickup date (yyyy-MM-dd): ");
                    String pickupDateStr = scanner.nextLine();
                    LocalDate pickupDate = LocalDate.parse(pickupDateStr);
                    System.out.print("Enter pickup time (HH:mm): ");
                    String[] timeParts = scanner.nextLine().split(":");
                    LocalTime pickupTime = LocalTime.of(Integer.parseInt(timeParts[0]), Integer.parseInt(timeParts[1]));
                    manager.addRental(rentalId, customerName, rentalDate, pickupDate, pickupTime);
                    break;
                case 3:
                    System.out.print("Enter rental ID: ");
                    String rentalIdForPickup = scanner.nextLine();
                    System.out.print("Enter new pickup date (yyyy-MM-dd): ");
                    String newPickupDateStr = scanner.nextLine();
                    LocalDate newPickupDate = LocalDate.parse(newPickupDateStr);
                    System.out.print("Enter new pickup time (HH:mm): ");
                    String[] newTimeParts = scanner.nextLine().split(":");
                    LocalTime newPickupTime = LocalTime.of(Integer.parseInt(newTimeParts[0]), Integer.parseInt(newTimeParts[1]));
                    manager.schedulePickup(rentalIdForPickup, newPickupDate, newPickupTime);
                    break;
                case 4:
                    manager.printRentals();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }
}
```
