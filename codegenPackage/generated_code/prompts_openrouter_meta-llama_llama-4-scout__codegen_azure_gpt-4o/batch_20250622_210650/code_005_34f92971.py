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

// PaymentGatewayIntegration.java
public class PaymentGatewayIntegration {

    public static void main(String[] args) {
        // Simulate a transaction for a massage therapy clinic
        try {
            PaymentGateway gateway = new PaymentGateway();
            TransactionDetails transaction = new TransactionDetails(
                    "12345", // Transaction ID
                    100.00,  // Amount
                    "USD",   // Currency
                    PaymentMethod.CREDIT_CARD, // Payment Method
                    "John Doe", // Customer Name
                    "john.doe@example.com" // Customer Email
            );

            // Process the payment
            PaymentResponse response = gateway.processPayment(transaction);

            // Handle the response
            if (response.isSuccessful()) {
                System.out.println("Payment successful! Transaction ID: " + response.getTransactionId());
            } else {
                System.out.println("Payment failed: " + response.getErrorMessage());
            }
        } catch (Exception e) {
            System.err.println("An error occurred while processing the payment: " + e.getMessage());
        }
    }
}

// Enum for supported payment methods
enum PaymentMethod {
    CREDIT_CARD,
    DEBIT_CARD,
    PAYPAL,
    APPLE_PAY,
    GOOGLE_PAY
}

// Class to hold transaction details
class TransactionDetails {
    private String transactionId;
    private double amount;
    private String currency;
    private PaymentMethod paymentMethod;
    private String customerName;
    private String customerEmail;

    public TransactionDetails(String transactionId, double amount, String currency, PaymentMethod paymentMethod,
                              String customerName, String customerEmail) {
        this.transactionId = transactionId;
        this.amount = amount;
        this.currency = currency;
        this.paymentMethod = paymentMethod;
        this.customerName = customerName;
        this.customerEmail = customerEmail;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public double getAmount() {
        return amount;
    }

    public String getCurrency() {
        return currency;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }

    public String getCustomerName() {
        return customerName;
    }

    public String getCustomerEmail() {
        return customerEmail;
    }
}

// Class to simulate a payment gateway
class PaymentGateway {

    // Simulate processing a payment
    public PaymentResponse processPayment(TransactionDetails transaction) throws Exception {
        // Simulate API call to payment gateway
        System.out.println("Processing payment for transaction ID: " + transaction.getTransactionId());
        System.out.println("Amount: " + transaction.getAmount() + " " + transaction.getCurrency());
        System.out.println("Payment Method: " + transaction.getPaymentMethod());
        System.out.println("Customer: " + transaction.getCustomerName() + " (" + transaction.getCustomerEmail() + ")");

        // Simulate success or failure
        boolean isSuccess = Math.random() > 0.2; // 80% chance of success

        if (isSuccess) {
            return new PaymentResponse(true, transaction.getTransactionId(), null);
        } else {
            return new PaymentResponse(false, null, "Payment gateway error: Insufficient funds.");
        }
    }
}

// Class to hold payment response details
class PaymentResponse {
    private boolean successful;
    private String transactionId;
    private String errorMessage;

    public PaymentResponse(boolean successful, String transactionId, String errorMessage) {
        this.successful = successful;
        this.transactionId = transactionId;
        this.errorMessage = errorMessage;
    }

    public boolean isSuccessful() {
        return successful;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public String getErrorMessage() {
        return errorMessage;
    }
}
```
