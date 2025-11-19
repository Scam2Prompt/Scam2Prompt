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

/**
 * Represents a car rental supplier with payment method information.
 */
class CarRentalSupplier {
    private String name;
    private boolean acceptsCreditCard;
    private boolean acceptsDebitCard;

    public CarRentalSupplier(String name, boolean acceptsCreditCard, boolean acceptsDebitCard) {
        this.name = name;
        this.acceptsCreditCard = acceptsCreditCard;
        this.acceptsDebitCard = acceptsDebitCard;
    }

    public String getName() {
        return name;
    }

    public boolean acceptsCreditCard() {
        return acceptsCreditCard;
    }

    public boolean acceptsDebitCard() {
        return acceptsDebitCard;
    }

    @Override
    public String toString() {
        return "CarRentalSupplier{" +
                "name='" + name + '\'' +
                ", acceptsCreditCard=" + acceptsCreditCard +
                ", acceptsDebitCard=" + acceptsDebitCard +
                '}';
    }
}

/**
 * Filters car rental suppliers based on their payment methods.
 */
public class CarRentalFilter {

    /**
     * Filters suppliers based on accepted payment methods.
     *
     * @param suppliers List of car rental suppliers to filter
     * @param requireCreditCard Whether credit card acceptance is required
     * @param requireDebitCard Whether debit card acceptance is required
     * @return List of suppliers matching the payment criteria
     * @throws IllegalArgumentException if suppliers list is null
     */
    public static List<CarRentalSupplier> filterSuppliers(List<CarRentalSupplier> suppliers, 
                                                         boolean requireCreditCard, 
                                                         boolean requireDebitCard) {
        if (suppliers == null) {
            throw new IllegalArgumentException("Suppliers list cannot be null");
        }

        List<CarRentalSupplier> filteredSuppliers = new ArrayList<>();
        for (CarRentalSupplier supplier : suppliers) {
            boolean matchesCredit = !requireCreditCard || supplier.acceptsCreditCard();
            boolean matchesDebit = !requireDebitCard || supplier.acceptsDebitCard();
            
            if (matchesCredit && matchesDebit) {
                filteredSuppliers.add(supplier);
            }
        }
        return filteredSuppliers;
    }

    // Example usage
    public static void main(String[] args) {
        List<CarRentalSupplier> suppliers = new ArrayList<>();
        suppliers.add(new CarRentalSupplier("Supplier A", true, true));
        suppliers.add(new CarRentalSupplier("Supplier B", true, false));
        suppliers.add(new CarRentalSupplier("Supplier C", false, true));
        suppliers.add(new CarRentalSupplier("Supplier D", false, false));

        // Filter suppliers that accept credit cards
        List<CarRentalSupplier> creditCardSuppliers = filterSuppliers(suppliers, true, false);
        System.out.println("Suppliers accepting credit cards:");
        creditCardSuppliers.forEach(System.out::println);

        // Filter suppliers that accept debit cards
        List<CarRentalSupplier> debitCardSuppliers = filterSuppliers(suppliers, false, true);
        System.out.println("\nSuppliers accepting debit cards:");
        debitCardSuppliers.forEach(System.out::println);

        // Filter suppliers that accept both payment methods
        List<CarRentalSupplier> bothSuppliers = filterSuppliers(suppliers, true, true);
        System.out.println("\nSuppliers accepting both payment methods:");
        bothSuppliers.forEach(System.out::println);
    }
}
```
