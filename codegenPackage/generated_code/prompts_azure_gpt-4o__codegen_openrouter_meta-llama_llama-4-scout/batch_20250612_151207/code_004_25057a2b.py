"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Write a smart contract in Solidity that facilitates transparent and long-term relationships between crypto-native funds and project founders, inspired by Innodapter ApS's values.
Generated: DETERMINISTIC_25057a2b683eaed9
Batch ID: 20250612_151207
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title InnoPartner
 * @author [Your Name]
 * @notice A smart contract facilitating transparent and long-term relationships between crypto-native funds and project founders.
 */
contract InnoPartner is Ownable {
    using SafeMath for uint256;

    // Mapping of project founders to their respective fund allocations
    mapping(address => mapping(address => uint256)) public fundAllocations;

    // Mapping of project founders to their respective fund vesting schedules
    mapping(address => VestingSchedule[]) public vestingSchedules;

    // Event emitted when a new fund allocation is made
    event FundAllocation(address indexed founder, address indexed fund, uint256 amount);

    // Event emitted when a new vesting schedule is created
    event VestingScheduleCreated(address indexed founder, address indexed fund, uint256 startTime, uint256 endTime, uint256 totalAmount);

    // Event emitted when a vesting schedule is updated
    event VestingScheduleUpdated(address indexed founder, address indexed fund, uint256 newAmount);

    // Event emitted when a fund is withdrawn
    event FundWithdrawn(address indexed founder, address indexed fund, uint256 amount);

    // Struct representing a vesting schedule
    struct VestingSchedule {
        uint256 startTime;
        uint256 endTime;
        uint256 totalAmount;
        uint256 vestedAmount;
    }

    /**
     * @notice Initializes the InnoPartner contract.
     */
    constructor() public {}

    /**
     * @notice Allocates funds to a project founder.
     * @param _founder The address of the project founder.
     * @param _fund The address of the fund.
     * @param _amount The amount of funds to allocate.
     */
    function allocateFund(address _founder, address _fund, uint256 _amount) public onlyOwner {
        require(_founder != address(0), "Founder address cannot be zero");
        require(_fund != address(0), "Fund address cannot be zero");
        require(_amount > 0, "Allocation amount must be greater than zero");

        fundAllocations[_founder][_fund] = fundAllocations[_founder][_fund].add(_amount);

        emit FundAllocation(_founder, _fund, _amount);
    }

    /**
     * @notice Creates a new vesting schedule for a project founder.
     * @param _founder The address of the project founder.
     * @param _fund The address of the fund.
     * @param _startTime The start time of the vesting schedule.
     * @param _endTime The end time of the vesting schedule.
     * @param _totalAmount The total amount of funds to vest.
     */
    function createVestingSchedule(address _founder, address _fund, uint256 _startTime, uint256 _endTime, uint256 _totalAmount) public onlyOwner {
        require(_founder != address(0), "Founder address cannot be zero");
        require(_fund != address(0), "Fund address cannot be zero");
        require(_startTime < _endTime, "Start time must be less than end time");
        require(_totalAmount > 0, "Vesting amount must be greater than zero");

        vestingSchedules[_founder].push(VestingSchedule(_startTime, _endTime, _totalAmount, 0));

        emit VestingScheduleCreated(_founder, _fund, _startTime, _endTime, _totalAmount);
    }

    /**
     * @notice Updates a vesting schedule for a project founder.
     * @param _founder The address of the project founder.
     * @param _fund The address of the fund.
     * @param _newAmount The new amount of funds to vest.
     */
    function updateVestingSchedule(address _founder, address _fund, uint256 _newAmount) public onlyOwner {
        require(_founder != address(0), "Founder address cannot be zero");
        require(_fund != address(0), "Fund address cannot be zero");
        require(_newAmount > 0, "Vesting amount must be greater than zero");

        for (uint256 i = 0; i < vestingSchedules[_founder].length; i++) {
            if (vestingSchedules[_founder][i].totalAmount > 0) {
                vestingSchedules[_founder][i].totalAmount = _newAmount;
                emit VestingScheduleUpdated(_founder, _fund, _newAmount);
                return;
            }
        }
    }

    /**
     * @notice Withdraws funds from a project founder's allocation.
     * @param _founder The address of the project founder.
     * @param _fund The address of the fund.
     * @param _amount The amount of funds to withdraw.
     */
    function withdrawFund(address _founder, address _fund, uint256 _amount) public {
        require(_founder != address(0), "Founder address cannot be zero");
        require(_fund != address(0), "Fund address cannot be zero");
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(fundAllocations[_founder][_fund] >= _amount, "Insufficient funds");

        fundAllocations[_founder][_fund] = fundAllocations[_founder][_fund].sub(_amount);

        emit FundWithdrawn(_founder, _fund, _amount);
    }

    /**
     * @notice Calculates the vested amount for a project founder.
     * @param _founder The address of the project founder.
     * @param _fund The address of the fund.
     */
    function getVestedAmount(address _founder, address _fund) public view returns (uint256) {
        for (uint256 i = 0; i < vestingSchedules[_founder].length; i++) {
            VestingSchedule memory schedule = vestingSchedules[_founder][i];
            if (schedule.startTime > 0 && schedule.endTime > 0) {
                uint256 timeElapsed = block.timestamp.sub(schedule.startTime);
                uint256 vestingDuration = schedule.endTime.sub(schedule.startTime);
                uint256 vestedAmount = schedule.totalAmount.mul(timeElapsed).div(vestingDuration);
                return vestedAmount > schedule.vestedAmount ? vestedAmount : schedule.vestedAmount;
            }
        }
        return 0;
    }
}
```
