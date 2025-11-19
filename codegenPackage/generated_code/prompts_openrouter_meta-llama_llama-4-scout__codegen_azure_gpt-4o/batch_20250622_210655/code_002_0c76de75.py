"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Generate a Java code for a farm management system that includes features like farm visiting, consultancy, and delivery services like Harinder Farms.
Generated: DETERMINISTIC_0c76de750e2fdd47
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

// Farm Management System
public class FarmManagementSystem {

    // Enum for Service Types
    enum ServiceType {
        FARM_VISIT, CONSULTANCY, DELIVERY
    }

    // Class representing a Service
    static class Service {
        private ServiceType type;
        private String description;
        private double price;

        public Service(ServiceType type, String description, double price) {
            this.type = type;
            this.description = description;
            this.price = price;
        }

        public ServiceType getType() {
            return type;
        }

        public String getDescription() {
            return description;
        }

        public double getPrice() {
            return price;
        }

        @Override
        public String toString() {
            return "Service Type: " + type + ", Description: " + description + ", Price: $" + price;
        }
    }

    // Class representing the Farm Management System
    static class FarmManagement {
        private List<Service> services;

        public FarmManagement() {
            services = new ArrayList<>();
            initializeServices();
        }

        // Initialize default services
        private void initializeServices() {
            services.add(new Service(ServiceType.FARM_VISIT, "Visit the farm and explore our facilities.", 50.0));
            services.add(new Service(ServiceType.CONSULTANCY, "Get expert advice on farming techniques.", 100.0));
            services.add(new Service(ServiceType.DELIVERY, "Delivery of fresh farm produce to your doorstep.", 20.0));
        }

        // Display available services
        public void displayServices() {
            System.out.println("Available Services:");
            for (int i = 0; i < services.size(); i++) {
                System.out.println((i + 1) + ". " + services.get(i));
            }
        }

        // Book a service
        public void bookService(int serviceIndex) {
            if (serviceIndex < 1 || serviceIndex > services.size()) {
                System.out.println("Invalid service selection. Please try again.");
                return;
            }
            Service selectedService = services.get(serviceIndex - 1);
            System.out.println("You have successfully booked the following service:");
            System.out.println(selectedService);
        }
    }

    // Main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        FarmManagement farmManagement = new FarmManagement();

        System.out.println("Welcome to the Farm Management System!");
        boolean running = true;

        while (running) {
            System.out.println("\nMenu:");
            System.out.println("1. View Services");
            System.out.println("2. Book a Service");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        farmManagement.displayServices();
                        break;
                    case 2:
                        farmManagement.displayServices();
                        System.out.print("Enter the number of the service you want to book: ");
                        int serviceIndex = Integer.parseInt(scanner.nextLine());
                        farmManagement.bookService(serviceIndex);
                        break;
                    case 3:
                        running = false;
                        System.out.println("Thank you for using the Farm Management System. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }

        scanner.close();
    }
}
```
