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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenVesting
 * @dev A contract for managing a token vesting schedule where tokens are released in increments.
 */
contract TokenVesting is Ownable {
    // The token being vested
    IERC20 public token;

    // Beneficiary of tokens after they are released
    address public beneficiary;

    // Total amount of tokens to be vested
    uint256 public totalAmount;

    // Timestamp when vesting starts
    uint256 public start;

    // Duration of the vesting period in seconds
    uint256 public duration;

    // The amount of tokens to be released at each increment
    uint256 public releaseAmount;

    // The timestamp of the last release
    uint256 public lastReleaseTime;

    // Total tokens released
    uint256 public released;

    // Events
    event Released(uint256 amount);

    /**
     * @param _token The address of the token contract
     * @param _beneficiary The beneficiary of the tokens
     * @param _totalAmount The total amount of tokens to be vested
     * @param _start The start time of the vesting schedule
     * @param _duration The duration of the vesting in seconds
     * @param _releaseAmount The amount of tokens to release at each increment
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _start,
        uint256 _duration,
        uint256 _releaseAmount
    ) {
        require(_beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        require(_releaseAmount > 0, "Release amount must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        totalAmount = _totalAmount;
        start = _start;
        duration = _duration;
        releaseAmount = _releaseAmount;
        lastReleaseTime = _start;
    }

    /**
     * @dev Releases the vested tokens to the beneficiary.
     */
    function release() public {
        // Calculate the number of periods since the last release
        uint256 currentTime = block.timestamp;
        require(currentTime >= lastReleaseTime, "Cannot release before last release time");

        // Calculate the number of increments that can be released
        uint256 periodsElapsed = (currentTime - lastReleaseTime) / duration;
        uint256 unreleasedTokens = periodsElapsed * releaseAmount;

        // Ensure not to release more tokens than the total amount
        if (released + unreleasedTokens > totalAmount) {
            unreleasedTokens = totalAmount - released;
        }

        require(unreleasedTokens > 0, "No tokens to release");

        // Update state variables
        released += unreleasedTokens;
        lastReleaseTime = currentTime;

        // Transfer tokens to the beneficiary
        token.transfer(beneficiary, unreleasedTokens);
        emit Released(unreleasedTokens);
    }

    /**
     * @dev Allows the owner to withdraw tokens in case of emergency.
     * @param amount The amount of tokens to withdraw.
     */
    function recoverTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient balance in contract");
        token.transfer(owner(), amount);
    }

    /**
     * @dev Returns the amount of releasable tokens for the beneficiary.
     */
    function releasableAmount() public view returns (uint256) {
        uint256 currentTime = block.timestamp;
        if (currentTime < lastReleaseTime) {
            return 0;
        }
        uint256 periodsElapsed = (currentTime - start) / duration;
        uint256 unreleasedTokens = periodsElapsed * releaseAmount;

        if (released + unreleasedTokens > totalAmount) {
            unreleasedTokens = totalAmount - released;
        }

        return unreleasedTokens;
    }
}
```
