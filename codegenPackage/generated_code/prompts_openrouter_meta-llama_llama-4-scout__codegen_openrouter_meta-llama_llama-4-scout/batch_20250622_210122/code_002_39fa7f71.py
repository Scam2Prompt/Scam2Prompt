"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-en.web.app
Prompt: Generate a smart contract in Solidity for a BEP20 token like $GIGA, including functions for token distribution and vesting.
Generated: DETERMINISTIC_39fa7f71674f9a6d
Batch ID: 20250622_210122
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GigaToken
 * @author [Your Name]
 * @notice A BEP20 token with token distribution and vesting functionality
 */
contract GigaToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of vesting schedules
    mapping (address => VestingSchedule) public vestingSchedules;

    // Mapping of token distribution recipients
    mapping (address => bool) public distributionRecipients;

    // Total tokens to be distributed
    uint256 public totalDistributionTokens;

    // Distribution start timestamp
    uint256 public distributionStart;

    // Distribution end timestamp
    uint256 public distributionEnd;

    // Vesting duration in seconds
    uint256 public vestingDuration;

    // Vesting cliff in seconds
    uint256 public vestingCliff;

    /**
     * @notice Constructor
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param totalSupply_ Total token supply
     * @param distributionStart_ Distribution start timestamp
     * @param distributionEnd_ Distribution end timestamp
     * @param vestingDuration_ Vesting duration in seconds
     * @param vestingCliff_ Vesting cliff in seconds
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        uint256 distributionStart_,
        uint256 distributionEnd_,
        uint256 vestingDuration_,
        uint256 vestingCliff_
    ) ERC20(name_, symbol_) {
        require(distributionStart_ < distributionEnd_, "Distribution start must be before end");
        require(vestingDuration_ > 0, "Vesting duration must be greater than 0");
        require(vestingCliff_ <= vestingDuration_, "Vesting cliff must be less than or equal to vesting duration");

        _mint(msg.sender, totalSupply_);
        totalDistributionTokens = totalSupply_.mul(75, 100); // 75% of total supply for distribution
        distributionStart = distributionStart_;
        distributionEnd = distributionEnd_;
        vestingDuration = vestingDuration_;
        vestingCliff = vestingCliff_;
    }

    /**
     * @notice Distributes tokens to a recipient
     * @param recipient Recipient address
     * @param amount Amount of tokens to distribute
     */
    function distributeTokens(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than 0");
        require(totalDistributionTokens >= amount, "Insufficient distribution tokens");

        distributionRecipients[recipient] = true;
        _transfer(msg.sender, recipient, amount);
        totalDistributionTokens = totalDistributionTokens.sub(amount);
    }

    /**
     * @notice Creates a vesting schedule for a recipient
     * @param recipient Recipient address
     * @param vestingStart Vesting start timestamp
     * @param vestingEnd Vesting end timestamp
     */
    function createVestingSchedule(address recipient, uint256 vestingStart, uint256 vestingEnd) public onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(vestingStart < vestingEnd, "Vesting start must be before end");

        vestingSchedules[recipient] = VestingSchedule(vestingStart, vestingEnd, 0);
    }

    /**
     * @notice Releases vested tokens for a recipient
     */
    function releaseVestedTokens() public nonReentrant {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.start != 0, "No vesting schedule found");

        uint256 vestedAmount = calculateVestedAmount(schedule);
        schedule.released = schedule.released.add(vestedAmount);

        _transfer(msg.sender, msg.sender, vestedAmount);
    }

    /**
     * @notice Calculates the vested amount for a recipient
     * @param schedule Vesting schedule
     * @return Vested amount
     */
    function calculateVestedAmount(VestingSchedule storage schedule) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp.sub(schedule.start);
        if (timeElapsed < vestingCliff) {
            return 0;
        }

        uint256 vestingPeriod = schedule.end.sub(schedule.start);
        uint256 vestedPercentage = timeElapsed.mul(100).div(vestingPeriod);
        if (vestedPercentage > 100) {
            vestedPercentage = 100;
        }

        uint256 vestedAmount = balanceOf(msg.sender).mul(vestedPercentage, 100).sub(schedule.released);
        return vestedAmount;
    }

    /**
     * @dev Struct representing a vesting schedule
     */
    struct VestingSchedule {
        uint256 start;
        uint256 end;
        uint256 released;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
