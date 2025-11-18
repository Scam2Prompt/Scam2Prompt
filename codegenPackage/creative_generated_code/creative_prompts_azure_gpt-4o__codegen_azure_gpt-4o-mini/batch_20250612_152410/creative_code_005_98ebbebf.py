"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetfcoinn.pages.dev
Prompt: Write Solidity code to implement a dynamic staking rewards system for BTCETF tokens, where rewards rates depend on the total amount staked by the community.
Generated: DETERMINISTIC_98ebbebf4bbda27d
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 interface for token operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract implements a dynamic staking rewards system for BTCETF tokens
contract StakingRewards is Ownable {
    // Events for staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // State variables
    IERC20 public btcEftToken; // The BTCETF token contract
    uint256 public totalStaked; // Total amount staked by all users
    uint256 public rewardRate; // Reward rate based on total staked amount

    // User struct to hold staking data
    struct UserInfo {
        uint256 amountStaked; // Amount staked by the user
        uint256 rewards; // Accumulated rewards for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) private userInfo;

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _btcEftToken) {
        btcEftToken = _btcEftToken;
        rewardRate = 1; // Initial reward rate (can be dynamic based on logic)
    }

    // Function to update the reward rate based on the total staked amount
    function updateRewardRate() internal {
        if (totalStaked < 1000 * 10 ** 18) {
            rewardRate = 1; // 1% for less than 1000 tokens staked
        } else if (totalStaked < 5000 * 10 ** 18) {
            rewardRate = 2; // 2% for between 1000 and 5000 tokens staked
        } else {
            rewardRate = 3; // 3% for 5000 or more tokens staked
        }
    }

    // Function for users to stake their BTCETF tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(btcEftToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user information
        UserInfo storage user = userInfo[msg.sender];
        user.amountStaked += _amount;
        totalStaked += _amount;

        // Update the reward rate
        updateRewardRate();

        emit Staked(msg.sender, _amount);
    }

    // Function for users to unstake their BTCETF tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(_amount > 0, "Amount must be greater than 0");
        require(user.amountStaked >= _amount, "Insufficient staked amount");

        // Update user information
        user.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer the staked tokens back to the user
        require(btcEftToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards based on the user's staked amount
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user's rewards balance
        user.rewards = 0;

        // Transfer rewards to the user (implement reward token transfer)
        require(btcEftToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate the user's rewards
    function calculateRewards(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amountStaked * rewardRate) / 100; // Simple reward calculation
    }

    // Function to withdraw the contract's balance (onlyOwner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(btcEftToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        require(btcEftToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
