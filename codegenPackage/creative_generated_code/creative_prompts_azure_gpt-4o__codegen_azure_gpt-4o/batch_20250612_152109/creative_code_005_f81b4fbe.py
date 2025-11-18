"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Develop a Solidity contract for a token vesting schedule that unlocks tokens in increments, similar to the $SCORP vesting plan outlined on the Scorpion Casino website.
Generated: DETERMINISTIC_f81b4fbe18a2f4c5
Batch ID: 20250612_152109
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
 * @title TokenVesting
 * @dev Implements a token vesting schedule with periodic token unlocks.
 */
contract TokenVesting {
    // ERC20 token contract address
    IERC20 public token;

    // Address of the beneficiary receiving the vested tokens
    address public beneficiary;

    // Total amount of tokens to be vested
    uint256 public totalAmount;

    // Start time of the vesting schedule (UNIX timestamp)
    uint256 public startTime;

    // Duration of each vesting period (in seconds)
    uint256 public periodDuration;

    // Number of vesting periods
    uint256 public totalPeriods;

    // Amount of tokens unlocked per period
    uint256 public tokensPerPeriod;

    // Last period claimed
    uint256 public lastClaimedPeriod;

    /**
     * @dev Initializes the vesting contract.
     * @param _token Address of the ERC20 token being vested.
     * @param _beneficiary Address of the beneficiary receiving the tokens.
     * @param _totalAmount Total number of tokens to be vested.
     * @param _startTime Start time of the vesting schedule (UNIX timestamp).
     * @param _periodDuration Duration of each vesting period (in seconds).
     * @param _totalPeriods Total number of vesting periods.
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _periodDuration,
        uint256 _totalPeriods
    ) {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_periodDuration > 0, "Period duration must be greater than zero");
        require(_totalPeriods > 0, "Total periods must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        totalAmount = _totalAmount;
        startTime = _startTime;
        periodDuration = _periodDuration;
        totalPeriods = _totalPeriods;
        tokensPerPeriod = _totalAmount / _totalPeriods;
        lastClaimedPeriod = 0;
    }

    /**
     * @dev Claims vested tokens for the beneficiary.
     */
    function claimTokens() external {
        require(block.timestamp >= startTime, "Vesting has not started yet");

        // Calculate the current vesting period
        uint256 currentPeriod = (block.timestamp - startTime) / periodDuration + 1;

        // Ensure the beneficiary cannot claim tokens for periods in the future
        if (currentPeriod > totalPeriods) {
            currentPeriod = totalPeriods;
        }

        require(currentPeriod > lastClaimedPeriod, "No tokens available to claim");

        // Calculate the number of tokens to unlock
        uint256 periodsToClaim = currentPeriod - lastClaimedPeriod;
        uint256 amountToClaim = periodsToClaim * tokensPerPeriod;

        // Update the last claimed period
        lastClaimedPeriod = currentPeriod;

        // Transfer the tokens to the beneficiary
        require(token.transfer(beneficiary, amountToClaim), "Token transfer failed");
    }

    /**
     * @dev Returns the amount of tokens left to be claimed.
     */
    function getRemainingTokens() external view returns (uint256) {
        return totalAmount - (lastClaimedPeriod * tokensPerPeriod);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
