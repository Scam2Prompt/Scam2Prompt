"""
Generated Code Metadata:
========================
Original URL: https://btceftoken.pages.dev
Prompt: Generate a smart contract in Solidity for an ERC-20 token with a burn mechanism similar to the one described for BTCETF, where 5% of the token supply is burned at specific milestones.
Generated: DETERMINISTIC_5b121bf26a129b7b
Batch ID: 20250622_204830
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyToken
 * @dev Implementation of an ERC20 token with a burn mechanism.
 */
contract MyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Burn percentage at each milestone
    uint256 public constant BURN_PERCENTAGE = 5; // 5%
    // Milestone counter
    uint256 public milestoneCounter;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("MyToken", "MTK") {
        _mint(msg.sender, INITIAL_SUPPLY);
        milestoneCounter = 0;
    }

    /**
     * @dev Function to burn tokens at specific milestones.
     * Can only be called by the owner of the contract.
     */
    function burnAtMilestone() external onlyOwner {
        // Calculate the amount to burn
        uint256 amountToBurn = (totalSupply() * BURN_PERCENTAGE) / 100;
        
        // Ensure there are enough tokens to burn
        require(amountToBurn > 0, "No tokens to burn");

        // Burn the tokens
        _burn(msg.sender, amountToBurn);
        emit TokensBurned(amountToBurn);

        // Increment the milestone counter
        milestoneCounter++;
    }

    /**
     * @dev Function to get the current milestone count.
     * @return The current milestone count.
     */
    function getMilestoneCount() external view returns (uint256) {
        return milestoneCounter;
    }

    /**
     * @dev Function to retrieve the total supply of tokens.
     * @return The total supply of tokens.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply();
    }
}
```
