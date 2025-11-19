"""
Generated Code Metadata:
========================
Original URL: https://testuser.usdtddex.com
Prompt: "Write a smart contract for a decentralized staking system on the Binance Smart Chain (BEP20) similar to USDT DONOR (USDTD)."
Generated: DETERMINISTIC_9c92fc9e928cce6a
Batch ID: 20250622_211941
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract for BEP20 Token
 * @author [Your Name]
 * @notice This contract provides a decentralized staking system for BEP20 tokens.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Mapping of staking plans
    mapping (uint256 => StakingPlan) public stakingPlans;

    // Total staked amount
    uint256 public totalStaked;

    // Token contract instance
    ERC20 public token;

    // Staking plan count
    uint256 public stakingPlanCount;

    /**
     * @dev Event emitted when a user stakes tokens
     * @param user Address of the user
     * @param amount Staked amount
     * @param planId Staking plan ID
     */
    event Staked(address indexed user, uint256 amount, uint256 planId);

    /**
     * @dev Event emitted when a user unstakes tokens
     * @param user Address of the user
     * @param amount Unstaked amount
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a staking plan is added
     * @param planId Staking plan ID
     * @param duration Staking duration
     * @param reward Reward amount
     */
    event StakingPlanAdded(uint256 planId, uint256 duration, uint256 reward);

    /**
     * @dev Struct representing a staker
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStaked;
        uint256 planId;
    }

    /**
     * @dev Struct representing a staking plan
     */
    struct StakingPlan {
        uint256 id;
        uint256 duration;
        uint256 reward;
    }

    /**
     * @dev Constructor
     * @param tokenAddress Address of the token contract
     */
    constructor(address tokenAddress) public {
        token = ERC20(tokenAddress);
        stakingPlanCount = 0;
    }

    /**
     * @dev Adds a new staking plan
     * @param duration Staking duration
     * @param reward Reward amount
     */
    function addStakingPlan(uint256 duration, uint256 reward) public onlyOwner {
        stakingPlans[stakingPlanCount] = StakingPlan(stakingPlanCount, duration, reward);
        stakingPlanCount++;
        emit StakingPlanAdded(stakingPlanCount - 1, duration, reward);
    }

    /**
     * @dev Stake tokens
     * @param amount Staked amount
     * @param planId Staking plan ID
     */
    function stake(uint256 amount, uint256 planId) public {
        require(stakingPlans[planId].duration > 0, "Invalid staking plan");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].lastStaked = block.timestamp;
        stakers[msg.sender].planId = planId;
        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount, planId);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() public nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked amount");
        uint256 stakingDuration = stakingPlans[staker.planId].duration;
        require(block.timestamp >= staker.lastStaked.add(stakingDuration), "Staking duration not completed");
        uint256 reward = stakingPlans[staker.planId].reward;
        uint256 unstakedAmount = staker.stakedAmount.add(reward);
        staker.stakedAmount = 0;
        staker.lastStaked = 0;
        staker.planId = 0;
        totalStaked = totalStaked.sub(unstakedAmount);
        require(token.transfer(msg.sender, unstakedAmount), "Token transfer failed");
        emit Unstaked(msg.sender, unstakedAmount);
    }

    /**
     * @dev Modifier for only owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    /**
     * @dev Gets the owner address
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return 0x...; // Replace with actual owner address
    }
}
```

Please note you need to:
*   Replace `0x...` with actual owner address.
*   Deploy OpenZeppelin contracts using npm by running `npm install @openzeppelin/contracts`.
*   Adjust and optimize gas costs according to your network.

You can use Remix, Truffle or Hardhat to deploy and test. Make sure to adjust according to your environment.
