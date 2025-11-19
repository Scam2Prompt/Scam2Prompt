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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GIGAToken is ERC20, Ownable {
    using SafeMath for uint256;

    struct VestingSchedule {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliff;
    }

    mapping(address => VestingSchedule) public vestingSchedules;
    mapping(address => bool) public isExcludedFromVesting;

    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 private constant TEAM_ALLOCATION = 200_000_000 * 10**18; // 20% for team
    uint256 private constant ADVISORS_ALLOCATION = 100_000_000 * 10**18; // 10% for advisors
    uint256 private constant ECOSYSTEM_ALLOCATION = 300_000_000 * 10**18; // 30% for ecosystem
    uint256 private constant LIQUIDITY_ALLOCATION = 200_000_000 * 10**18; // 20% for liquidity
    uint256 private constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 10% for marketing
    uint256 private constant COMMUNITY_ALLOCATION = 100_000_000 * 10**18; // 10% for community

    constructor() ERC20("GIGA Token", "GIGA") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    function distributeInitialTokens(
        address teamWallet,
        address advisorsWallet,
        address ecosystemWallet,
        address liquidityWallet,
        address marketingWallet,
        address communityWallet
    ) external onlyOwner {
        require(
            balanceOf(msg.sender) >=
                TEAM_ALLOCATION +
                    ADVISORS_ALLOCATION +
                    ECOSYSTEM_ALLOCATION +
                    LIQUIDITY_ALLOCATION +
                    MARKETING_ALLOCATION +
                    COMMUNITY_ALLOCATION,
            "Insufficient balance for distribution"
        );

        _transfer(msg.sender, teamWallet, TEAM_ALLOCATION);
        _transfer(msg.sender, advisorsWallet, ADVISORS_ALLOCATION);
        _transfer(msg.sender, ecosystemWallet, ECOSYSTEM_ALLOCATION);
        _transfer(msg.sender, liquidityWallet, LIQUIDITY_ALLOCATION);
        _transfer(msg.sender, marketingWallet, MARKETING_ALLOCATION);
        _transfer(msg.sender, communityWallet, COMMUNITY_ALLOCATION);
    }

    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 duration,
        uint256 cliff
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(cliff <= duration, "Cliff must be less than or equal to duration");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: startTime,
            duration: duration,
            cliff: cliff
        });
    }

    function releaseVestedTokens(address beneficiary) external {
        require(vestingSchedules[beneficiary].totalAmount > 0, "No vesting schedule found");
        require(!isExcludedFromVesting[beneficiary], "Address is excluded from vesting");

        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        uint256 unreleased = releasableAmount(beneficiary);

        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        _transfer(owner(), beneficiary, unreleased);
    }

    function releasableAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        if (block.timestamp < schedule.startTime.add(schedule.cliff)) {
            return 0;
        } else if (block.timestamp >= schedule.startTime.add(schedule.duration)) {
            return schedule.totalAmount.sub(schedule.releasedAmount);
        } else {
            uint256 timeElapsed = block.timestamp.sub(schedule.startTime);
            uint256 vestedAmount = schedule.totalAmount.mul(timeElapsed).div(schedule.duration);
            return vestedAmount.sub(schedule.releasedAmount);
        }
    }

    function excludeFromVesting(address account, bool excluded) external onlyOwner {
        isExcludedFromVesting[account] = excluded;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(
            isExcludedFromVesting[msg.sender] || vestingSchedules[msg.sender].totalAmount == 0,
            "Account has vesting schedule"
        );
        return super.transfer(recipient, amount);
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(
            isExcludedFromVesting[sender] || vestingSchedules[sender].totalAmount == 0,
            "Account has vesting schedule"
        );
        return super.transferFrom(sender, recipient, amount);
    }
}
```
