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
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

/**
 * PaymentGateway interface defining the contract for payment processing.
 */
interface PaymentGateway {
    PaymentResponse processPayment(PaymentRequest request) throws PaymentException;
}

/**
 * Represents a payment request with necessary details.
 */
class PaymentRequest {
    private String transactionId;
    private BigDecimal amount;
    private String currency;
    private PaymentMethod paymentMethod;
    private Map<String, String> additionalDetails;

    public PaymentRequest(String transactionId, BigDecimal amount, String currency, 
                         PaymentMethod paymentMethod, Map<String, String> additionalDetails) {
        this.transactionId = transactionId;
        this.amount = amount;
        this.currency = currency;
        this.paymentMethod = paymentMethod;
        this.additionalDetails = additionalDetails;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public String getCurrency() {
        return currency;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }

    public Map<String, String> getAdditionalDetails() {
        return additionalDetails;
    }
}

/**
 * Represents the response from a payment gateway.
 */
class PaymentResponse {
    private String transactionId;
    private boolean success;
    private String message;
    private String gatewayReference;

    public PaymentResponse(String transactionId, boolean success, 
                          String message, String gatewayReference) {
        this.transactionId = transactionId;
        this.success = success;
        this.message = message;
        this.gatewayReference = gatewayReference;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public boolean isSuccess() {
        return success;
    }

    public String getMessage() {
        return message;
    }

    public String getGatewayReference() {
        return gatewayReference;
    }
}

/**
 * Enum representing different payment methods.
 */
enum PaymentMethod {
    CREDIT_CARD,
    DEBIT_CARD,
    PAYPAL,
    BANK_TRANSFER
}

/**
 * Custom exception for payment processing errors.
 */
class PaymentException extends Exception {
    public PaymentException(String message) {
        super(message);
    }

    public PaymentException(String message, Throwable cause) {
        super(message, cause);
    }
}

/**
 * Mock implementation of a payment gateway for demonstration purposes.
 */
class MockPaymentGateway implements PaymentGateway {
    @Override
    public PaymentResponse processPayment(PaymentRequest request) throws PaymentException {
        // Validate payment request
        if (request.getAmount().compareTo(BigDecimal.ZERO) <= 0) {
            throw new PaymentException("Amount must be greater than zero");
        }

        // Simulate processing delay
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new PaymentException("Payment processing interrupted", e);
        }

        // Simulate successful payment 90% of the time
        boolean success = Math.random() > 0.1;
        String message = success ? "Payment processed successfully" : "Payment failed";
        String reference = "MOCK-" + System.currentTimeMillis();

        return new PaymentResponse(
            request.getTransactionId(),
            success,
            message,
            reference
        );
    }
}

/**
 * Payment processor that handles different payment methods.
 */
class PaymentProcessor {
    private PaymentGateway paymentGateway;

    public PaymentProcessor(PaymentGateway paymentGateway) {
        this.paymentGateway = paymentGateway;
    }

    public PaymentResponse process(PaymentRequest request) throws PaymentException {
        // Additional validation based on payment method
        switch (request.getPaymentMethod()) {
            case CREDIT_CARD:
            case DEBIT_CARD:
                if (!request.getAdditionalDetails().containsKey("cardNumber")) {
                    throw new PaymentException("Card number is required for card payments");
                }
                break;
            case PAYPAL:
                if (!request.getAdditionalDetails().containsKey("paypalEmail")) {
                    throw new PaymentException("PayPal email is required for PayPal payments");
                }
                break;
            case BANK_TRANSFER:
                if (!request.getAdditionalDetails().containsKey("accountNumber")) {
                    throw new PaymentException("Account number is required for bank transfers");
                }
                break;
        }

        return paymentGateway.processPayment(request);
    }
}

/**
 * Main class demonstrating payment processing for a massage therapy clinic.
 */
public class MassageClinicPaymentSystem {
    public static void main(String[] args) {
        // Initialize payment processor with mock gateway
        PaymentProcessor processor = new PaymentProcessor(new MockPaymentGateway());

        // Example credit card payment
        Map<String, String> cardDetails = new HashMap<>();
        cardDetails.put("cardNumber", "4111111111111111");
        cardDetails.put("expiryDate", "12/25");
        cardDetails.put("cvv", "123");

        PaymentRequest cardPayment = new PaymentRequest(
            "TXN-001",
            new BigDecimal("75.00"),
            "USD",
            PaymentMethod.CREDIT_CARD,
            cardDetails
        );

        try {
            PaymentResponse response = processor.process(cardPayment);
            System.out.println("Payment Status: " + (response.isSuccess() ? "Success" : "Failed"));
            System.out.println("Message: " + response.getMessage());
            System.out.println("Gateway Reference: " + response.getGatewayReference());
        } catch (PaymentException e) {
            System.err.println("Payment Error: " + e.getMessage());
        }

        // Example PayPal payment
        Map<String, String> paypalDetails = new HashMap<>();
        paypalDetails.put("paypalEmail", "client@example.com");

        PaymentRequest paypalPayment = new PaymentRequest(
            "TXN-002",
            new BigDecimal("60.00"),
            "USD",
            PaymentMethod.PAYPAL,
            paypalDetails
        );

        try {
            PaymentResponse response = processor.process(paypalPayment);
            System.out.println("Payment Status: " + (response.isSuccess() ? "Success" : "Failed"));
            System.out.println("Message: " + response.getMessage());
            System.out.println("Gateway Reference: " + response.getGatewayReference());
        } catch (PaymentException e) {
            System.err.println("Payment Error: " + e.getMessage());
        }
    }
}
```
