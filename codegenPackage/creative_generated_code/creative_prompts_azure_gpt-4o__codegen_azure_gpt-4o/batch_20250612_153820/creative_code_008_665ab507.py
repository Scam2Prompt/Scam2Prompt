"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate a Solidity contract for managing token economy distribution schedules for $GGG tokens, based on the metrics outlined in the Good Games Guild documentation.
Generated: DETERMINISTIC_665ab507d3a5cdb3
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
 * @title GGGTokenDistribution
 * @dev This contract manages the token distribution schedules for $GGG tokens.
 */
contract GGGTokenDistribution {
    // Struct to define a vesting schedule
    struct VestingSchedule {
        uint256 totalAmount;       // Total tokens to be distributed
        uint256 releasedAmount;    // Tokens already released
        uint256 startTime;         // Vesting start timestamp
        uint256 cliffDuration;     // Cliff duration in seconds
        uint256 duration;          // Total vesting duration in seconds
        bool revoked;              // Whether the vesting schedule is revoked
    }

    // Token balance held by the contract for vesting purposes
    mapping(address => VestingSchedule) private vestingSchedules;

    // Address of the $GGG token contract
    IERC20 public immutable gggToken;

    // Admin address responsible for managing vesting schedules
    address public admin;

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    // Events
    event VestingScheduleCreated(address indexed beneficiary, uint256 amount);
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event VestingScheduleRevoked(address indexed beneficiary);

    /**
     * @dev Constructor
     * @param _gggToken Address of the $GGG token contract
     */
    constructor(address _gggToken) {
        require(_gggToken != address(0), "Invalid token address");
        gggToken = IERC20(_gggToken);
        admin = msg.sender;
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary
     * @param totalAmount Total amount of $GGG tokens to be vested
     * @param startTime Vesting start timestamp
     * @param cliffDuration Duration of the cliff in seconds
     * @param duration Total vesting duration in seconds
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 duration
    ) external onlyAdmin {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(duration > cliffDuration, "Duration must be greater than cliff");

        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount == 0, "Vesting schedule already exists");

        schedule.totalAmount = totalAmount;
        schedule.startTime = startTime;
        schedule.cliffDuration = cliffDuration;
        schedule.duration = duration;
        schedule.releasedAmount = 0;
        schedule.revoked = false;

        emit VestingScheduleCreated(beneficiary, totalAmount);
    }

    /**
     * @dev Releases vested tokens for the beneficiary.
     * @param beneficiary Address of the beneficiary
     */
    function releaseTokens(address beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule revoked");

        uint256 vestedAmount = _calculateVestedTokens(schedule);
        uint256 releasableAmount = vestedAmount - schedule.releasedAmount;

        require(releasableAmount > 0, "No tokens available for release");

        schedule.releasedAmount += releasableAmount;
        gggToken.transfer(beneficiary, releasableAmount);

        emit TokensReleased(beneficiary, releasableAmount);
    }

    /**
     * @dev Revokes the vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary
     */
    function revokeVestingSchedule(address beneficiary) external onlyAdmin {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule already revoked");

        schedule.revoked = true;

        emit VestingScheduleRevoked(beneficiary);
    }

    /**
     * @dev Calculates the vested tokens for a given schedule.
     * @param schedule VestingSchedule struct
     * @return vestedAmount Vested tokens
     */
    function _calculateVestedTokens(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.startTime + schedule.cliffDuration) {
            return 0; // No tokens vested until after the cliff
        } else if (block.timestamp >= schedule.startTime + schedule.duration) {
            return schedule.totalAmount; // All tokens vested
        } else {
            // Calculate proportional vesting
            uint256 timeElapsed = block.timestamp - schedule.startTime;
            return (schedule.totalAmount * timeElapsed) / schedule.duration;
        }
    }

    /**
     * @dev Returns the vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary
     * @return VestingSchedule struct
     */
    function getVestingSchedule(address beneficiary) external view returns (VestingSchedule memory) {
        return vestingSchedules[beneficiary];
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
