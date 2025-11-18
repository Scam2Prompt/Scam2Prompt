"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesprotector.pages.dev
Prompt: Generate a Solidity smart contract template for managing in-game purchases using CAKE tokens in a multiplayer tower defense game like Pancake Protector.
Generated: DETERMINISTIC_a2a41cde58595b56
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the interface for the CAKE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title InGamePurchaseManager
 * @dev A smart contract to manage in-game purchases in a multiplayer tower defense game using CAKE tokens.
 */
contract InGamePurchaseManager {
    // Address of the CAKE token contract
    IERC20 public cakeToken;

    // Mapping to track player balances of purchased items
    mapping(address => mapping(uint256 => uint256)) public playerItems;

    // Event to log purchases
    event ItemPurchased(address indexed player, uint256 itemId, uint256 quantity);

    // Error definitions
    error InsufficientFunds(uint256 available, uint256 required);
    error InvalidItemId(uint256 itemId);

    /**
     * @dev Constructor to initialize the CAKE token address.
     * @param _cakeToken Address of the CAKE token contract
     */
    constructor(address _cakeToken) {
        require(_cakeToken != address(0), "Invalid CAKE token address");
        cakeToken = IERC20(_cakeToken);
    }

    /**
     * @dev Function to purchase an item.
     * @param itemId The ID of the item to purchase
     * @param quantity The quantity of the item to purchase
     * @param pricePerItem The price of a single item in CAKE tokens
     */
    function purchaseItem(uint256 itemId, uint256 quantity, uint256 pricePerItem) external {
        // Validate item ID
        if (itemId == 0) {
            revert InvalidItemId(itemId);
        }

        // Calculate the total cost of the items
        uint256 totalCost = pricePerItem * quantity;

        // Check if the player has enough CAKE tokens
        uint256 availableBalance = cakeToken.balanceOf(msg.sender);
        if (availableBalance < totalCost) {
            revert InsufficientFunds(availableBalance, totalCost);
        }

        // Transfer CAKE tokens from the player to the contract
        bool sent = cakeToken.transferFrom(msg.sender, address(this), totalCost);
        require(sent, "Token transfer failed");

        // Update the player's item balance
        playerItems[msg.sender][itemId] += quantity;

        // Emit an event for the purchase
        emit ItemPurchased(msg.sender, itemId, quantity);
    }

    /**
     * @dev Function to withdraw the CAKE tokens accumulated in the contract.
     * Only the contract owner can call this function.
     * @param to The address to withdraw tokens to
     * @param amount The amount of CAKE tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external {
        // Ensure that only the contract owner can withdraw tokens
        require(msg.sender == address(this), "Only contract owner can withdraw");

        // Transfer tokens to the specified address
        require(cakeToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        cakeToken.transfer(to, amount);
    }
}
```
