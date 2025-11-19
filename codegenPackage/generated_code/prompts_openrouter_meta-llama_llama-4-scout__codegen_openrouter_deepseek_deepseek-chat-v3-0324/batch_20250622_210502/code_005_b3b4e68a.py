"""
Generated Code Metadata:
========================
Original URL: https://cybro-en.pages.dev
Prompt: "Design a tokenomics model for a new cryptocurrency on Blast L2, inspired by CYBRO's token allocation and vesting schedule."
Generated: DETERMINISTIC_b3b4e68a5e0d9b30
Batch ID: 20250622_210502
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

contract TokenomicsToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocation percentages
    uint256 public constant TEAM_ALLOCATION = 15;
    uint256 public constant ADVISORS_ALLOCATION = 5;
    uint256 public constant ECOSYSTEM_FUND = 20;
    uint256 public constant LIQUIDITY_POOL = 10;
    uint256 public constant COMMUNITY_REWARDS = 25;
    uint256 public constant PUBLIC_SALE = 25;

    // Vesting periods in seconds
    uint256 public constant TEAM_VESTING_PERIOD = 2 * 365 * 24 * 60 * 60; // 2 years
    uint256 public constant ADVISORS_VESTING_PERIOD = 1 * 365 * 24 * 60 * 60; // 1 year
    uint256 public constant ECOSYSTEM_VESTING_PERIOD = 3 * 365 * 24 * 60 * 60; // 3 years

    // Vesting start time
    uint256 public vestingStartTime;

    // Allocation addresses
    address public teamAddress;
    address public advisorsAddress;
    address public ecosystemFundAddress;
    address public liquidityPoolAddress;
    address public communityRewardsAddress;
    address public publicSaleAddress;

    // Track claimed tokens
    mapping(address => uint256) public claimedTokens;

    event TokensClaimed(address indexed beneficiary, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        address _teamAddress,
        address _advisorsAddress,
        address _ecosystemFundAddress,
        address _liquidityPoolAddress,
        address _communityRewardsAddress,
        address _publicSaleAddress
    ) ERC20(name, symbol) {
        require(totalSupply > 0, "Total supply must be positive");
        require(_teamAddress != address(0), "Invalid team address");
        require(_advisorsAddress != address(0), "Invalid advisors address");
        require(_ecosystemFundAddress != address(0), "Invalid ecosystem fund address");
        require(_liquidityPoolAddress != address(0), "Invalid liquidity pool address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_publicSaleAddress != address(0), "Invalid public sale address");

        teamAddress = _teamAddress;
        advisorsAddress = _advisorsAddress;
        ecosystemFundAddress = _ecosystemFundAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        communityRewardsAddress = _communityRewardsAddress;
        publicSaleAddress = _publicSaleAddress;

        vestingStartTime = block.timestamp;

        // Mint initial allocations (non-vested portions)
        _mint(liquidityPoolAddress, totalSupply.mul(LIQUIDITY_POOL).div(100));
        _mint(communityRewardsAddress, totalSupply.mul(COMMUNITY_REWARDS).div(100));
        _mint(publicSaleAddress, totalSupply.mul(PUBLIC_SALE).div(100));
    }

    function claimTeamTokens() external {
        require(msg.sender == teamAddress, "Only team can claim");
        _claimVestedTokens(teamAddress, TEAM_ALLOCATION, TEAM_VESTING_PERIOD);
    }

    function claimAdvisorsTokens() external {
        require(msg.sender == advisorsAddress, "Only advisors can claim");
        _claimVestedTokens(advisorsAddress, ADVISORS_ALLOCATION, ADVISORS_VESTING_PERIOD);
    }

    function claimEcosystemTokens() external {
        require(msg.sender == ecosystemFundAddress, "Only ecosystem fund can claim");
        _claimVestedTokens(ecosystemFundAddress, ECOSYSTEM_FUND, ECOSYSTEM_VESTING_PERIOD);
    }

    function _claimVestedTokens(address beneficiary, uint256 allocationPercentage, uint256 vestingPeriod) internal {
        require(vestingStartTime > 0, "Vesting not started");
        require(block.timestamp > vestingStartTime, "Vesting period not started");

        uint256 totalAllocation = totalSupply().mul(allocationPercentage).div(100);
        uint256 elapsedTime = block.timestamp.sub(vestingStartTime);
        uint256 vestedAmount;

        if (elapsedTime >= vestingPeriod) {
            vestedAmount = totalAllocation;
        } else {
            vestedAmount = totalAllocation.mul(elapsedTime).div(vestingPeriod);
        }

        uint256 claimableAmount = vestedAmount.sub(claimedTokens[beneficiary]);
        require(claimableAmount > 0, "No tokens available to claim");

        claimedTokens[beneficiary] = claimedTokens[beneficiary].add(claimableAmount);
        _mint(beneficiary, claimableAmount);

        emit TokensClaimed(beneficiary, claimableAmount);
    }

    function updateVestingStartTime(uint256 newStartTime) external onlyOwner {
        require(newStartTime > block.timestamp, "New start time must be in the future");
        require(vestingStartTime > block.timestamp || vestingStartTime == 0, "Vesting already started");
        vestingStartTime = newStartTime;
    }
}
```
