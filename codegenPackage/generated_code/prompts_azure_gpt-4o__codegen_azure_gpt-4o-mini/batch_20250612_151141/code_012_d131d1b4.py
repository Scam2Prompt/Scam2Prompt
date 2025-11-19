"""
Generated Code Metadata:
========================
Original URL: https://multichainetfclaim.pages.dev
Prompt: Develop a smart contract that automatically burns 25% of the BTCETF token supply over time, with incremental burns of 5% tied to Bitcoin ETF milestones.
Generated: DETERMINISTIC_d131d1b4af6a2c1d
Batch ID: 20250612_151141
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Token Contract
 * @dev This contract implements a token that automatically burns 25% of its supply over time,
 * with incremental burns of 5% tied to Bitcoin ETF milestones.
 */
contract BTCETF is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens
    // Total percentage to burn
    uint256 private constant TOTAL_BURN_PERCENTAGE = 25; // 25%
    // Incremental burn percentage
    uint256 private constant INCREMENTAL_BURN_PERCENTAGE = 5; // 5%
    // Milestone counter
    uint256 public milestoneCount;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);

    constructor() ERC20("BTCETF Token", "BTCETF") {
        _mint(msg.sender, INITIAL_SUPPLY);
        milestoneCount = 0; // Initialize milestone count
    }

    /**
     * @dev Function to burn tokens based on milestones.
     * Can only be called by the owner of the contract.
     */
    function burnTokens() external onlyOwner {
        require(milestoneCount < TOTAL_BURN_PERCENTAGE / INCREMENTAL_BURN_PERCENTAGE, "All burns completed");

        // Calculate the amount to burn
        uint256 burnAmount = (totalSupply() * INCREMENTAL_BURN_PERCENTAGE) / 100;
        
        // Ensure we do not exceed the total burn limit
        require(burnAmount <= (INITIAL_SUPPLY * TOTAL_BURN_PERCENTAGE) / 100, "Burn exceeds total burn limit");

        // Burn the tokens
        _burn(msg.sender, burnAmount);
        emit TokensBurned(burnAmount);

        // Increment the milestone count
        milestoneCount++;
    }

    /**
     * @dev Function to get the current milestone count.
     * @return The current milestone count.
     */
    function getMilestoneCount() external view returns (uint256) {
        return milestoneCount;
    }

    /**
     * @dev Function to get the total supply of the token.
     * @return The total supply of the token.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply();
    }
}
```
