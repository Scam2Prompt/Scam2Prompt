"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Generate a Solidity contract to implement TG.Casino's NFT-based High Roller rewards system, including staking bonuses and rakeback percentages.
Generated: DETERMINISTIC_fba084acdc676fc0
Batch ID: 20250612_153517
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

// Importing OpenZeppelin's ERC721 and Ownable contracts for NFT functionality and ownership management
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ERC20 token to handle rewards and staking
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Main contract for TG.Casino's NFT-based High Roller rewards system
contract HighRollerRewards is ERC721, Ownable {
    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public nextTokenId; // Counter for NFT IDs
    IERC20 public rewardToken; // ERC20 token used for rewards

    // Struct for user information
    struct UserInfo {
        uint256 stakedAmount; // Amount staked by the user
        uint256 lastClaimed; // Last timestamp when rewards were claimed
        uint256 rakeback; // Rakeback percentage for the user
    }

    // Mapping from user address to their information
    mapping(address => UserInfo) public userInfo;

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token name, symbol, and reward token
    constructor(address _rewardToken) ERC721("TG.Casino High Roller", "TGHRC") {
        rewardToken = IERC20(_rewardToken);
    }

    // Function to mint an NFT for a user
    function mintNFT() external onlyOwner {
        require(nextTokenId < MAX_SUPPLY, "Max supply reached");
        _mint(msg.sender, nextTokenId);
        nextTokenId++;
    }

    // Function to stake tokens for rewards
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake a positive amount");
        
        // Transfer tokens from user to this contract
        rewardToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.stakedAmount += amount;
        user.lastClaimed = block.timestamp; // Reset last claimed time

        // Calculate and set rakeback based on staked amount (example logic)
        user.rakeback = (user.stakedAmount * 10) / 100; // 10% rakeback for example
    }

    // Function to claim rewards for the user
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        
        require(user.stakedAmount > 0, "No staked amount found");

        // Calculate rewards based on staked amount and time elapsed
        uint256 elapsedTime = block.timestamp - user.lastClaimed;
        uint256 rewardAmount = (user.stakedAmount * elapsedTime) / 1 days; // Example reward calculation
        
        // Transfer rewards to user
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient rewards in contract");
        rewardToken.transfer(msg.sender, rewardAmount);

        // Update last claimed timestamp
        user.lastClaimed = block.timestamp;

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw staked tokens (only if not staked)
    function withdraw(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];

        require(user.stakedAmount >= amount, "Withdraw amount exceeds staked amount");

        // Transfer tokens back to user
        user.stakedAmount -= amount;
        rewardToken.transfer(msg.sender, amount);
    }

    // Function for owner to withdraw tokens from the contract (emergency function)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance in the contract");
        rewardToken.transfer(msg.sender, amount);
    }
}
```
