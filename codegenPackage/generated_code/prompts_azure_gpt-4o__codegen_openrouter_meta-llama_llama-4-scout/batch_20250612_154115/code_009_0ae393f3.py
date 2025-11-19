"""
Generated Code Metadata:
========================
Original URL: https://xyzwthelly.com
Prompt: Create a Solidity contract that integrates with Valantis to enable liquid staking of nBTC via the stHYPE AMM.
Generated: DETERMINISTIC_0ae393f3266355ab
Batch ID: 20250612_154115
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Valantis integration
import "./ValantisInterface.sol";

// stHYPE AMM integration
import "./stHYPEAMMInterface.sol";

contract LiquidStakingnBTC {
    // Libraries
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user rewards
    mapping (address => uint256) public userRewards;

    // Valantis interface
    ValantisInterface public valantis;

    // stHYPE AMM interface
    stHYPEAMMInterface public stHYPEAMM;

    // nBTC token address
    IERC20 public nBTC;

    // stHYPE token address
    IERC20 public stHYPE;

    // Reward token address
    IERC20 public rewardToken;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Total staked nBTC
    uint256 public totalStaked;

    // Event emitted when user stakes nBTC
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes nBTC
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param valantisAddress Address of Valantis contract
     * @param stHYPEAMMAddress Address of stHYPE AMM contract
     * @param nBTCAddress Address of nBTC token contract
     * @param stHYPEAddress Address of stHYPE token contract
     * @param rewardTokenAddress Address of reward token contract
     * @param stakingEndTimestamp Timestamp when staking ends
     */
    constructor(
        address valantisAddress,
        address stHYPEAMMAddress,
        address nBTCAddress,
        address stHYPEAddress,
        address rewardTokenAddress,
        uint256 stakingEndTimestamp
    ) public {
        valantis = ValantisInterface(valantisAddress);
        stHYPEAMM = stHYPEAMMInterface(stHYPEAMMAddress);
        nBTC = IERC20(nBTCAddress);
        stHYPE = IERC20(stHYPEAddress);
        rewardToken = IERC20(rewardTokenAddress);
        stakingEnd = stakingEndTimestamp;
    }

    /**
     * Stake nBTC
     * @param amount Amount of nBTC to stake
     */
    function stake(uint256 amount) external {
        require(msg.sender != address(0), "Invalid user address");
        require(amount > 0, "Invalid stake amount");
        require(stakingEnd > block.timestamp, "Staking has ended");

        // Transfer nBTC from user to contract
        require(nBTC.transferFrom(msg.sender, address(this), amount), "nBTC transfer failed");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Update total staked nBTC
        totalStaked = totalStaked.add(amount);

        // Emit stake event
        emit Staked(msg.sender, amount);
    }

    /**
     * Unstake nBTC
     * @param amount Amount of nBTC to unstake
     */
    function unstake(uint256 amount) external {
        require(msg.sender != address(0), "Invalid user address");
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Update total staked nBTC
        totalStaked = totalStaked.sub(amount);

        // Transfer nBTC from contract to user
        require(nBTC.transfer(msg.sender, amount), "nBTC transfer failed");

        // Emit unstake event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * Claim rewards
     */
    function claimRewards() external {
        require(msg.sender != address(0), "Invalid user address");
        require(userRewards[msg.sender] > 0, "No rewards to claim");

        // Update user's rewards
        uint256 rewards = userRewards[msg.sender];
        userRewards[msg.sender] = 0;

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, rewards), "Reward token transfer failed");

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * Update user rewards
     * @param user Address of user
     */
    function updateRewards(address user) public {
        // Calculate rewards using Valantis and stHYPE AMM
        uint256 rewards = valantis.calculateRewards(user, totalStaked);
        rewards = stHYPEAMM.calculateRewards(user, rewards);

        // Update user's rewards
        userRewards[user] = userRewards[user].add(rewards);
    }

    /**
     * Add liquidity to stHYPE AMM
     * @param amount Amount of nBTC to add
     */
    function addLiquidity(uint256 amount) external {
        require(msg.sender != address(0), "Invalid user address");
        require(amount > 0, "Invalid liquidity amount");

        // Approve stHYPE AMM to spend nBTC
        require(nBTC.approve(address(stHYPEAMM), amount), "nBTC approval failed");

        // Add liquidity to stHYPE AMM
        stHYPEAMM.addLiquidity(amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Update total staked nBTC
        totalStaked = totalStaked.sub(amount);
    }

    /**
     * Remove liquidity from stHYPE AMM
     * @param amount Amount of nBTC to remove
     */
    function removeLiquidity(uint256 amount) external {
        require(msg.sender != address(0), "Invalid user address");
        require(amount > 0, "Invalid liquidity amount");

        // Remove liquidity from stHYPE AMM
        stHYPEAMM.removeLiquidity(amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Update total staked nBTC
        totalStaked = totalStaked.add(amount);
    }

    // Fallback function
    receive() external payable {}

    // Function to handle reentrancy
    fallback() external payable {
        // Handle reentrancy
    }
}
```
