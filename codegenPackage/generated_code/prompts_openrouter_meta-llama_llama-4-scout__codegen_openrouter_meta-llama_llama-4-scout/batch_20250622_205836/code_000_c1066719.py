"""
Generated Code Metadata:
========================
Original URL: https://appmasks.pages.dev
Prompt: Write a smart contract for a tokenized engagement platform using Solidity, incorporating a vesting airdrop feature.
Generated: DETERMINISTIC_c1066719ed5f9b87
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Tokenized Engagement Platform
 * @author [Your Name]
 * @notice A tokenized engagement platform with a vesting airdrop feature.
 */
contract TokenizedEngagementPlatform is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Mapping of claimed amounts
    mapping(address => uint256) public claimedAmounts;

    // Airdrop start and end timestamps
    uint256 public airdropStart;
    uint256 public airdropEnd;

    // Total airdrop amount
    uint256 public totalAirdropAmount;

    // Token vesting duration in seconds
    uint256 public vestingDuration;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param airdropStartTimestamp Airdrop start timestamp
     * @param airdropEndTimestamp Airdrop end timestamp
     * @param vestingDurationSeconds Token vesting duration in seconds
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 airdropStartTimestamp,
        uint256 airdropEndTimestamp,
        uint256 vestingDurationSeconds
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        airdropStart = airdropStartTimestamp;
        airdropEnd = airdropEndTimestamp;
        vestingDuration = vestingDurationSeconds;
        totalAirdropAmount = totalSupply.div(10); // 10% of total supply for airdrop
    }

    /**
     * @notice Claim airdrop tokens
     */
    function claimAirdrop() external nonReentrant {
        require(airdropStart <= block.timestamp && block.timestamp <= airdropEnd, "Airdrop not active");
        require(vestingSchedules[msg.sender].start == 0, "Vesting schedule already created");

        vestingSchedules[msg.sender] = VestingSchedule(
            block.timestamp,
            totalAirdropAmount.div(100), // Assuming 100 recipients
            0
        );

        emit AirdropClaimed(msg.sender, vestingSchedules[msg.sender].amount);
    }

    /**
     * @notice Release vested tokens
     */
    function releaseVestedTokens() external nonReentrant {
        require(vestingSchedules[msg.sender].start != 0, "No vesting schedule found");

        uint256 vestedAmount = calculateVestedAmount(msg.sender);
        require(vestedAmount > 0, "No vested tokens to release");

        vestingSchedules[msg.sender].released = vestingSchedules[msg.sender].released.add(vestedAmount);
        claimedAmounts[msg.sender] = claimedAmounts[msg.sender].add(vestedAmount);

        _transfer(address(this), msg.sender, vestedAmount);

        emit TokensReleased(msg.sender, vestedAmount);
    }

    /**
     * @notice Calculate vested amount
     * @param beneficiary Address of beneficiary
     * @return Vested amount
     */
    function calculateVestedAmount(address beneficiary) internal view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        uint256 timeElapsed = block.timestamp.sub(schedule.start);
        uint256 vestedPercentage = timeElapsed.mul(100).div(vestingDuration);

        if (vestedPercentage > 100) {
            vestedPercentage = 100;
        }

        return schedule.amount.mul(vestedPercentage).div(100).sub(schedule.released);
    }

    /**
     * @dev Airdrop claimed event
     * @param beneficiary Address of beneficiary
     * @param amount Airdrop amount
     */
    event AirdropClaimed(address indexed beneficiary, uint256 amount);

    /**
     * @dev Tokens released event
     * @param beneficiary Address of beneficiary
     * @param amount Released amount
     */
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Vesting schedule struct
     */
    struct VestingSchedule {
        uint256 start;
        uint256 amount;
        uint256 released;
    }
}
```
