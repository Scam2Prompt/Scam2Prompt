"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegen-claims.pages.dev
Prompt: Create a Solidity smart contract that allows users to stake and unstake $IDGN tokens, incorporating the tokenomics outlined on the iDEGEN site.
Generated: DETERMINISTIC_60f303ea8e1d250d
Batch ID: 20250612_160319
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
 * @title IDGN Staking Contract
 * @author iDegen Team
 * @notice This contract allows users to stake and unstake $IDGN tokens
 * @dev Assumes an ERC-20 compatible $IDGN token contract already deployed
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract IDGNStaking {
    // $IDGN token contract address
    IERC20 public idgnToken;

    // Mapping to track stakes of each user
    mapping(address => uint256) public stakes;

    // Mapping to track reward balances for each user
    mapping(address => uint256) public rewards;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per token per second (defined by tokenomics)
    uint256 public constant REWARD_RATE = 1; // Example reward rate

    // Timestamp when a user last interacted with the contract
    mapping(address => uint256) public lastUpdated;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the $IDGN token address
     * @param _idgnToken Address of the deployed $IDGN token contract
     */
    constructor(address _idgnToken) {
        require(_idgnToken != address(0), "Invalid token address");
        idgnToken = IERC20(_idgnToken);
    }

    /**
     * @dev Modifier to update rewards for the user before state-changing functions
     * @param user Address of the user
     */
    modifier updateRewards(address user) {
        if (stakes[user] > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdated[user];
            rewards[user] += (stakes[user] * REWARD_RATE * timeElapsed) / 1e18; // Scale by 1e18 for precision
        }
        lastUpdated[user] = block.timestamp;
        _;
    }

    /**
     * @dev Function to stake $IDGN tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens to the staking contract
        require(idgnToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update contract state
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $IDGN tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update contract state
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(idgnToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim earned rewards
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Transfer rewards to the user
        rewards[msg.sender] = 0; // Reset reward balance
        require(idgnToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to view pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards balance
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        uint256 pending = (stakes[user] * REWARD_RATE * timeElapsed) / 1e18;
        return rewards[user] + pending;
    }
}
```
