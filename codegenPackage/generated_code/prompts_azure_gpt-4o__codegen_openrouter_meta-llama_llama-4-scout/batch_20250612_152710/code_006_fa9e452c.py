"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Develop a smart contract that supports multiple staking pools for AITECH tokens with varying lock terms, reward compositions, and tier boosts, as outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_fa9e452cb2af083b
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/utils/Pausable.sol";

contract AITECHStakingPool is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of pool IDs to their respective details
    mapping(uint256 => Pool) public pools;

    // Mapping of user staking details
    mapping(address => mapping(uint256 => UserStaking)) public userStakings;

    // Mapping of pool ID to reward composition
    mapping(uint256 => RewardComposition) public rewardCompositions;

    // Mapping of pool ID to tier boosts
    mapping(uint256 => TierBoosts) public tierBoosts;

    // Event emitted when a new pool is created
    event NewPool(uint256 indexed poolId, uint256 lockTerm, uint256 reward);

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 indexed poolId, uint256 amount);

    // Struct to represent a staking pool
    struct Pool {
        uint256 id;
        uint256 lockTerm; // Lock term in seconds
        uint256 totalStaked; // Total tokens staked in the pool
        uint256 reward; // Total reward for the pool
    }

    // Struct to represent user staking details
    struct UserStaking {
        uint256 stakedAmount; // Tokens staked by the user
        uint256 stakedAt; // Timestamp when tokens were staked
    }

    // Struct to represent reward composition
    struct RewardComposition {
        uint256 rewardPercentage; // Percentage of reward
        address rewardToken; // Address of reward token
    }

    // Struct to represent tier boosts
    struct TierBoosts {
        uint256[] tierAmounts; // Tier amounts
        uint256[] boosts; // Corresponding boosts
    }

    // Function to create a new staking pool
    function createPool(
        uint256 _lockTerm,
        uint256 _reward,
        uint256 _rewardPercentage,
        address _rewardToken
    ) public onlyOwner {
        require(_lockTerm > 0, "Lock term must be greater than 0");
        require(_reward > 0, "Reward must be greater than 0");
        require(_rewardPercentage > 0, "Reward percentage must be greater than 0");
        require(_rewardToken != address(0), "Reward token address cannot be 0");

        uint256 poolId = uint256(keccak256(abi.encodePacked(_lockTerm, _reward))) % (2**256);
        pools[poolId] = Pool(poolId, _lockTerm, 0, _reward);
        rewardCompositions[poolId] = RewardComposition(_rewardPercentage, _rewardToken);
        emit NewPool(poolId, _lockTerm, _reward);
    }

    // Function to stake tokens in a pool
    function stake(uint256 _poolId, uint256 _amount) public whenNotPaused {
        require(pools[_poolId].lockTerm > 0, "Pool does not exist");
        require(_amount > 0, "Staking amount must be greater than 0");

        Pool storage pool = pools[_poolId];
        UserStaking storage userStaking = userStakings[msg.sender][_poolId];

        IERC20(AITECH_TOKEN_ADDRESS).transferFrom(msg.sender, address(this), _amount);
        pool.totalStaked = pool.totalStaked.add(_amount);
        userStaking.stakedAmount = userStaking.stakedAmount.add(_amount);
        userStaking.stakedAt = block.timestamp;
        emit Staked(msg.sender, _poolId, _amount);
    }

    // Function to unstake tokens from a pool
    function unstake(uint256 _poolId) public whenNotPaused {
        require(pools[_poolId].lockTerm > 0, "Pool does not exist");
        require(userStakings[msg.sender][_poolId].stakedAmount > 0, "User has not staked in this pool");

        Pool storage pool = pools[_poolId];
        UserStaking storage userStaking = userStakings[msg.sender][_poolId];

        require(block.timestamp >= userStaking.stakedAt.add(pool.lockTerm), "Lock term has not expired");

        uint256 unstakeAmount = userStaking.stakedAmount;
        pool.totalStaked = pool.totalStaked.sub(unstakeAmount);
        userStaking.stakedAmount = 0;
        IERC20(AITECH_TOKEN_ADDRESS).transfer(msg.sender, unstakeAmount);
        emit Unstaked(msg.sender, _poolId, unstakeAmount);
    }

    // Function to claim rewards
    function claimRewards(uint256 _poolId) public whenNotPaused {
        require(pools[_poolId].lockTerm > 0, "Pool does not exist");
        require(userStakings[msg.sender][_poolId].stakedAmount > 0, "User has not staked in this pool");

        Pool storage pool = pools[_poolId];
        UserStaking storage userStaking = userStakings[msg.sender][_poolId];

        require(block.timestamp >= userStaking.stakedAt.add(pool.lockTerm), "Lock term has not expired");

        RewardComposition storage rewardComposition = rewardCompositions[_poolId];
        uint256 rewardAmount = pool.reward.mul(rewardComposition.rewardPercentage).div(100);
        IERC20(rewardComposition.rewardToken).transfer(msg.sender, rewardAmount);
        emit RewardsClaimed(msg.sender, _poolId, rewardAmount);
    }

    // Function to add tier boosts
    function addTierBoosts(uint256 _poolId, uint256[] memory _tierAmounts, uint256[] memory _boosts) public onlyOwner {
        require(pools[_poolId].lockTerm > 0, "Pool does not exist");
        require(_tierAmounts.length == _boosts.length, "Tier amounts and boosts must have the same length");

        tierBoosts[_poolId] = TierBoosts(_tierAmounts, _boosts);
    }

    // Function to get user staking details
    function getUserStaking(address _user, uint256 _poolId) public view returns (uint256, uint256) {
        UserStaking storage userStaking = userStakings[_user][_poolId];
        return (userStaking.stakedAmount, userStaking.stakedAt);
    }

    // Function to get pool details
    function getPool(uint256 _poolId) public view returns (uint256, uint256, uint256) {
        Pool storage pool = pools[_poolId];
        return (pool.id, pool.lockTerm, pool.totalStaked);
    }
}

// Example usage
contract AITECHToken is IERC20 {
    mapping(address => uint256) public balances;

    function transfer(address _to, uint256 _amount) public returns (bool) {
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _amount) public returns (bool) {
        balances[_from] = balances[_from].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }
}

address constant AITECH_TOKEN_ADDRESS = address(new AITECHToken());
```
