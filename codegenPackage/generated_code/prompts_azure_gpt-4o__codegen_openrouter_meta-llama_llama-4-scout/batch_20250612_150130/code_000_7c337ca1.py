"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a smart contract in Solidity that implements the vesting and distribution mechanics described in the $EARNM 'Fractal Box' protocol, ensuring a 12-month holding period and automatic redistribution of forfeited assets.
Generated: DETERMINISTIC_7c337ca1621ea956
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FractalBoxVestingContract
 * @author [Your Name]
 * @notice Implements vesting and distribution mechanics for $EARNM 'Fractal Box' protocol.
 */
contract FractalBoxVestingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Constants
    uint256 public constant VESTING_PERIOD = 365 days; // 12 months
    uint256 public constant CLIFF_PERIOD = 0; // No cliff

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Mapping of forfeited assets
    mapping(address => uint256) public forfeitedAssets;

    // IERC20 token instance
    IERC20 public token;

    // Distributor address
    address public distributor;

    // Event emitted when vesting schedule is created
    event VestingScheduleCreated(address indexed beneficiary, uint256 startTime, uint256 endTime, uint256 amount);

    // Event emitted when tokens are vested
    event TokensVested(address indexed beneficiary, uint256 amount);

    // Event emitted when tokens are forfeited
    event TokensForfeited(address indexed beneficiary, uint256 amount);

    // Event emitted when tokens are redistributed
    event TokensRedistributed(address indexed redistributor, uint256 amount);

    /**
     * @param _token IERC20 token instance
     * @param _distributor Distributor address
     */
    constructor(IERC20 _token, address _distributor) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_distributor != address(0), "Distributor address cannot be zero");

        token = _token;
        distributor = _distributor;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param amount Amount of tokens to vest.
     */
    function createVestingSchedule(address beneficiary, uint256 amount) public {
        require(msg.sender == distributor, "Only distributor can create vesting schedules");

        // Calculate start and end times
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(VESTING_PERIOD);

        // Update vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule(startTime, endTime, amount);

        // Emit event
        emit VestingScheduleCreated(beneficiary, startTime, endTime, amount);

        // Transfer tokens to the contract
        token.safeTransferFrom(distributor, address(this), amount);
    }

    /**
     * @dev Vests tokens for a beneficiary.
     */
    function vest() public {
        address beneficiary = msg.sender;
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        require(schedule.startTime != 0, "Vesting schedule not found");

        // Calculate vested amount
        uint256 vestedAmount = calculateVestedAmount(schedule);

        // Update vesting schedule
        schedule.endTime = block.timestamp;

        // Transfer vested tokens to beneficiary
        token.safeTransfer(beneficiary, vestedAmount);

        // Emit event
        emit TokensVested(beneficiary, vestedAmount);
    }

    /**
     * @dev Forfeits tokens for a beneficiary.
     */
    function forfeit() public {
        address beneficiary = msg.sender;
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        require(schedule.startTime != 0, "Vesting schedule not found");

        // Calculate forfeited amount
        uint256 forfeitedAmount = schedule.amount.sub(calculateVestedAmount(schedule));

        // Update forfeited assets
        forfeitedAssets[beneficiary] = forfeitedAssets[beneficiary].add(forfeitedAmount);

        // Update vesting schedule
        schedule.endTime = block.timestamp;

        // Emit event
        emit TokensForfeited(beneficiary, forfeitedAmount);
    }

    /**
     * @dev Redistribute forfeited assets.
     */
    function redistributeForfeitedAssets() public {
        require(msg.sender == distributor, "Only distributor can redistribute forfeited assets");

        uint256 totalForfeitedAssets = 0;
        for (address beneficiary in forfeitedAssets) {
            totalForfeitedAssets = totalForfeitedAssets.add(forfeitedAssets[beneficiary]);
        }

        // Transfer forfeited assets to distributor
        token.safeTransfer(distributor, totalForfeitedAssets);

        // Emit event
        emit TokensRedistributed(distributor, totalForfeitedAssets);

        // Reset forfeited assets
        for (address beneficiary in forfeitedAssets) {
            forfeitedAssets[beneficiary] = 0;
        }
    }

    /**
     * @dev Calculates vested amount for a vesting schedule.
     * @param schedule Vesting schedule.
     * @return Vested amount.
     */
    function calculateVestedAmount(VestingSchedule storage schedule) internal view returns (uint256) {
        if (block.timestamp >= schedule.endTime) {
            return schedule.amount;
        }

        uint256 vestedTime = block.timestamp.sub(schedule.startTime);
        return schedule.amount.mul(vestedTime).div(VESTING_PERIOD);
    }

    // Struct for vesting schedule
    struct VestingSchedule {
        uint256 startTime;
        uint256 endTime;
        uint256 amount;
    }
}
```
