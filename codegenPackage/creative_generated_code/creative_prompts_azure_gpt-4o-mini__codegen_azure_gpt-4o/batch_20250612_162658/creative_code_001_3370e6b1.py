"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibaswap.mypixieset.com
Prompt: How can I implement a staking mechanism in my DeFi project similar to ShibaSwap's "BURY" feature for staking SHIB, LEASH, and BONE tokens?
Generated: DETERMINISTIC_3370e6b146eb65c1
Batch ID: 20250612_162658
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
 * @title StakingContract
 * @dev A contract that allows users to stake tokens (SHIB, LEASH, BONE) and earn rewards.
 * Inspired by the "BURY" feature in ShibaSwap.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Struct to track staking information for each user
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastStakedTimestamp; // Timestamp of the last stake
    }

    // Supported tokens for staking
    IERC20 public shibToken;
    IERC20 public leashToken;
    IERC20 public boneToken;

    // Mapping of token address to mapping of user address to their stake information
    mapping(address => mapping(address => StakeInfo)) public stakes;

    // Reward rate per second (adjustable by the owner)
    uint256 public rewardRatePerSecond;

    // Events for transparency
    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event ClaimedRewards(address indexed user, address indexed token, uint256 rewards);

    /**
     * @dev Constructor to initialize staking tokens and reward rate.
     * @param _shibToken Address of the SHIB token smart contract.
     * @param _leashToken Address of the LEASH token smart contract.
     * @param _boneToken Address of the BONE token smart contract.
     * @param _rewardRatePerSecond Base reward rate per second.
     */
    constructor(
        address _shibToken,
        address _leashToken,
        address _boneToken,
        uint256 _rewardRatePerSecond
    ) {
        shibToken = IERC20(_shibToken);
        leashToken = IERC20(_leashToken);
        boneToken = IERC20(_boneToken);
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Modifier to validate token is supported.
     * @param token Address of the token to validate.
     */
    modifier validToken(address token) {
        require(
            token == address(shibToken) || token == address(leashToken) || token == address(boneToken),
            "Invalid token!"
        );
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param token Address of the token to stake.
     * @param amount Amount of tokens to stake.
     */
    function stake(address token, uint256 amount) external validToken(token) {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update user staking info
        StakeInfo storage userStake = stakes[token][msg.sender];
        userStake.rewardDebt += calculatePendingRewards(token, msg.sender); // Update pending rewards
        userStake.amount += amount; // Update staked amount
        userStake.lastStakedTimestamp = block.timestamp; // Update last staked timestamp

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param token Address of the token to unstake.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(address token, uint256 amount) external validToken(token) {
        require(amount > 0, "Cannot unstake 0 tokens");

        StakeInfo storage userStake = stakes[token][msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards(token);

        // Update user staking info
        userStake.amount -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Claim staking rewards.
     * @param token Address of the token to claim rewards from.
     */
    function claimRewards(address token) public validToken(token) {
        uint256 pendingRewards = calculatePendingRewards(token, msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt
        StakeInfo storage userStake = stakes[token][msg.sender];
        userStake.rewardDebt = 0;

        // Transfer rewards (for simplicity, assuming rewards are paid in the same token)
        IERC20(token).transfer(msg.sender, pendingRewards);

        emit ClaimedRewards(msg.sender, token, pendingRewards);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param token Address of the token to calculate rewards for.
     * @param user Address of the user to calculate rewards for.
     * @return Pending rewards for the user.
     */
    function calculatePendingRewards(address token, address user) internal view returns (uint256) {
        StakeInfo memory userStake = stakes[token][user];

        if (userStake.amount == 0) {
            return 0; // No rewards for zero staked amount
        }

        // Calculate rewards based on staked duration and reward rate
        uint256 stakingDuration = block.timestamp - userStake.lastStakedTimestamp;
        uint256 rewards = (stakingDuration * userStake.amount * rewardRatePerSecond) / 1e18;

        return rewards + userStake.rewardDebt;
    }

    /**
     * @dev Update the reward rate per second. Only callable by the owner.
     * @param newRewardRatePerSecond New reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRatePerSecond) external onlyOwner {
        rewardRatePerSecond = newRewardRatePerSecond;
    }
}
```
