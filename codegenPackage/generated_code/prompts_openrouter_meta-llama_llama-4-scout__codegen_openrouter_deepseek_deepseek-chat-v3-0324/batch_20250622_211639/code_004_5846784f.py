"""
Generated Code Metadata:
========================
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a smart contract using Solidity to create a decentralized meme coin index, including functions for buying, staking, and claiming rewards.
Generated: DETERMINISTIC_5846784f2346b2c5
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeCoinIndex
 * @dev A decentralized meme coin index with buy, stake, and claim reward functions
 */
contract MemeCoinIndex is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store staker information
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    // Token details
    IERC20 public memeToken;
    string public name;
    string public symbol;
    uint8 public decimals;

    // Staking variables
    uint256 public totalStaked;
    uint256 public rewardRate = 100; // Rewards per block (adjust as needed)
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Bought(address indexed buyer, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Constructor initializes the meme token
     * @param _tokenAddress Address of the meme token
     * @param _name Name of the index
     * @param _symbol Symbol of the index
     * @param _decimals Decimals of the token
     */
    constructor(
        address _tokenAddress,
        string memory _name,
        string memory _symbol,
        uint8 _decimals
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        memeToken = IERC20(_tokenAddress);
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Buy meme tokens (simplified for example)
     * @param amount Amount of tokens to buy
     */
    function buy(uint256 amount) external payable nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value >= amount, "Insufficient ETH sent");

        // In a real scenario, you would implement token minting or transfer logic
        // For this example, we assume the contract already has tokens
        require(memeToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Bought(msg.sender, amount);
    }

    /**
     * @dev Stake meme tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        updateRewards();

        Staker storage staker = stakers[msg.sender];
        if (staker.amount > 0) {
            uint256 pending = staker.amount.mul(accRewardPerShare).div(1e18).sub(staker.rewardDebt);
            if (pending > 0) {
                safeTransferRewards(msg.sender, pending);
            }
        }

        require(memeToken.transferFrom(msg.sender, address(this, amount), "Token transfer failed");
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.amount.mul(accRewardPerShare).div(1e18);
        staker.lastClaimTime = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake meme tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than 0");
        require(staker.amount >= amount, "Insufficient staked amount");

        updateRewards();
        uint256 pending = staker.amount.mul(accRewardPerShare).div(1e18).sub(staker.rewardDebt);
        if (pending > 0) {
            safeTransferRewards(msg.sender, pending);
        }

        staker.amount = staker.amount.sub(amount);
        staker.rewardDebt = staker.amount.mul(accRewardPerShare).div(1e18);
        totalStaked = totalStaked.sub(amount);

        require(memeToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        updateRewards();

        uint256 pending = staker.amount.mul(accRewardPerShare).div(1e18).sub(staker.rewardDebt);
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = staker.amount.mul(accRewardPerShare).div(1e18);
        staker.lastClaimTime = block.timestamp;

        safeTransferRewards(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Update reward calculations
     */
    function updateRewards() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number.sub(lastRewardBlock);
        uint256 rewards = blocksPassed.mul(rewardRate);
        accRewardPerShare = accRewardPerShare.add(rewards.mul(1e18).div(totalStaked));
        lastRewardBlock = block.number;
    }

    /**
     * @dev Safely transfer rewards to staker
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function safeTransferRewards(address to, uint256 amount) internal {
        uint256 balance = memeToken.balanceOf(address(this));
        if (amount > balance) {
            memeToken.transfer(to, balance);
        } else {
            memeToken.transfer(to, amount);
        }
    }

    /**
     * @dev View function to check pending rewards
     * @param _user Address of the staker
     * @return Pending rewards for the staker
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksPassed = block.number.sub(lastRewardBlock);
            uint256 rewards = blocksPassed.mul(rewardRate);
            tempAccRewardPerShare = tempAccRewardPerShare.add(rewards.mul(1e18).div(totalStaked));
        }
        return staker.amount.mul(tempAccRewardPerShare).div(1e18).sub(staker.rewardDebt);
    }
}
```
