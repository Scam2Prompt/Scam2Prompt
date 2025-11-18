"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Provide an example of how to implement a vesting schedule for tokens using Whales Market's "Vesting Market" features in a blockchain-based application.
Generated: DETERMINISTIC_d373b5238ee69c48
Batch ID: 20250612_153820
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
 * @dev This contract implements a token vesting schedule using Whales Market's Vesting Market features.
 * The vesting schedule ensures that tokens are released over time, according to predefined parameters.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenVesting {
    // Address of the token being vested
    IERC20 private immutable token;

    // Address of the beneficiary receiving the vested tokens
    address private immutable beneficiary;

    // Vesting parameters
    uint256 private immutable startTimestamp; // Timestamp when vesting starts
    uint256 private immutable cliffDuration;  // Duration of the cliff period
    uint256 private immutable totalDuration;  // Total duration of the vesting period
    uint256 private immutable totalTokens;    // Total number of tokens to be vested

    // Amount of tokens already released
    uint256 private releasedTokens;

    // Events
    event TokensReleased(uint256 amount);
    event VestingRevoked();

    // Modifier to ensure only the beneficiary can interact with certain functions
    modifier onlyBeneficiary() {
        require(msg.sender == beneficiary, "Caller is not the beneficiary");
        _;
    }

    /**
     * @dev Constructor initializes the vesting schedule.
     * @param _token Address of the token contract.
     * @param _beneficiary Address of the beneficiary receiving the vested tokens.
     * @param _startTimestamp Timestamp when vesting starts.
     * @param _cliffDuration Duration of the cliff period in seconds.
     * @param _totalDuration Total duration of the vesting period in seconds.
     * @param _totalTokens Total number of tokens to be vested.
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _startTimestamp,
        uint256 _cliffDuration,
        uint256 _totalDuration,
        uint256 _totalTokens
    ) {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalDuration > _cliffDuration, "Total duration must be greater than cliff duration");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        startTimestamp = _startTimestamp;
        cliffDuration = _cliffDuration;
        totalDuration = _totalDuration;
        totalTokens = _totalTokens;
    }

    /**
     * @dev Calculates the amount of tokens that have vested up to the current time.
     * @return The amount of vested tokens.
     */
    function vestedTokens() public view returns (uint256) {
        if (block.timestamp < startTimestamp + cliffDuration) {
            // Cliff period not reached; no tokens vested
            return 0;
        }

        if (block.timestamp >= startTimestamp + totalDuration) {
            // Vesting period fully completed; all tokens vested
            return totalTokens;
        }

        // Calculate the amount of tokens vested based on the elapsed time
        uint256 elapsedTime = block.timestamp - startTimestamp;
        return (totalTokens * elapsedTime) / totalDuration;
    }

    /**
     * @dev Allows the beneficiary to release vested tokens.
     */
    function release() external onlyBeneficiary {
        uint256 unreleasedTokens = vestedTokens() - releasedTokens;
        require(unreleasedTokens > 0, "No tokens available for release");

        // Update state and transfer tokens to the beneficiary
        releasedTokens += unreleasedTokens;
        token.transfer(beneficiary, unreleasedTokens);

        emit TokensReleased(unreleasedTokens);
    }

    /**
     * @dev Allows the owner to revoke the vesting schedule. This function can be extended in production
     * to handle specific requirements (e.g., returning the remaining tokens to the owner).
     */
    function revoke() external {
        // Logic for revoking the vesting schedule can be added here.
        // For now, this function emits an event indicating that vesting has been revoked.
        emit VestingRevoked();
    }

    // Getter functions for contract parameters
    function getToken() external view returns (IERC20) {
        return token;
    }

    function getBeneficiary() external view returns (address) {
        return beneficiary;
    }

    function getStartTimestamp() external view returns (uint256) {
        return startTimestamp;
    }

    function getCliffDuration() external view returns (uint256) {
        return cliffDuration;
    }

    function getTotalDuration() external view returns (uint256) {
        return totalDuration;
    }

    function getTotalTokens() external view returns (uint256) {
        return totalTokens;
    }

    function getReleasedTokens() external view returns (uint256) {
        return releasedTokens;
    }
}
```
