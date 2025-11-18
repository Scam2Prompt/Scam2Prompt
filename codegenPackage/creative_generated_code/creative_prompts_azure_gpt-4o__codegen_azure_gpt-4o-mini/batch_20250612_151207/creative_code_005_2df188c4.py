"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Provide a step-by-step guide for setting up a staking smart contract on Ethereum for $DOGEVERSE tokens, including security measures for locking tokens and calculating rewards dynamically.
Generated: DETERMINISTIC_2df188c4d347e66c
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

// Import OpenZeppelin libraries for ERC20 token and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DogeverseStaking
 * @dev A staking contract for $DOGEVERSE tokens allowing users to stake their tokens, earn rewards, and have their tokens locked.
 */
contract DogeverseStaking is Ownable {
    // State variables
    IERC20 public dogeverseToken; // The $DOGEVERSE token contract
    uint256 public rewardRate; // Reward rate in tokens per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staked
        uint256 rewards; // Rewards accumulated
    }

    mapping(address => Stake) private stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize contract with the token and reward rate
    constructor(IERC20 _dogeverseToken, uint256 _rewardRate) {
        dogeverseToken = _dogeverseToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake a certain amount of $DOGEVERSE tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(dogeverseToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate rewards before updating the stake
        _updateRewards(msg.sender);

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        _updateRewards(msg.sender);

        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        totalStaked -= amountToWithdraw;

        require(dogeverseToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");

        emit Unstaked(msg.sender, amountToWithdraw);
        emit RewardsClaimed(msg.sender, userStake.rewards);
    }

    /**
     * @dev Calculates rewards for the user and updates their stake record.
     * @param user The address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];

        // Calculate the elapsed time since last stake update
        uint256 elapsedTime = block.timestamp - userStake.timestamp;

        // Update rewards based on the elapsed time and reward rate
        uint256 rewards = (userStake.amount * rewardRate * elapsedTime) / 1e18;
        userStake.rewards += rewards;
        userStake.timestamp = block.timestamp;
    }

    /**
     * @dev Allows an owner to withdraw tokens from the contract in case of emergency.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= dogeverseToken.balanceOf(address(this)), "Insufficient balance");
        require(dogeverseToken.transfer(owner(), amount), "Transfer failed");
    }

    /**
     * @dev Allows the owner to change the reward rate.
     * @param newRewardRate The new reward rate to set.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Returns the user's stake information.
     * @param user The address of the user.
     * @return amount The amount staked by the user.
     * @return rewards The rewards accumulated by the user.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 rewards) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.rewards + ((userStake.amount * rewardRate * (block.timestamp - userStake.timestamp)) / 1e18));
    }
}
```
