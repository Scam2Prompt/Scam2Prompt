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

// Class representing a Farm
class Farm {
    private String name;
    private String location;

    public Farm(String name, String location) {
        this.name = name;
        this.location = location;
    }

    public String getName() {
        return name;
    }

    public String getLocation() {
        return location;
    }

    @Override
    public String toString() {
        return "Farm Name: " + name + ", Location: " + location;
    }
}

// Class representing a Consultancy Service
class ConsultancyService {
    private String serviceName;
    private double fee;

    public ConsultancyService(String serviceName, double fee) {
        this.serviceName = serviceName;
        this.fee = fee;
    }

    public String getServiceName() {
        return serviceName;
    }

    public double getFee() {
        return fee;
    }

    @Override
    public String toString() {
        return "Consultancy Service: " + serviceName + ", Fee: $" + fee;
    }
}

// Class representing Delivery Service
class DeliveryService {
    private String deliveryType;
    private double cost;

    public DeliveryService(String deliveryType, double cost) {
        this.deliveryType = deliveryType;
        this.cost = cost;
    }

    public String getDeliveryType() {
        return deliveryType;
    }

    public double getCost() {
        return cost;
    }

    @Override
    public String toString() {
        return "Delivery Type: " + deliveryType + ", Cost: $" + cost;
    }
}

// Main class for Farm Management System
public class FarmManagementSystem {
    private List<Farm> farms;
    private List<ConsultancyService> consultancyServices;
    private List<DeliveryService> deliveryServices;

    public FarmManagementSystem() {
        farms = new ArrayList<>();
        consultancyServices = new ArrayList<>();
        deliveryServices = new ArrayList<>();
    }

    // Method to add a farm
    public void addFarm(String name, String location) {
        farms.add(new Farm(name, location));
    }

    // Method to add a consultancy service
    public void addConsultancyService(String serviceName, double fee) {
        consultancyServices.add(new ConsultancyService(serviceName, fee));
    }

    // Method to add a delivery service
    public void addDeliveryService(String deliveryType, double cost) {
        deliveryServices.add(new DeliveryService(deliveryType, cost));
    }

    // Method to display all farms
    public void displayFarms() {
        System.out.println("Farms:");
        for (Farm farm : farms) {
            System.out.println(farm);
        }
    }

    // Method to display all consultancy services
    public void displayConsultancyServices() {
        System.out.println("Consultancy Services:");
        for (ConsultancyService service : consultancyServices) {
            System.out.println(service);
        }
    }

    // Method to display all delivery services
    public void displayDeliveryServices() {
        System.out.println("Delivery Services:");
        for (DeliveryService service : deliveryServices) {
            System.out.println(service);
        }
    }

    // Main method to run the Farm Management System
    public static void main(String[] args) {
        FarmManagementSystem system = new FarmManagementSystem();
        Scanner scanner = new Scanner(System.in);

        // Sample data
        system.addFarm("Harinder Farms", "Punjab");
        system.addConsultancyService("Crop Management", 150.0);
        system.addDeliveryService("Vegetable Delivery", 20.0);

        // Displaying the data
        system.displayFarms();
        system.displayConsultancyServices();
        system.displayDeliveryServices();

        // Closing the scanner
        scanner.close();
    }
}
```
