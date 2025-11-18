"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claims.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates Kangamoon's $KANG token, allowing users to stake their tokens and earn rewards based on the staking duration. Ensure compatibility with the ERC-20 standard.
Generated: DETERMINISTIC_4b279f70bdfcd03d
Batch ID: 20250612_145625
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

// Importing OpenZeppelin libraries for ERC20 functionality and SafeMath
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title KangamoonTokenStaking
 * @dev A smart contract allowing users to stake $KANG tokens and earn rewards based on staking duration.
 */
contract KangamoonTokenStaking is Ownable {
    using SafeMath for uint256;

    // Instance of the $KANG token
    IERC20 public kangToken;

    // Staking structure to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp of when tokens were staked
    }

    // Mapping of address to Stake information
    mapping(address => Stake) public stakes;

    // Annual percentage yield (APY) for rewards
    uint256 public rewardRatePerYear = 10; // 10% APY

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $KANG token address.
     * @param _kangToken Address of the ERC20 $KANG token contract.
     */
    constructor(address _kangToken) {
        require(_kangToken != address(0), "Invalid token address");
        kangToken = IERC20(_kangToken);
    }

    /**
     * @dev Function allowing users to stake $KANG tokens.
     * @param amount Amount of $KANG tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(kangToken.balanceOf(msg.sender) >= amount, "Insufficient $KANG balance");

        // Transfer $KANG tokens from user to the contract
        kangToken.transferFrom(msg.sender, address(this), amount);

        // Update staking information
        if (stakes[msg.sender].amount > 0) {
            // If user already has an active stake, first calculate pending rewards
            uint256 pendingReward = calculateReward(msg.sender);
            stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
            stakes[msg.sender].startTime = block.timestamp; // Reset start time
            // Emit event for the pending rewards
            emit RewardsClaimed(msg.sender, pendingReward);
        } else {
            stakes[msg.sender] = Stake(amount, block.timestamp);
        }

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function allowing users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Get the staked amount and reset user stake
        uint256 stakedAmount = stakes[msg.sender].amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;

        // Transfer staked tokens and rewards back to the user
        kangToken.transfer(msg.sender, stakedAmount.add(reward));

        // Update total staked tokens
        totalStaked = totalStaked.sub(stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate rewards for a user based on staking duration.
     * @param user Address of the user whose reward is to be calculated.
     * @return reward The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp.sub(userStake.startTime); // Staking duration in seconds
        uint256 annualReward = userStake.amount.mul(rewardRatePerYear).div(100); // Annual reward
        reward = annualReward.mul(stakingDuration).div(365 days); // Pro-rata reward based on staking duration
    }

    /**
     * @dev Function to change the reward rate. Only callable by the contract owner.
     * @param newRewardRate New reward rate in percentage per year.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRatePerYear = newRewardRate;
    }

    /**
     * @dev Emergency function allowing the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0 && amount <= kangToken.balanceOf(address(this)), "Invalid withdraw amount");
        kangToken.transfer(owner(), amount);
    }
}
```
