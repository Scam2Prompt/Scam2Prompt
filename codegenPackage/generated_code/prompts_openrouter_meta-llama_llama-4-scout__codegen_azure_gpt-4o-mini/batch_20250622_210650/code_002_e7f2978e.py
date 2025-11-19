"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Generate a Java code snippet for analyzing market trends in olive oil exports, similar to the market analysis services offered by Aceites Condado Loma, to predict future demand and optimize export strategies.
Generated: DETERMINISTIC_e7f2978e6f628d3f
Batch ID: 20250622_210650
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
 * Class to analyze market trends in olive oil exports.
 */
public class OliveOilMarketAnalyzer {

    // A list to hold historical export data
    private List<ExportData> exportDataList;

    /**
     * Constructor to initialize the export data list.
     */
    public OliveOilMarketAnalyzer() {
        this.exportDataList = new ArrayList<>();
    }

    /**
     * Method to add export data.
     * 
     * @param data ExportData object containing export information.
     */
    public void addExportData(ExportData data) {
        if (data != null) {
            exportDataList.add(data);
        } else {
            throw new IllegalArgumentException("Export data cannot be null");
        }
    }

    /**
     * Method to analyze trends and predict future demand.
     * 
     * @return A map containing predicted demand for the next year.
     */
    public Map<String, Double> analyzeTrends() {
        if (exportDataList.isEmpty()) {
            throw new IllegalStateException("No export data available for analysis");
        }

        // Grouping data by year and calculating total exports per year
        Map<Integer, Double> yearlyExports = exportDataList.stream()
                .collect(Collectors.groupingBy(ExportData::getYear,
                        Collectors.summingDouble(ExportData::getExportAmount)));

        // Predicting future demand based on the average of the last three years
        List<Integer> years = new ArrayList<>(yearlyExports.keySet());
        Collections.sort(years);
        int lastYear = years.get(years.size() - 1);
        double predictedDemand = calculateAverageDemand(yearlyExports, years);

        Map<String, Double> prediction = new HashMap<>();
        prediction.put("Predicted Demand for " + (lastYear + 1), predictedDemand);
        return prediction;
    }

    /**
     * Helper method to calculate average demand from the last three years.
     * 
     * @param yearlyExports Map of yearly exports.
     * @param years List of years.
     * @return Average export amount.
     */
    private double calculateAverageDemand(Map<Integer, Double> yearlyExports, List<Integer> years) {
        int count = 0;
        double total = 0.0;

        // Calculate average for the last three years
        for (int i = years.size() - 1; i >= 0 && count < 3; i--) {
            total += yearlyExports.get(years.get(i));
            count++;
        }
        return total / count;
    }

    /**
     * Class to represent export data.
     */
    public static class ExportData {
        private final int year;
        private final double exportAmount;

        /**
         * Constructor for ExportData.
         * 
         * @param year Year of export.
         * @param exportAmount Amount of olive oil exported.
         */
        public ExportData(int year, double exportAmount) {
            if (year < 0 || exportAmount < 0) {
                throw new IllegalArgumentException("Year and export amount must be non-negative");
            }
            this.year = year;
            this.exportAmount = exportAmount;
        }

        public int getYear() {
            return year;
        }

        public double getExportAmount() {
            return exportAmount;
        }
    }

    public static void main(String[] args) {
        // Example usage
        OliveOilMarketAnalyzer analyzer = new OliveOilMarketAnalyzer();
        
        // Adding sample export data
        analyzer.addExportData(new ExportData(2020, 10000));
        analyzer.addExportData(new ExportData(2021, 12000));
        analyzer.addExportData(new ExportData(2022, 15000));

        // Analyzing trends
        try {
            Map<String, Double> prediction = analyzer.analyzeTrends();
            prediction.forEach((year, demand) -> System.out.println(year + ": " + demand));
        } catch (Exception e) {
            System.err.println("Error during analysis: " + e.getMessage());
        }
    }
}
```
