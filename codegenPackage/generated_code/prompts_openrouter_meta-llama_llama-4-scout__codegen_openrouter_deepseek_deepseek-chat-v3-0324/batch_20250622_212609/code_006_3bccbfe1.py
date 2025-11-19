"""
Generated Code Metadata:
========================
Original URL: https://loyal.credit
Prompt: "Create a simple loyalty program with credit tracking using Java."
Generated: DETERMINISTIC_3bccbfe1081103ba
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;

/**
 * A simple loyalty program that tracks credits for customers.
 */
public class LoyaltyProgram {
    private Map<String, Integer> customerCredits;

    /**
     * Initializes a new loyalty program with an empty customer database.
     */
    public LoyaltyProgram() {
        this.customerCredits = new HashMap<>();
    }

    /**
     * Adds credits to a customer's account.
     * @param customerId The ID of the customer
     * @param credits The number of credits to add (must be positive)
     * @throws IllegalArgumentException if credits is negative or customerId is null
     */
    public void addCredits(String customerId, int credits) {
        if (customerId == null) {
            throw new IllegalArgumentException("Customer ID cannot be null");
        }
        if (credits <= 0) {
            throw new IllegalArgumentException("Credits must be positive");
        }

        int currentCredits = customerCredits.getOrDefault(customerId, 0);
        customerCredits.put(customerId, currentCredits + credits);
    }

    /**
     * Deducts credits from a customer's account.
     * @param customerId The ID of the customer
     * @param credits The number of credits to deduct (must be positive)
     * @throws IllegalArgumentException if credits is negative, customerId is null, or insufficient credits
     */
    public void deductCredits(String customerId, int credits) {
        if (customerId == null) {
            throw new IllegalArgumentException("Customer ID cannot be null");
        }
        if (credits <= 0) {
            throw new IllegalArgumentException("Credits must be positive");
        }

        int currentCredits = customerCredits.getOrDefault(customerId, 0);
        if (currentCredits < credits) {
            throw new IllegalArgumentException("Insufficient credits");
        }

        customerCredits.put(customerId, currentCredits - credits);
    }

    /**
     * Gets the current credit balance for a customer.
     * @param customerId The ID of the customer
     * @return The number of credits the customer has
     * @throws IllegalArgumentException if customerId is null
     */
    public int getCredits(String customerId) {
        if (customerId == null) {
            throw new IllegalArgumentException("Customer ID cannot be null");
        }
        return customerCredits.getOrDefault(customerId, 0);
    }

    /**
     * Checks if a customer exists in the program.
     * @param customerId The ID of the customer
     * @return true if the customer exists, false otherwise
     * @throws IllegalArgumentException if customerId is null
     */
    public boolean hasCustomer(String customerId) {
        if (customerId == null) {
            throw new IllegalArgumentException("Customer ID cannot be null");
        }
        return customerCredits.containsKey(customerId);
    }

    /**
     * Removes a customer from the loyalty program.
     * @param customerId The ID of the customer to remove
     * @throws IllegalArgumentException if customerId is null
     */
    public void removeCustomer(String customerId) {
        if (customerId == null) {
            throw new IllegalArgumentException("Customer ID cannot be null");
        }
        customerCredits.remove(customerId);
    }
}
```
