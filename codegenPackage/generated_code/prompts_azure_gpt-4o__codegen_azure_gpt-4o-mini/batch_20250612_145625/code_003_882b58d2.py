"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Provide a step-by-step guide in Solidity for implementing a token burning mechanism that reduces the BTCETF token supply by 5% whenever a Bitcoin ETF milestone is reached.
Generated: DETERMINISTIC_882b58d244b72f2f
Batch ID: 20250612_145625
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BTCETF Token contract
contract BTCETF is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Milestone threshold for burning tokens
    uint256 public milestoneThreshold;

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _milestoneThreshold) 
        ERC20(name, symbol) 
    {
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply);
        milestoneThreshold = _milestoneThreshold;
    }

    // Function to burn tokens when a milestone is reached
    function burnTokens() external onlyOwner {
        // Calculate 5% of the current total supply
        uint256 amountToBurn = totalSupply() * 5 / 100;

        // Ensure that the amount to burn does not exceed the total supply
        require(amountToBurn > 0, "No tokens to burn");

        // Burn the tokens by calling the internal _burn function
        _burn(msg.sender, amountToBurn);

        // Emit an event for the burned tokens
        emit TokensBurned(msg.sender, amountToBurn);
    }

    // Function to simulate reaching a milestone (for demonstration purposes)
    function reachMilestone() external onlyOwner {
        // Logic to check if a milestone is reached
        // This is a placeholder for actual milestone logic
        require(milestoneThreshold > 0, "Milestone threshold not set");

        // Call the burnTokens function when a milestone is reached
        burnTokens();
    }

    // Function to set a new milestone threshold
    function setMilestoneThreshold(uint256 newThreshold) external onlyOwner {
        milestoneThreshold = newThreshold;
    }
}
```
