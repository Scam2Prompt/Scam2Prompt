"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beyond-blitz.pages.dev
Prompt: Develop a smart contract that facilitates the earning and claiming of cryptocurrency rewards based on user activity, inspired by Beyond Blitz's $BEYOND reward system.
Generated: DETERMINISTIC_0cbb89ed6d53302e
Batch ID: 20250612_153225
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
 * @title RewardsContract
 * @dev A smart contract for earning and claiming cryptocurrency rewards based on user activity.
 */
contract RewardsContract {
    // Address of the contract owner
    address public owner;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Mapping to store user activity points
    mapping(address => uint256) public userPoints;

    // Mapping to store user claimable rewards
    mapping(address => uint256) public claimableRewards;

    // Event emitted when rewards are earned
    event RewardsEarned(address indexed user, uint256 points, uint256 rewards);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    /**
     * @dev Constructor to set the owner and reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        owner = msg.sender;
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to earn rewards based on user activity points.
     * Only the contract owner can call this function.
     * @param user Address of the user earning rewards.
     * @param points Activity points earned by the user.
     */
    function earnRewards(address user, uint256 points) external onlyOwner {
        // Convert activity points to rewards (e.g., 1 point = 1 reward token)
        uint256 rewards = points;

        // Update user points and claimable rewards
        userPoints[user] += points;
        claimableRewards[user] += rewards;

        emit RewardsEarned(user, points, rewards);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() external {
        uint256 amount = claimableRewards[msg.sender];

        // Ensure user has rewards to claim
        require(amount > 0, "No rewards available to claim");

        // Ensure the contract has enough tokens to transfer
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Reset claimable rewards
        claimableRewards[msg.sender] = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, amount);

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to deposit reward tokens into the contract.
     * Only the contract owner can call this function.
     * @param amount Amount of tokens to deposit.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid deposit amount");
        rewardToken.transferFrom(msg.sender, address(this), amount);
    }

    /**
     * @dev Function to check the contract's reward token balance.
     * @return The balance of reward tokens held by the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}

/**
 * @dev Interface for ERC20 token standard.
 * Used to interact with the reward token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function allowance(address owner, address spender) external view returns (uint256);
}
```
