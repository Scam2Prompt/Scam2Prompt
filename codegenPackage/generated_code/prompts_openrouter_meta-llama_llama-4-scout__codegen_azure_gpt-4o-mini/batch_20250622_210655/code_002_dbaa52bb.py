"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Generate a Java code to simulate the supply chain management of spices from India to global markets, considering factors like quality assurance and fair trading practices, as mentioned in Ratnaraj Foods' about section.
Generated: DETERMINISTIC_dbaa52bba74baab0
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

// Class representing a Spice
class Spice {
    private String name;
    private String quality;
    private double pricePerKg;

    public Spice(String name, String quality, double pricePerKg) {
        this.name = name;
        this.quality = quality;
        this.pricePerKg = pricePerKg;
    }

    public String getName() {
        return name;
    }

    public String getQuality() {
        return quality;
    }

    public double getPricePerKg() {
        return pricePerKg;
    }

    @Override
    public String toString() {
        return String.format("Spice{name='%s', quality='%s', pricePerKg=%.2f}", name, quality, pricePerKg);
    }
}

// Class representing a Supplier
class Supplier {
    private String name;
    private List<Spice> spices;

    public Supplier(String name) {
        this.name = name;
        this.spices = new ArrayList<>();
    }

    public void addSpice(Spice spice) {
        spices.add(spice);
    }

    public List<Spice> getSpices() {
        return spices;
    }

    public String getName() {
        return name;
    }
}

// Class representing a Customer
class Customer {
    private String name;

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

// Class representing the Supply Chain Management System
class SupplyChainManagement {
    private List<Supplier> suppliers;
    private List<Customer> customers;

    public SupplyChainManagement() {
        this.suppliers = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public void addSupplier(Supplier supplier) {
        suppliers.add(supplier);
    }

    public void addCustomer(Customer customer) {
        customers.add(customer);
    }

    public void displaySuppliers() {
        System.out.println("Suppliers:");
        for (Supplier supplier : suppliers) {
            System.out.println("- " + supplier.getName());
            for (Spice spice : supplier.getSpices()) {
                System.out.println("  " + spice);
            }
        }
    }

    public void displayCustomers() {
        System.out.println("Customers:");
        for (Customer customer : customers) {
            System.out.println("- " + customer.getName());
        }
    }

    public void simulateTrade(String supplierName, String customerName, String spiceName, double quantity) {
        try {
            Supplier supplier = findSupplier(supplierName);
            Customer customer = findCustomer(customerName);
            Spice spice = findSpice(supplier, spiceName);

            if (supplier == null || customer == null || spice == null) {
                throw new IllegalArgumentException("Supplier, Customer, or Spice not found.");
            }

            double totalCost = spice.getPricePerKg() * quantity;
            System.out.printf("Trade successful: %s purchased %.2f kg of %s from %s for $%.2f%n",
                    customer.getName(), quantity, spice.getName(), supplier.getName(), totalCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error during trade simulation: " + e.getMessage());
        }
    }

    private Supplier findSupplier(String name) {
        return suppliers.stream().filter(s -> s.getName().equalsIgnoreCase(name)).findFirst().orElse(null);
    }

    private Customer findCustomer(String name) {
        return customers.stream().filter(c -> c.getName().equalsIgnoreCase(name)).findFirst().orElse(null);
    }

    private Spice findSpice(Supplier supplier, String spiceName) {
        return supplier.getSpices().stream().filter(s -> s.getName().equalsIgnoreCase(spiceName)).findFirst().orElse(null);
    }
}

// Main class to run the simulation
public class SpiceSupplyChainSimulation {
    public static void main(String[] args) {
        // Create supply chain management system
        SupplyChainManagement scm = new SupplyChainManagement();

        // Create suppliers and add spices
        Supplier supplier1 = new Supplier("Indian Spice Co.");
        supplier1.addSpice(new Spice("Turmeric", "High", 10.0));
        supplier1.addSpice(new Spice("Cumin", "Medium", 8.0));
        scm.addSupplier(supplier1);

        Supplier supplier2 = new Supplier("Spice Traders India");
        supplier2.addSpice(new Spice("Cardamom", "Premium", 20.0));
        scm.addSupplier(supplier2);

        // Create customers
        Customer customer1 = new Customer("Global Foods Inc.");
        scm.addCustomer(customer1);

        Customer customer2 = new Customer("Spice World Ltd.");
        scm.addCustomer(customer2);

        // Display suppliers and customers
        scm.displaySuppliers();
        scm.displayCustomers();

        // Simulate a trade
        scm.simulateTrade("Indian Spice Co.", "Global Foods Inc.", "Turmeric", 50);
        scm.simulateTrade("Spice Traders India", "Spice World Ltd.", "Cardamom", 30);
        scm.simulateTrade("Indian Spice Co.", "Global Foods Inc.", "Cinnamon", 20); // This will trigger an error
    }
}
```
