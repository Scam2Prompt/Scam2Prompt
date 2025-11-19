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
 * PaymentGateway interface defines the methods for processing payments.
 */
interface PaymentGateway {
    boolean processPayment(PaymentDetails paymentDetails);
}

/**
 * PaymentDetails class holds the information required to process a payment.
 */
class PaymentDetails {
    private String paymentMethod; // e.g., "CREDIT_CARD", "PAYPAL"
    private double amount;
    private String currency;

    public PaymentDetails(String paymentMethod, double amount, String currency) {
        this.paymentMethod = paymentMethod;
        this.amount = amount;
        this.currency = currency;
    }

    public String getPaymentMethod() {
        return paymentMethod;
    }

    public double getAmount() {
        return amount;
    }

    public String getCurrency() {
        return currency;
    }
}

/**
 * CreditCardPaymentGateway class implements the PaymentGateway interface for credit card payments.
 */
class CreditCardPaymentGateway implements PaymentGateway {
    @Override
    public boolean processPayment(PaymentDetails paymentDetails) {
        // Simulate credit card payment processing
        System.out.println("Processing credit card payment of " + paymentDetails.getAmount() + " " + paymentDetails.getCurrency());
        // Here you would integrate with a real credit card processing API
        return true; // Assume payment is successful
    }
}

/**
 * PayPalPaymentGateway class implements the PaymentGateway interface for PayPal payments.
 */
class PayPalPaymentGateway implements PaymentGateway {
    @Override
    public boolean processPayment(PaymentDetails paymentDetails) {
        // Simulate PayPal payment processing
        System.out.println("Processing PayPal payment of " + paymentDetails.getAmount() + " " + paymentDetails.getCurrency());
        // Here you would integrate with a real PayPal API
        return true; // Assume payment is successful
    }
}

/**
 * PaymentProcessor class handles the payment processing logic.
 */
class PaymentProcessor {
    private Map<String, PaymentGateway> paymentGateways;

    public PaymentProcessor() {
        paymentGateways = new HashMap<>();
        // Register available payment gateways
        paymentGateways.put("CREDIT_CARD", new CreditCardPaymentGateway());
        paymentGateways.put("PAYPAL", new PayPalPaymentGateway());
    }

    /**
     * Processes a payment using the specified payment method.
     *
     * @param paymentDetails The details of the payment to process.
     * @return true if the payment was processed successfully, false otherwise.
     */
    public boolean processPayment(PaymentDetails paymentDetails) {
        PaymentGateway gateway = paymentGateways.get(paymentDetails.getPaymentMethod());
        if (gateway == null) {
            System.err.println("Error: Unsupported payment method: " + paymentDetails.getPaymentMethod());
            return false;
        }
        return gateway.processPayment(paymentDetails);
    }
}

/**
 * Main class to demonstrate payment processing for a massage therapy clinic.
 */
public class MassageTherapyClinic {
    public static void main(String[] args) {
        PaymentProcessor paymentProcessor = new PaymentProcessor();

        // Example payment details
        PaymentDetails creditCardPayment = new PaymentDetails("CREDIT_CARD", 100.0, "USD");
        PaymentDetails paypalPayment = new PaymentDetails("PAYPAL", 150.0, "USD");

        // Process credit card payment
        if (paymentProcessor.processPayment(creditCardPayment)) {
            System.out.println("Credit card payment processed successfully.");
        } else {
            System.out.println("Credit card payment failed.");
        }

        // Process PayPal payment
        if (paymentProcessor.processPayment(paypalPayment)) {
            System.out.println("PayPal payment processed successfully.");
        } else {
            System.out.println("PayPal payment failed.");
        }

        // Attempt to process an unsupported payment method
        PaymentDetails unsupportedPayment = new PaymentDetails("BITCOIN", 200.0, "USD");
        paymentProcessor.processPayment(unsupportedPayment);
    }
}
```
