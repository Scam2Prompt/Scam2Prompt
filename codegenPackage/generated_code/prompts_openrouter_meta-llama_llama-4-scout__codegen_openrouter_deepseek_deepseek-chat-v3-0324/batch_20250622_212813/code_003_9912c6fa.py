"""
Generated Code Metadata:
========================
Original URL: https://www.guardian-associates.com
Prompt: "Develop a code snippet in Java to automate the monitoring and reporting of a Rolling Reserve account, including transaction tracking and alert systems for suspicious activity."
Generated: DETERMINISTIC_9912c6fa5ba30414
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;
import java.time.*;
import java.math.BigDecimal;
import java.util.stream.Collectors;

// Interface for notification service
interface NotificationService {
    void sendAlert(String message);
}

// Email notification implementation
class EmailNotificationService implements NotificationService {
    @Override
    public void sendAlert(String message) {
        // Implementation for sending email
        System.out.println("Email Alert: " + message);
    }
}

// SMS notification implementation
class SMSNotificationService implements NotificationService {
    @Override
    public void sendAlert(String message) {
        // Implementation for sending SMS
        System.out.println("SMS Alert: " + message);
    }
}

// Represents a transaction in the rolling reserve account
class Transaction {
    private String transactionId;
    private LocalDateTime timestamp;
    private BigDecimal amount;
    private String merchantId;
    private String description;

    public Transaction(String transactionId, LocalDateTime timestamp, BigDecimal amount, 
                      String merchantId, String description) {
        this.transactionId = transactionId;
        this.timestamp = timestamp;
        this.amount = amount;
        this.merchantId = merchantId;
        this.description = description;
    }

    // Getters
    public String getTransactionId() { return transactionId; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public BigDecimal getAmount() { return amount; }
    public String getMerchantId() { return merchantId; }
    public String getDescription() { return description; }
}

// Represents the rolling reserve account
class RollingReserveAccount {
    private String accountId;
    private BigDecimal balance;
    private List<Transaction> transactions;
    private BigDecimal reservePercentage;
    private BigDecimal thresholdAmount;
    private List<NotificationService> notificationServices;

    public RollingReserveAccount(String accountId, BigDecimal initialBalance, 
                               BigDecimal reservePercentage, BigDecimal thresholdAmount) {
        this.accountId = accountId;
        this.balance = initialBalance;
        this.reservePercentage = reservePercentage;
        this.thresholdAmount = thresholdAmount;
        this.transactions = new ArrayList<>();
        this.notificationServices = new ArrayList<>();
    }

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
        BigDecimal reserveAmount = calculateReserveAmount(transaction.getAmount());
        balance = balance.subtract(reserveAmount);
        checkForSuspiciousActivity(transaction);
    }

    private BigDecimal calculateReserveAmount(BigDecimal transactionAmount) {
        return transactionAmount.multiply(reservePercentage).divide(BigDecimal.valueOf(100));
    }

    private void checkForSuspiciousActivity(Transaction transaction) {
        // Check for large transactions
        if (transaction.getAmount().compareTo(thresholdAmount) > 0) {
            triggerAlert("Large transaction detected: " + transaction.getAmount() + 
                        " for merchant " + transaction.getMerchantId());
        }

        // Check for unusual frequency
        long recentTransactions = transactions.stream()
            .filter(t -> t.getTimestamp().isAfter(LocalDateTime.now().minusHours(1)))
            .count();
        
        if (recentTransactions > 5) {
            triggerAlert("Unusual transaction frequency detected: " + recentTransactions + 
                        " transactions in the last hour");
        }
    }

    public void addNotificationService(NotificationService service) {
        notificationServices.add(service);
    }

    private void triggerAlert(String message) {
        for (NotificationService service : notificationServices) {
            service.sendAlert(message);
        }
    }

    public BigDecimal getBalance() { return balance; }

    public List<Transaction> getTransactions() { return Collections.unmodifiableList(transactions); }

    public List<Transaction> getTransactionsForMerchant(String merchantId) {
        return transactions.stream()
            .filter(t -> t.getMerchantId().equals(merchantId))
            .collect(Collectors.toList());
    }

    public BigDecimal getTotalReserveAmount() {
        return transactions.stream()
            .map(t -> calculateReserveAmount(t.getAmount()))
            .reduce(BigDecimal.ZERO, BigDecimal::add);
    }
}

// Main class for monitoring and reporting
public class RollingReserveMonitor {
    public static void main(String[] args) {
        // Create account with initial balance, reserve percentage, and threshold
        RollingReserveAccount account = new RollingReserveAccount(
            "RR-12345", 
            new BigDecimal("100000.00"), 
            new BigDecimal("10"), 
            new BigDecimal("5000.00")
        );

        // Add notification services
        account.addNotificationService(new EmailNotificationService());
        account.addNotificationService(new SMSNotificationService());

        // Simulate transactions
        account.addTransaction(new Transaction(
            "TXN-001", 
            LocalDateTime.now(), 
            new BigDecimal("1000.00"), 
            "MERCHANT-001", 
            "Payment for goods"
        ));

        account.addTransaction(new Transaction(
            "TXN-002", 
            LocalDateTime.now().minusMinutes(10), 
            new BigDecimal("5500.00"), 
            "MERCHANT-002", 
            "Large payment"
        ));

        // Add multiple transactions to trigger frequency alert
        for (int i = 0; i < 6; i++) {
            account.addTransaction(new Transaction(
                "TXN-" + (100 + i), 
                LocalDateTime.now().minusMinutes(i * 5), 
                new BigDecimal("100.00"), 
                "MERCHANT-003", 
                "Small payment " + i
            ));
        }

        // Generate report
        System.out.println("\n=== Account Summary ===");
        System.out.println("Account ID: " + account.getAccountId());
        System.out.println("Current Balance: " + account.getBalance());
        System.out.println("Total Reserve Amount: " + account.getTotalReserveAmount());
        System.out.println("Total Transactions: " + account.getTransactions().size());

        System.out.println("\n=== Recent Transactions ===");
        account.getTransactions().stream()
            .sorted(Comparator.comparing(Transaction::getTimestamp).reversed())
            .limit(5)
            .forEach(t -> System.out.println(
                t.getTimestamp() + " - " + t.getMerchantId() + " - " + t.getAmount()
            ));
    }
}
```
