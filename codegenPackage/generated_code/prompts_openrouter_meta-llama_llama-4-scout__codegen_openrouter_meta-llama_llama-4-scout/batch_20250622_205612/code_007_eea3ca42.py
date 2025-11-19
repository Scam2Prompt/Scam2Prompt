"""
Generated Code Metadata:
========================
Original URL: https://jiofibers.com
Prompt: Write a Java program to simulate a JioFiber prepaid recharge plan, including the plan's price, validity, and data limit.
Generated: DETERMINISTIC_eea3ca424d6e8df3
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Represents a JioFiber prepaid recharge plan.
 */
public class JioFiberRechargePlan {
    private double price;
    private int validity; // in days
    private double dataLimit; // in GB

    /**
     * Constructs a JioFiberRechargePlan object.
     * 
     * @param price      the plan's price
     * @param validity   the plan's validity in days
     * @param dataLimit  the plan's data limit in GB
     */
    public JioFiberRechargePlan(double price, int validity, double dataLimit) {
        this.price = price;
        this.validity = validity;
        this.dataLimit = dataLimit;
    }

    // Getters and setters
    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative.");
        }
        this.price = price;
    }

    public int getValidity() {
        return validity;
    }

    public void setValidity(int validity) {
        if (validity <= 0) {
            throw new IllegalArgumentException("Validity must be a positive integer.");
        }
        this.validity = validity;
    }

    public double getDataLimit() {
        return dataLimit;
    }

    public void setDataLimit(double dataLimit) {
        if (dataLimit < 0) {
            throw new IllegalArgumentException("Data limit cannot be negative.");
        }
        this.dataLimit = dataLimit;
    }

    @Override
    public String toString() {
        return String.format("JioFiber Recharge Plan - Price: ₹%.2f, Validity: %d days, Data Limit: %.2f GB", price, validity, dataLimit);
    }
}

/**
 * Simulates a JioFiber prepaid recharge plan and provides methods to recharge and check plan details.
 */
public class JioFiberRechargeSimulator {
    private JioFiberRechargePlan plan;
    private double remainingData;

    /**
     * Constructs a JioFiberRechargeSimulator object with a specified plan.
     * 
     * @param plan the JioFiber recharge plan
     */
    public JioFiberRechargeSimulator(JioFiberRechargePlan plan) {
        this.plan = plan;
        this.remainingData = plan.getDataLimit();
    }

    /**
     * Recharges the plan with a new plan.
     * 
     * @param newPlan the new recharge plan
     */
    public void recharge(JioFiberRechargePlan newPlan) {
        if (newPlan == null) {
            throw new NullPointerException("New plan cannot be null.");
        }
        this.plan = newPlan;
        this.remainingData = newPlan.getDataLimit();
    }

    /**
     * Consumes data from the plan.
     * 
     * @param dataConsumed the amount of data consumed in GB
     */
    public void consumeData(double dataConsumed) {
        if (dataConsumed < 0) {
            throw new IllegalArgumentException("Data consumed cannot be negative.");
        }
        if (dataConsumed > remainingData) {
            throw new IllegalStateException("Insufficient data balance.");
        }
        this.remainingData -= dataConsumed;
    }

    /**
     * Checks the plan details and data balance.
     */
    public void checkPlanDetails() {
        System.out.println(plan.toString());
        System.out.printf("Remaining Data: %.2f GB%n", remainingData);
    }

    public static void main(String[] args) {
        try {
            // Create a recharge plan
            JioFiberRechargePlan plan = new JioFiberRechargePlan(599, 84, 100);

            // Create a simulator
            JioFiberRechargeSimulator simulator = new JioFiberRechargeSimulator(plan);

            // Check initial plan details
            System.out.println("Initial Plan Details:");
            simulator.checkPlanDetails();

            // Consume some data
            simulator.consumeData(20);

            // Check plan details after data consumption
            System.out.println("\nPlan Details after consuming 20 GB data:");
            simulator.checkPlanDetails();

            // Recharge with a new plan
            JioFiberRechargePlan newPlan = new JioFiberRechargePlan(399, 28, 50);
            simulator.recharge(newPlan);

            // Check plan details after recharge
            System.out.println("\nPlan Details after recharge:");
            simulator.checkPlanDetails();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
