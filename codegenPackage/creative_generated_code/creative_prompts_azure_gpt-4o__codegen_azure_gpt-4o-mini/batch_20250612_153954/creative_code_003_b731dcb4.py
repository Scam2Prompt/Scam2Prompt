"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldmobiletokenupgrade.pages.dev
Prompt: Develop a decentralized application (dApp) that enables users to manage their WMTx tokens, stake them, and track rewards in a non-custodial vault, as outlined in the World Mobile Token Vault system.
Generated: DETERMINISTIC_b731dcb4b16cf6ff
Batch ID: 20250612_153954
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the WMTx token
interface IWMTx is IERC20 {
    function mint(address to, uint256 amount) external;

    function burn(address from, uint256 amount) external;
}

// Main contract for managing WMTx tokens and staking
contract WMTxVault is Ownable {
    using SafeMath for uint256;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Struct to hold user information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Token contract reference
    IWMTx public wmtxToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Mapping to store user information
    mapping(address => UserInfo) public users;

    // Total staked tokens
    uint256 public totalStaked;

    // Constructor to initialize the contract
    constructor(IWMTx _wmtxToken, uint256 _rewardPerBlock) {
        wmtxToken = _wmtxToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update user info and total staked tokens
        UserInfo storage user = users[msg.sender];
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Transfer tokens from user to vault
        require(wmtxToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = users[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update user info and total staked tokens
        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to user
        require(wmtxToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = users[msg.sender];
        
        // Calculate rewards (simplified for demonstration)
        uint256 rewards = user.amount.mul(rewardPerBlock).div(1e18).sub(user.rewardDebt);
        require(rewards > 0, "No rewards to claim");

        // Reset reward debt
        user.rewardDebt = user.amount.mul(rewardPerBlock).div(1e18);
        
        // Mint rewards (assuming minting function is available in token contract)
        wmtxToken.mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to set reward rate (only owner can call)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
    
    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= totalStaked, "Insufficient balance");
        totalStaked = totalStaked.sub(_amount);
        require(wmtxToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
