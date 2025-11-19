"""
Generated Code Metadata:
========================
Original URL: https://bitbama.pages.dev
Prompt: Develop a smart contract snippet for staking Bama tokens on-chain, ensuring compatibility with the Bitbama governance model.
Generated: DETERMINISTIC_1d0f4d31df39f988
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BamaTokenStakingContract
 * @author [Your Name]
 * @notice A staking contract for Bama tokens, compatible with the Bitbama governance model.
 */
contract BamaTokenStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user staking rewards
    mapping(address => uint256) public stakingRewards;

    // Bama token contract instance
    IERC20 public bamaToken;

    // Staking reward rate (per block)
    uint256 public stakingRewardRate;

    // Total staked Bama tokens
    uint256 public totalStaked;

    // Bitbama governance model contract instance
    address public governanceContract;

    /**
     * @dev Event emitted when a user stakes Bama tokens
     * @param user The user's address
     * @param amount The amount of Bama tokens staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user unstakes Bama tokens
     * @param user The user's address
     * @param amount The amount of Bama tokens unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user claims staking rewards
     * @param user The user's address
     * @param amount The amount of rewards claimed
     */
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _bamaToken The address of the Bama token contract
     * @param _governanceContract The address of the Bitbama governance model contract
     * @param _stakingRewardRate The staking reward rate (per block)
     */
    constructor(
        address _bamaToken,
        address _governanceContract,
        uint256 _stakingRewardRate
    ) {
        require(_bamaToken != address(0), "Bama token contract address cannot be zero");
        require(_governanceContract != address(0), "Governance contract address cannot be zero");
        require(_stakingRewardRate > 0, "Staking reward rate must be greater than zero");

        bamaToken = IERC20(_bamaToken);
        governanceContract = _governanceContract;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @dev Stake Bama tokens
     * @param amount The amount of Bama tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(bamaToken.balanceOf(msg.sender) >= amount, "Insufficient Bama token balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        bamaToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake Bama tokens
     * @param amount The amount of Bama tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        bamaToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        stakingRewards[msg.sender] = 0;

        bamaToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user
     * @param user The user's address
     * @return The user's staking rewards
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 rewards = stakingBalances[user].mul(stakingRewardRate);
        return rewards.add(stakingRewards[user]);
    }

    /**
     * @dev Update staking reward rate
     * @param _stakingRewardRate The new staking reward rate (per block)
     */
    function updateStakingRewardRate(uint256 _stakingRewardRate) external onlyOwner {
        require(_stakingRewardRate > 0, "Staking reward rate must be greater than zero");

        stakingRewardRate = _stakingRewardRate;
    }
}
```
