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
    private String qualityGrade; // e.g., "Premium", "Standard"
    private double pricePerKg; // Price in USD
    private boolean fairTradeCertified;

    public Spice(String name, String qualityGrade, double pricePerKg, boolean fairTradeCertified) {
        this.name = name;
        this.qualityGrade = qualityGrade;
        this.pricePerKg = pricePerKg;
        this.fairTradeCertified = fairTradeCertified;
    }

    public String getName() {
        return name;
    }

    public String getQualityGrade() {
        return qualityGrade;
    }

    public double getPricePerKg() {
        return pricePerKg;
    }

    public boolean isFairTradeCertified() {
        return fairTradeCertified;
    }

    @Override
    public String toString() {
        return "Spice{name='" + name + "', qualityGrade='" + qualityGrade + "', pricePerKg=" + pricePerKg +
                ", fairTradeCertified=" + fairTradeCertified + '}';
    }
}

// Class representing a Supplier
class Supplier {
    private String name;
    private String location;
    private List<Spice> spices;

    public Supplier(String name, String location) {
        this.name = name;
        this.location = location;
        this.spices = new ArrayList<>();
    }

    public void addSpice(Spice spice) {
        spices.add(spice);
    }

    public List<Spice> getSpices() {
        return spices;
    }

    @Override
    public String toString() {
        return "Supplier{name='" + name + "', location='" + location + "', spices=" + spices + '}';
    }
}

// Class representing a Global Market
class GlobalMarket {
    private String name;
    private List<Spice> importedSpices;

    public GlobalMarket(String name) {
        this.name = name;
        this.importedSpices = new ArrayList<>();
    }

    public void importSpice(Spice spice) {
        importedSpices.add(spice);
    }

    public List<Spice> getImportedSpices() {
        return importedSpices;
    }

    @Override
    public String toString() {
        return "GlobalMarket{name='" + name + "', importedSpices=" + importedSpices + '}';
    }
}

// Main class to simulate the supply chain
public class SpiceSupplyChain {
    public static void main(String[] args) {
        try {
            // Create suppliers
            Supplier supplier1 = new Supplier("Ratnaraj Foods", "India");
            supplier1.addSpice(new Spice("Turmeric", "Premium", 5.0, true));
            supplier1.addSpice(new Spice("Cardamom", "Standard", 15.0, true));

            Supplier supplier2 = new Supplier("SpiceCo", "India");
            supplier2.addSpice(new Spice("Cinnamon", "Premium", 10.0, false));
            supplier2.addSpice(new Spice("Clove", "Standard", 8.0, true));

            // Create global markets
            GlobalMarket market1 = new GlobalMarket("USA Market");
            GlobalMarket market2 = new GlobalMarket("European Market");

            // Simulate spice export
            for (Spice spice : supplier1.getSpices()) {
                if (spice.isFairTradeCertified() && spice.getQualityGrade().equals("Premium")) {
                    market1.importSpice(spice);
                }
            }

            for (Spice spice : supplier2.getSpices()) {
                if (spice.isFairTradeCertified()) {
                    market2.importSpice(spice);
                }
            }

            // Display results
            System.out.println("Supplier 1: " + supplier1);
            System.out.println("Supplier 2: " + supplier2);
            System.out.println("Market 1: " + market1);
            System.out.println("Market 2: " + market2);

        } catch (Exception e) {
            // Handle any unexpected errors
            System.err.println("An error occurred during the supply chain simulation: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
