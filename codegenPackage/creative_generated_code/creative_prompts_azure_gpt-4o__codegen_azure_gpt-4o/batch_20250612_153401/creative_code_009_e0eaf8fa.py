"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Create a Solidity contract that implements a presale mechanism with tiered pricing and a total supply limit, inspired by the JESSE presale model.
Generated: DETERMINISTIC_e0eaf8fa5d08f72f
Batch ID: 20250612_153401
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

/**
 * @title PresaleContract
 * @dev Implements a tiered pricing presale mechanism with a total supply limit.
 */
contract PresaleContract {
    // Variables for presale settings
    uint256 public constant TOTAL_SUPPLY = 10000; // Total supply limit of tokens
    uint256 public totalSold = 0;                // Total tokens sold in the presale
    address public owner;                        // Owner of the contract

    // Struct for tier pricing
    struct Tier {
        uint256 price;       // Price per token in the tier (in wei)
        uint256 limit;       // Maximum number of tokens sold in the tier
    }
    
    // Array of tiers
    Tier[] public tiers;

    // Mapping to track contributions by address
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with tiers and set the owner.
     * @param _tierPrices Array of tier prices in wei.
     * @param _tierLimits Array of tier token limits.
     */
    constructor(uint256[] memory _tierPrices, uint256[] memory _tierLimits) {
        require(_tierPrices.length == _tierLimits.length, "Invalid input: mismatched arrays");
        owner = msg.sender;

        // Initialize tiers
        for (uint256 i = 0; i < _tierPrices.length; i++) {
            tiers.push(Tier({
                price: _tierPrices[i],
                limit: _tierLimits[i]
            }));
        }
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param tokenAmount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(totalSold + tokenAmount <= TOTAL_SUPPLY, "Exceeds total supply limit");

        uint256 cost = calculateCost(tokenAmount);
        require(msg.value == cost, "Incorrect ETH value sent");

        // Update state
        totalSold += tokenAmount;
        contributions[msg.sender] += tokenAmount;

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount, cost);
    }

    /**
     * @dev Internal function to calculate the cost of purchasing tokens based on tiers.
     * @param tokenAmount Number of tokens to purchase.
     * @return cost Total cost in wei.
     */
    function calculateCost(uint256 tokenAmount) internal view returns (uint256 cost) {
        uint256 remaining = tokenAmount;
        uint256 currentTier = 0;

        while (remaining > 0) {
            require(currentTier < tiers.length, "Insufficient tier capacity");

            Tier memory tier = tiers[currentTier];
            uint256 tierRemaining = tier.limit - totalSold;

            if (tierRemaining > 0) {
                uint256 purchaseQuantity = remaining > tierRemaining ? tierRemaining : remaining;
                cost += purchaseQuantity * tier.price;
                remaining -= purchaseQuantity;
            }

            currentTier++;
        }
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to withdraw collected ETH from presale by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to get the number of tiers.
     * @return Number of tiers.
     */
    function getTierCount() external view returns (uint256) {
        return tiers.length;
    }
}
```
