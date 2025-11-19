"""
Generated Code Metadata:
========================
Original URL: https://gen-da6.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token similar to "$ENTS," including functionality for tokenomics and rewards distribution.
Generated: DETERMINISTIC_4be2cce457ff2382
Batch ID: 20250612_151024
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

contract SENTS is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * 10**18; // 10% for team
    uint256 public constant REWARD_POOL = 200_000_000 * 10**18; // 20% for rewards
    uint256 public constant PRESALE_ALLOCATION = 300_000_000 * 10**18; // 30% for presale
    uint256 public constant LIQUIDITY_POOL = 400_000_000 * 10**18; // 40% for liquidity

    // Reward distribution
    uint256 public rewardRate = 100; // 1% reward rate
    uint256 public lastRewardDistribution;
    uint256 public rewardDistributionInterval = 1 days;

    // Addresses
    address public teamWallet;
    address public rewardPool;
    address public presaleContract;
    address public liquidityPool;

    // Mappings
    mapping(address => bool) public excludedFromRewards;
    mapping(address => uint256) public lastClaimTime;

    // Events
    event RewardsDistributed(address indexed user, uint256 amount);
    event ExcludedFromRewards(address indexed account);
    event IncludedInRewards(address indexed account);

    constructor(
        address _teamWallet,
        address _rewardPool,
        address _presaleContract,
        address _liquidityPool
    ) ERC20("SENTS", "SENTS") {
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_rewardPool != address(0), "Invalid reward pool");
        require(_presaleContract != address(0), "Invalid presale contract");
        require(_liquidityPool != address(0), "Invalid liquidity pool");

        teamWallet = _teamWallet;
        rewardPool = _rewardPool;
        presaleContract = _presaleContract;
        liquidityPool = _liquidityPool;

        // Mint initial allocations
        _mint(teamWallet, TEAM_ALLOCATION);
        _mint(rewardPool, REWARD_POOL);
        _mint(presaleContract, PRESALE_ALLOCATION);
        _mint(liquidityPool, LIQUIDITY_POOL);

        // Exclude system addresses from rewards
        excludedFromRewards[teamWallet] = true;
        excludedFromRewards[rewardPool] = true;
        excludedFromRewards[presaleContract] = true;
        excludedFromRewards[liquidityPool] = true;

        lastRewardDistribution = block.timestamp;
    }

    // Modifier to check reward eligibility
    modifier onlyEligible(address account) {
        require(!excludedFromRewards[account], "Account is excluded from rewards");
        _;
    }

    // Function to distribute rewards
    function distributeRewards() public {
        require(block.timestamp >= lastRewardDistribution + rewardDistributionInterval, "Too soon to distribute rewards");
        
        uint256 rewardAmount = totalSupply().mul(rewardRate).div(10000);
        require(balanceOf(rewardPool) >= rewardAmount, "Insufficient reward pool balance");

        _transfer(rewardPool, address(this), rewardAmount);
        lastRewardDistribution = block.timestamp;
    }

    // Function to claim rewards
    function claimRewards() public onlyEligible(msg.sender) {
        require(block.timestamp >= lastClaimTime[msg.sender] + rewardDistributionInterval, "Too soon to claim rewards");

        uint256 userBalance = balanceOf(msg.sender);
        require(userBalance > 0, "No tokens to claim rewards");

        uint256 rewardAmount = totalSupply().mul(rewardRate).div(10000).mul(userBalance).div(totalSupply());
        require(rewardAmount > 0, "No rewards available");

        _transfer(address(this), msg.sender, rewardAmount);
        lastClaimTime[msg.sender] = block.timestamp;

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Owner functions
    function setRewardRate(uint256 _rate) external onlyOwner {
        require(_rate <= 500, "Reward rate too high"); // Max 5%
        rewardRate = _rate;
    }

    function setRewardDistributionInterval(uint256 _interval) external onlyOwner {
        rewardDistributionInterval = _interval;
    }

    function excludeFromRewards(address _account) external onlyOwner {
        excludedFromRewards[_account] = true;
        emit ExcludedFromRewards(_account);
    }

    function includeInRewards(address _account) external onlyOwner {
        excludedFromRewards[_account] = false;
        emit IncludedInRewards(_account);
    }

    // Override transfer to handle rewards
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        super._transfer(sender, recipient, amount);

        // Auto-claim rewards for eligible accounts
        if (!excludedFromRewards[sender] && lastClaimTime[sender] + rewardDistributionInterval <= block.timestamp) {
            claimRewards();
        }
    }
}
```
