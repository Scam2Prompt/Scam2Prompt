"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Develop a Java program to manage bookings and scheduling for armourer services, uniform hire, and prop rentals for a film production company.
Generated: DETERMINISTIC_054359a2514a22d5
Batch ID: 20250622_204920
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
import java.util.List;
import java.util.Scanner;

// Enum to represent service types
enum ServiceType {
    ARMOURER_SERVICES,
    UNIFORM_HIRE,
    PROP_RENTALS
}

// Class to represent a booking
class Booking {
    private String customerName;
    private ServiceType serviceType;
    private LocalDate bookingDate;
    private LocalDate serviceDate;

    public Booking(String customerName, ServiceType serviceType, LocalDate bookingDate, LocalDate serviceDate) {
        this.customerName = customerName;
        this.serviceType = serviceType;
        this.bookingDate = bookingDate;
        this.serviceDate = serviceDate;
    }

    public String getCustomerName() {
        return customerName;
    }

    public ServiceType getServiceType() {
        return serviceType;
    }

    public LocalDate getBookingDate() {
        return bookingDate;
    }

    public LocalDate getServiceDate() {
        return serviceDate;
    }

    @Override
    public String toString() {
        return "Booking{" +
                "customerName='" + customerName + '\'' +
                ", serviceType=" + serviceType +
                ", bookingDate=" + bookingDate +
                ", serviceDate=" + serviceDate +
                '}';
    }
}

// Class to manage bookings
class BookingManager {
    private List<Booking> bookings;

    public BookingManager() {
        bookings = new ArrayList<>();
    }

    // Add a new booking
    public void addBooking(String customerName, ServiceType serviceType, LocalDate bookingDate, LocalDate serviceDate) {
        if (serviceDate.isBefore(bookingDate)) {
            throw new IllegalArgumentException("Service date cannot be before booking date.");
        }
        Booking booking = new Booking(customerName, serviceType, bookingDate, serviceDate);
        bookings.add(booking);
        System.out.println("Booking added successfully.");
    }

    // View all bookings
    public void viewBookings() {
        if (bookings.isEmpty()) {
            System.out.println("No bookings available.");
        } else {
            for (Booking booking : bookings) {
                System.out.println(booking);
            }
        }
    }

    // Search bookings by customer name
    public void searchBookingsByCustomer(String customerName) {
        boolean found = false;
        for (Booking booking : bookings) {
            if (booking.getCustomerName().equalsIgnoreCase(customerName)) {
                System.out.println(booking);
                found = true;
            }
        }
        if (!found) {
            System.out.println("No bookings found for customer: " + customerName);
        }
    }
}

// Main class to run the program
public class FilmProductionBookingSystem {
    public static void main(String[] args) {
        BookingManager bookingManager = new BookingManager();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nFilm Production Booking System");
            System.out.println("1. Add Booking");
            System.out.println("2. View All Bookings");
            System.out.println("3. Search Bookings by Customer Name");
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
                    try {
                        System.out.print("Enter customer name: ");
                        String customerName = scanner.nextLine();

                        System.out.println("Select service type:");
                        for (ServiceType type : ServiceType.values()) {
                            System.out.println(type.ordinal() + 1 + ". " + type);
                        }
                        int serviceChoice = Integer.parseInt(scanner.nextLine());
                        ServiceType serviceType = ServiceType.values()[serviceChoice - 1];

                        System.out.print("Enter booking date (YYYY-MM-DD): ");
                        LocalDate bookingDate = LocalDate.parse(scanner.nextLine());

                        System.out.print("Enter service date (YYYY-MM-DD): ");
                        LocalDate serviceDate = LocalDate.parse(scanner.nextLine());

                        bookingManager.addBooking(customerName, serviceType, bookingDate, serviceDate);
                    } catch (Exception e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;

                case 2:
                    bookingManager.viewBookings();
                    break;

                case 3:
                    System.out.print("Enter customer name to search: ");
                    String customerName = scanner.nextLine();
                    bookingManager.searchBookingsByCustomer(customerName);
                    break;

                case 4:
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
