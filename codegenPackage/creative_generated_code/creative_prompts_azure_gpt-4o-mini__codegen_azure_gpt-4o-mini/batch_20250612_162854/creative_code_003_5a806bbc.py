"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Generate a sample smart contract that utilizes Moxie’s bonding curves to emphasize utility over speculation in token distribution.
Generated: DETERMINISTIC_5a806bbc2952e4d6
Batch ID: 20250612_162854
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title UtilityToken
 * @dev This contract implements a bonding curve for token distribution,
 *      emphasizing utility over speculation.
 */
contract UtilityToken is ERC20, Ownable {
    // Bonding curve parameters
    uint256 public constant BASE_PRICE = 0.01 ether; // Price per token at base level
    uint256 public constant MULTIPLIER = 2; // Price multiplier for each token
    
    // Total tokens that have been minted
    uint256 public totalMinted;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the token with a name and symbol
     */
    constructor() ERC20("UtilityToken", "UTK") {}

    /**
     * @dev Purchase tokens based on the bonding curve
     * @param amount The number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero.");
        
        uint256 totalCost = calculateCost(amount);
        require(msg.value >= totalCost, "Insufficient Ether sent for purchase.");

        // Mint new tokens to the buyer
        _mint(msg.sender, amount);
        totalMinted += amount;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess Ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Calculate the cost of purchasing a given number of tokens
     * @param amount The amount of tokens to calculate the cost for
     * @return cost The calculated cost in wei
     */
    function calculateCost(uint256 amount) public view returns (uint256 cost) {
        cost = 0;
        for (uint256 i = 0; i < amount; i++) {
            cost += BASE_PRICE * (MULTIPLIER ** (totalMinted + i));
        }
    }

    /**
     * @dev Withdraw accumulated Ether by the contract owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw.");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed. Use purchaseTokens.");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed.");
    }
}
```
