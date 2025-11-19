"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: How can I implement a staking mechanism for OMEME tokens that rewards users with a 652% dynamic percentage on the Oracle Meme platform?
Generated: DETERMINISTIC_98b5e260cf655fcf
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

// Importing OpenZeppelin's SafeMath library for safe mathematical operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OMEME Staking Contract
 * @dev This contract allows users to stake OMEME tokens and earn rewards based on a dynamic percentage.
 */
contract OMEMEStaking is Ownable {
    using SafeMath for uint256;

    // The OMEME token contract
    IERC20 public immutable omemeToken;

    // Struct to hold user's staking information
    struct Staker {
        uint256 amountStaked;
        uint256 lastRewardTime;
    }

    // Mapping from user addresses to their staking information
    mapping(address => Staker) private stakers;

    // Total amount of OMEME tokens staked
    uint256 public totalStaked;

    // Dynamic reward percentage (in basis points, 10000 = 100%)
    uint256 public constant rewardPercentage = 65200; // 652%

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor that sets the OMEME token address.
     * @param _omemeToken Address of the OMEME token contract.
     */
    constructor(address _omemeToken) {
        require(_omemeToken != address(0), "Invalid token address");
        omemeToken = IERC20(_omemeToken);
    }

    /**
     * @dev Allows users to stake OMEME tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(omemeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastRewardTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim rewards before withdrawing
        claimRewards();

        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(omemeToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards based on the staked amount.
     */
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards available");

        // Update user's last reward time
        staker.lastRewardTime = block.timestamp;

        require(omemeToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a given user.
     * @param user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 stakedDuration = block.timestamp.sub(staker.lastRewardTime);

        // Reward formula: (staked amount * reward percentage * staking duration) / (365 days in seconds)
        return staker.amountStaked
            .mul(rewardPercentage)
            .mul(stakedDuration)
            .div(365 days)
            .div(10000); // adjust for basis points
    }

    /**
     * @dev Returns the staked amount of a user.
     * @param user The address of the user.
     * @return The amount staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }
}
```
