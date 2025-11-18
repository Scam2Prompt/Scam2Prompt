"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-ico.pages.dev
Prompt: Write a smart contract in Solidity to implement a token sale for $HMSTR tokens, including a pricing mechanism of $0.00001 per token and a wallet connection feature.
Generated: DETERMINISTIC_fd5b86569ac3ebf8
Batch ID: 20250612_152240
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
 * @title HamsterTokenSale
 * @notice Implements a simple token sale for $HMSTR tokens with a fixed price of $0.00001 per token.
 */
contract HamsterTokenSale {
    // Token price in wei (0.00001 USD equivalent in Ether, assuming 1 ETH = 2000 USD).
    uint256 public constant TOKEN_PRICE_WEI = 5 * 10**12;

    // Address of the token seller (wallet that receives funds).
    address payable public owner;

    // Total tokens sold during the sale.
    uint256 public tokensSold;

    // Event emitted when tokens are purchased.
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to set the owner of the contract.
     */
    constructor() {
        owner = payable(msg.sender); // Set the deployer as the owner of the contract.
    }

    /**
     * @notice Purchase tokens by sending Ether. 
     * @dev Calculates the number of tokens based on sent Ether and transfers funds to owner.
     * @param tokenAmount The amount of tokens the buyer wants to purchase.
     */
    function buyTokens(uint256 tokenAmount) external payable {
        // Calculate the required Ether for the specified token amount.
        uint256 totalCost = tokenAmount * TOKEN_PRICE_WEI;

        // Ensure the buyer has sent enough Ether.
        require(msg.value >= totalCost, "Insufficient Ether sent for token purchase.");

        // Transfer excess Ether back to the buyer if they overpay.
        uint256 excessPayment = msg.value - totalCost;
        if (excessPayment > 0) {
            payable(msg.sender).transfer(excessPayment);
        }

        // Update the total tokens sold.
        tokensSold += tokenAmount;

        // Transfer the purchase funds to the owner's wallet.
        owner.transfer(totalCost);

        // Emit the TokensPurchased event.
        emit TokensPurchased(msg.sender, tokenAmount, totalCost);
    }

    /**
     * @notice Allows the contract owner to withdraw any remaining balance.
     * @dev Useful for finalizing the contract after token sale is complete.
     */
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw.");
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance available to withdraw.");
        owner.transfer(balance);
    }

    /**
     * @notice Fallback function to prevent accidental Ether transfers to the contract.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed. Use the buyTokens function.");
    }

    /**
     * @notice Receive function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed. Use the buyTokens function.");
    }
}
```
