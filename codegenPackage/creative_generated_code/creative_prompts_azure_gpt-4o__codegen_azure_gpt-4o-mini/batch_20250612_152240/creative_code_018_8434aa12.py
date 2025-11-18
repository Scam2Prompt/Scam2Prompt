"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Develop a Solidity contract for managing the release schedule of $EMT tokens after the presale, ensuring compliance with the biweekly 20% distribution model.
Generated: DETERMINISTIC_8434aa12bf82bccc
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EMTTokenRelease
 * @dev A contract to manage the biweekly release of $EMT tokens after the presale
 */
contract EMTTokenRelease is Ownable {
    IERC20 public emtToken; // The address of the $EMT token contract
    uint256 public totalTokens; // Total amount of tokens to be distributed
    uint256 public releasedTokens; // Total amount of tokens released
    uint256 public startReleaseTime; // The time when the release starts
    uint256 public releaseInterval; // Time between each release (in seconds)
    uint256 public constant RELEASE_PERCENTAGE = 20; // Percentage of tokens to be released biweekly
    uint256 public constant INTERVALS_PER_YEAR = 26; // Number of biweekly intervals in a year

    // Event to emit when tokens are released
    event TokensReleased(address recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract parameters
     * @param _emtToken Address of the $EMT token contract
     * @param _totalTokens Total tokens to be managed by this contract
     */
    constructor(IERC20 _emtToken, uint256 _totalTokens) {
        require(address(_emtToken) != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        emtToken = _emtToken;
        totalTokens = _totalTokens;
        releasedTokens = 0;
        startReleaseTime = block.timestamp; // Set the release start time to the current block time
        releaseInterval = 14 days; // Set the release interval to biweekly
    }

    /**
     * @dev Release tokens according to the biweekly distribution schedule
     * @param recipient Address to receive the released tokens
     */
    function releaseTokens(address recipient) external onlyOwner {
        require(block.timestamp >= startReleaseTime, "Release period has not started yet");
        require(releasedTokens < totalTokens, "All tokens have been released");

        // Determine the number of release intervals that have passed
        uint256 intervalsPassed = (block.timestamp - startReleaseTime) / releaseInterval;
        uint256 tokensToRelease = (totalTokens * RELEASE_PERCENTAGE) / 100;

        // Ensure we do not release more than the total tokens allocated
        if (releasedTokens + tokensToRelease > totalTokens) {
            tokensToRelease = totalTokens - releasedTokens;
        }

        // Update the released tokens count
        releasedTokens += tokensToRelease;

        // Transfer the tokens to the recipient
        require(emtToken.transfer(recipient, tokensToRelease), "Token transfer failed");

        emit TokensReleased(recipient, tokensToRelease);
    }

    /**
     * @dev Get the amount of tokens that can be released at the current time
     * @return The amount of tokens available for release
     */
    function availableTokens() external view returns (uint256) {
        if (releasedTokens >= totalTokens) {
            return 0;
        }
        
        uint256 intervalsPassed = (block.timestamp - startReleaseTime) / releaseInterval;
        uint256 totalReleasable = (intervalsPassed * (totalTokens * RELEASE_PERCENTAGE) / 100);
        
        if (totalReleasable + releasedTokens > totalTokens) {
            totalReleasable = totalTokens - releasedTokens;
        }
        
        return totalReleasable;
    }

    /**
     * @dev Allow the owner to withdraw any remaining tokens in the event of an emergency
     * @param amount Amount of tokens to withdraw
     */
    function withdrawRemainingTokens(uint256 amount) external onlyOwner {
        require(emtToken.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");
        require(amount > 0, "Withdraw amount must be greater than zero");

        require(emtToken.transfer(owner(), amount), "Withdrawal transfer failed");
    }
}
```
