"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuvius.com
Prompt: Provide an example of a smart contract implementation that enforces the lock-up period and vesting parameters outlined by Illuvius for MXNA tokens.
Generated: DETERMINISTIC_753c8afd8edbb621
Batch ID: 20250612_155048
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
 * @title MXNA Token Lock-Up and Vesting Smart Contract
 * @dev Implements a lock-up period and vesting schedule for MXNA tokens
 */
contract MXNALockupVesting {
    // Token contract interface
    IERC20 public immutable token;

    // Struct to track vesting details
    struct VestingSchedule {
        uint256 totalAmount;         // Total tokens to be vested
        uint256 amountClaimed;       // Tokens already claimed
        uint256 startTime;           // Vesting start time
        uint256 lockupDuration;      // Lock-up period duration (in seconds)
        uint256 vestingDuration;     // Total vesting duration (in seconds)
    }

    // Mapping to associate beneficiary addresses with their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Events for logging contract activity
    event TokensAllocated(address indexed beneficiary, uint256 totalAmount);
    event TokensClaimed(address indexed beneficiary, uint256 amountClaimed);

    /**
     * @dev Constructor to initialize the contract with the token address
     * @param _token Address of the MXNA token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Allocates tokens to a beneficiary with lock-up and vesting parameters
     * @param beneficiary Address of the beneficiary
     * @param totalAmount Total amount of tokens to allocate
     * @param lockupDuration Lock-up period duration (in seconds)
     * @param vestingDuration Total vesting duration (in seconds)
     */
    function allocateTokens(
        address beneficiary,
        uint256 totalAmount,
        uint256 lockupDuration,
        uint256 vestingDuration
    ) external {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(lockupDuration < vestingDuration, "Lock-up duration must be less than vesting duration");

        // Ensure no prior vesting schedule exists for the beneficiary
        require(
            vestingSchedules[beneficiary].totalAmount == 0,
            "Vesting schedule already exists for the beneficiary"
        );

        // Transfer tokens to the contract
        require(
            token.transferFrom(msg.sender, address(this), totalAmount),
            "Token transfer failed"
        );

        // Create a new vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            amountClaimed: 0,
            startTime: block.timestamp,
            lockupDuration: lockupDuration,
            vestingDuration: vestingDuration
        });

        emit TokensAllocated(beneficiary, totalAmount);
    }

    /**
     * @dev Allows a beneficiary to claim vested tokens
     */
    function claimTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        // Ensure the vesting schedule exists
        require(schedule.totalAmount > 0, "No vesting schedule found");

        // Ensure lock-up period is over
        require(
            block.timestamp >= schedule.startTime + schedule.lockupDuration,
            "Lock-up period is not over yet"
        );

        // Calculate available claimable tokens
        uint256 elapsedTime = block.timestamp - schedule.startTime;
        uint256 vestingTime = schedule.vestingDuration;
        uint256 vestedAmount = (schedule.totalAmount * elapsedTime) / vestingTime;
        uint256 claimableAmount = vestedAmount - schedule.amountClaimed;

        // Ensure there are tokens to claim
        require(claimableAmount > 0, "No tokens available for claiming");

        // Update the amount claimed
        schedule.amountClaimed += claimableAmount;

        // Transfer tokens to the beneficiary
        require(token.transfer(msg.sender, claimableAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Returns the claimable token amount for a given beneficiary
     * @param beneficiary Address of the beneficiary
     * @return claimableAmount Tokens available for claiming
     */
    function getClaimableAmount(address beneficiary) external view returns (uint256 claimableAmount) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        // Ensure the vesting schedule exists
        if (schedule.totalAmount == 0) {
            return 0;
        }

        // Ensure lock-up period is over
        if (block.timestamp < schedule.startTime + schedule.lockupDuration) {
            return 0;
        }

        // Calculate available claimable tokens
        uint256 elapsedTime = block.timestamp - schedule.startTime;
        uint256 vestingTime = schedule.vestingDuration;
        uint256 vestedAmount = (schedule.totalAmount * elapsedTime) / vestingTime;

        return vestedAmount - schedule.amountClaimed;
    }
}

/**
 * @dev IERC20 interface for token contract compatibility
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
