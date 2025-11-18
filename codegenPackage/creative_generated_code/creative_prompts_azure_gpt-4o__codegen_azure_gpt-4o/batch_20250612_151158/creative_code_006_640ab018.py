"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefi-ai.pages.dev
Prompt: Create a Solidity smart contract for a token vesting schedule, ensuring liquidity locks and alignment with the long-term commitment goals outlined on the QuDefi website.
Generated: DETERMINISTIC_640ab018e82cb380
Batch ID: 20250612_151158
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
 * @dev A token vesting smart contract designed to support liquidity locks
 * and long-term commitment goals. It allows tokens to be distributed over time
 * to beneficiaries while preventing premature access to locked tokens.
 */
contract TokenVesting {
    // Address of the ERC20 token contract
    IERC20 public immutable token;

    // Address of the beneficiary receiving vested tokens
    address public immutable beneficiary;

    // Start timestamp for the vesting schedule
    uint256 public immutable startTimestamp;

    // Duration of the vesting period (in seconds)
    uint256 public immutable vestingDuration;

    // Total amount of tokens allocated for vesting
    uint256 public immutable totalAllocated;

    // Amount of tokens already claimed by the beneficiary
    uint256 public tokensClaimed;

    // Event to track token claims
    event TokensClaimed(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the vesting schedule.
     * @param _token Address of the ERC20 token contract.
     * @param _beneficiary Address of the beneficiary to receive vested tokens.
     * @param _startTimestamp Start time for the vesting schedule (UNIX timestamp).
     * @param _vestingDuration Duration of the vesting schedule (in seconds).
     * @param _totalAllocated Total number of tokens allocated for vesting.
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _startTimestamp,
        uint256 _vestingDuration,
        uint256 _totalAllocated
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_vestingDuration > 0, "Vesting duration must be greater than zero");
        require(_totalAllocated > 0, "Total allocated tokens must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        startTimestamp = _startTimestamp;
        vestingDuration = _vestingDuration;
        totalAllocated = _totalAllocated;
    }

    /**
     * @dev Calculates the amount of vested tokens available to claim at the current time.
     * @return The amount of vested tokens available for the beneficiary.
     */
    function vestedAmount() public view returns (uint256) {
        if (block.timestamp < startTimestamp) {
            return 0; // Vesting has not started yet
        } else if (block.timestamp >= startTimestamp + vestingDuration) {
            return totalAllocated; // Vesting is complete
        } else {
            // Linear vesting calculation
            uint256 elapsedTime = block.timestamp - startTimestamp;
            return (totalAllocated * elapsedTime) / vestingDuration;
        }
    }

    /**
     * @dev Allows the beneficiary to claim their vested tokens.
     * Tokens are transferred to the beneficiary's address.
     */
    function claimTokens() external {
        require(msg.sender == beneficiary, "Only the beneficiary can claim tokens");

        uint256 claimableAmount = vestedAmount() - tokensClaimed;
        require(claimableAmount > 0, "No tokens available for claim");

        tokensClaimed += claimableAmount;

        // Transfer the tokens to the beneficiary
        require(token.transfer(beneficiary, claimableAmount), "Token transfer failed");

        emit TokensClaimed(beneficiary, claimableAmount);
    }

    /**
     * @dev Prevent accidental receipt of ETH or other tokens into this contract.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}

/**
 * @dev Minimal interface for an ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
