"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeversehub.pages.dev
Prompt: Generate a Solidity contract for staking $DOGEVERSE tokens on the Ethereum network.
Generated: DETERMINISTIC_6ac5c4a53a95e9ae
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
 * @title DogeverseTokenStaking
 * @dev A staking contract for $DOGEVERSE tokens where users can stake and earn rewards.
 */
contract DogeverseTokenStaking {
    // ERC-20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $DOGEVERSE token contract address
    IERC20 public immutable dogeverseToken;
    
    // Owner of the contract
    address public owner;

    // Reward rate (e.g., tokens earned per second of staking)
    uint256 public rewardRate;

    // User staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the user last interacted (for rewards calculation)
        uint256 accumulated; // Accumulated rewards that are yet to be claimed
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Modifier to restrict access to owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _dogeverseToken Address of the $DOGEVERSE token contract
     * @param _rewardRate Reward rate (tokens earned per second of staking)
     */
    constructor(IERC20 _dogeverseToken, uint256 _rewardRate) {
        dogeverseToken = _dogeverseToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Number of $DOGEVERSE tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        Stake storage userStake = stakes[msg.sender];

        // Update accumulated rewards
        userStake.accumulated += _calculateRewards(msg.sender);

        // Update timestamp
        userStake.timestamp = block.timestamp;

        // Increase staked amount
        userStake.amount += _amount;

        // Transfer tokens to the contract
        require(
            dogeverseToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = _calculateRewards(msg.sender);

        // Update accumulated rewards
        userStake.accumulated += rewards;

        // Calculate unstaked amount
        uint256 unstakedAmount = userStake.amount;

        // Reset user stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens back to user
        require(
            dogeverseToken.transfer(msg.sender, unstakedAmount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, unstakedAmount);
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = _calculateRewards(msg.sender) + userStake.accumulated;

        require(rewards > 0, "No rewards available");

        // Reset accumulated rewards
        userStake.accumulated = 0;

        // Update timestamp
        userStake.timestamp = block.timestamp;

        // Transfer rewards to user
        require(
            dogeverseToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Owner function to update the reward rate.
     * @param _newRewardRate New reward rate (tokens earned per second of staking)
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param _user Address of the user
     * @return Rewards earned by the user
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.timestamp == 0) {
            return 0;
        }
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return userStake.amount * rewardRate * stakedDuration / 1e18;
    }
}
```
