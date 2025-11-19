"""
Generated Code Metadata:
========================
Original URL: https://the-tradeflex-gpt.com
Prompt: Generate a code snippet in Java to create a simple trading simulator that allows users to practice investing in cryptocurrencies, such as Bitcoin, using historical market data from TradeFlex GPT.
Generated: DETERMINISTIC_c6ed41a4520f3e87
Batch ID: 20250622_211906
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
import java.util.Scanner;

/**
 * A simple trading simulator for practicing cryptocurrency investments using historical market data.
 * This simulator allows users to buy and sell Bitcoin (BTC) with a virtual balance.
 */
public class CryptoTradingSimulator {

    // Historical BTC prices (simplified for demonstration)
    private static final Map<String, Double> historicalBTCData = new HashMap<>();
    static {
        historicalBTCData.put("2023-01-01", 16500.0);
        historicalBTCData.put("2023-01-02", 16800.0);
        historicalBTCData.put("2023-01-03", 17200.0);
        historicalBTCData.put("2023-01-04", 16900.0);
        historicalBTCData.put("2023-01-05", 17500.0);
    }

    private double balance;
    private double btcAmount;
    private String currentDate;

    /**
     * Constructor initializes the simulator with starting balance and date.
     * @param initialBalance Starting virtual balance in USD.
     * @param startDate Initial date for simulation.
     */
    public CryptoTradingSimulator(double initialBalance, String startDate) {
        if (initialBalance <= 0) {
            throw new IllegalArgumentException("Initial balance must be positive");
        }
        if (!historicalBTCData.containsKey(startDate)) {
            throw new IllegalArgumentException("Invalid start date or no data available");
        }

        this.balance = initialBalance;
        this.btcAmount = 0;
        this.currentDate = startDate;
    }

    /**
     * Buys Bitcoin at the current date's price.
     * @param usdAmount Amount in USD to spend on BTC.
     * @throws IllegalArgumentException if amount is invalid or insufficient funds.
     */
    public void buyBTC(double usdAmount) {
        if (usdAmount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        if (usdAmount > balance) {
            throw new IllegalArgumentException("Insufficient funds");
        }

        double btcPrice = historicalBTCData.get(currentDate);
        double purchasedAmount = usdAmount / btcPrice;
        
        btcAmount += purchasedAmount;
        balance -= usdAmount;
    }

    /**
     * Sells Bitcoin at the current date's price.
     * @param btcAmount Amount in BTC to sell.
     * @throws IllegalArgumentException if amount is invalid or insufficient BTC.
     */
    public void sellBTC(double btcAmount) {
        if (btcAmount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        if (btcAmount > this.btcAmount) {
            throw new IllegalArgumentException("Insufficient BTC");
        }

        double btcPrice = historicalBTCData.get(currentDate);
        double usdAmount = btcAmount * btcPrice;
        
        this.btcAmount -= btcAmount;
        balance += usdAmount;
    }

    /**
     * Advances the simulation to the next available date.
     * @return true if date was advanced, false if no more dates available.
     */
    public boolean nextDay() {
        // Find the next date in the historical data
        boolean foundCurrent = false;
        for (String date : historicalBTCData.keySet()) {
            if (foundCurrent) {
                currentDate = date;
                return true;
            }
            if (date.equals(currentDate)) {
                foundCurrent = true;
            }
        }
        return false;
    }

    /**
     * Gets the current portfolio value in USD.
     * @return Total value of balance + BTC holdings.
     */
    public double getPortfolioValue() {
        double btcPrice = historicalBTCData.get(currentDate);
        return balance + (btcAmount * btcPrice);
    }

    // Getters
    public double getBalance() { return balance; }
    public double getBtcAmount() { return btcAmount; }
    public String getCurrentDate() { return currentDate; }
    public double getCurrentBTCPrice() { return historicalBTCData.get(currentDate); }

    /**
     * Main method to run the trading simulator CLI.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Crypto Trading Simulator ===");
        System.out.println("Available dates: " + String.join(", ", historicalBTCData.keySet()));
        
        System.out.print("Enter starting date (YYYY-MM-DD): ");
        String startDate = scanner.nextLine();
        
        System.out.print("Enter initial balance (USD): ");
        double initialBalance = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        
        try {
            CryptoTradingSimulator simulator = new CryptoTradingSimulator(initialBalance, startDate);
            
            while (true) {
                System.out.println("\nCurrent date: " + simulator.getCurrentDate());
                System.out.printf("BTC Price: $%.2f\n", simulator.getCurrentBTCPrice());
                System.out.printf("Balance: $%.2f | BTC: %.8f | Portfolio: $%.2f\n", 
                    simulator.getBalance(), simulator.getBtcAmount(), simulator.getPortfolioValue());
                
                System.out.println("\n1. Buy BTC");
                System.out.println("2. Sell BTC");
                System.out.println("3. Next day");
                System.out.println("4. Exit");
                System.out.print("Choose an option: ");
                
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline
                
                switch (choice) {
                    case 1:
                        System.out.print("Enter USD amount to buy: ");
                        double buyAmount = scanner.nextDouble();
                        scanner.nextLine();
                        try {
                            simulator.buyBTC(buyAmount);
                            System.out.println("Purchase successful!");
                        } catch (IllegalArgumentException e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                        break;
                    case 2:
                        System.out.print("Enter BTC amount to sell: ");
                        double sellAmount = scanner.nextDouble();
                        scanner.nextLine();
                        try {
                            simulator.sellBTC(sellAmount);
                            System.out.println("Sale successful!");
                        } catch (IllegalArgumentException e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                        break;
                    case 3:
                        if (!simulator.nextDay()) {
                            System.out.println("No more data available. Simulation ended.");
                            return;
                        }
                        break;
                    case 4:
                        System.out.println("Final portfolio value: $" + simulator.getPortfolioValue());
                        System.out.println("Exiting simulator...");
                        return;
                    default:
                        System.out.println("Invalid option");
                }
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
