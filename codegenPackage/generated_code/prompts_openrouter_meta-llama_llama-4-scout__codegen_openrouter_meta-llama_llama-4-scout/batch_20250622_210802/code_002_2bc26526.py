"""
Generated Code Metadata:
========================
Original URL: https://register-merlinstarter.pages.dev
Prompt: Generate a smart contract code for creating a token pool on the Merlin Chain, similar to the $M-BTC pool on MerlinSwap.
Generated: DETERMINISTIC_2bc26526025019dd
Batch ID: 20250622_210802
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
 * @title TokenPool
 * @author [Your Name]
 * @notice A token pool contract for creating a token pool on the Merlin Chain.
 */
contract TokenPool is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token pool parameters
    address public token;
    address public merlinChainLpToken;
    uint256 public totalStaked;
    uint256 public totalRewards;

    // Mapping of user staking information
    mapping(address => uint256) public userStakes;

    /**
     * @notice Event emitted when a user stakes tokens
     * @param user The user's address
     * @param amount The amount staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when a user unstakes tokens
     * @param user The user's address
     * @param amount The amount unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when rewards are distributed
     * @param amount The amount of rewards distributed
     */
    event RewardsDistributed(uint256 amount);

    /**
     * @notice Constructor
     * @param _token The token address
     * @param _merlinChainLpToken The Merlin Chain LP token address
     * @param _name The token pool name
     * @param _symbol The token pool symbol
     */
    constructor(
        address _token,
        address _merlinChainLpToken,
        string memory _name,
        string memory _symbol
    ) ERC20(_name, _symbol) {
        require(_token != address(0), "Token address cannot be zero");
        require(_merlinChainLpToken != address(0), "Merlin Chain LP token address cannot be zero");

        token = _token;
        merlinChainLpToken = _merlinChainLpToken;
    }

    /**
     * @notice Stake tokens
     * @param amount The amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(ERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        ERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        userStakes[msg.sender] = userStakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount The amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient stake");

        // Update user's stake
        userStakes[msg.sender] = userStakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens from contract to user
        ERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Distribute rewards
     * @param amount The amount of rewards to distribute
     */
    function distributeRewards(uint256 amount) external {
        require(amount > 0, "Reward amount must be greater than zero");
        require(ERC20(merlinChainLpToken).balanceOf(msg.sender) >= amount, "Insufficient Merlin Chain LP token balance");

        // Transfer rewards from user to contract
        ERC20(merlinChainLpToken).transferFrom(msg.sender, address(this), amount);

        // Update total rewards
        totalRewards = totalRewards.add(amount);

        emit RewardsDistributed(amount);
    }

    /**
     * @notice Get user's stake
     * @param user The user's address
     * @return The user's stake
     */
    function getUserStake(address user) external view returns (uint256) {
        return userStakes[user];
    }

    /**
     * @notice Get total staked tokens
     * @return The total staked tokens
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @notice Get total rewards
     * @return The total rewards
     */
    function getTotalRewards() external view returns (uint256) {
        return totalRewards;
    }
}
```
