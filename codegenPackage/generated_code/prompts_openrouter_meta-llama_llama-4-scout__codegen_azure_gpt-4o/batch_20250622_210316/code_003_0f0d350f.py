"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Design a smart contract for a token-based rewards system that unlocks rewards in equal monthly installments over 3 years, with a specific payout ratio for individual winners, conservation organizations, and referral rewards.
Generated: DETERMINISTIC_0f0d350f3eac621d
Batch ID: 20250622_210316
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

/**
 * @title TokenRewards
 * @dev A smart contract for a token-based rewards system with monthly installments over 3 years.
 */
contract TokenRewards {
    // Token contract interface
    IERC20 public token;

    // Constants
    uint256 public constant TOTAL_MONTHS = 36; // 3 years = 36 months
    uint256 public constant MONTHLY_INTERVAL = 30 days; // Approximate monthly interval

    // Reward distribution ratios (in percentage, scaled by 100)
    uint256 public constant WINNER_RATIO = 50; // 50%
    uint256 public constant CONSERVATION_RATIO = 30; // 30%
    uint256 public constant REFERRAL_RATIO = 20; // 20%

    // Struct to track reward details
    struct Reward {
        uint256 totalAmount;
        uint256 claimedAmount;
        uint256 startTime;
    }

    // Mappings to track rewards for different categories
    mapping(address => Reward) public winnerRewards;
    mapping(address => Reward) public conservationRewards;
    mapping(address => Reward) public referralRewards;

    // Events
    event RewardAdded(address indexed recipient, uint256 amount, string category);
    event RewardClaimed(address indexed recipient, uint256 amount, string category);

    /**
     * @dev Constructor to initialize the token contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /**
     * @dev Add rewards for a recipient in a specific category.
     * @param recipient Address of the recipient.
     * @param amount Total reward amount.
     * @param category Reward category ("winner", "conservation", "referral").
     */
    function addReward(
        address recipient,
        uint256 amount,
        string memory category
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        Reward storage reward;

        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("winner"))) {
            reward = winnerRewards[recipient];
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("conservation"))) {
            reward = conservationRewards[recipient];
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("referral"))) {
            reward = referralRewards[recipient];
        } else {
            revert("Invalid category");
        }

        reward.totalAmount += amount;
        reward.startTime = block.timestamp;

        emit RewardAdded(recipient, amount, category);
    }

    /**
     * @dev Claim rewards for a recipient in a specific category.
     * @param category Reward category ("winner", "conservation", "referral").
     */
    function claimReward(string memory category) external {
        Reward storage reward;

        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("winner"))) {
            reward = winnerRewards[msg.sender];
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("conservation"))) {
            reward = conservationRewards[msg.sender];
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("referral"))) {
            reward = referralRewards[msg.sender];
        } else {
            revert("Invalid category");
        }

        require(reward.totalAmount > 0, "No rewards available");
        require(block.timestamp >= reward.startTime, "Rewards not yet started");

        uint256 monthsElapsed = (block.timestamp - reward.startTime) / MONTHLY_INTERVAL;
        uint256 totalClaimable = (reward.totalAmount * monthsElapsed) / TOTAL_MONTHS;
        uint256 claimableAmount = totalClaimable - reward.claimedAmount;

        require(claimableAmount > 0, "No claimable rewards");

        reward.claimedAmount += claimableAmount;
        token.transfer(msg.sender, claimableAmount);

        emit RewardClaimed(msg.sender, claimableAmount, category);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
