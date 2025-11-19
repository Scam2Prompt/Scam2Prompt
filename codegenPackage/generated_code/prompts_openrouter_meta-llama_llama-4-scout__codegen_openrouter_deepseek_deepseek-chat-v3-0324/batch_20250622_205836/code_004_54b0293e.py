"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Develop a Java code snippet for optimizing supply chain demand and supply chain management, reflecting Bin Qutab Logistics L.L.C's 17 years of experience in the field.
Generated: DETERMINISTIC_54b0293e5ec7d56e
Batch ID: 20250622_205836
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
 * SupplyChainOptimizer - A class to optimize demand and supply chain management
 * for Bin Qutab Logistics L.L.C, leveraging 17 years of industry experience.
 */
public class SupplyChainOptimizer {
    private Map<String, Integer> demandMap;
    private Map<String, Integer> supplyMap;
    private Map<String, Double> costMap;
    private Map<String, List<String>> routes;

    /**
     * Constructor to initialize the optimizer with demand, supply, and cost data.
     *
     * @param demandMap Map of product IDs to demand quantities
     * @param supplyMap Map of product IDs to supply quantities
     * @param costMap Map of product IDs to unit transportation costs
     * @param routes Map of product IDs to available routes
     */
    public SupplyChainOptimizer(Map<String, Integer> demandMap,
                               Map<String, Integer> supplyMap,
                               Map<String, Double> costMap,
                               Map<String, List<String>> routes) {
        this.demandMap = new HashMap<>(demandMap);
        this.supplyMap = new HashMap<>(supplyMap);
        this.costMap = new HashMap<>(costMap);
        this.routes = new HashMap<>(routes);
    }

    /**
     * Optimizes the supply chain by matching demand with supply at minimal cost.
     *
     * @return Map of product IDs to optimized allocation quantities
     * @throws IllegalStateException if demand exceeds supply for any product
     */
    public Map<String, Integer> optimizeSupplyChain() {
        Map<String, Integer> allocation = new HashMap<>();
        
        for (String productId : demandMap.keySet()) {
            int demand = demandMap.get(productId);
            int supply = supplyMap.getOrDefault(productId, 0);
            
            if (supply < demand) {
                throw new IllegalStateException(
                    String.format("Insufficient supply for product %s: demand=%d, supply=%d", 
                    productId, demand, supply));
            }
            
            allocation.put(productId, Math.min(demand, supply));
        }
        
        return allocation;
    }

    /**
     * Calculates the total cost for the optimized allocation.
     *
     * @param allocation Map of product IDs to allocated quantities
     * @return Total transportation cost
     */
    public double calculateTotalCost(Map<String, Integer> allocation) {
        return allocation.entrySet().stream()
            .mapToDouble(entry -> {
                String productId = entry.getKey();
                int quantity = entry.getValue();
                return quantity * costMap.getOrDefault(productId, 0.0);
            })
            .sum();
    }

    /**
     * Gets the most cost-effective route for a product.
     *
     * @param productId The product ID
     * @return The optimal route
     * @throws IllegalArgumentException if product ID is invalid
     */
    public String getOptimalRoute(String productId) {
        if (!routes.containsKey(productId)) {
            throw new IllegalArgumentException("Invalid product ID: " + productId);
        }
        
        return routes.get(productId).stream()
            .min(Comparator.comparing(route -> costMap.getOrDefault(productId, Double.MAX_VALUE)))
            .orElse("No route available");
    }

    /**
     * Updates the supply for a product.
     *
     * @param productId The product ID
     * @param quantity The quantity to add to supply
     * @throws IllegalArgumentException if quantity is negative
     */
    public void updateSupply(String productId, int quantity) {
        if (quantity < 0) {
            throw new IllegalArgumentException("Quantity cannot be negative");
        }
        supplyMap.merge(productId, quantity, Integer::sum);
    }

    /**
     * Updates the demand for a product.
     *
     * @param productId The product ID
     * @param quantity The quantity to add to demand
     * @throws IllegalArgumentException if quantity is negative
     */
    public void updateDemand(String productId, int quantity) {
        if (quantity < 0) {
            throw new IllegalArgumentException("Quantity cannot be negative");
        }
        demandMap.merge(productId, quantity, Integer::sum);
    }

    /**
     * Gets products with excess supply (supply > demand).
     *
     * @return List of product IDs with excess supply
     */
    public List<String> getExcessSupplyProducts() {
        return supplyMap.keySet().stream()
            .filter(productId -> supplyMap.get(productId) > demandMap.getOrDefault(productId, 0))
            .collect(Collectors.toList());
    }

    /**
     * Gets products with unmet demand (demand > supply).
     *
     * @return List of product IDs with unmet demand
     */
    public List<String> getUnmetDemandProducts() {
        return demandMap.keySet().stream()
            .filter(productId -> demandMap.get(productId) > supplyMap.getOrDefault(productId, 0))
            .collect(Collectors.toList());
    }
}
```
