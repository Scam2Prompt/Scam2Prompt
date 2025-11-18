"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Write a smart contract in Solidity for a token vesting system tailored for ScapesMania's $MANIA token, ensuring compatibility with the project's Web3 gaming ecosystem.
Generated: DETERMINISTIC_fefe6236912ee6bb
Batch ID: 20250612_152714
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
 * @dev A smart contract for managing token vesting tailored to ScapesMania's $MANIA token.
 */
contract TokenVesting {
    // The $MANIA token contract address
    IERC20 public immutable token;

    // Struct to hold vesting details
    struct VestingSchedule {
        uint256 amount;            // Total vested amount
        uint256 released;          // Amount already released
        uint256 start;             // Start time of the vesting (UNIX timestamp)
        uint256 duration;          // Duration of the vesting period in seconds
    }

    // Mapping user addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Event to notify when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Event to notify when a new vesting schedule is created
    event VestingScheduleCreated(address indexed beneficiary, uint256 amount, uint256 start, uint256 duration);

    /**
     * @dev Constructor to set the $MANIA token address.
     * @param _token Address of the $MANIA token contract.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param amount Number of tokens to be vested.
     * @param start Start time of the vesting (UNIX timestamp).
     * @param duration Duration of the vesting period in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 start,
        uint256 duration
    ) external {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(amount > 0, "Vesting amount must be greater than zero");
        require(duration > 0, "Vesting duration must be greater than zero");
        require(vestingSchedules[beneficiary].amount == 0, "Vesting schedule already exists for this beneficiary");

        // Transfer tokens from sender to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            amount: amount,
            released: 0,
            start: start,
            duration: duration
        });

        emit VestingScheduleCreated(beneficiary, amount, start, duration);
    }

    /**
     * @dev Releases vested tokens for the calling beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.amount > 0, "No vesting schedule found for the caller");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are available for release");

        schedule.released += unreleased;

        require(token.transfer(msg.sender, unreleased), "Token transfer failed");
        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculates the amount of tokens that are releasable for the beneficiary.
     * @param schedule The vesting schedule of the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        uint256 vestedAmount = _vestedAmount(schedule);
        return vestedAmount - schedule.released;
    }

    /**
     * @dev Calculates the amount of tokens that have vested.
     * @param schedule The vesting schedule of the beneficiary.
     * @return The amount of tokens that have vested.
     */
    function _vestedAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.amount;
        } else {
            return (schedule.amount * (block.timestamp - schedule.start)) / schedule.duration;
        }
    }
}

/**
 * @dev Interface for ERC20 token functions used in the vesting contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
