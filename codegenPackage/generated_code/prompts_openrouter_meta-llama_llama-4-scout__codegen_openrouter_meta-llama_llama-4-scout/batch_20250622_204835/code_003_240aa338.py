"""
Generated Code Metadata:
========================
Original URL: https://wenwendrop.com
Prompt: "Create a Java function to categorize fruits based on their health benefits, such as boosting the immune system or reducing the risk of chronic diseases like heart disease and diabetes."
Generated: DETERMINISTIC_240aa3381dd252a1
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;

/**
 * Enum representing different health benefits of fruits.
 */
enum HealthBenefit {
    BOOSTS_IMMUNE_SYSTEM,
    REDUCES_CHRONIC_DISEASES,
    ANTIOXIDANT_RICH,
    SUPPORTS_DIGESTIVE_HEALTH,
    OTHER
}

/**
 * Class representing a fruit with its name and health benefits.
 */
class Fruit {
    private String name;
    private List<HealthBenefit> healthBenefits;

    /**
     * Constructor to initialize a fruit object.
     * 
     * @param name           the name of the fruit
     * @param healthBenefits the health benefits of the fruit
     */
    public Fruit(String name, List<HealthBenefit> healthBenefits) {
        this.name = name;
        this.healthBenefits = healthBenefits;
    }

    /**
     * Getter for the fruit name.
     * 
     * @return the name of the fruit
     */
    public String getName() {
        return name;
    }

    /**
     * Getter for the health benefits of the fruit.
     * 
     * @return the health benefits of the fruit
     */
    public List<HealthBenefit> getHealthBenefits() {
        return healthBenefits;
    }
}

/**
 * Class with a function to categorize fruits based on their health benefits.
 */
public class FruitCategorizer {

    /**
     * Function to categorize fruits based on their health benefits.
     * 
     * @param fruits the list of fruits to categorize
     * @return a map with health benefits as keys and lists of fruits as values
     */
    public static Map<HealthBenefit, List<Fruit>> categorizeFruits(List<Fruit> fruits) {
        Map<HealthBenefit, List<Fruit>> categorizedFruits = new EnumMap<>(HealthBenefit.class);

        // Initialize empty lists for each health benefit
        for (HealthBenefit benefit : HealthBenefit.values()) {
            categorizedFruits.put(benefit, new ArrayList<>());
        }

        // Categorize fruits based on their health benefits
        for (Fruit fruit : fruits) {
            for (HealthBenefit benefit : fruit.getHealthBenefits()) {
                categorizedFruits.get(benefit).add(fruit);
            }
        }

        return categorizedFruits;
    }

    public static void main(String[] args) {
        // Example usage
        Fruit apple = new Fruit("Apple", Arrays.asList(HealthBenefit.BOOSTS_IMMUNE_SYSTEM, HealthBenefit.SUPPORTS_DIGESTIVE_HEALTH));
        Fruit blueberry = new Fruit("Blueberry", Arrays.asList(HealthBenefit.ANTIOXIDANT_RICH, HealthBenefit.REDUCES_CHRONIC_DISEASES));
        Fruit orange = new Fruit("Orange", Arrays.asList(HealthBenefit.BOOSTS_IMMUNE_SYSTEM, HealthBenefit.ANTIOXIDANT_RICH));

        List<Fruit> fruits = Arrays.asList(apple, blueberry, orange);

        try {
            Map<HealthBenefit, List<Fruit>> categorizedFruits = categorizeFruits(fruits);

            // Print categorized fruits
            for (Map.Entry<HealthBenefit, List<Fruit>> entry : categorizedFruits.entrySet()) {
                System.out.println(entry.getKey() + ":");
                for (Fruit fruit : entry.getValue()) {
                    System.out.println("  - " + fruit.getName());
                }
            }
        } catch (Exception e) {
            System.err.println("Error categorizing fruits: " + e.getMessage());
        }
    }
}
```
