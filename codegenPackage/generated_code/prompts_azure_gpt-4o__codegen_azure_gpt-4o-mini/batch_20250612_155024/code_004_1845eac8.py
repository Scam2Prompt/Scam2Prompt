"""
Generated Code Metadata:
========================
Original URL: https://dinamikaplus.ru
Prompt: Write a smart contract in Solidity to enable staking of BELT tokens and distribute rewards based on the mechanisms described in Belt Finance.
Generated: DETERMINISTIC_1845eac8f9ec3e5e
Batch ID: 20250612_155024
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

// Interface for the BELT token
interface IBeltToken is IERC20 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Staking contract for BELT tokens
contract BeltStaking is Ownable {
    // State variables
    IBeltToken public beltToken; // BELT token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    // User staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // User's reward debt
    }

    mapping(address => UserInfo) public userInfo; // Mapping of user addresses to their staking info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the BELT token and reward rate
    constructor(IBeltToken _beltToken, uint256 _rewardRate) {
        beltToken = _beltToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards before any staking or unstaking action
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 blocksPassed = block.number - lastUpdateBlock;
            uint256 reward = blocksPassed * rewardRate;
            beltToken.mint(address(this), reward); // Mint rewards to the contract
        }
        lastUpdateBlock = block.number;
        _;
    }

    // Function to stake BELT tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer BELT tokens from user to contract
        beltToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        user.rewardDebt = user.amount * rewardRate; // Update reward debt

        totalStaked += amount; // Update total staked amount

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BELT tokens
    function unstake(uint256 amount) external updateRewards {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update user info
        user.amount -= amount;
        user.rewardDebt = user.amount * rewardRate; // Update reward debt

        totalStaked -= amount; // Update total staked amount

        // Transfer BELT tokens back to user
        beltToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = (user.amount * rewardRate) - user.rewardDebt; // Calculate reward

        require(reward > 0, "No rewards to claim");

        // Update user's reward debt
        user.rewardDebt = user.amount * rewardRate;

        // Transfer rewards to user
        beltToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        beltToken.transfer(msg.sender, amount);
    }
}
```
