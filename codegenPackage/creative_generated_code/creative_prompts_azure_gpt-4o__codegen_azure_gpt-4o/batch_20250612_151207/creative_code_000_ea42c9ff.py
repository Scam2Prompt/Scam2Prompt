"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Write a smart contract in Solidity for staking $DOGEVERSE tokens on the Ethereum network, ensuring dynamic rewards based on the staking duration. Reference the Dogeverse staking mechanism.
Generated: DETERMINISTIC_ea42c9ff37ebbe4a
Batch ID: 20250612_151207
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
 * @title DogeverseStaking
 * @dev A smart contract for staking $DOGEVERSE tokens with dynamic rewards based on the staking duration.
 */
contract DogeverseStaking {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the $DOGEVERSE token contract
    IERC20 public dogeverseToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool active; // Whether the stake is active
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate per hour (in percentage, e.g., 1 = 1%)
    uint256 public rewardRatePerHour;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _dogeverseToken Address of the $DOGEVERSE token contract.
     * @param _rewardRatePerHour Reward rate per hour in percentage.
     */
    constructor(IERC20 _dogeverseToken, uint256 _rewardRatePerHour) {
        dogeverseToken = _dogeverseToken;
        rewardRatePerHour = _rewardRatePerHour;
        owner = msg.sender;
    }

    /**
     * @dev Stake $DOGEVERSE tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(!stakes[msg.sender].active, "Already staking");

        // Transfer tokens from the user's wallet to the contract
        require(dogeverseToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record staking details
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            active: true
        });

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.active, "No active stake found");

        // Calculate reward based on staking duration
        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        uint256 reward = calculateReward(stakeInfo.amount, stakingDuration);

        // Transfer staked tokens back to the user
        require(dogeverseToken.transfer(msg.sender, stakeInfo.amount), "Token transfer failed");

        // Transfer rewards to the user
        require(dogeverseToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Clear staking record
        stakeInfo.active = false;

        emit Unstaked(msg.sender, stakeInfo.amount, reward);
    }

    /**
     * @dev Calculate reward based on staking duration and amount.
     * @param amount Amount of tokens staked.
     * @param duration Duration of staking in seconds.
     * @return reward Calculated reward amount.
     */
    function calculateReward(uint256 amount, uint256 duration) public view returns (uint256 reward) {
        uint256 hoursStaked = duration / 3600; // Convert seconds to hours
        reward = (amount * rewardRatePerHour * hoursStaked) / 100;
    }

    /**
     * @dev Update the reward rate per hour. Only callable by the owner.
     * @param newRate New reward rate per hour in percentage.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRatePerHour = newRate;
    }

    /**
     * @dev Emergency withdrawal of tokens in case of an issue. Only callable by the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(dogeverseToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
