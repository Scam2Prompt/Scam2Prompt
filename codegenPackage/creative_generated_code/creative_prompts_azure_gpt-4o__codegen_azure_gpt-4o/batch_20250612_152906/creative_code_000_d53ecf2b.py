"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbittherious.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens, inspired by the functionality described on the "Rious The Rabbit" website.
Generated: DETERMINISTIC_d53ecf2b25d13f65
Batch ID: 20250612_152906
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
 * @title TokenStaking
 * @dev A smart contract for staking ERC20 tokens. Users can deposit tokens, earn rewards, and withdraw their staked tokens.
 */
contract TokenStaking {
    // Token used for staking
    IERC20 public stakingToken;

    // Mapping to track user balances
    mapping(address => uint256) private stakedBalances;

    // Mapping to track user reward balances
    mapping(address => uint256) private rewardBalances;

    // Annual percentage yield (APY) for rewards
    uint256 public rewardRate; // e.g., 10 for 10%

    // Timestamp of last update for rewards
    mapping(address => uint256) private lastUpdateTimestamp;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Event emitted when tokens are staked.
     * @param user The address of the user staking tokens.
     * @param amount The amount of tokens staked.
     */
    event TokensStaked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when rewards are claimed.
     * @param user The address of the user claiming rewards.
     * @param amount The amount of rewards claimed.
     */
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when tokens are withdrawn.
     * @param user The address of the user withdrawing tokens.
     * @param amount The amount of tokens withdrawn.
     */
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the staking token and reward rate.
     * @param _stakingToken Address of the staking ERC20 token.
     * @param _rewardRate Annual percentage yield (APY) rate for rewards.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update staked balance
        stakedBalances[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = rewardBalances[msg.sender];
        require(rewardsToClaim > 0, "No rewards available");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to user
        require(
            stakingToken.transfer(msg.sender, rewardsToClaim),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            stakedBalances[msg.sender] >= amount,
            "Insufficient staked balance"
        );

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        // Update staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer staked tokens back to user
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Update rewards for a user based on the staking duration.
     * @param user Address of the user whose rewards are to be updated.
     */
    function _updateRewards(address user) internal {
        uint256 stakedAmount = stakedBalances[user];
        if (stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTimestamp[user];
            uint256 newRewards = (stakedAmount * rewardRate * timeElapsed) /
                (365 days * 100); // Calculate rewards based on APY
            rewardBalances[user] += newRewards;
        }
        lastUpdateTimestamp[user] = block.timestamp;
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function stakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the reward balance of a user.
     * @param user Address of the user.
     * @return The reward balance of the user.
     */
    function rewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }

    /**
     * @dev Update the reward rate. Only the owner can call this.
     * @param _rewardRate New annual percentage yield (APY) rate for rewards.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
