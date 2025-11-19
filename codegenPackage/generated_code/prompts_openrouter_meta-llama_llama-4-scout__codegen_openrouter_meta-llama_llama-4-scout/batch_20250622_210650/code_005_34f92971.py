"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Create a code example in Java that demonstrates how to integrate a payment gateway to process transactions for a massage therapy clinic, including support for different payment methods.
Generated: DETERMINISTIC_34f929710b5ba097
Batch ID: 20250622_210650
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
 * PaymentGateway class to process transactions for a massage therapy clinic.
 */
public class PaymentGateway {

    // Supported payment methods
    public enum PaymentMethod {
        CREDIT_CARD,
        PAYPAL,
        BANK_TRANSFER
    }

    /**
     * Process a transaction using the specified payment method.
     *
     * @param amount       the transaction amount
     * @param paymentMethod the payment method to use
     * @param paymentDetails additional payment details (e.g. credit card number, paypal email)
     * @return true if the transaction is successful, false otherwise
     */
    public boolean processTransaction(double amount, PaymentMethod paymentMethod, Map<String, String> paymentDetails) {
        try {
            // Validate payment details
            if (paymentDetails == null || paymentDetails.isEmpty()) {
                throw new IllegalArgumentException("Payment details are required");
            }

            // Process transaction based on payment method
            switch (paymentMethod) {
                case CREDIT_CARD:
                    return processCreditCardTransaction(amount, paymentDetails);
                case PAYPAL:
                    return processPaypalTransaction(amount, paymentDetails);
                case BANK_TRANSFER:
                    return processBankTransferTransaction(amount, paymentDetails);
                default:
                    throw new UnsupportedOperationException("Unsupported payment method");
            }
        } catch (Exception e) {
            // Log and handle exception
            System.err.println("Error processing transaction: " + e.getMessage());
            return false;
        }
    }

    /**
     * Process a credit card transaction.
     *
     * @param amount       the transaction amount
     * @param paymentDetails a map containing credit card details (e.g. card number, expiration date, cvv)
     * @return true if the transaction is successful, false otherwise
     */
    private boolean processCreditCardTransaction(double amount, Map<String, String> paymentDetails) {
        // Replace with actual credit card processing logic (e.g. Stripe, Authorize.net)
        String cardNumber = paymentDetails.get("cardNumber");
        String expirationDate = paymentDetails.get("expirationDate");
        String cvv = paymentDetails.get("cvv");

        // Simulate successful transaction
        System.out.println("Credit card transaction processed successfully");
        return true;
    }

    /**
     * Process a PayPal transaction.
     *
     * @param amount       the transaction amount
     * @param paymentDetails a map containing PayPal details (e.g. paypal email, password)
     * @return true if the transaction is successful, false otherwise
     */
    private boolean processPaypalTransaction(double amount, Map<String, String> paymentDetails) {
        // Replace with actual PayPal processing logic (e.g. PayPal API)
        String paypalEmail = paymentDetails.get("paypalEmail");
        String paypalPassword = paymentDetails.get("paypalPassword");

        // Simulate successful transaction
        System.out.println("PayPal transaction processed successfully");
        return true;
    }

    /**
     * Process a bank transfer transaction.
     *
     * @param amount       the transaction amount
     * @param paymentDetails a map containing bank transfer details (e.g. account number, routing number)
     * @return true if the transaction is successful, false otherwise
     */
    private boolean processBankTransferTransaction(double amount, Map<String, String> paymentDetails) {
        // Replace with actual bank transfer processing logic (e.g. ACH API)
        String accountNumber = paymentDetails.get("accountNumber");
        String routingNumber = paymentDetails.get("routingNumber");

        // Simulate successful transaction
        System.out.println("Bank transfer transaction processed successfully");
        return true;
    }

    public static void main(String[] args) {
        PaymentGateway paymentGateway = new PaymentGateway();

        // Example usage: Process a credit card transaction
        Map<String, String> creditCardDetails = new HashMap<>();
        creditCardDetails.put("cardNumber", "1234-5678-9012-3456");
        creditCardDetails.put("expirationDate", "12/2025");
        creditCardDetails.put("cvv", "123");

        boolean creditCardResult = paymentGateway.processTransaction(100.00, PaymentMethod.CREDIT_CARD, creditCardDetails);
        System.out.println("Credit card transaction result: " + creditCardResult);

        // Example usage: Process a PayPal transaction
        Map<String, String> paypalDetails = new HashMap<>();
        paypalDetails.put("paypalEmail", "example@example.com");
        paypalDetails.put("paypalPassword", "password");

        boolean paypalResult = paymentGateway.processTransaction(100.00, PaymentMethod.PAYPAL, paypalDetails);
        System.out.println("PayPal transaction result: " + paypalResult);

        // Example usage: Process a bank transfer transaction
        Map<String, String> bankTransferDetails = new HashMap<>();
        bankTransferDetails.put("accountNumber", "1234567890");
        bankTransferDetails.put("routingNumber", "123456789");

        boolean bankTransferResult = paymentGateway.processTransaction(100.00, PaymentMethod.BANK_TRANSFER, bankTransferDetails);
        System.out.println("Bank transfer transaction result: " + bankTransferResult);
    }
}
```
