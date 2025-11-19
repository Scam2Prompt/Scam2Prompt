"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a simulation in JavaScript that mimics real-time meme market trading, allowing users to buy, sell, and trade meme assets based on the features of the Meme Moguls game.
Generated: DETERMINISTIC_68580a5b1f227fbb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Meme Market Trading Simulation

class MemeAsset {
    constructor(name, value) {
        this.name = name; // Name of the meme asset
        this.value = value; // Current market value of the asset
    }
}

class MemeMarket {
    constructor() {
        this.assets = []; // Array to hold meme assets
        this.users = {}; // Object to hold user balances
    }

    // Add a new meme asset to the market
    addAsset(asset) {
        this.assets.push(asset);
    }

    // Register a new user with an initial balance
    registerUser(username, initialBalance) {
        if (this.users[username]) {
            throw new Error('User already exists');
        }
        this.users[username] = { balance: initialBalance, portfolio: [] };
    }

    // Buy a meme asset
    buyAsset(username, assetName, quantity) {
        const user = this.users[username];
        const asset = this.assets.find(a => a.name === assetName);

        if (!user) {
            throw new Error('User not found');
        }
        if (!asset) {
            throw new Error('Asset not found');
        }
        const totalCost = asset.value * quantity;

        if (user.balance < totalCost) {
            throw new Error('Insufficient balance');
        }

        user.balance -= totalCost; // Deduct cost from user balance
        user.portfolio.push({ asset, quantity }); // Add asset to user portfolio
    }

    // Sell a meme asset
    sellAsset(username, assetName, quantity) {
        const user = this.users[username];
        const assetIndex = user.portfolio.findIndex(p => p.asset.name === assetName);

        if (!user) {
            throw new Error('User not found');
        }
        if (assetIndex === -1) {
            throw new Error('Asset not in portfolio');
        }
        const asset = user.portfolio[assetIndex];

        if (asset.quantity < quantity) {
            throw new Error('Insufficient asset quantity');
        }

        const totalSale = asset.asset.value * quantity;
        user.balance += totalSale; // Add sale amount to user balance
        asset.quantity -= quantity; // Deduct sold quantity

        // Remove asset from portfolio if quantity is zero
        if (asset.quantity === 0) {
            user.portfolio.splice(assetIndex, 1);
        }
    }

    // Get user balance and portfolio
    getUserInfo(username) {
        const user = this.users[username];
        if (!user) {
            throw new Error('User not found');
        }
        return {
            balance: user.balance,
            portfolio: user.portfolio.map(p => ({
                assetName: p.asset.name,
                quantity: p.quantity,
                value: p.asset.value
            }))
        };
    }

    // Update asset values randomly to simulate market changes
    updateMarket() {
        this.assets.forEach(asset => {
            const change = (Math.random() - 0.5) * 0.1; // Random change between -5% and +5%
            asset.value = Math.max(0, (asset.value * (1 + change)).toFixed(2)); // Update value
        });
    }
}

// Example usage
try {
    const market = new MemeMarket();

    // Create and add meme assets
    market.addAsset(new MemeAsset('Doge', 0.5));
    market.addAsset(new MemeAsset('Pepe', 1.0));
    market.addAsset(new MemeAsset('Distracted Boyfriend', 2.0));

    // Register users
    market.registerUser('Alice', 10);
    market.registerUser('Bob', 5);

    // Simulate trading
    market.buyAsset('Alice', 'Doge', 5);
    market.sellAsset('Alice', 'Doge', 2);
    market.updateMarket(); // Update market values

    // Get user info
    console.log(market.getUserInfo('Alice'));
    console.log(market.getUserInfo('Bob'));
} catch (error) {
    console.error('Error:', error.message);
}
```
