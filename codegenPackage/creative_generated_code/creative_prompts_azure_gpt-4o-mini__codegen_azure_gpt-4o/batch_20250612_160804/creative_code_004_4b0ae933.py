"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: Describe the steps to stake DOGE20 tokens and how the smart contract distributes rewards over a two-year period.
Generated: DETERMINISTIC_4b0ae9333216ea7b
Batch ID: 20250612_160804
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
 * @title DOGE20 Staking Contract
 * @dev A smart contract to allow users to stake DOGE20 tokens and distribute rewards over a two-year period.
 */
contract DOGE20Staking {
    // Token interface
    IERC20 public immutable dogeToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 startTime;       // Timestamp when staking started
        uint256 rewardClaimed;   // Amount of rewards already claimed
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) public stakes;

    // Total rewards pool
    uint256 public totalRewards;

    // Reward distribution period (2 years in seconds)
    uint256 public constant REWARD_PERIOD = 2 * 365 * 24 * 60 * 60;

    // Ownership of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _dogeToken Address of the DOGE20 token contract.
     * @param _totalRewards Initial rewards pool.
     */
    constructor(IERC20 _dogeToken, uint256 _totalRewards) {
        require(address(_dogeToken) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Reward pool must be greater than zero");

        dogeToken = _dogeToken;
        totalRewards = _totalRewards;
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to stake DOGE20 tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            dogeToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update the staking information
        if (stakes[msg.sender].amount > 0) {
            // If already staking, claim pending rewards first
            claimRewards();
        }

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];

        if (stakeInfo.amount == 0 || block.timestamp < stakeInfo.startTime) {
            return 0;
        }

        // Calculate the time elapsed since staking started
        uint256 timeElapsed = block.timestamp - stakeInfo.startTime;
        if (timeElapsed > REWARD_PERIOD) {
            timeElapsed = REWARD_PERIOD; // Cap at maximum reward period
        }

        // Calculate the rewards proportionally based on time elapsed
        uint256 totalUserReward = (stakeInfo.amount * totalRewards) /
            dogeToken.totalSupply();
        uint256 proportionalReward = (totalUserReward * timeElapsed) /
            REWARD_PERIOD;

        return proportionalReward - stakeInfo.rewardClaimed;
    }

    /**
     * @dev Function for users to claim their pending rewards.
     */
    function claimRewards() public {
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available");

        // Update the reward claimed and transfer tokens to the user
        stakes[msg.sender].rewardClaimed += pendingRewards;
        require(
            dogeToken.transfer(msg.sender, pendingRewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Function for users to withdraw their staked tokens.
     */
    function withdrawStake() external {
        Stake memory stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        // Claim any pending rewards before withdrawal
        claimRewards();

        uint256 stakedAmount = stakeInfo.amount;

        // Reset user stake details
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;
        stakes[msg.sender].rewardClaimed = 0;

        // Transfer staked tokens back to the user
        require(
            dogeToken.transfer(msg.sender, stakedAmount),
            "Withdraw transfer failed"
        );

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Function for the owner to add more rewards to the pool.
     * @param amount Amount of rewards to add.
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Rewards amount must be greater than zero");

        // Transfer additional rewards to the contract
        require(
            dogeToken.transferFrom(msg.sender, address(this), amount),
            "Reward transfer failed"
        );

        totalRewards += amount;
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

        function transfer(address recipient, uint256 amount)
            external
            returns (bool);

        function totalSupply() external view returns (uint256);
    }
}
```
