"""
Generated Code Metadata:
========================
Original URL: https://agodarentacar.com
Prompt: Create a code snippet in Java to filter car rental suppliers based on their payment methods, such as debit or credit card acceptance.
Generated: DETERMINISTIC_e3fb64f086257f1e
Batch ID: 20250622_205045
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
import java.util.stream.Collectors;

/**
 * Represents a car rental supplier with a name and accepted payment methods.
 */
class CarRentalSupplier {
    private String name;
    private List<String> acceptedPaymentMethods;

    public CarRentalSupplier(String name, List<String> acceptedPaymentMethods) {
        this.name = name;
        this.acceptedPaymentMethods = acceptedPaymentMethods;
    }

    public String getName() {
        return name;
    }

    public List<String> getAcceptedPaymentMethods() {
        return acceptedPaymentMethods;
    }
}

/**
 * Utility class for filtering car rental suppliers based on payment methods.
 */
public class CarRentalFilter {

    /**
     * Filters the list of car rental suppliers based on the specified payment method.
     *
     * @param suppliers the list of car rental suppliers to filter
     * @param paymentMethod the payment method to filter by (e.g., "Debit Card", "Credit Card")
     * @return a list of suppliers that accept the specified payment method
     * @throws IllegalArgumentException if the suppliers list is null or paymentMethod is null or empty
     */
    public static List<CarRentalSupplier> filterSuppliersByPaymentMethod(
            List<CarRentalSupplier> suppliers, String paymentMethod) {
        
        // Validate input parameters
        if (suppliers == null) {
            throw new IllegalArgumentException("Suppliers list cannot be null.");
        }
        if (paymentMethod == null || paymentMethod.isEmpty()) {
            throw new IllegalArgumentException("Payment method cannot be null or empty.");
        }

        // Filter suppliers based on the accepted payment method
        return suppliers.stream()
                .filter(supplier -> supplier.getAcceptedPaymentMethods().contains(paymentMethod))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        // Sample data
        List<CarRentalSupplier> suppliers = new ArrayList<>();
        suppliers.add(new CarRentalSupplier("Supplier A", List.of("Credit Card", "Debit Card")));
        suppliers.add(new CarRentalSupplier("Supplier B", List.of("Credit Card")));
        suppliers.add(new CarRentalSupplier("Supplier C", List.of("Debit Card")));

        // Filter suppliers that accept Debit Card
        try {
            List<CarRentalSupplier> debitCardSuppliers = filterSuppliersByPaymentMethod(suppliers, "Debit Card");
            System.out.println("Suppliers accepting Debit Card:");
            debitCardSuppliers.forEach(supplier -> System.out.println(supplier.getName()));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
