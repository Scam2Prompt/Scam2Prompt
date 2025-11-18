"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syrupps.pages.dev
Prompt: Develop a smart contract that aligns with Syrup Finance's value accrual and staking reward mechanisms.
Generated: DETERMINISTIC_4a0f886e0127a096
Batch ID: 20250612_145913
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
 * @title SyrupFinanceStaking
 * @dev Smart Contract to handle staking, rewards, and value accrual mechanisms for Syrup Finance.
 */
contract SyrupFinanceStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total tokens staked
    uint256 public lastUpdateBlock; // Last block when rewards were updated
    uint256 public rewardPerTokenStored; // Aggregate reward per token

    struct UserInfo {
        uint256 stakedAmount; // Amount of tokens staked by the user
        uint256 rewards; // User's pending rewards
        uint256 rewardPerTokenPaid; // User's reward per token paid
    }

    mapping(address => UserInfo) public userInfo; // Mapping of user addresses to their staking details
    IERC20 public stakingToken; // ERC20 token used for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Modifier to restrict access to owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per block.
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Updates reward data for the entire contract.
     */
    function updateReward() internal {
        if (totalStaked > 0) {
            rewardPerTokenStored +=
                (rewardRate * (block.number - lastUpdateBlock) * 1e18) /
                totalStaked;
        }
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Updates reward data for a specific user.
     * @param user Address of the user to update rewards for.
     */
    function updateUserReward(address user) internal {
        UserInfo storage userInfoData = userInfo[user];
        userInfoData.rewards +=
            (userInfoData.stakedAmount *
                (rewardPerTokenStored - userInfoData.rewardPerTokenPaid)) /
            1e18;
        userInfoData.rewardPerTokenPaid = rewardPerTokenStored;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        updateReward();
        updateUserReward(msg.sender);

        // Transfer staking tokens to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user info and total staked
        UserInfo storage userInfoData = userInfo[msg.sender];
        userInfoData.stakedAmount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        UserInfo storage userInfoData = userInfo[msg.sender];
        require(userInfoData.stakedAmount >= amount, "Insufficient staked balance");

        updateReward();
        updateUserReward(msg.sender);

        // Update user info and total staked
        userInfoData.stakedAmount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimReward() external {
        updateReward();
        updateUserReward(msg.sender);

        UserInfo storage userInfoData = userInfo[msg.sender];
        uint256 reward = userInfoData.rewards;
        require(reward > 0, "No rewards to claim");

        userInfoData.rewards = 0;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate New reward rate per block.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateReward();
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        stakingToken.transfer(owner, amount);
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
