"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: Design a smart contract using Solidity to facilitate the $MEMEX presale, including functions for buying, staking, and claiming rewards, while ensuring security and transparency.
Generated: DETERMINISTIC_cfabe02ebe9782f6
Batch ID: 20250622_211639
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MEMEX Presale Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates the $MEMEX presale, allowing users to buy, stake, and claim rewards.
 */
contract MEMEXPresale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // MEMEX token
    IERC20 public memexToken;

    // Presale token price
    uint256 public presalePrice;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Reward per second
    uint256 public rewardPerSecond;

    // Total staked amount
    uint256 public totalStaked;

    // Staking start time
    uint256 public stakingStartTime;

    // Event emitted when user buys MEMEX tokens
    event BuyMEMEX(address indexed buyer, uint256 amount);

    // Event emitted when user stakes MEMEX tokens
    event StakeMEMEX(address indexed staker, uint256 amount);

    // Event emitted when user claims rewards
    event ClaimRewards(address indexed staker, uint256 rewards);

    // Event emitted when owner updates presale price
    event UpdatePresalePrice(uint256 newPrice);

    // Event emitted when owner updates reward per second
    event UpdateRewardPerSecond(uint256 newReward);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastClaimed;
    }

    /**
     * @dev Constructor
     * @param _memexTokenAddress MEMEX token address
     * @param _presalePrice Presale token price
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _memexTokenAddress,
        uint256 _presalePrice,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        require(_memexTokenAddress != address(0), "MEMEX token address cannot be zero");
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_stakingDuration > 0, "Staking duration must be greater than zero");
        require(_rewardPerSecond > 0, "Reward per second must be greater than zero");

        memexToken = IERC20(_memexTokenAddress);
        presalePrice = _presalePrice;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
        stakingStartTime = block.timestamp;
    }

    /**
     * @dev Function to buy MEMEX tokens
     * @param _amount Amount of tokens to buy
     */
    function buyMEMEX(uint256 _amount) external payable nonReentrant {
        require(msg.value >= _amount.mul(presalePrice), "Insufficient payment");
        require(_amount > 0, "Buy amount must be greater than zero");

        balances[msg.sender] = balances[msg.sender].add(_amount);
        memexToken.transfer(msg.sender, _amount);

        emit BuyMEMEX(msg.sender, _amount);
    }

    /**
     * @dev Function to stake MEMEX tokens
     * @param _amount Amount of tokens to stake
     */
    function stakeMEMEX(uint256 _amount) external nonReentrant {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_amount > 0, "Stake amount must be greater than zero");
        require(block.timestamp >= stakingStartTime, "Staking not started yet");
        require(block.timestamp < stakingStartTime.add(stakingDuration), "Staking period ended");

        balances[msg.sender] = balances[msg.sender].sub(_amount);
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);
        stakers[msg.sender].lastClaimed = block.timestamp;

        emit StakeMEMEX(msg.sender, _amount);
    }

    /**
     * @dev Function to claim rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount");
        require(block.timestamp >= stakingStartTime, "Staking not started yet");
        require(block.timestamp < stakingStartTime.add(stakingDuration), "Staking period ended");

        uint256 rewards = calculateRewards(msg.sender);
        stakers[msg.sender].lastClaimed = block.timestamp;

        memexToken.transfer(msg.sender, rewards);

        emit ClaimRewards(msg.sender, rewards);
    }

    /**
     * @dev Function to calculate rewards for a staker
     * @param _staker Staker's address
     * @return Rewards for the staker
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(stakers[_staker].lastClaimed);
        return stakers[_staker].stakedAmount.mul(stakedDuration).mul(rewardPerSecond).div(1e18);
    }

    /**
     * @dev Function to update presale price
     * @param _newPrice New presale price
     */
    function updatePresalePrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Presale price must be greater than zero");

        presalePrice = _newPrice;

        emit UpdatePresalePrice(_newPrice);
    }

    /**
     * @dev Function to update reward per second
     * @param _newReward New reward per second
     */
    function updateRewardPerSecond(uint256 _newReward) external onlyOwner {
        require(_newReward > 0, "Reward per second must be greater than zero");

        rewardPerSecond = _newReward;

        emit UpdateRewardPerSecond(_newReward);
    }

    /**
     * @dev Function to withdraw tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");
        require(_amount > 0, "Withdraw amount must be greater than zero");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);

        memexToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Function to get staker's information
     * @param _staker Staker's address
     * @return Staker's information
     */
    function getStakerInfo(address _staker) external view returns (uint256 stakedAmount, uint256 lastClaimed) {
        return (stakers[_staker].stakedAmount, stakers[_staker].lastClaimed);
    }

    /**
     * @dev Function to get user's balance
     * @param _user User's address
     * @return User's balance
     */
    function getBalance(address _user) external view returns (uint256) {
        return balances[_user];
    }
}
```
