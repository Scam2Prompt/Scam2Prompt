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
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * SalesAnalyzer analyzes agricultural chemical sales data for Tấn Hưng Việt Nam.
 */
public class SalesAnalyzer {
    private static final DecimalFormat df = new DecimalFormat("#,##0.00");
    
    /**
     * Represents a sales record for agricultural chemicals.
     */
    static class SalesRecord {
        String productId;
        String productName;
        String category;
        double quantity;
        double unitPrice;
        String region;
        String date;

        public SalesRecord(String productId, String productName, String category, 
                         double quantity, double unitPrice, String region, String date) {
            this.productId = productId;
            this.productName = productName;
            this.category = category;
            this.quantity = quantity;
            this.unitPrice = unitPrice;
            this.region = region;
            this.date = date;
        }

        public double getTotalPrice() {
            return quantity * unitPrice;
        }
    }

    /**
     * Main method to analyze sales data.
     * @param args Command line arguments (expects input file path)
     */
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java SalesAnalyzer <input_file_path>");
            System.exit(1);
        }

        try {
            List<SalesRecord> salesData = loadSalesData(args[0]);
            analyzeSales(salesData);
        } catch (IOException e) {
            System.err.println("Error processing sales data: " + e.getMessage());
            System.exit(1);
        }
    }

    /**
     * Loads sales data from a CSV file.
     * @param filePath Path to the CSV file
     * @return List of SalesRecord objects
     * @throws IOException If there's an error reading the file
     */
    private static List<SalesRecord> loadSalesData(String filePath) throws IOException {
        List<SalesRecord> records = new ArrayList<>();
        
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            boolean isHeader = true;
            
            while ((line = br.readLine()) != null) {
                if (isHeader) {
                    isHeader = false;
                    continue;
                }
                
                String[] values = line.split(",");
                if (values.length != 7) {
                    throw new IOException("Invalid data format in CSV file");
                }
                
                try {
                    SalesRecord record = new SalesRecord(
                        values[0].trim(),
                        values[1].trim(),
                        values[2].trim(),
                        Double.parseDouble(values[3].trim()),
                        Double.parseDouble(values[4].trim()),
                        values[5].trim(),
                        values[6].trim()
                    );
                    records.add(record);
                } catch (NumberFormatException e) {
                    throw new IOException("Invalid numeric value in CSV file", e);
                }
            }
        }
        
        return records;
    }

    /**
     * Analyzes and prints sales statistics.
     * @param salesData List of sales records to analyze
     */
    private static void analyzeSales(List<SalesRecord> salesData) {
        if (salesData.isEmpty()) {
            System.out.println("No sales data to analyze.");
            return;
        }

        // Initialize data structures for analysis
        Map<String, Double> categoryRevenue = new HashMap<>();
        Map<String, Double> regionRevenue = new HashMap<>();
        Map<String, Integer> productCount = new HashMap<>();
        double totalRevenue = 0;
        int totalItemsSold = 0;

        // Process each sales record
        for (SalesRecord record : salesData) {
            double saleAmount = record.getTotalPrice();
            
            // Category analysis
            categoryRevenue.merge(record.category, saleAmount, Double::sum);
            
            // Region analysis
            regionRevenue.merge(record.region, saleAmount, Double::sum);
            
            // Product popularity
            productCount.merge(record.productName, (int)record.quantity, Integer::sum);
            
            totalRevenue += saleAmount;
            totalItemsSold += record.quantity;
        }

        // Print summary statistics
        System.out.println("=== SALES ANALYSIS REPORT ===");
        System.out.println("Total Revenue: " + df.format(totalRevenue) + " VND");
        System.out.println("Total Items Sold: " + totalItemsSold);
        System.out.println("\nRevenue by Category:");
        categoryRevenue.forEach((k, v) -> 
            System.out.println("  " + k + ": " + df.format(v) + " VND"));
        
        System.out.println("\nRevenue by Region:");
        regionRevenue.forEach((k, v) -> 
            System.out.println("  " + k + ": " + df.format(v) + " VND"));
        
        System.out.println("\nTop Selling Products:");
        productCount.entrySet().stream()
            .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
            .limit(5)
            .forEach(entry -> 
                System.out.println("  " + entry.getKey() + ": " + entry.getValue() + " units"));
    }
}
```
