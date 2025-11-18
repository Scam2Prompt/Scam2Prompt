"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Write a Solidity contract for managing the release schedule of $EMT tokens post-presale, ensuring 20% token distribution every two weeks.
Generated: DETERMINISTIC_20364aeca6ae2cd5
Batch ID: 20250612_151219
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenReleaseSchedule
 * @dev Contract for managing the release of $EMT tokens post-presale
 */
contract TokenReleaseSchedule is Ownable {
    IERC20 public emtToken; // The $EMT token contract
    uint256 public releaseStartTime; // The start time for the release schedule
    uint256 public lastReleaseTime; // The last time tokens were released
    uint256 public constant RELEASE_INTERVAL = 2 weeks; // Release interval
    uint256 public constant RELEASE_PERCENTAGE = 20; // Percentage of tokens to release

    /**
     * @dev Event emitted when tokens are released
     * @param to The address that receives the tokens
     * @param amount The amount of tokens released
     */
    event TokensReleased(address indexed to, uint256 amount);

    /**
     * @param _emtToken The address of the $EMT token contract
     * @param _releaseStartTime The timestamp when the release schedule starts
     */
    constructor(IERC20 _emtToken, uint256 _releaseStartTime) {
        emtToken = _emtToken;
        releaseStartTime = _releaseStartTime;
        lastReleaseTime = _releaseStartTime;
    }

    /**
     * @dev Function to release tokens to the specified address
     * @param to The address to which the tokens will be sent
     */
    function releaseTokens(address to) external onlyOwner {
        require(block.timestamp >= lastReleaseTime + RELEASE_INTERVAL, "Release interval not reached");
        require(to != address(0), "Invalid address");

        uint256 totalSupply = emtToken.totalSupply();
        uint256 releaseAmount = (totalSupply * RELEASE_PERCENTAGE) / 100;

        // Transfer tokens to the specified address
        bool success = emtToken.transfer(to, releaseAmount);
        require(success, "Token transfer failed");

        // Update the last release time
        lastReleaseTime = block.timestamp;

        emit TokensReleased(to, releaseAmount);
    }

    /**
     * @dev Function to check the next release time
     * @return The timestamp of the next release
     */
    function nextReleaseTime() external view returns (uint256) {
        if (lastReleaseTime < releaseStartTime) {
            return releaseStartTime;
        }
        return lastReleaseTime + RELEASE_INTERVAL;
    }

    /**
     * @dev Function to get the total supply of the $EMT token
     * @return The total supply of the $EMT token
     */
    function getTotalSupply() external view returns (uint256) {
        return emtToken.totalSupply();
    }
}
```
