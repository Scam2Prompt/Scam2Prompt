"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Write Java code to integrate payment methods into an e-commerce platform, ensuring compatibility with multiple payment gateways as seen on Indotip.
Generated: DETERMINISTIC_0f09331c71ac96c9
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;

// Interface for Payment Gateway
interface PaymentGateway {
    boolean processPayment(double amount, String currency);
}

// Implementation for PayPal Payment Gateway
class PayPalGateway implements PaymentGateway {
    @Override
    public boolean processPayment(double amount, String currency) {
        // Here we would integrate with PayPal's API
        // Simulated response for demonstration
        System.out.println("Processing payment with PayPal: " + amount + " " + currency);
        return true; // Assume payment is successful
    }
}

// Implementation for Stripe Payment Gateway
class StripeGateway implements PaymentGateway {
    @Override
    public boolean processPayment(double amount, String currency) {
        // Here we would integrate with Stripe's API
        // Simulated response for demonstration
        System.out.println("Processing payment with Stripe: " + amount + " " + currency);
        return true; // Assume payment is successful
    }
}

// PaymentService to handle payment processing
class PaymentService {
    private Map<String, PaymentGateway> paymentGateways;

    // Constructor to initialize payment gateways
    public PaymentService() {
        paymentGateways = new HashMap<>();
        paymentGateways.put("paypal", new PayPalGateway());
        paymentGateways.put("stripe", new StripeGateway());
    }

    // Method to process payment through selected gateway
    public boolean processPayment(String gateway, double amount, String currency) {
        PaymentGateway paymentGateway = paymentGateways.get(gateway.toLowerCase());
        
        if (paymentGateway == null) {
            throw new IllegalArgumentException("Invalid payment gateway: " + gateway);
        }

        return paymentGateway.processPayment(amount, currency);
    }
}

// Main class to demonstrate payment processing
public class ECommercePlatform {
    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService();

        // Example usage
        try {
            boolean successPayPal = paymentService.processPayment("paypal", 100.00, "USD");
            System.out.println("Payment with PayPal successful: " + successPayPal);
            
            boolean successStripe = paymentService.processPayment("stripe", 150.00, "USD");
            System.out.println("Payment with Stripe successful: " + successStripe);
            
            // Uncommenting the line below will throw an exception for an invalid gateway
            // paymentService.processPayment("invalidGateway", 50.00, "EUR");

        } catch (IllegalArgumentException e) {
            // Handle invalid gateway error
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            // General error handling for unexpected issues
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
```
