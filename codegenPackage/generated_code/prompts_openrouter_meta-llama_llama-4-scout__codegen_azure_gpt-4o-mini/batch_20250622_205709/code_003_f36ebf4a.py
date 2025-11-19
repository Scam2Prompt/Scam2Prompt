"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Create a Java code snippet to analyze sales data for a company like Tấn Hưng Việt Nam that sells various types of agricultural chemicals."
Generated: DETERMINISTIC_f36ebf4a4abf1850
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Class to analyze sales data for agricultural chemicals.
 */
public class SalesDataAnalyzer {

    // A list to hold sales records
    private List<SaleRecord> salesRecords;

    /**
     * Constructor to initialize the sales records list.
     */
    public SalesDataAnalyzer() {
        this.salesRecords = new ArrayList<>();
    }

    /**
     * Method to add a sale record.
     * 
     * @param record The sale record to be added.
     */
    public void addSaleRecord(SaleRecord record) {
        if (record == null) {
            throw new IllegalArgumentException("Sale record cannot be null");
        }
        salesRecords.add(record);
    }

    /**
     * Method to analyze total sales by product type.
     * 
     * @return A map containing product types and their total sales.
     */
    public Map<String, Double> analyzeTotalSalesByProduct() {
        Map<String, Double> totalSalesByProduct = new HashMap<>();

        for (SaleRecord record : salesRecords) {
            totalSalesByProduct.merge(record.getProductType(), record.getAmount(), Double::sum);
        }

        return totalSalesByProduct;
    }

    /**
     * Main method to demonstrate the functionality of the SalesDataAnalyzer.
     * 
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        SalesDataAnalyzer analyzer = new SalesDataAnalyzer();

        // Sample sale records
        analyzer.addSaleRecord(new SaleRecord("Fertilizer", 1500.00));
        analyzer.addSaleRecord(new SaleRecord("Pesticide", 800.00));
        analyzer.addSaleRecord(new SaleRecord("Fertilizer", 1200.00));
        analyzer.addSaleRecord(new SaleRecord("Herbicide", 600.00));

        // Analyze total sales by product type
        Map<String, Double> totalSales = analyzer.analyzeTotalSalesByProduct();

        // Print the total sales
        totalSales.forEach((product, total) -> 
            System.out.println("Product: " + product + ", Total Sales: " + total));
    }
}

/**
 * Class to represent a sale record.
 */
class SaleRecord {
    private String productType;
    private double amount;

    /**
     * Constructor to initialize a sale record.
     * 
     * @param productType The type of product sold.
     * @param amount The amount of the sale.
     */
    public SaleRecord(String productType, double amount) {
        if (productType == null || productType.isEmpty()) {
            throw new IllegalArgumentException("Product type cannot be null or empty");
        }
        if (amount < 0) {
            throw new IllegalArgumentException("Amount cannot be negative");
        }
        this.productType = productType;
        this.amount = amount;
    }

    public String getProductType() {
        return productType;
    }

    public double getAmount() {
        return amount;
    }
}
```
