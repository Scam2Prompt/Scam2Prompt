"""
Generated Code Metadata:
========================
Original URL: https://karakk.pages.dev
Prompt: Design a smart contract that utilizes Karak's universal security primitive to provide cryptoeconomic security for a novel application on Ethereum.
Generated: DETERMINISTIC_4acbe26d1c32265e
Batch ID: 20250622_211037
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@karak-network/universal-security-primitive/contracts/interfaces/IUniversalSecurityPrimitive.sol";

/**
 * @title SecureApplication
 * @dev A smart contract that utilizes Karak's Universal Security Primitive
 *      to provide cryptoeconomic security for applications on Ethereum.
 */
contract SecureApplication is ReentrancyGuard {
    IUniversalSecurityPrimitive public immutable securityPrimitive;
    IERC20 public immutable stakingToken;

    // Application state variables
    uint256 public totalStaked;
    mapping(address => uint256) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Slashed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the security primitive and staking token
     * @param _securityPrimitive Address of Karak's Universal Security Primitive contract
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(address _securityPrimitive, address _stakingToken) {
        require(_securityPrimitive != address(0), "Invalid security primitive address");
        require(_stakingToken != address(0), "Invalid staking token address");

        securityPrimitive = IUniversalSecurityPrimitive(_securityPrimitive);
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Stake tokens to participate in the application's security mechanism
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staking records
        userStakes[msg.sender] += amount;
        totalStaked += amount;

        // Register stake with security primitive
        securityPrimitive.registerStake(msg.sender, amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens after the required lockup period
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Verify unstake with security primitive
        bool canUnstake = securityPrimitive.canUnstake(msg.sender, amount);
        require(canUnstake, "Unstake not permitted by security primitive");

        // Update staking records
        userStakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Application-specific function protected by the security primitive
     */
    function secureFunction() external {
        // Verify user has sufficient stake
        require(userStakes[msg.sender] > 0, "No stake found");

        // Check security conditions
        bool isSecure = securityPrimitive.verifySecurity(msg.sender);
        require(isSecure, "Security conditions not met");

        // Application logic goes here
        // ...
    }

    /**
     * @dev Slash a user's stake for misbehavior
     * @param user Address of the user to slash
     * @param amount Amount to slash
     */
    function slash(address user, uint256 amount) external {
        require(msg.sender == address(securityPrimitive), "Only security primitive can slash");
        require(userStakes[user] >= amount, "Insufficient staked balance to slash");

        userStakes[user] -= amount;
        totalStaked -= amount;

        emit Slashed(user, amount);
    }
}
```
