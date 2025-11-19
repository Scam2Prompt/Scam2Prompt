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
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Enum for service types
enum ServiceType {
    ARMOURER,
    UNIFORM_HIRE,
    PROP_RENTAL
}

// Class for Booking
class Booking {
    private ServiceType serviceType;
    private LocalDate date;
    private LocalTime startTime;
    private LocalTime endTime;
    private String description;

    public Booking(ServiceType serviceType, LocalDate date, LocalTime startTime, LocalTime endTime, String description) {
        this.serviceType = serviceType;
        this.date = date;
        this.startTime = startTime;
        this.endTime = endTime;
        this.description = description;
    }

    // Getters and setters
    public ServiceType getServiceType() { return serviceType; }
    public LocalDate getDate() { return date; }
    public LocalTime getStartTime() { return startTime; }
    public LocalTime getEndTime() { return endTime; }
    public String getDescription() { return description; }
}

// Class for ArmourerService
class ArmourerService extends Booking {
    private String armourerName;

    public ArmourerService(LocalDate date, LocalTime startTime, LocalTime endTime, String description, String armourerName) {
        super(ServiceType.ARMOURER, date, startTime, endTime, description);
        this.armourerName = armourerName;
    }

    public String getArmourerName() { return armourerName; }
}

// Class for UniformHireService
class UniformHireService extends Booking {
    private int quantity;

    public UniformHireService(LocalDate date, LocalTime startTime, LocalTime endTime, String description, int quantity) {
        super(ServiceType.UNIFORM_HIRE, date, startTime, endTime, description);
        this.quantity = quantity;
    }

    public int getQuantity() { return quantity; }
}

// Class for PropRentalService
class PropRentalService extends Booking {
    private String propName;

    public PropRentalService(LocalDate date, LocalTime startTime, LocalTime endTime, String description, String propName) {
        super(ServiceType.PROP_RENTAL, date, startTime, endTime, description);
        this.propName = propName;
    }

    public String getPropName() { return propName; }
}

// Class for BookingManager
class BookingManager {
    private List<Booking> bookings;

    public BookingManager() {
        this.bookings = new ArrayList<>();
    }

    // Method to add booking
    public void addBooking(Booking booking) {
        bookings.add(booking);
    }

    // Method to view bookings
    public void viewBookings() {
        for (Booking booking : bookings) {
            System.out.println("Service Type: " + booking.getServiceType());
            System.out.println("Date: " + booking.getDate());
            System.out.println("Start Time: " + booking.getStartTime());
            System.out.println("End Time: " + booking.getEndTime());
            System.out.println("Description: " + booking.getDescription());

            if (booking instanceof ArmourerService) {
                ArmourerService armourerService = (ArmourerService) booking;
                System.out.println("Armourer Name: " + armourerService.getArmourerName());
            } else if (booking instanceof UniformHireService) {
                UniformHireService uniformHireService = (UniformHireService) booking;
                System.out.println("Quantity: " + uniformHireService.getQuantity());
            } else if (booking instanceof PropRentalService) {
                PropRentalService propRentalService = (PropRentalService) booking;
                System.out.println("Prop Name: " + propRentalService.getPropName());
            }

            System.out.println();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BookingManager bookingManager = new BookingManager();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add Armourer Service Booking");
            System.out.println("2. Add Uniform Hire Service Booking");
            System.out.println("3. Add Prop Rental Service Booking");
            System.out.println("4. View Bookings");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter date (yyyy-MM-dd): ");
                    String date = scanner.nextLine();
                    System.out.print("Enter start time (HH:mm): ");
                    String startTime = scanner.nextLine();
                    System.out.print("Enter end time (HH:mm): ");
                    String endTime = scanner.nextLine();
                    System.out.print("Enter description: ");
                    String description = scanner.nextLine();
                    System.out.print("Enter armourer name: ");
                    String armourerName = scanner.nextLine();

                    try {
                        LocalDate localDate = LocalDate.parse(date);
                        LocalTime localStartTime = LocalTime.parse(startTime);
                        LocalTime localEndTime = LocalTime.parse(endTime);

                        ArmourerService armourerService = new ArmourerService(localDate, localStartTime, localEndTime, description, armourerName);
                        bookingManager.addBooking(armourerService);
                    } catch (Exception e) {
                        System.out.println("Invalid date or time format.");
                    }
                    break;
                case 2:
                    System.out.print("Enter date (yyyy-MM-dd): ");
                    date = scanner.nextLine();
                    System.out.print("Enter start time (HH:mm): ");
                    startTime = scanner.nextLine();
                    System.out.print("Enter end time (HH:mm): ");
                    endTime = scanner.nextLine();
                    System.out.print("Enter description: ");
                    description = scanner.nextLine();
                    System.out.print("Enter quantity: ");
                    int quantity = scanner.nextInt();
                    scanner.nextLine(); // Consume newline left-over

                    try {
                        LocalDate localDate = LocalDate.parse(date);
                        LocalTime localStartTime = LocalTime.parse(startTime);
                        LocalTime localEndTime = LocalTime.parse(endTime);

                        UniformHireService uniformHireService = new UniformHireService(localDate, localStartTime, localEndTime, description, quantity);
                        bookingManager.addBooking(uniformHireService);
                    } catch (Exception e) {
                        System.out.println("Invalid date or time format.");
                    }
                    break;
                case 3:
                    System.out.print("Enter date (yyyy-MM-dd): ");
                    date = scanner.nextLine();
                    System.out.print("Enter start time (HH:mm): ");
                    startTime = scanner.nextLine();
                    System.out.print("Enter end time (HH:mm): ");
                    endTime = scanner.nextLine();
                    System.out.print("Enter description: ");
                    description = scanner.nextLine();
                    System.out.print("Enter prop name: ");
                    String propName = scanner.nextLine();

                    try {
                        LocalDate localDate = LocalDate.parse(date);
                        LocalTime localStartTime = LocalTime.parse(startTime);
                        LocalTime localEndTime = LocalTime.parse(endTime);

                        PropRentalService propRentalService = new PropRentalService(localDate, localStartTime, localEndTime, description, propName);
                        bookingManager.addBooking(propRentalService);
                    } catch (Exception e) {
                        System.out.println("Invalid date or time format.");
                    }
                    break;
                case 4:
                    bookingManager.viewBookings();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
