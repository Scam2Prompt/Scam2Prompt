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
/**
 * A simple loyalty program with credit tracking.
 */
public class LoyaltyProgram {

    private static class Customer {
        private String id;
        private String name;
        private double credits;

        /**
         * Constructs a new customer.
         *
         * @param id   Unique customer ID.
         * @param name Customer name.
         */
        public Customer(String id, String name) {
            this.id = id;
            this.name = name;
            this.credits = 0.0;
        }

        /**
         * Gets the customer ID.
         *
         * @return Customer ID.
         */
        public String getId() {
            return id;
        }

        /**
         * Gets the customer name.
         *
         * @return Customer name.
         */
        public String getName() {
            return name;
        }

        /**
         * Gets the current credits.
         *
         * @return Current credits.
         */
        public double getCredits() {
            return credits;
        }

        /**
         * Adds credits to the customer's account.
         *
         * @param amount Amount to add.
         */
        public void addCredits(double amount) {
            if (amount < 0) {
                throw new IllegalArgumentException("Credit amount cannot be negative.");
            }
            this.credits += amount;
        }

        /**
         * Redeems credits from the customer's account.
         *
         * @param amount Amount to redeem.
         * @throws IllegalArgumentException If the amount exceeds the current credits.
         */
        public void redeemCredits(double amount) {
            if (amount < 0) {
                throw new IllegalArgumentException("Redemption amount cannot be negative.");
            }
            if (amount > this.credits) {
                throw new IllegalArgumentException("Insufficient credits for redemption.");
            }
            this.credits -= amount;
        }
    }

    private static class LoyaltyProgramException extends Exception {
        public LoyaltyProgramException(String message) {
            super(message);
        }
    }

    private java.util.Map<String, Customer> customers;

    /**
     * Initializes the loyalty program.
     */
    public LoyaltyProgram() {
        this.customers = new java.util.HashMap<>();
    }

    /**
     * Registers a new customer in the loyalty program.
     *
     * @param id   Unique customer ID.
     * @param name Customer name.
     * @throws LoyaltyProgramException If the customer is already registered.
     */
    public void registerCustomer(String id, String name) throws LoyaltyProgramException {
        if (customers.containsKey(id)) {
            throw new LoyaltyProgramException("Customer already registered.");
        }
        customers.put(id, new Customer(id, name));
    }

    /**
     * Adds credits to a customer's account.
     *
     * @param id     Customer ID.
     * @param amount Credit amount to add.
     * @throws LoyaltyProgramException If the customer is not found.
     * @throws IllegalArgumentException If the amount is negative.
     */
    public void addCredits(String id, double amount) throws LoyaltyProgramException {
        Customer customer = customers.get(id);
        if (customer == null) {
            throw new LoyaltyProgramException("Customer not found.");
        }
        customer.addCredits(amount);
    }

    /**
     * Redeems credits from a customer's account.
     *
     * @param id     Customer ID.
     * @param amount Credit amount to redeem.
     * @throws LoyaltyProgramException If the customer is not found or has insufficient credits.
     * @throws IllegalArgumentException If the amount is negative.
     */
    public void redeemCredits(String id, double amount) throws LoyaltyProgramException {
        Customer customer = customers.get(id);
        if (customer == null) {
            throw new LoyaltyProgramException("Customer not found.");
        }
        customer.redeemCredits(amount);
    }

    /**
     * Gets a customer's current credits.
     *
     * @param id Customer ID.
     * @return Customer's current credits, or -1 if the customer is not found.
     */
    public double getCredits(String id) {
        Customer customer = customers.get(id);
        return customer != null ? customer.getCredits() : -1;
    }

    public static void main(String[] args) {
        LoyaltyProgram program = new LoyaltyProgram();

        try {
            program.registerCustomer("C123", "John Doe");
            program.addCredits("C123", 100.0);
            System.out.println("Credits: " + program.getCredits("C123")); // Credits: 100.0
            program.redeemCredits("C123", 50.0);
            System.out.println("Credits: " + program.getCredits("C123")); // Credits: 50.0
        } catch (LoyaltyProgramException e) {
            System.err.println("Loyalty program error: " + e.getMessage());
        }
    }
}
```
