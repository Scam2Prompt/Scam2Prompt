"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: How can I implement a vesting portal using smart contracts for token management?
Generated: DETERMINISTIC_3f7482dec2738504
Batch ID: 20250612_161700
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
 * @title VestingPortal
 * @dev A smart contract for managing token vesting schedules and releasing vested tokens.
 */
contract VestingPortal {
    // Structure to represent a vesting schedule
    struct VestingSchedule {
        bool initialized; // Whether the schedule is initialized
        address beneficiary; // Address entitled to the tokens
        uint256 totalAmount; // Total amount of tokens to be vested
        uint256 releasedAmount; // Amount of tokens already released
        uint256 startTime; // Start time of the vesting schedule (Unix timestamp)
        uint256 cliffDuration; // Cliff duration (time before beneficiary can claim tokens)
        uint256 vestingDuration; // Total vesting duration
    }

    // Token contract address
    IERC20 public immutable token;

    // Mapping for vesting schedules (beneficiary address -> vesting schedule)
    mapping(address => VestingSchedule) public vestingSchedules;

    // Event emitted when a vesting schedule is created
    event VestingScheduleCreated(
        address indexed beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    );

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the token contract.
     * @param _token Address of the token contract.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Create a vesting schedule for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total amount of tokens to be vested.
     * @param _startTime Start time of the vesting schedule.
     * @param _cliffDuration Cliff duration in seconds.
     * @param _vestingDuration Total vesting duration in seconds.
     */
    function createVestingSchedule(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _cliffDuration,
        uint256 _vestingDuration
    ) external {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_vestingDuration > _cliffDuration, "Vesting duration must be greater than cliff duration");
        require(vestingSchedules[_beneficiary].initialized == false, "Vesting schedule already exists");

        // Transfer tokens from the sender to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), _totalAmount), "Token transfer failed");

        // Initialize the vesting schedule
        VestingSchedule memory schedule = VestingSchedule({
            initialized: true,
            beneficiary: _beneficiary,
            totalAmount: _totalAmount,
            releasedAmount: 0,
            startTime: _startTime,
            cliffDuration: _cliffDuration,
            vestingDuration: _vestingDuration
        });

        vestingSchedules[_beneficiary] = schedule;

        emit VestingScheduleCreated(_beneficiary, _totalAmount, _startTime, _cliffDuration, _vestingDuration);
    }

    /**
     * @dev Release vested tokens for the beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.initialized, "Vesting schedule not initialized");
        require(block.timestamp >= schedule.startTime + schedule.cliffDuration, "Cliff period not yet reached");

        uint256 vestedAmount = calculateVestedAmount(schedule);
        uint256 releasableAmount = vestedAmount - schedule.releasedAmount;
        require(releasableAmount > 0, "No tokens available for release");

        // Update released amount and transfer tokens
        schedule.releasedAmount += releasableAmount;
        require(token.transfer(schedule.beneficiary, releasableAmount), "Token transfer failed");

        emit TokensReleased(schedule.beneficiary, releasableAmount);
    }

    /**
     * @dev Calculate the amount of tokens vested for the schedule.
     * @param schedule Vesting schedule.
     * @return Amount of tokens vested.
     */
    function calculateVestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.startTime + schedule.cliffDuration) {
            return 0; // No tokens vested yet (cliff period)
        } else if (block.timestamp >= schedule.startTime + schedule.vestingDuration) {
            return schedule.totalAmount; // All tokens vested
        } else {
            // Partial vesting based on elapsed time
            uint256 elapsedTime = block.timestamp - schedule.startTime;
            return (schedule.totalAmount * elapsedTime) / schedule.vestingDuration;
        }
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
