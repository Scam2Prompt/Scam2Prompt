"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Create a smart contract in Solidity to manage the Dogeverse tokenomics, including token allocation, presale, and staking mechanisms.
Generated: DETERMINISTIC_bb8eb372b8a1cc0c
Batch ID: 20250622_204646
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DogeverseToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 30;
    uint256 public constant TEAM_ALLOCATION = 15;
    uint256 public constant MARKETING_ALLOCATION = 10;
    uint256 public constant DEVELOPMENT_ALLOCATION = 10;
    uint256 public constant STAKING_REWARDS_ALLOCATION = 35;

    // Token distribution addresses
    address public presaleAddress;
    address public teamAddress;
    address public marketingAddress;
    address public developmentAddress;
    address public stakingRewardsAddress;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per ETH
    uint256 public presaleMinContribution;
    uint256 public presaleMaxContribution;
    uint256 public presaleHardCap;
    uint256 public presaleTotalContribution;

    // Staking parameters
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardRate;
    }

    mapping(address => Stake[]) public stakes;
    uint256 public stakingRewardRate; // Annual percentage rate (APR)
    uint256 public stakingLockPeriod; // In seconds

    // Events
    event PresaleContribution(address indexed contributor, uint256 amount, uint256 tokens);
    event TokensClaimed(address indexed recipient, uint256 amount);
    event Staked(address indexed staker, uint256 amount, uint256 rewardRate);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    constructor(
        uint256 _totalSupply,
        address _presaleAddress,
        address _teamAddress,
        address _marketingAddress,
        address _developmentAddress,
        address _stakingRewardsAddress
    ) ERC20("Dogeverse", "DOGEV") {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_teamAddress != address(0), "Invalid team address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_developmentAddress != address(0), "Invalid development address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");

        // Calculate token allocations
        uint256 presaleTokens = _totalSupply.mul(PRESALE_ALLOCATION).div(100);
        uint256 teamTokens = _totalSupply.mul(TEAM_ALLOCATION).div(100);
        uint256 marketingTokens = _totalSupply.mul(MARKETING_ALLOCATION).div(100);
        uint256 developmentTokens = _totalSupply.mul(DEVELOPMENT_ALLOCATION).div(100);
        uint256 stakingRewardsTokens = _totalSupply.mul(STAKING_REWARDS_ALLOCATION).div(100);

        // Mint tokens to respective addresses
        _mint(_presaleAddress, presaleTokens);
        _mint(_teamAddress, teamTokens);
        _mint(_marketingAddress, marketingTokens);
        _mint(_developmentAddress, developmentTokens);
        _mint(_stakingRewardsAddress, stakingRewardsTokens);

        // Set distribution addresses
        presaleAddress = _presaleAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
        stakingRewardsAddress = _stakingRewardsAddress;

        // Initialize staking parameters
        stakingRewardRate = 20; // 20% APR
        stakingLockPeriod = 30 days;
    }

    // Presale functions
    function setupPresale(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _rate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) external onlyOwner {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_rate > 0, "Rate must be greater than 0");
        require(_minContribution > 0, "Min contribution must be greater than 0");
        require(_maxContribution > _minContribution, "Max contribution must be greater than min");
        require(_hardCap > 0, "Hard cap must be greater than 0");

        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        presaleRate = _rate;
        presaleMinContribution = _minContribution;
        presaleMaxContribution = _maxContribution;
        presaleHardCap = _hardCap;
    }

    function contributeToPresale() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value >= presaleMinContribution, "Contribution is below minimum");
        require(msg.value <= presaleMaxContribution, "Contribution exceeds maximum");
        require(presaleTotalContribution.add(msg.value) <= presaleHardCap, "Hard cap reached");

        uint256 tokens = msg.value.mul(presaleRate);
        require(balanceOf(presaleAddress) >= tokens, "Not enough tokens in presale allocation");

        presaleTotalContribution = presaleTotalContribution.add(msg.value);
        _transfer(presaleAddress, msg.sender, tokens);

        emit PresaleContribution(msg.sender, msg.value, tokens);
    }

    function withdrawPresaleFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        payable(owner()).transfer(address(this).balance);
    }

    // Staking functions
    function stakeTokens(uint256 _amount, uint256 _duration) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        uint256 rewardRate = stakingRewardRate.mul(_duration).div(365 days);
        _transfer(msg.sender, stakingRewardsAddress, _amount);

        stakes[msg.sender].push(Stake({
            amount: _amount,
            startTime: block.timestamp,
            rewardRate: rewardRate
        }));

        emit Staked(msg.sender, _amount, rewardRate);
    }

    function unstakeTokens(uint256 _stakeIndex) external nonReentrant {
        require(_stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage stake = stakes[msg.sender][_stakeIndex];
        require(block.timestamp >= stake.startTime.add(stakingLockPeriod), "Tokens are still locked");

        uint256 reward = stake.amount.mul(stake.rewardRate).div(100);
        uint256 totalAmount = stake.amount.add(reward);

        require(balanceOf(stakingRewardsAddress) >= totalAmount, "Insufficient rewards pool");

        _transfer(stakingRewardsAddress, msg.sender, totalAmount);

        // Remove the stake
        stakes[msg.sender][_stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        emit Unstaked(msg.sender, stake.amount, reward);
    }

    function emergencyWithdraw(uint256 _stakeIndex) external nonReentrant {
        require(_stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage stake = stakes[msg.sender][_stakeIndex];

        _transfer(stakingRewardsAddress, msg.sender, stake.amount);

        // Remove the stake
        stakes[msg.sender][_stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        emit EmergencyWithdraw(msg.sender, stake.amount);
    }

    function getStakes(address _user) external view returns (Stake[] memory) {
        return stakes[_user];
    }

    function calculateReward(uint256 _stakeIndex, address _user) public view returns (uint256) {
        require(_stakeIndex < stakes[_user].length, "Invalid stake index");
        Stake storage stake = stakes[_user][_stakeIndex];
        return stake.amount.mul(stake.rewardRate).div(
