"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Write a smart contract for vault staking that offers 5% APR rewards, as described in the Dypius Vault feature.
Generated: DETERMINISTIC_546cb77fad8f3665
Batch ID: 20250612_153527
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
 * @title VaultStaking
 * @dev A smart contract that allows users to stake tokens in a vault and earn 5% APR rewards.
 */
contract VaultStaking {
    // Token interface
    IERC20 public immutable stakingToken;

    // Constants
    uint256 public constant APR = 5; // Annual Percentage Rate (5%)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // State variables
    mapping(address => uint256) public stakedBalances; // Tracks staked amounts per user
    mapping(address => uint256) public lastStakedTimestamp; // Tracks last staking timestamp per user

    uint256 public totalStaked; // Total amount of staked tokens
    address public owner; // Contract owner (can be used for upgrades or management)

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "VaultStaking: Not contract owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the staking token address.
     * @param _stakingToken Address of the ERC20 token to be staked.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake tokens into the vault.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "VaultStaking: Cannot stake zero");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "VaultStaking: Token transfer failed");

        // Calculate rewards for any previously staked tokens
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update user's staked balance and timestamp
        stakedBalances[msg.sender] += amount + pendingRewards;
        lastStakedTimestamp[msg.sender] = block.timestamp;

        // Update total staked balance
        totalStaked += amount + pendingRewards;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "VaultStaking: No tokens to unstake");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Reset user's staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        lastStakedTimestamp[msg.sender] = 0;

        // Update total staked balance
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        require(stakingToken.transfer(msg.sender, stakedAmount + rewards), "VaultStaking: Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Calculates the rewards for a user based on their staked amount and duration.
     * @param user Address of the user whose rewards are being calculated.
     * @return reward Amount of rewards earned.
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        uint256 stakingDuration = block.timestamp - lastStakedTimestamp[user];
        return (stakedAmount * APR * stakingDuration) / (100 * SECONDS_IN_YEAR);
    }

    /**
     * @dev Emergency function to allow users to withdraw staked tokens without rewards.
     */
    function emergencyWithdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "VaultStaking: No tokens to withdraw");

        // Reset user's staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        lastStakedTimestamp[msg.sender] = 0;

        // Update total staked balance
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "VaultStaking: Token transfer failed");

        emit EmergencyWithdraw(msg.sender, stakedAmount);
    }

    /**
     * @dev Owner-only function to withdraw excess tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "VaultStaking: Cannot withdraw zero tokens");
        require(stakingToken.balanceOf(address(this)) >= amount, "VaultStaking: Insufficient contract balance");

        require(stakingToken.transfer(owner, amount), "VaultStaking: Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
