"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Generate code in Java to implement a secure deposit and withdrawal system for an online gambling platform, ensuring compliance with the HONGTOGEL payment methods.
Generated: DETERMINISTIC_2a3ba57cd8154df5
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

/**
 * Represents a secure deposit and withdrawal system for an online gambling platform.
 * This implementation is designed to ensure compliance with HONGTOGEL payment methods.
 */
public class SecureTransactionSystem {
    
    // Constants for transaction limits
    private static final BigDecimal MIN_DEPOSIT_AMOUNT = new BigDecimal("10.00");
    private static final BigDecimal MAX_DEPOSIT_AMOUNT = new BigDecimal("5000.00");
    private static final BigDecimal MIN_WITHDRAWAL_AMOUNT = new BigDecimal("20.00");
    private static final BigDecimal MAX_WITHDRAWAL_AMOUNT = new BigDecimal("3000.00");

    // User balance map
    private final Map<String, BigDecimal> userBalances;

    public SecureTransactionSystem() {
        this.userBalances = new HashMap<>();
    }

    /**
     * Deposits a specified amount into the user's account.
     * 
     * @param userId The ID of the user making the deposit.
     * @param amount The amount to deposit.
     * @throws IllegalArgumentException If the deposit amount is invalid.
     */
    public void deposit(String userId, BigDecimal amount) {
        validateDepositAmount(amount);
        userBalances.put(userId, userBalances.getOrDefault(userId, BigDecimal.ZERO).add(amount));
        System.out.println("Deposit successful! New balance for " + userId + ": " + userBalances.get(userId));
    }

    /**
     * Withdraws a specified amount from the user's account.
     * 
     * @param userId The ID of the user making the withdrawal.
     * @param amount The amount to withdraw.
     * @throws IllegalArgumentException If the withdrawal amount is invalid or exceeds balance.
     */
    public void withdraw(String userId, BigDecimal amount) {
        validateWithdrawalAmount(userId, amount);
        userBalances.put(userId, userBalances.get(userId).subtract(amount));
        System.out.println("Withdrawal successful! New balance for " + userId + ": " + userBalances.get(userId));
    }

    /**
     * Validates the deposit amount.
     * 
     * @param amount The amount to validate.
     * @throws IllegalArgumentException If the amount is invalid.
     */
    private void validateDepositAmount(BigDecimal amount) {
        if (amount == null || amount.compareTo(MIN_DEPOSIT_AMOUNT) < 0 || amount.compareTo(MAX_DEPOSIT_AMOUNT) > 0) {
            throw new IllegalArgumentException("Invalid deposit amount. Must be between " + MIN_DEPOSIT_AMOUNT + " and " + MAX_DEPOSIT_AMOUNT + ".");
        }
    }

    /**
     * Validates the withdrawal amount.
     * 
     * @param userId The ID of the user.
     * @param amount The amount to validate.
     * @throws IllegalArgumentException If the amount is invalid or exceeds the user's balance.
     */
    private void validateWithdrawalAmount(String userId, BigDecimal amount) {
        if (amount == null || amount.compareTo(MIN_WITHDRAWAL_AMOUNT) < 0 || amount.compareTo(MAX_WITHDRAWAL_AMOUNT) > 0) {
            throw new IllegalArgumentException("Invalid withdrawal amount. Must be between " + MIN_WITHDRAWAL_AMOUNT + " and " + MAX_WITHDRAWAL_AMOUNT + ".");
        }
        BigDecimal currentBalance = userBalances.getOrDefault(userId, BigDecimal.ZERO);
        if (currentBalance.compareTo(amount) < 0) {
            throw new IllegalArgumentException("Insufficient funds. Current balance: " + currentBalance);
        }
    }

    /**
     * Retrieves the current balance for a specified user.
     * 
     * @param userId The ID of the user.
     * @return The current balance.
     */
    public BigDecimal getBalance(String userId) {
        return userBalances.getOrDefault(userId, BigDecimal.ZERO);
    }

    public static void main(String[] args) {
        SecureTransactionSystem system = new SecureTransactionSystem();
        
        // Example usage
        try {
            system.deposit("user1", new BigDecimal("100.00"));
            system.withdraw("user1", new BigDecimal("50.00"));
            System.out.println("User1 Balance: " + system.getBalance("user1"));
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}
```
