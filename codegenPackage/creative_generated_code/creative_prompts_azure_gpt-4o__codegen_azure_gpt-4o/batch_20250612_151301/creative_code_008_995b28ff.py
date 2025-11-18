"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Create a Solidity contract that integrates `$LEGEND` token staking with additional features for sports-related rewards or fan engagement.
Generated: DETERMINISTIC_995b28ff7361c6c1
Batch ID: 20250612_151301
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

/**
 * @title LegendTokenStaking
 * @dev A staking contract for the $LEGEND token with sports-related rewards functionality.
 */
contract LegendTokenStaking {
    // Token interface for $LEGEND
    IERC20 public legendToken;

    // Owner of the contract for administrative control
    address public owner;

    // Struct to hold staking details
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Time when the stake was created
        uint256 points;       // Reward points earned
    }

    // Mapping of user address to their stake
    mapping(address => Stake) public stakes;

    // Event declarations for transparency
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 points);
    event RewardsClaimed(address indexed user, uint256 points);

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _legendToken Address of the $LEGEND token contract.
     */
    constructor(address _legendToken) {
        require(_legendToken != address(0), "Invalid token address");
        legendToken = IERC20(_legendToken);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $LEGEND tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(legendToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        require(legendToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Calculate reward points based on the staked amount
        uint256 pointsEarned = _amount / 1000; // Example: 1 point per 1000 tokens
        userStake.points += pointsEarned;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amountToUnstake = userStake.amount;
        uint256 pointsToClaim = userStake.points;

        // Reset user's stake
        userStake.amount = 0;
        userStake.points = 0;

        // Transfer staked tokens back to the user
        require(legendToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, pointsToClaim);
    }

    /**
     * @dev Allows users to claim their reward points for sports-related engagement.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.points > 0, "No reward points to claim");

        uint256 pointsToClaim = userStake.points;
        userStake.points = 0;

        // Implement sports reward logic here (e.g., NFTs, entries to sports events, etc.)

        emit RewardsClaimed(msg.sender, pointsToClaim);
    }

    /**
     * @dev Emergency function for the owner to withdraw all funds.
     * @param _to Address to send the funds to.
     */
    function emergencyWithdraw(address _to) external onlyOwner {
        require(_to != address(0), "Invalid address");
        uint256 contractBalance = legendToken.balanceOf(address(this));
        require(legendToken.transfer(_to, contractBalance), "Token transfer failed");
    }
}

// Interface for ERC20
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
