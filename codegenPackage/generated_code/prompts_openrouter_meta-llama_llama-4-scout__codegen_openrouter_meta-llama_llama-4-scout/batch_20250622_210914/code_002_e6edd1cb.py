"""
Generated Code Metadata:
========================
Original URL: https://ether-etherfi.github.io
Prompt: Generate a smart contract code for a yield farming and staking platform using the Ethereum blockchain, inspired by Ether Fi's features.
Generated: DETERMINISTIC_e6edd1cba2b568c1
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title YieldFarmingStakingContract
 * @author [Your Name]
 * @notice A smart contract for yield farming and staking on Ethereum, inspired by Ether Fi.
 */
contract YieldFarmingStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user farming rewards
    mapping(address => uint256) public farmingRewards;

    // Mapping of pool information
    mapping(address => Pool) public pools;

    // List of supported tokens for staking and farming
    address[] public supportedTokens;

    // Total value locked in the contract
    uint256 public totalValueLocked;

    // Farming reward rate
    uint256 public farmingRewardRate;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user farms tokens
    event Farmed(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user claims farming rewards
    event FarmingRewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when a user claims staking rewards
    event StakingRewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold pool information
    struct Pool {
        address token;
        uint256 totalStaked;
        uint256 totalFarmed;
    }

    /**
     * @notice Constructor for the YieldFarmingStakingContract
     * @param _farmingRewardRate The farming reward rate
     * @param _stakingRewardRate The staking reward rate
     */
    constructor(uint256 _farmingRewardRate, uint256 _stakingRewardRate) public {
        farmingRewardRate = _farmingRewardRate;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @notice Adds a new token to the list of supported tokens
     * @param _token The address of the token to add
     */
    function addSupportedToken(address _token) public onlyOwner {
        require(IERC20(_token).totalSupply() > 0, "Token must have a total supply");
        supportedTokens.push(_token);
    }

    /**
     * @notice Removes a token from the list of supported tokens
     * @param _token The address of the token to remove
     */
    function removeSupportedToken(address _token) public onlyOwner {
        require(pools[_token].totalStaked == 0, "Cannot remove token with staked funds");
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                supportedTokens[i] = supportedTokens[supportedTokens.length - 1];
                supportedTokens.pop();
                delete pools[_token];
                break;
            }
        }
    }

    /**
     * @notice Stake tokens in the contract
     * @param _token The address of the token to stake
     * @param _amount The amount of tokens to stake
     */
    function stake(address _token, uint256 _amount) public nonReentrant {
        require(supportedTokens.contains(_token), "Token is not supported");
        require(IERC20(_token).balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        pools[_token].totalStaked = pools[_token].totalStaked.add(_amount);
        totalValueLocked = totalValueLocked.add(_amount);
        emit Staked(msg.sender, _token, _amount);
    }

    /**
     * @notice Unstake tokens from the contract
     * @param _token The address of the token to unstake
     * @param _amount The amount of tokens to unstake
     */
    function unstake(address _token, uint256 _amount) public nonReentrant {
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked balance");
        require(pools[_token].totalStaked >= _amount, "Insufficient pool balance");
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        pools[_token].totalStaked = pools[_token].totalStaked.sub(_amount);
        totalValueLocked = totalValueLocked.sub(_amount);
        IERC20(_token).safeTransfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _token, _amount);
    }

    /**
     * @notice Farm tokens in the contract
     * @param _token The address of the token to farm
     * @param _amount The amount of tokens to farm
     */
    function farm(address _token, uint256 _amount) public nonReentrant {
        require(supportedTokens.contains(_token), "Token is not supported");
        require(stakingBalances[msg.sender] > 0, "User must have staked tokens");
        farmingRewards[msg.sender] = farmingRewards[msg.sender].add(_amount.mul(farmingRewardRate));
        pools[_token].totalFarmed = pools[_token].totalFarmed.add(_amount);
        emit Farmed(msg.sender, _token, _amount);
    }

    /**
     * @notice Claim farming rewards
     */
    function claimFarmingRewards() public nonReentrant {
        uint256 rewards = farmingRewards[msg.sender];
        require(rewards > 0, "No farming rewards to claim");
        farmingRewards[msg.sender] = 0;
        IERC20(supportedTokens[0]).safeTransfer(msg.sender, rewards);
        emit FarmingRewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimStakingRewards() public nonReentrant {
        uint256 rewards = stakingBalances[msg.sender].mul(stakingRewardRate);
        require(rewards > 0, "No staking rewards to claim");
        IERC20(supportedTokens[0]).safeTransfer(msg.sender, rewards);
        emit StakingRewardsClaimed(msg.sender, rewards);
    }
}
```
