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
import java.util.List;

/**
 * Represents a sales data point for agricultural chemicals.
 */
class SalesData {
    private String chemicalName;
    private double quantitySold;
    private double revenue;

    public SalesData(String chemicalName, double quantitySold, double revenue) {
        this.chemicalName = chemicalName;
        this.quantitySold = quantitySold;
        this.revenue = revenue;
    }

    // Getters and setters
    public String getChemicalName() { return chemicalName; }
    public double getQuantitySold() { return quantitySold; }
    public double getRevenue() { return revenue; }
}

public class AgriculturalChemicalSalesAnalyzer {

    /**
     * Analyzes sales data for agricultural chemicals.
     * 
     * @param salesDataList List of sales data points
     * @return A summary of sales data, including total revenue and top-selling chemicals
     */
    public static SalesSummary analyzeSalesData(List<SalesData> salesDataList) {
        if (salesDataList == null || salesDataList.isEmpty()) {
            throw new IllegalArgumentException("Sales data list cannot be empty");
        }

        double totalRevenue = 0;
        int topSellingChemicalIndex = 0;
        double maxRevenue = 0;

        for (int i = 0; i < salesDataList.size(); i++) {
            SalesData salesData = salesDataList.get(i);
            totalRevenue += salesData.getRevenue();

            if (salesData.getRevenue() > maxRevenue) {
                maxRevenue = salesData.getRevenue();
                topSellingChemicalIndex = i;
            }
        }

        String topSellingChemical = salesDataList.get(topSellingChemicalIndex).getChemicalName();

        return new SalesSummary(totalRevenue, topSellingChemical);
    }

    /**
     * Represents a summary of sales data.
     */
    public static class SalesSummary {
        private double totalRevenue;
        private String topSellingChemical;

        public SalesSummary(double totalRevenue, String topSellingChemical) {
            this.totalRevenue = totalRevenue;
            this.topSellingChemical = topSellingChemical;
        }

        // Getters
        public double getTotalRevenue() { return totalRevenue; }
        public String getTopSellingChemical() { return topSellingChemical; }
    }

    public static void main(String[] args) {
        List<SalesData> salesDataList = new ArrayList<>();

        // Example sales data
        salesDataList.add(new SalesData("Fertilizer", 1000, 50000));
        salesDataList.add(new SalesData("Pesticide", 500, 20000));
        salesDataList.add(new SalesData("Herbicide", 2000, 80000));

        try {
            SalesSummary salesSummary = analyzeSalesData(salesDataList);

            System.out.println("Total Revenue: " + salesSummary.getTotalRevenue());
            System.out.println("Top Selling Chemical: " + salesSummary.getTopSellingChemical());
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
