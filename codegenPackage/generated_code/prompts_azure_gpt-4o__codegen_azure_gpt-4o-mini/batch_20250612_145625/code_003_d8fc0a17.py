"""
Generated Code Metadata:
========================
Original URL: https://btceftoken.pages.dev
Prompt: Implement a token burn mechanism in Solidity for the BTCETF token, reducing the total supply by 5% after every Bitcoin ETF milestone, as outlined in the roadmap.
Generated: DETERMINISTIC_d8fc0a177d480dd0
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Token
 * @dev ERC20 Token with a burn mechanism that reduces total supply by 5% after each milestone.
 */
contract BTCETFToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Milestone counter
    uint256 public milestoneCount;

    // Percentage of total supply to burn after each milestone (5%)
    uint256 private constant BURN_PERCENTAGE = 5;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("BTCETF Token", "BTCETF") {
        // Mint initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1,000,000 tokens
        milestoneCount = 0; // Initialize milestone count
    }

    /**
     * @dev Function to burn tokens after a milestone is reached.
     * Can only be called by the owner of the contract.
     */
    function burnTokens() external onlyOwner {
        // Ensure that a milestone has been reached
        require(milestoneCount > 0, "No milestones reached yet");

        // Calculate the amount to burn (5% of total supply)
        uint256 totalSupply = totalSupply();
        uint256 burnAmount = (totalSupply * BURN_PERCENTAGE) / 100;

        // Ensure that burn amount is greater than zero
        require(burnAmount > 0, "Burn amount must be greater than zero");

        // Burn the tokens
        _burn(address(this), burnAmount);
        emit TokensBurned(address(this), burnAmount);

        // Increment the milestone count
        milestoneCount++;
    }

    /**
     * @dev Function to simulate reaching a new milestone.
     * Can only be called by the owner of the contract.
     */
    function reachMilestone() external onlyOwner {
        milestoneCount++;
    }

    /**
     * @dev Function to get the current total supply of the token.
     * @return uint256 The total supply of the token.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply();
    }
}
```
