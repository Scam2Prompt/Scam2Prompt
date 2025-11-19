"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasdflsd.pages.dev
Prompt: Generate a Solidity contract that allows users to participate in the $BLAST Airdrop and manage rewards.
Generated: DETERMINISTIC_689270982e49cdc3
Batch ID: 20250612_160940
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
 * @title BLAST Airdrop Contract
 * @dev This contract allows users to participate in the $BLAST token airdrop and manage rewards.
 * It ensures security and proper distribution of tokens.
 */
contract BlastAirdrop {
    // The owner of the contract
    address public owner;

    // The $BLAST token address
    address public blastToken;

    // Mapping to track users' rewards
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when user registers for the airdrop
    event UserRegistered(address indexed user);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _blastToken Address of the $BLAST token contract.
     */
    constructor(address _blastToken) {
        require(_blastToken != address(0), "Invalid token address");
        owner = msg.sender;
        blastToken = _blastToken;
    }

    /**
     * @dev Register a user for airdrop rewards.
     * Adds user to rewards mapping with initial reward amount.
     */
    function registerUser(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(rewards[user] == 0, "User already registered");

        rewards[user] = rewardAmount;

        emit UserRegistered(user);
    }

    /**
     * @dev Claim rewards for the caller.
     * Transfers the user's rewards from the contract to the caller.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset user's rewards to prevent double claiming
        rewards[msg.sender] = 0;

        // Transfer $BLAST tokens to the user
        require(
            IERC20(blastToken).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Emergency function to withdraw leftover tokens.
     * Can only be called by the owner.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens back to the owner
        require(
            IERC20(blastToken).transfer(owner, amount),
            "Token transfer failed"
        );
    }
}

/**
 * @dev Interface for ERC20 token standard.
 * Used for interacting with the $BLAST token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account)
        external
        view
        returns (uint256);
}
```
