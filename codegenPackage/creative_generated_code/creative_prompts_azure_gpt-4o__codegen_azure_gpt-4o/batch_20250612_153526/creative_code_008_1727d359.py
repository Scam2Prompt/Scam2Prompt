"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherfi-app.github.io
Prompt: Generate a Solidity contract for a yield farming system that distributes rewards based on liquidity contributions, inspired by Ether Fi's staking and farming features.
Generated: DETERMINISTIC_1727d35989f33c54
Batch ID: 20250612_153526
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
 * @title YieldFarmingContract
 * @dev This contract allows users to stake liquidity and earn rewards based on their contributions.
 * Rewards are distributed proportionally to the stake of each user.
 */
contract YieldFarmingContract {
    // State Variables
    address public owner; // Contract owner address
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock; // Last block number when rewards were distributed

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Tracks rewards already paid out
    }

    mapping(address => StakeInfo) public stakes; // User address => StakeInfo

    // ERC20 token implementation for staking and rewards
    IERC20 public stakingToken;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract variables.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per block.
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Function to stake tokens into the yield farming contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        updateRewards();

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt =
            (userStake.amount * rewardRate * (block.number - lastRewardBlock)) /
            totalStaked;

        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        updateRewards();

        userStake.amount -= amount;
        userStake.rewardDebt =
            (userStake.amount * rewardRate * (block.number - lastRewardBlock)) /
            totalStaked;

        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards accumulated by the user.
     */
    function claimRewards() external {
        updateRewards();

        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingRewards = (userStake.amount * rewardRate) -
            userStake.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        userStake.rewardDebt += pendingRewards;

        require(
            stakingToken.transfer(msg.sender, pendingRewards),
            "Token transfer failed"
        );

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update rewards distribution.
     */
    function updateRewards() internal {
        if (block.number > lastRewardBlock && totalStaked > 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            lastRewardBlock = block.number;

            // Rewards distributed proportionally based on staked amount
            // Calculation logic can be extended if needed
        }
    }

    /**
     * @dev Function to update the reward rate.
     * @param _rewardRate New reward rate per block.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        updateRewards();
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency function to allow owner to recover staking tokens in case of a contract issue.
     */
    function recoverTokens() external onlyOwner {
        uint256 contractBalance = stakingToken.balanceOf(address(this));
        require(
            stakingToken.transfer(owner, contractBalance),
            "Token transfer failed"
        );
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
