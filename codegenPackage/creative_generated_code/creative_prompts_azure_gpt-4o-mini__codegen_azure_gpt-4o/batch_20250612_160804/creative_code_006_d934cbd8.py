"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: How can I integrate DOGE20's staking rewards into a decentralized application (dApp) using its ERC-20 token features?
Generated: DETERMINISTIC_d934cbd867b47a76
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT

// Import OpenZeppelin libraries
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Doge20Staking is Ownable, ReentrancyGuard {
    // DOGE20 token contract address
    IERC20 public doge20Token;

    // Struct to store staking information for each address
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the stake was created
    }

    // Mapping to store stakes by user address
    mapping(address => Stake) public stakes;

    // Annual reward rate (e.g., 10% annual rewards)
    uint256 public annualRewardRate = 10;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardsWithdrawn(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to initialize the Doge20 token contract.
     */
    constructor(address _doge20TokenAddress) {
        require(_doge20TokenAddress != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20TokenAddress);
    }

    /**
     * @dev Stake DOGE20 tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");
        require(
            doge20Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Calculate rewards for previous stake (if any)
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            stakes[msg.sender].amount += rewards; // Reinvest rewards into stake
        }

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and withdraw rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount + rewards;

        // Transfer staked tokens and rewards back to user
        require(
            doge20Token.transfer(msg.sender, totalAmount),
            "Token transfer failed"
        );

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        emit Unstaked(msg.sender, totalAmount, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user.
     * @param _user The address of the user.
     * @return The calculated rewards.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0; // No rewards for zero staked tokens
        }

        // Calculate the time difference since the stake was created
        uint256 timeElapsed = block.timestamp - userStake.timestamp;

        // Rewards = (staked amount) * (annual rate) * (time elapsed) / (1 year in seconds)
        uint256 rewards = (userStake.amount * annualRewardRate * timeElapsed) /
            (100 * 365 days);
        return rewards;
    }

    /**
     * @dev Set the annual reward rate (only owner).
     * @param _annualRewardRate The new annual reward rate (percentage).
     */
    function setAnnualRewardRate(uint256 _annualRewardRate) external onlyOwner {
        require(_annualRewardRate > 0, "Invalid reward rate");
        annualRewardRate = _annualRewardRate;
    }

    /**
     * @dev Emergency token withdrawal by the owner.
     * @param _tokenAddress The address of the token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _tokenAddress, uint256 _amount)
        external
        onlyOwner
    {
        IERC20 token = IERC20(_tokenAddress);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }
}
```
