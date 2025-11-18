"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Provide an example of a Solidity contract that enforces a presale cap of 5,000 ETH and calculates token distribution based on the rate of 1 ETH = 99,500 KSI.
Generated: DETERMINISTIC_83c27f03c2b9d685
Batch ID: 20250612_152827
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
 * @title KSI Presale Contract
 * @dev This contract enforces a presale cap, accepts ETH payments, and distributes KSI tokens based on a fixed rate.
 */
contract KSIPresale {
    // Presale cap in ETH
    uint256 public constant PRESALE_CAP = 5000 ether;

    // Token distribution rate (1 ETH = 99,500 KSI)
    uint256 public constant RATE = 99500;

    // Total ETH raised during the presale
    uint256 public totalRaised;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to accept ETH directly
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase tokens during the presale
     */
    function purchaseTokens() public payable {
        // Ensure the presale cap has not been exceeded
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to distribute
        uint256 tokens = msg.value * RATE;

        // Update the total ETH raised
        totalRaised += msg.value;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, msg.value, tokens);

        // Note: Token distribution logic would go here (e.g., integration with ERC20 contract)
        // For simplicity, this example assumes off-chain distribution is handled separately.
    }

    /**
     * @dev Function to withdraw the collected ETH by the owner
     */
    function withdrawFunds() external onlyOwner {
        // Transfer the entire contract balance to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }
}
```
