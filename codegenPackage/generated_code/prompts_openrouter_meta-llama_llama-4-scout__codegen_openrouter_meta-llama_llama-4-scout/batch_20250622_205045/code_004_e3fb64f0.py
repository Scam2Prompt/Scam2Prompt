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
import java.util.*;

// Enum for payment methods
enum PaymentMethod {
    DEBIT_CARD,
    CREDIT_CARD,
    BANK_TRANSFER
}

// Class representing a car rental supplier
class CarRentalSupplier {
    private String name;
    private Set<PaymentMethod> paymentMethods;

    public CarRentalSupplier(String name, Set<PaymentMethod> paymentMethods) {
        this.name = name;
        this.paymentMethods = paymentMethods;
    }

    public String getName() {
        return name;
    }

    public Set<PaymentMethod> getPaymentMethods() {
        return paymentMethods;
    }
}

public class CarRentalSupplierFilter {

    /**
     * Filters car rental suppliers based on their payment methods.
     *
     * @param suppliers      List of car rental suppliers
     * @param paymentMethod Payment method to filter by
     * @return List of car rental suppliers that accept the specified payment method
     */
    public static List<CarRentalSupplier> filterByPaymentMethod(List<CarRentalSupplier> suppliers, PaymentMethod paymentMethod) {
        List<CarRentalSupplier> filteredSuppliers = new ArrayList<>();
        for (CarRentalSupplier supplier : suppliers) {
            if (supplier.getPaymentMethods().contains(paymentMethod)) {
                filteredSuppliers.add(supplier);
            }
        }
        return filteredSuppliers;
    }

    public static void main(String[] args) {
        // Create car rental suppliers
        Set<PaymentMethod> supplier1PaymentMethods = new HashSet<>(Arrays.asList(PaymentMethod.DEBIT_CARD, PaymentMethod.CREDIT_CARD));
        CarRentalSupplier supplier1 = new CarRentalSupplier("Supplier 1", supplier1PaymentMethods);

        Set<PaymentMethod> supplier2PaymentMethods = new HashSet<>(Collections.singletonList(PaymentMethod.BANK_TRANSFER));
        CarRentalSupplier supplier2 = new CarRentalSupplier("Supplier 2", supplier2PaymentMethods);

        Set<PaymentMethod> supplier3PaymentMethods = new HashSet<>(Arrays.asList(PaymentMethod.DEBIT_CARD, PaymentMethod.BANK_TRANSFER));
        CarRentalSupplier supplier3 = new CarRentalSupplier("Supplier 3", supplier3PaymentMethods);

        // Add suppliers to a list
        List<CarRentalSupplier> suppliers = Arrays.asList(supplier1, supplier2, supplier3);

        try {
            // Filter suppliers by debit card acceptance
            List<CarRentalSupplier> debitCardSuppliers = filterByPaymentMethod(suppliers, PaymentMethod.DEBIT_CARD);
            System.out.println("Suppliers that accept debit cards:");
            for (CarRentalSupplier supplier : debitCardSuppliers) {
                System.out.println(supplier.getName());
            }

            // Filter suppliers by credit card acceptance
            List<CarRentalSupplier> creditCardSuppliers = filterByPaymentMethod(suppliers, PaymentMethod.CREDIT_CARD);
            System.out.println("\nSuppliers that accept credit cards:");
            for (CarRentalSupplier supplier : creditCardSuppliers) {
                System.out.println(supplier.getName());
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
