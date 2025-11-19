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
import java.util.*;
import java.util.stream.Collectors;

/**
 * SalesAnalyzer class to analyze sales data for a company.
 * This class provides functionality to calculate total sales, 
 * average sales, and filter top-performing products.
 */
public class SalesAnalyzer {

    // Represents a single product's sales data
    static class ProductSales {
        private String productName;
        private double salesAmount;

        public ProductSales(String productName, double salesAmount) {
            this.productName = productName;
            this.salesAmount = salesAmount;
        }

        public String getProductName() {
            return productName;
        }

        public double getSalesAmount() {
            return salesAmount;
        }
    }

    /**
     * Calculates the total sales from a list of ProductSales objects.
     *
     * @param salesData List of ProductSales objects
     * @return Total sales amount
     */
    public static double calculateTotalSales(List<ProductSales> salesData) {
        return salesData.stream()
                .mapToDouble(ProductSales::getSalesAmount)
                .sum();
    }

    /**
     * Calculates the average sales from a list of ProductSales objects.
     *
     * @param salesData List of ProductSales objects
     * @return Average sales amount
     */
    public static double calculateAverageSales(List<ProductSales> salesData) {
        if (salesData.isEmpty()) {
            return 0.0; // Avoid division by zero
        }
        return calculateTotalSales(salesData) / salesData.size();
    }

    /**
     * Filters the top-performing products based on a sales threshold.
     *
     * @param salesData List of ProductSales objects
     * @param threshold Minimum sales amount to qualify as top-performing
     * @return List of top-performing ProductSales objects
     */
    public static List<ProductSales> filterTopPerformingProducts(List<ProductSales> salesData, double threshold) {
        return salesData.stream()
                .filter(product -> product.getSalesAmount() >= threshold)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        // Sample sales data
        List<ProductSales> salesData = Arrays.asList(
                new ProductSales("Fertilizer A", 1500.0),
                new ProductSales("Pesticide B", 2500.0),
                new ProductSales("Herbicide C", 800.0),
                new ProductSales("Fertilizer D", 3000.0)
        );

        try {
            // Calculate total sales
            double totalSales = calculateTotalSales(salesData);
            System.out.println("Total Sales: " + totalSales);

            // Calculate average sales
            double averageSales = calculateAverageSales(salesData);
            System.out.println("Average Sales: " + averageSales);

            // Filter top-performing products
            double threshold = 2000.0;
            List<ProductSales> topPerformingProducts = filterTopPerformingProducts(salesData, threshold);
            System.out.println("Top-Performing Products (Sales >= " + threshold + "):");
            for (ProductSales product : topPerformingProducts) {
                System.out.println("- " + product.getProductName() + ": " + product.getSalesAmount());
            }
        } catch (Exception e) {
            // Handle unexpected errors gracefully
            System.err.println("An error occurred while analyzing sales data: " + e.getMessage());
        }
    }
}
```
