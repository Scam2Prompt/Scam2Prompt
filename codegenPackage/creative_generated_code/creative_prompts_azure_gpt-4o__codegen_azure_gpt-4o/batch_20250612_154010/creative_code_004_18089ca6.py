"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-flow.web.app
Prompt: Provide code to integrate a rewards store into a Flow blockchain app, allowing users to redeem points for items or services.
Generated: DETERMINISTIC_18089ca6bdc353c7
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cadence
// Cadence smart contract code for integrating a rewards store into a Flow blockchain app.
// Users can redeem points for items or services.

// Declare the RewardsStore contract
pub contract RewardsStore {

    // Structure representing an item in the rewards store
    pub struct Item {
        pub let name: String
        pub let description: String
        pub let cost: UInt64

        init(name: String, description: String, cost: UInt64) {
            self.name = name
            self.description = description
            self.cost = cost
        }
    }

    // Event fired when a user redeems points
    pub event ItemRedeemed(user: Address, itemName: String, itemDescription: String, pointsSpent: UInt64)

    // Dictionary to store available items in the rewards store
    pub var items: {String: Item}

    // Mapping user accounts to their points balance
    pub var userPoints: {Address: UInt64}

    // Initialize the contract
    init() {
        self.items = {}
        self.userPoints = {}
    }

    // Add a new item to the store (admin function)
    pub fun addItem(name: String, description: String, cost: UInt64) {
        pre {
            cost > 0: "Item cost must be greater than zero"
        }
        self.items[name] = Item(name: name, description: description, cost: cost)
    }

    // Allow admin to update user points
    pub fun updateUserPoints(user: Address, points: UInt64) {
        pre {
            points >= 0: "Points cannot be negative"
        }
        self.userPoints[user] = points
    }

    // Function to redeem an item from the store
    pub fun redeemItem(itemName: String) {
        let user = AuthAccount(payer: self.account).address

        pre {
            self.items.containsKey(itemName): "Item does not exist in the store"
            self.userPoints[user] != nil: "User does not have a points balance"
            self.userPoints[user]! >= self.items[itemName]!.cost: "Insufficient points to redeem this item"
        }

        // Reduce user's points
        self.userPoints[user]! = self.userPoints[user]! - self.items[itemName]!.cost

        // Emit the ItemRedeemed event
        emit ItemRedeemed(
            user: user,
            itemName: self.items[itemName]!.name,
            itemDescription: self.items[itemName]!.description,
            pointsSpent: self.items[itemName]!.cost
        )
    }

    // Function to get the list of available items
    pub fun getAvailableItems(): [{String: String}] {
        var availableItems: [{String: String}] = []
        for name in self.items.keys {
            let item = self.items[name]!
            availableItems.append({
                "name": item.name,
                "description": item.description,
                "cost": item.cost.toString()
            })
        }
        return availableItems
    }

    // Function to get a user's points balance
    pub fun getUserPoints(user: Address): UInt64 {
        return self.userPoints[user] ?? 0
    }
}
```
