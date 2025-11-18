"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-io.web.app
Prompt: Generate Solidity code for a staking contract compatible with the $GIGA token, ensuring LP tokens are locked and rewards are distributed based on staked amounts.
Generated: DETERMINISTIC_9ba7ef4362d5f6aa
Batch ID: 20250612_152422
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
 * @title GIGA Staking Contract
 * @author Expert Programmer
 * @notice This contract allows users to stake LP tokens and earn $GIGA token rewards proportional to their staked amount.
 */
contract GIGAStaking {
    // The address of the $GIGA token contract
    IERC20 public gigaToken;

    // The address of the LP token contract
    IERC20 public lpToken;

    // Total amount of LP tokens staked in the contract
    uint256 public totalStaked;

    // Mapping from user address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping from user address to their pending rewards
    mapping(address => uint256) public rewardBalances;

    // Reward rate in $GIGA tokens per second per staked LP token
    uint256 public rewardRate;

    // Last time rewards were updated
    mapping(address => uint256) public lastUpdated;

    // Contract owner
    address public owner;

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract
     * @param _gigaToken Address of the $GIGA token contract
     * @param _lpToken Address of the LP token contract
     * @param _rewardRate Rewards rate in $GIGA tokens per second per staked LP token
     */
    constructor(
        IERC20 _gigaToken,
        IERC20 _lpToken,
        uint256 _rewardRate
    ) {
        gigaToken = _gigaToken;
        lpToken = _lpToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Updates the rewards for a user
     * @param user Address of the user
     */
    function updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        rewardBalances[user] += stakedBalances[user] * rewardRate * timeElapsed;
        lastUpdated[user] = block.timestamp;
    }

    /**
     * @dev Stake LP tokens to start earning rewards
     * @param amount Amount of LP tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update rewards before modifying balances
        updateRewards(msg.sender);

        // Transfer LP tokens from the user to the contract
        require(lpToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking balances
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Record the last updated time
        lastUpdated[msg.sender] = block.timestamp;
    }

    /**
     * @dev Unstake LP tokens and claim rewards
     * @param amount Amount of LP tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before modifying balances
        updateRewards(msg.sender);

        // Transfer LP tokens back to the user
        require(lpToken.transfer(msg.sender, amount), "Transfer failed");

        // Update staking balances
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
    }

    /**
     * @dev Claim $GIGA rewards earned from staking
     */
    function claimRewards() external {
        // Update rewards before claiming
        updateRewards(msg.sender);

        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer $GIGA tokens to the user
        require(gigaToken.transfer(msg.sender, rewards), "Transfer failed");
    }

    /**
     * @dev Set a new rewards rate
     * @param _rewardRate New reward rate in $GIGA per second per LP token
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens by the owner
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
}

/**
 * @dev Interface for ERC20 token
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
