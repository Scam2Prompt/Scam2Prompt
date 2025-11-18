"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Write a Solidity smart contract to enable staking $ARTY tokens for vesting rewards, ensuring governance token functionality for the Artyfact ecosystem.
Generated: DETERMINISTIC_992bd915fcb39935
Batch ID: 20250612_152441
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

// Importing the ERC20 interface to interact with the $ARTY token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ArtyfactStaking
 * @dev A smart contract to enable staking of $ARTY tokens for vesting rewards
 */
contract ArtyfactStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;  // Amount of tokens staked
        uint256 rewardDebt;     // Amount of rewards owed
        uint256 lastStakedTime; // Last time the tokens were staked
    }

    // Mapping from staker address to their staking details
    mapping(address => Staker) public stakers;
    // Total amount of $ARTY tokens staked
    uint256 public totalStaked;
    // Address of the $ARTY token contract
    IERC20 public token;

    // Reward rate per second (adjustable based on governance)
    uint256 public rewardRate = 1 ether; // Example: 1 token per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the $ARTY token address
     * @param _token The address of the $ARTY token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Allows users to stake $ARTY tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update the staker's information
        _updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update the staker's amount and total staked
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update the staker's amount and total staked
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the staker
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 rewards = stakers[msg.sender].rewardDebt;

        require(rewards > 0, "No rewards available");

        // Reset the rewardDebt for the staker to zero
        stakers[msg.sender].rewardDebt = 0;

        // Transfer the rewards to the staker
        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a staker
     * @param user The address of the user to update rewards for
     */
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;

        if (staker.amountStaked > 0) {
            // Calculate rewards based on the time staked and reward rate
            uint256 rewards = timeStaked * rewardRate * staker.amountStaked / 1 ether;
            staker.rewardDebt += rewards;
        }

        // Update the last staked time to the current block time
        staker.lastStakedTime = block.timestamp;
    }

    /**
     * @dev Allows the owner to set a new reward rate
     * @param _rewardRate The new reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
