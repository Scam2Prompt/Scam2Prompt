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

/**
 * @title TokenVesting
 * @dev A contract to manage post-presale token release schedule for $EMT tokens.
 * The distribution model ensures biweekly 20% releases until the balance is fully distributed.
 */
contract TokenVesting {
    // The address of the token contract
    IERC20 public token;

    // Address of the beneficiary
    address public beneficiary;

    // Total amount of tokens to be vested
    uint256 public totalVested;

    // Amount of tokens released so far
    uint256 public released;

    // Timestamp of the start of vesting schedule
    uint256 public startTime;

    // Duration between each release (biweekly: 14 days)
    uint256 public constant RELEASE_INTERVAL = 14 days;

    // Percentage of tokens released per interval (20%)
    uint256 public constant RELEASE_PERCENTAGE = 20;

    // Events
    event TokensReleased(uint256 amount);
    event BeneficiaryUpdated(address newBeneficiary);

    /**
     * @dev Constructor to initialize the vesting contract.
     * @param _token Address of the $EMT token contract.
     * @param _beneficiary Address of the beneficiary receiving the vested tokens.
     * @param _totalVested Total amount of tokens to be vested.
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _totalVested
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalVested > 0, "Total vested must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        totalVested = _totalVested;
        startTime = block.timestamp; // Set the start time of the vesting
    }

    /**
     * @dev Function to release tokens based on the vesting schedule.
     */
    function release() external {
        require(block.timestamp >= startTime, "Vesting has not started yet");

        // Calculate the number of intervals passed since the start time
        uint256 intervalsPassed = (block.timestamp - startTime) / RELEASE_INTERVAL;

        // Calculate the maximum amount of tokens that can be released so far
        uint256 maxReleased = (totalVested * intervalsPassed * RELEASE_PERCENTAGE) / 100;

        // Ensure the new released amount does not exceed the total vested amount
        if (maxReleased > totalVested) {
            maxReleased = totalVested;
        }

        // Calculate the difference between the maximum released and already released tokens
        uint256 releaseAmount = maxReleased - released;

        require(releaseAmount > 0, "No tokens available for release");

        // Update the released amount
        released += releaseAmount;

        // Transfer tokens to the beneficiary
        require(
            token.transfer(beneficiary, releaseAmount),
            "Token transfer failed"
        );

        emit TokensReleased(releaseAmount);
    }

    /**
     * @dev Function to update the beneficiary address.
     * @param _newBeneficiary The new beneficiary address.
     */
    function updateBeneficiary(address _newBeneficiary) external {
        require(msg.sender == beneficiary, "Only the beneficiary can update the address");
        require(_newBeneficiary != address(0), "New beneficiary address cannot be zero");

        beneficiary = _newBeneficiary;

        emit BeneficiaryUpdated(_newBeneficiary);
    }

    /**
     * @dev Function to check the amount of tokens left for release.
     * @return The remaining amount of tokens to be released.
     */
    function remainingTokens() external view returns (uint256) {
        return totalVested - released;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
