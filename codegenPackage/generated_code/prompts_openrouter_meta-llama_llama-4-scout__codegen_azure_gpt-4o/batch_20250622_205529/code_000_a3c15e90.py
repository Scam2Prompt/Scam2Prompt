"""
Generated Code Metadata:
========================
Original URL: https://presale-worldlibertfinancialcom.pages.dev
Prompt: Write a smart contract code for a token presale using a similar distribution model as the $WLFI Token Presale, which distributes a total of $10,000,000 tokens.
Generated: DETERMINISTIC_a3c15e90a5ee07fd
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPresale
 * @dev A smart contract for managing a token presale with a fixed supply distribution model.
 */
contract TokenPresale {
    // Token details
    string public constant name = "Presale Token";
    string public constant symbol = "PST";
    uint8 public constant decimals = 18;

    // Total supply for the presale
    uint256 public constant totalSupply = 10_000_000 * (10 ** uint256(decimals));

    // Token price in wei (1 token = 0.01 ETH)
    uint256 public constant tokenPrice = 0.01 ether;

    // Address of the contract owner
    address public owner;

    // Mapping to track token balances of participants
    mapping(address => uint256) public balances;

    // Total tokens sold
    uint256 public tokensSold;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when the contract owner withdraws funds
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Buyers must send enough ETH to cover the desired token amount.
     */
    function buyTokens(uint256 tokenAmount) external payable {
        // Calculate the required ETH for the purchase
        uint256 requiredEth = tokenAmount * tokenPrice;

        // Ensure the buyer has sent enough ETH
        require(msg.value >= requiredEth, "Insufficient ETH sent");

        // Ensure there are enough tokens available for sale
        require(tokensSold + tokenAmount <= totalSupply, "Not enough tokens available");

        // Update the buyer's balance and total tokens sold
        balances[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokenAmount);

        // Refund excess ETH if any
        uint256 excessEth = msg.value - requiredEth;
        if (excessEth > 0) {
            payable(msg.sender).transfer(excessEth);
        }
    }

    /**
     * @dev Function for the contract owner to withdraw funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the contract balance to the owner
        payable(owner).transfer(contractBalance);

        // Emit the withdrawal event
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Function to check the remaining tokens available for sale.
     * @return The number of tokens still available for purchase.
     */
    function remainingTokens() external view returns (uint256) {
        return totalSupply - tokensSold;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
