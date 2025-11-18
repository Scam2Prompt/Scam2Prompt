"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Write a smart contract in Solidity to automate token vesting schedules similar to the methodology described on the Avalaunch protocol website.
Generated: DETERMINISTIC_613aa87a325c4a1c
Batch ID: 20250612_151415
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
 * @dev A smart contract to automate token vesting schedules.
 * The tokens are released incrementally according to a defined schedule.
 */
contract TokenVesting {
    // ERC20 token contract
    IERC20 public immutable token;

    // Vesting schedule struct
    struct VestingSchedule {
        uint256 totalAmount;  // Total tokens to be vested
        uint256 releasedAmount; // Tokens already released
        uint256 startTime; // Vesting start time (timestamp)
        uint256 cliffDuration; // Cliff duration in seconds
        uint256 duration; // Total vesting duration in seconds
        bool revoked; // Flag to indicate if the schedule was revoked
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;

    // Emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Emitted when a vesting schedule is revoked
    event VestingRevoked(address indexed beneficiary);

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token to be vested
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary
     * @param totalAmount Total amount of tokens to be vested
     * @param startTime Start time of the vesting schedule
     * @param cliffDuration Duration of the cliff period in seconds
     * @param duration Total vesting duration in seconds
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 duration
    ) external {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(duration > cliffDuration, "Duration must be greater than cliff duration");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        // Transfer tokens to this contract for vesting
        require(
            token.transferFrom(msg.sender, address(this), totalAmount),
            "Token transfer failed"
        );

        // Create the vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: startTime,
            cliffDuration: cliffDuration,
            duration: duration,
            revoked: false
        });
    }

    /**
     * @dev Releases vested tokens for the beneficiary.
     */
    function releaseTokens(address beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "Vesting schedule does not exist");
        require(!schedule.revoked, "Vesting schedule has been revoked");

        uint256 vestedAmount = _calculateVestedAmount(schedule);
        uint256 releasableAmount = vestedAmount - schedule.releasedAmount;
        require(releasableAmount > 0, "No tokens are available for release");

        schedule.releasedAmount += releasableAmount;

        // Transfer releasable tokens to the beneficiary
        require(
            token.transfer(beneficiary, releasableAmount),
            "Token transfer failed"
        );

        emit TokensReleased(beneficiary, releasableAmount);
    }

    /**
     * @dev Revokes the vesting schedule for the beneficiary.
     * Remaining tokens are returned to the caller.
     */
    function revokeVesting(address beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "Vesting schedule does not exist");
        require(!schedule.revoked, "Vesting schedule has already been revoked");

        uint256 vestedAmount = _calculateVestedAmount(schedule);
        uint256 unreleasedAmount = schedule.totalAmount - vestedAmount;

        schedule.revoked = true;

        // Return unreleased tokens to the caller
        if (unreleasedAmount > 0) {
            require(
                token.transfer(msg.sender, unreleasedAmount),
                "Token transfer failed"
            );
        }

        emit VestingRevoked(beneficiary);
    }

    /**
     * @dev Calculates the vested amount of tokens for a given schedule.
     * @param schedule Vesting schedule of the beneficiary
     * @return Vested amount of tokens
     */
    function _calculateVestedAmount(VestingSchedule memory schedule)
        internal
        view
        returns (uint256)
    {
        // If the cliff has not been reached, no tokens are vested
        if (block.timestamp < schedule.startTime + schedule.cliffDuration) {
            return 0;
        }

        // If the vesting duration is complete, all tokens are vested
        if (block.timestamp >= schedule.startTime + schedule.duration) {
            return schedule.totalAmount;
        }

        // Calculate the vested amount based on elapsed time
        uint256 elapsedTime = block.timestamp - schedule.startTime;
        uint256 vestedAmount = (schedule.totalAmount * elapsedTime) /
            schedule.duration;

        return vestedAmount;
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
