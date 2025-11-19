"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Generate a code snippet in Java to simulate a cryptocurrency trading platform that allows users to buy and sell tokens, taking into account the importance of liquidity and attention for a project's growth and success.
Generated: DETERMINISTIC_5d580d2aa4edd7da
Batch ID: 20250622_211643
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
import java.util.Scanner;

public class CryptoTradingPlatform {

    // Represents a user's wallet with balances for different tokens
    static class Wallet {
        private final Map<String, BigDecimal> balances = new HashMap<>();

        public Wallet() {
            // Initialize wallet with some default balances
            balances.put("USD", new BigDecimal("1000.00")); // Fiat currency
            balances.put("BTC", BigDecimal.ZERO); // Bitcoin
            balances.put("ETH", BigDecimal.ZERO); // Ethereum
        }

        public BigDecimal getBalance(String token) {
            return balances.getOrDefault(token, BigDecimal.ZERO);
        }

        public void updateBalance(String token, BigDecimal amount) {
            balances.put(token, getBalance(token).add(amount));
        }
    }

    // Represents the trading platform
    static class TradingPlatform {
        private final Wallet userWallet = new Wallet();
        private final Map<String, BigDecimal> tokenPrices = new HashMap<>();

        public TradingPlatform() {
            // Initialize token prices (in USD)
            tokenPrices.put("BTC", new BigDecimal("30000.00"));
            tokenPrices.put("ETH", new BigDecimal("2000.00"));
        }

        // Simulates buying a token
        public void buyToken(String token, BigDecimal amountInUSD) {
            if (!tokenPrices.containsKey(token)) {
                System.out.println("Error: Token not supported.");
                return;
            }

            BigDecimal tokenPrice = tokenPrices.get(token);
            BigDecimal tokensToBuy = amountInUSD.divide(tokenPrice, 8, BigDecimal.ROUND_HALF_UP);

            if (userWallet.getBalance("USD").compareTo(amountInUSD) < 0) {
                System.out.println("Error: Insufficient USD balance.");
                return;
            }

            userWallet.updateBalance("USD", amountInUSD.negate());
            userWallet.updateBalance(token, tokensToBuy);

            System.out.printf("Successfully bought %.8f %s for $%.2f%n", tokensToBuy, token, amountInUSD);
        }

        // Simulates selling a token
        public void sellToken(String token, BigDecimal amountToSell) {
            if (!tokenPrices.containsKey(token)) {
                System.out.println("Error: Token not supported.");
                return;
            }

            if (userWallet.getBalance(token).compareTo(amountToSell) < 0) {
                System.out.println("Error: Insufficient token balance.");
                return;
            }

            BigDecimal tokenPrice = tokenPrices.get(token);
            BigDecimal usdEarned = amountToSell.multiply(tokenPrice);

            userWallet.updateBalance(token, amountToSell.negate());
            userWallet.updateBalance("USD", usdEarned);

            System.out.printf("Successfully sold %.8f %s for $%.2f%n", amountToSell, token, usdEarned);
        }

        // Displays the user's wallet balances
        public void displayWallet() {
            System.out.println("Wallet Balances:");
            userWallet.balances.forEach((token, balance) -> 
                System.out.printf("%s: %.8f%n", token, balance));
        }
    }

    public static void main(String[] args) {
        TradingPlatform platform = new TradingPlatform();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Crypto Trading Platform!");

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Buy Token");
            System.out.println("2. Sell Token");
            System.out.println("3. View Wallet");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number between 1 and 4.");
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.print("Enter token to buy (BTC/ETH): ");
                    String buyToken = scanner.nextLine().toUpperCase();
                    System.out.print("Enter amount in USD: ");
                    try {
                        BigDecimal amountInUSD = new BigDecimal(scanner.nextLine());
                        platform.buyToken(buyToken, amountInUSD);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount. Please enter a valid number.");
                    }
                    break;

                case 2:
                    System.out.print("Enter token to sell (BTC/ETH): ");
                    String sellToken = scanner.nextLine().toUpperCase();
                    System.out.print("Enter amount to sell: ");
                    try {
                        BigDecimal amountToSell = new BigDecimal(scanner.nextLine());
                        platform.sellToken(sellToken, amountToSell);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount. Please enter a valid number.");
                    }
                    break;

                case 3:
                    platform.displayWallet();
                    break;

                case 4:
                    System.out.println("Exiting the platform. Goodbye!");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please select a valid option.");
            }
        }
    }
}
```
