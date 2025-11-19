"""
Generated Code Metadata:
========================
Original URL: https://everlodge-io.web.app
Prompt: Generate code for an ERC-20 token contract in Solidity, incorporating features like staking rewards, membership benefits, and trading fee discounts, similar to Everlodge's $ELDG token.
Generated: DETERMINISTIC_45835d6c394b383c
Batch ID: 20250612_151906
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ELDGToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user stakes
    mapping(address => Stake) public stakes;

    // Total rewards distributed
    uint256 public totalRewards;

    // Trading fee percentage (in basis points)
    uint256 public tradingFeePercentage = 200; // 2%

    // Membership benefits threshold
    uint256 public membershipThreshold = 1000 * 10**decimals(); // 1000 tokens

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("Everlodge Token", "ELDG") {
        _mint(msg.sender, 1000000 * 10**decimals()); // Mint initial supply
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);

        // Update the stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            totalRewards = totalRewards.add(rewards);
            _mint(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Update the stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Simple reward calculation based on time and amount staked
        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 rewardRate = 10; // 10 tokens per second per staked token
        return userStake.amount.mul(rewardRate).mul(stakingDuration);
    }

    // Function to set trading fee percentage
    function setTradingFeePercentage(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        tradingFeePercentage = newFee;
    }

    // Function to get membership benefits
    function hasMembershipBenefits(address user) external view returns (bool) {
        return stakes[user].amount >= membershipThreshold;
    }

    // Override transfer function to include trading fee
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 fee = amount.mul(tradingFeePercentage).div(10000);
        uint256 amountAfterFee = amount.sub(fee);

        // Transfer fee to the contract
        super._transfer(sender, address(this), fee);
        // Transfer remaining amount to recipient
        super._transfer(sender, recipient, amountAfterFee);
    }
}
```
