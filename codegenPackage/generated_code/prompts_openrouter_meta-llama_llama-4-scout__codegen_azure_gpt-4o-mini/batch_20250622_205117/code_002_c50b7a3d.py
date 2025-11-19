"""
Generated Code Metadata:
========================
Original URL: https://gmnt.org
Prompt: "Design a smart contract for a new DeFi protocol on the Binance Smart Chain, incorporating features similar to GMNT's staking and yield farming."
Generated: DETERMINISTIC_c50b7a3dc102867b
Batch ID: 20250622_205117
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token to be staked
interface IStakableToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract for the DeFi protocol
contract DeFiProtocol is Ownable {
    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;

    // The token being staked
    IStakableToken public stakableToken;

    // Reward per block for staking
    uint256 public rewardPerBlock;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IStakableToken _stakableToken, uint256 _rewardPerBlock) {
        stakableToken = _stakableToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        user.rewardDebt += (_amount * rewardPerBlock);

        // Update total staked amount
        totalStaked += _amount;

        // Transfer tokens from user to contract
        stakableToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update user info
        user.amount -= _amount;
        user.rewardDebt -= (_amount * rewardPerBlock);

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer tokens back to user
        stakableToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pendingRewards = (user.amount * rewardPerBlock) - user.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Update total rewards distributed
        totalRewards += pendingRewards;

        // Transfer rewards to user
        stakableToken.mint(msg.sender, pendingRewards);

        // Update user's reward debt
        user.rewardDebt += pendingRewards;

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to set the reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= totalStaked, "Insufficient balance");
        stakableToken.transfer(msg.sender, _amount);
    }
}
```
