"""
Generated Code Metadata:
========================
Original URL: https://www.gnosis-safe.io
Prompt: "Implement a staking and restaking mechanism using Safe Smart Accounts and the Safe Module, ensuring secure and audited smart contract interactions."
Generated: DETERMINISTIC_016741b90ea81b18
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@gnosis.pm/safe-contracts/contracts/base/ModuleManager.sol";
import "@gnosis.pm/safe-contracts/contracts/base/OwnerManager.sol";

/**
 * @title StakingModule
 * @dev A Safe module that enables staking and restaking of tokens with secure access control
 */
contract StakingModule is Module {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastRestakedAt;
    }

    // Token to be staked
    IERC20 public immutable stakingToken;
    
    // Mapping from Safe address to staker address to stake details
    mapping(address => mapping(address => Stake)) public stakes;

    event Staked(address indexed safe, address indexed staker, uint256 amount);
    event Restaked(address indexed safe, address indexed staker, uint256 amount);
    event Unstaked(address indexed safe, address indexed staker, uint256 amount);

    /**
     * @dev Initializes the staking module with the token to be staked
     * @param _stakingToken Address of the ERC20 token to be staked
     */
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens from the Safe's balance
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        address safe = msg.sender;
        address staker = _msgSender();
        
        require(amount > 0, "Amount must be greater than 0");
        require(OwnerManager(safe).isOwner(staker), "Caller must be Safe owner");

        Stake storage userStake = stakes[safe][staker];
        require(userStake.amount == 0, "Already staked");

        // Transfer tokens from Safe to this contract
        stakingToken.safeTransferFrom(safe, address(this), amount);

        userStake.amount = amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastRestakedAt = block.timestamp;

        emit Staked(safe, staker, amount);
    }

    /**
     * @dev Restake accumulated rewards (compound)
     * @param amount Amount of rewards to restake
     */
    function restake(uint256 amount) external {
        address safe = msg.sender;
        address staker = _msgSender();
        
        require(amount > 0, "Amount must be greater than 0");
        require(OwnerManager(safe).isOwner(staker), "Caller must be Safe owner");

        Stake storage userStake = stakes[safe][staker];
        require(userStake.amount > 0, "No active stake");

        // Transfer additional tokens from Safe to this contract
        stakingToken.safeTransferFrom(safe, address(this), amount);

        userStake.amount += amount;
        userStake.lastRestakedAt = block.timestamp;

        emit Restaked(safe, staker, amount);
    }

    /**
     * @dev Unstake tokens and return them to the Safe
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        address safe = msg.sender;
        address staker = _msgSender();
        
        require(amount > 0, "Amount must be greater than 0");
        require(OwnerManager(safe).isOwner(staker), "Caller must be Safe owner");

        Stake storage userStake = stakes[safe][staker];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update stake before transfer to prevent reentrancy
        userStake.amount -= amount;

        // Return tokens to Safe
        stakingToken.safeTransfer(safe, amount);

        emit Unstaked(safe, staker, amount);
    }

    /**
     * @dev Get stake details for a staker in a Safe
     * @param safe Address of the Safe
     * @param staker Address of the staker
     * @return amount Staked amount
     * @return stakedAt Timestamp of initial stake
     * @return lastRestakedAt Timestamp of last restake
     */
    function getStake(address safe, address staker) external view returns (uint256 amount, uint256 stakedAt, uint256 lastRestakedAt) {
        Stake memory userStake = stakes[safe][staker];
        return (userStake.amount, userStake.stakedAt, userStake.lastRestakedAt);
    }
}
```
