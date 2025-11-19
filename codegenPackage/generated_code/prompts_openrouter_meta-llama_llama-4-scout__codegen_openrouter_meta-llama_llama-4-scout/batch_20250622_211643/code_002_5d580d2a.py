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
import java.util.HashMap;
import java.util.Map;

/**
 * Simulates a basic cryptocurrency trading platform.
 */
public class CryptoTradingPlatform {

    // Data structure to hold token information
    static class Token {
        String name;
        double price;
        int supply;
        int liquidity;

        public Token(String name, double price, int supply) {
            this.name = name;
            this.price = price;
            this.supply = supply;
            this.liquidity = 0;
        }
    }

    // Data structure to hold user information
    static class User {
        String name;
        Map<String, Integer> portfolio;

        public User(String name) {
            this.name = name;
            this.portfolio = new HashMap<>();
        }
    }

    private Map<String, Token> tokens;
    private Map<String, User> users;

    public CryptoTradingPlatform() {
        this.tokens = new HashMap<>();
        this.users = new HashMap<>();
    }

    /**
     * Adds a new token to the platform.
     * 
     * @param name    Token name
     * @param price   Initial token price
     * @param supply  Total token supply
     */
    public void addToken(String name, double price, int supply) {
        if (tokens.containsKey(name)) {
            System.out.println("Token already exists.");
            return;
        }
        tokens.put(name, new Token(name, price, supply));
    }

    /**
     * Adds a new user to the platform.
     * 
     * @param name User name
     */
    public void addUser(String name) {
        if (users.containsKey(name)) {
            System.out.println("User already exists.");
            return;
        }
        users.put(name, new User(name));
    }

    /**
     * Buys a specified amount of tokens for a user.
     * 
     * @param userName  User name
     * @param tokenName Token name
     * @param amount    Amount to buy
     */
    public void buyToken(String userName, String tokenName, int amount) {
        User user = users.get(userName);
        Token token = tokens.get(tokenName);

        if (user == null || token == null) {
            System.out.println("User or token does not exist.");
            return;
        }

        double cost = token.price * amount;
        // Simple validation, real scenario would involve more complex logic
        if (cost > 10000) { // Assuming $10,000 as a max budget for simplicity
            System.out.println("Insufficient funds.");
            return;
        }

        // Update user's portfolio
        user.portfolio.put(tokenName, user.portfolio.getOrDefault(tokenName, 0) + amount);

        // Update token liquidity
        token.liquidity += amount;

        System.out.printf("%s bought %d %s tokens.\n", userName, amount, tokenName);
    }

    /**
     * Sells a specified amount of tokens for a user.
     * 
     * @param userName  User name
     * @param tokenName Token name
     * @param amount    Amount to sell
     */
    public void sellToken(String userName, String tokenName, int amount) {
        User user = users.get(userName);
        Token token = tokens.get(tokenName);

        if (user == null || token == null) {
            System.out.println("User or token does not exist.");
            return;
        }

        // Check if user has enough tokens to sell
        if (user.portfolio.getOrDefault(tokenName, 0) < amount) {
            System.out.println("User does not have enough tokens to sell.");
            return;
        }

        // Update user's portfolio
        user.portfolio.put(tokenName, user.portfolio.get(tokenName) - amount);

        // Update token liquidity
        token.liquidity -= amount;

        System.out.printf("%s sold %d %s tokens.\n", userName, amount, tokenName);
    }

    /**
     * Lists user's portfolio.
     * 
     * @param userName User name
     */
    public void listPortfolio(String userName) {
        User user = users.get(userName);

        if (user == null) {
            System.out.println("User does not exist.");
            return;
        }

        System.out.printf("%s's portfolio:\n", userName);
        for (Map.Entry<String, Integer> entry : user.portfolio.entrySet()) {
            System.out.printf("%s: %d\n", entry.getKey(), entry.getValue());
        }
    }

    public static void main(String[] args) {
        CryptoTradingPlatform platform = new CryptoTradingPlatform();

        platform.addToken("ABC", 10.0, 100000);
        platform.addUser("JohnDoe");

        platform.buyToken("JohnDoe", "ABC", 100);
        platform.listPortfolio("JohnDoe");
        platform.sellToken("JohnDoe", "ABC", 50);
        platform.listPortfolio("JohnDoe");
    }
}
```
