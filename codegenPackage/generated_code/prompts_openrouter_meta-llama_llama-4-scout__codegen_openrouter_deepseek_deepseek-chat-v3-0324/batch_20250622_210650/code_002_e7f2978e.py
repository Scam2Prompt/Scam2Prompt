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
import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.stream.Collectors;

/**
 * MarketTrendAnalyzer analyzes olive oil export data to predict future demand
 * and optimize export strategies.
 */
public class MarketTrendAnalyzer {
    private List<ExportRecord> exportData;
    private Map<String, Double> countryDemandIndex;

    /**
     * Represents a single export record
     */
    public static class ExportRecord {
        private LocalDate date;
        private String destinationCountry;
        private double quantityInLiters;
        private double pricePerLiter;

        public ExportRecord(LocalDate date, String destinationCountry, 
                          double quantityInLiters, double pricePerLiter) {
            this.date = date;
            this.destinationCountry = destinationCountry;
            this.quantityInLiters = quantityInLiters;
            this.pricePerLiter = pricePerLiter;
        }

        // Getters
        public LocalDate getDate() { return date; }
        public String getDestinationCountry() { return destinationCountry; }
        public double getQuantityInLiters() { return quantityInLiters; }
        public double getPricePerLiter() { return pricePerLiter; }
    }

    /**
     * Initializes the analyzer with export data
     * @param exportData List of historical export records
     */
    public MarketTrendAnalyzer(List<ExportRecord> exportData) {
        if (exportData == null || exportData.isEmpty()) {
            throw new IllegalArgumentException("Export data cannot be null or empty");
        }
        this.exportData = new ArrayList<>(exportData);
        this.countryDemandIndex = new HashMap<>();
        calculateDemandIndices();
    }

    /**
     * Calculates demand indices for each country based on historical data
     */
    private void calculateDemandIndices() {
        Map<String, List<ExportRecord>> exportsByCountry = exportData.stream()
            .collect(Collectors.groupingBy(ExportRecord::getDestinationCountry));

        exportsByCountry.forEach((country, records) -> {
            double totalVolume = records.stream()
                .mapToDouble(ExportRecord::getQuantityInLiters)
                .sum();
            double avgPrice = records.stream()
                .mapToDouble(ExportRecord::getPricePerLiter)
                .average()
                .orElse(0.0);
            
            // Demand index formula: total volume * (1 - normalized price)
            double normalizedPrice = avgPrice / getMaxPrice();
            countryDemandIndex.put(country, totalVolume * (1 - normalizedPrice));
        });
    }

    /**
     * Gets the maximum price per liter from all records
     */
    private double getMaxPrice() {
        return exportData.stream()
            .mapToDouble(ExportRecord::getPricePerLiter)
            .max()
            .orElse(1.0); // Avoid division by zero
    }

    /**
     * Predicts demand for the next quarter based on historical trends
     * @return Map of country to predicted demand in liters
     */
    public Map<String, Double> predictDemand() {
        Map<String, Double> predictions = new HashMap<>();
        countryDemandIndex.forEach((country, index) -> {
            // Simple prediction: demand grows proportionally to demand index
            predictions.put(country, index * 1.1); // 10% growth assumption
        });
        return predictions;
    }

    /**
     * Identifies the most promising markets based on demand index
     * @param topN Number of top markets to return
     * @return List of top markets ordered by demand potential
     */
    public List<String> getTopMarkets(int topN) {
        if (topN <= 0) {
            throw new IllegalArgumentException("topN must be positive");
        }

        return countryDemandIndex.entrySet().stream()
            .sorted(Map.Entry.<String, Double>comparingByValue().reversed())
            .limit(topN)
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());
    }

    /**
     * Calculates seasonal trends in exports
     * @return Map of month to average export volume
     */
    public Map<Integer, Double> calculateSeasonalTrends() {
        Map<Integer, List<ExportRecord>> exportsByMonth = exportData.stream()
            .collect(Collectors.groupingBy(r -> r.getDate().getMonthValue()));

        Map<Integer, Double> monthlyAverages = new HashMap<>();
        exportsByMonth.forEach((month, records) -> {
            double avg = records.stream()
                .mapToDouble(ExportRecord::getQuantityInLiters)
                .average()
                .orElse(0.0);
            monthlyAverages.put(month, avg);
        });

        return monthlyAverages;
    }

    /**
     * Optimizes pricing strategy based on demand elasticity
     * @param country Target country
     * @return Suggested price per liter
     */
    public double optimizePrice(String country) {
        if (!countryDemandIndex.containsKey(country)) {
            throw new IllegalArgumentException("No data available for country: " + country);
        }

        List<ExportRecord> countryExports = exportData.stream()
            .filter(r -> r.getDestinationCountry().equals(country))
            .collect(Collectors.toList());

        double avgPrice = countryExports.stream()
            .mapToDouble(ExportRecord::getPricePerLiter)
            .average()
            .orElse(0.0);

        double demandIndex = countryDemandIndex.get(country);
        double maxPrice = getMaxPrice();

        // Price optimization formula: balance between demand and price
        return avgPrice * (1 + (demandIndex / (maxPrice * 100)));
    }
}
```
