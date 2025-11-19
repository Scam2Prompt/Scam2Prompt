"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Generate Solidity code for creating a farming pool contract that aligns with Mike Token's roadmap goals for staking and compounding rewards.
Generated: DETERMINISTIC_ac1d4c0ccd1cee9c
Batch ID: 20250612_154216
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FarmingPool contract for staking and compounding rewards
contract FarmingPool is Ownable {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // The token being staked
    IERC20 public stakingToken;

    // Reward token for the users
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number that rewards were distributed
    uint256 public lastRewardBlock;

    // Total rewards accumulated
    uint256 public accRewardPerShare;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to update rewards based on the current block
    function updateRewards() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = block.number - lastRewardBlock;
        uint256 reward = multiplier * rewardPerBlock;
        accRewardPerShare += (reward * 1e12) / totalStaked; // Update accumulated rewards per share
        lastRewardBlock = block.number;
    }

    // Function for users to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        updateRewards();

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            // Calculate pending rewards
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                rewardToken.transfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount; // Update user's staked amount
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12; // Update user's reward debt
        totalStaked += _amount; // Update total staked amount

        emit Staked(msg.sender, _amount);
    }

    // Function for users to withdraw their staked tokens
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        updateRewards();

        // Calculate pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        // Update user's staked amount and total staked amount
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards without withdrawing staked tokens
    function claimRewards() external {
        updateRewards();
        UserInfo storage user = userInfo[msg.sender];

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12; // Update user's reward debt
        rewardToken.transfer(msg.sender, pending); // Transfer rewards to user

        emit RewardClaimed(msg.sender, pending);
    }

    // Function to set new reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updateRewards();
        rewardPerBlock = _rewardPerBlock;
    }
}
```
