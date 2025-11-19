"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: Can you provide an example of a smart contract for managing vesting schedules in a blockchain project?
Generated: DETERMINISTIC_3153d600bfe4bc04
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
 * @title VestingContract
 * @dev A smart contract for managing token vesting schedules.
 * This allows the allocation of tokens to beneficiaries with a vesting schedule.
 */

contract VestingContract {
    // Structure to represent a vesting schedule
    struct VestingSchedule {
        uint256 totalAmount;    // Total amount of tokens allocated
        uint256 releasedAmount; // Amount of tokens already released
        uint256 startTime;      // Vesting start time (timestamp)
        uint256 cliffDuration;  // Cliff duration in seconds
        uint256 vestingDuration;// Total vesting duration in seconds
        bool revoked;           // Indicates whether the vesting schedule has been revoked
    }

    // Mapping of beneficiary to their vesting schedule
    mapping(address => VestingSchedule) private vestingSchedules;

    // Token contract address
    IERC20 private immutable token;

    // Owner of the contract (can revoke vesting schedules)
    address private owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Emitted when tokens are released for a beneficiary.
     */
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Emitted when a vesting schedule is revoked.
     */
    event VestingRevoked(address indexed beneficiary);

    /**
     * @dev Constructor to initialize the contract with the token address and owner.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Function to create a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param totalAmount Total amount of tokens allocated.
     * @param startTime Vesting start time (timestamp).
     * @param cliffDuration Cliff duration in seconds.
     * @param vestingDuration Total vesting duration in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists for beneficiary");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: startTime,
            cliffDuration: cliffDuration,
            vestingDuration: vestingDuration,
            revoked: false
        });

        token.transferFrom(msg.sender, address(this), totalAmount);
    }

    /**
     * @dev Function to release vested tokens for a beneficiary.
     */
    function release() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule has been revoked");

        uint256 vestedAmount = _calculateVestedAmount(schedule);
        uint256 releasableAmount = vestedAmount - schedule.releasedAmount;

        require(releasableAmount > 0, "No tokens available for release");

        schedule.releasedAmount += releasableAmount;
        token.transfer(msg.sender, releasableAmount);

        emit TokensReleased(msg.sender, releasableAmount);
    }

    /**
     * @dev Function to revoke a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     */
    function revokeVestingSchedule(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule already revoked");

        uint256 vestedAmount = _calculateVestedAmount(schedule);
        uint256 unreleasedAmount = schedule.totalAmount - vestedAmount;

        schedule.revoked = true;

        if (unreleasedAmount > 0) {
            token.transfer(owner, unreleasedAmount);
        }

        emit VestingRevoked(beneficiary);
    }

    /**
     * @dev Internal function to calculate the amount of vested tokens.
     * @param schedule Vesting schedule of the beneficiary.
     * @return Amount of vested tokens.
     */
    function _calculateVestedAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.startTime + schedule.cliffDuration) {
            return 0;
        }
        if (block.timestamp >= schedule.startTime + schedule.vestingDuration) {
            return schedule.totalAmount;
        }

        uint256 elapsedTime = block.timestamp - schedule.startTime;
        return (schedule.totalAmount * elapsedTime) / schedule.vestingDuration;
    }

    /**
     * @dev Function to get the vesting schedule details of a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @return Vesting schedule details.
     */
    function getVestingSchedule(address beneficiary) external view returns (VestingSchedule memory) {
        return vestingSchedules[beneficiary];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
