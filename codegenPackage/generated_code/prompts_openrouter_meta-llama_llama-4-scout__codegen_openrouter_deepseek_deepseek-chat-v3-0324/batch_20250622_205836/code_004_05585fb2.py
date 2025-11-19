"""
Generated Code Metadata:
========================
Original URL: https://sophpon.pages.dev
Prompt: Design a tokenomics model for a new blockchain project, inspired by Sophon's $SOPH token allocation and vesting schedule.
Generated: DETERMINISTIC_05585fb2456bbd78
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SophonToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocation percentages
    uint256 public constant TEAM_ALLOCATION = 20;
    uint256 public constant ADVISORS_ALLOCATION = 10;
    uint256 public constant ECOSYSTEM_FUND = 25;
    uint256 public constant PUBLIC_SALE = 15;
    uint256 public constant PRIVATE_SALE = 20;
    uint256 public constant COMMUNITY_REWARDS = 10;

    // Vesting schedules
    struct VestingSchedule {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliff;
    }

    mapping(address => VestingSchedule) public vestingSchedules;
    address[] public vestingParticipants;

    // Allocation addresses
    address public teamAddress;
    address public advisorsAddress;
    address public ecosystemFundAddress;
    address public publicSaleAddress;
    address public privateSaleAddress;
    address public communityRewardsAddress;

    // Total supply: 1 billion tokens with 18 decimals
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    constructor(
        address _teamAddress,
        address _advisorsAddress,
        address _ecosystemFundAddress,
        address _publicSaleAddress,
        address _privateSaleAddress,
        address _communityRewardsAddress
    ) ERC20("Sophon Token", "SOPH") {
        require(
            _teamAddress != address(0) &&
            _advisorsAddress != address(0) &&
            _ecosystemFundAddress != address(0) &&
            _publicSaleAddress != address(0) &&
            _privateSaleAddress != address(0) &&
            _communityRewardsAddress != address(0),
            "Invalid address"
        );

        teamAddress = _teamAddress;
        advisorsAddress = _advisorsAddress;
        ecosystemFundAddress = _ecosystemFundAddress;
        publicSaleAddress = _publicSaleAddress;
        privateSaleAddress = _privateSaleAddress;
        communityRewardsAddress = _communityRewardsAddress;

        // Mint initial allocations
        _mint(teamAddress, TOTAL_SUPPLY.mul(TEAM_ALLOCATION).div(100));
        _mint(advisorsAddress, TOTAL_SUPPLY.mul(ADVISORS_ALLOCATION).div(100));
        _mint(ecosystemFundAddress, TOTAL_SUPPLY.mul(ECOSYSTEM_FUND).div(100));
        _mint(publicSaleAddress, TOTAL_SUPPLY.mul(PUBLIC_SALE).div(100));
        _mint(privateSaleAddress, TOTAL_SUPPLY.mul(PRIVATE_SALE).div(100));
        _mint(communityRewardsAddress, TOTAL_SUPPLY.mul(COMMUNITY_REWARDS).div(100));
    }

    /**
     * @dev Setup vesting schedule for a participant
     * @param beneficiary Address of the beneficiary
     * @param amount Total amount to be vested
     * @param startTime When vesting starts (unix timestamp)
     * @param duration Duration of vesting in seconds
     * @param cliff Cliff period in seconds
     */
    function setupVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 startTime,
        uint256 duration,
        uint256 cliff
    ) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be greater than 0");
        require(startTime > block.timestamp, "Start time must be in the future");
        require(duration > 0, "Duration must be greater than 0");
        require(cliff <= duration, "Cliff must be less than or equal to duration");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            startTime: startTime,
            duration: duration,
            cliff: cliff
        });

        vestingParticipants.push(beneficiary);
    }

    /**
     * @dev Release vested tokens to beneficiary
     * @param beneficiary Address of the beneficiary
     */
    function releaseVestedTokens(address beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");

        uint256 unreleased = releasableAmount(beneficiary);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        _transfer(address(this), beneficiary, unreleased);
    }

    /**
     * @dev Calculate releasable amount for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function releasableAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        return vestedAmount(beneficiary).sub(schedule.releasedAmount);
    }

    /**
     * @dev Calculate vested amount for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return Amount of tokens that have vested
     */
    function vestedAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        if (block.timestamp < schedule.startTime.add(schedule.cliff)) {
            return 0;
        } else if (block.timestamp >= schedule.startTime.add(schedule.duration)) {
            return schedule.totalAmount;
        } else {
            uint256 timeElapsed = block.timestamp.sub(schedule.startTime);
            return schedule.totalAmount.mul(timeElapsed).div(schedule.duration);
        }
    }

    /**
     * @dev Get all vesting participants
     * @return Array of participant addresses
     */
    function getVestingParticipants() external view returns (address[] memory) {
        return vestingParticipants;
    }
}
```
