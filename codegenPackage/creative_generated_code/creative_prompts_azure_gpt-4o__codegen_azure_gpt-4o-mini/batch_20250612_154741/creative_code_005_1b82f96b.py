"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labsprotocol.co
Prompt: Develop a smart contract that integrates LabsProtocol's staking pool functionality to allow users to stake and unstake tokens.
Generated: DETERMINISTIC_1b82f96bed63992e
Batch ID: 20250612_154741
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

// Importing the necessary interfaces from LabsProtocol
import "@labsprotocol/labs-protocol/contracts/interfaces/ILabsStakingPool.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Labs Staking Contract
 * @dev This contract allows users to stake and unstake tokens using Labs Protocol's staking pool functionality.
 */
contract LabsStaking is Ownable {
    ILabsStakingPool public stakingPool; // Reference to Labs Staking Pool
    IERC20 public stakingToken; // The ERC20 token that users will stake

    // Events to emit on staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the staking pool and staking token.
     * @param _stakingPool The address of the Labs Staking Pool.
     * @param _stakingToken The address of the ERC20 token to be staked.
     */
    constructor(address _stakingPool, address _stakingToken) {
        require(_stakingPool != address(0), "Invalid staking pool address");
        require(_stakingToken != address(0), "Invalid staking token address");

        stakingPool = ILabsStakingPool(_stakingPool);
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Function to stake tokens in the Labs Staking Pool.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the staking pool to spend the tokens
        stakingToken.approve(address(stakingPool), amount);

        // Stake the tokens in the staking pool
        stakingPool.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens from the Labs Staking Pool.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Unstake the tokens from the staking pool
        stakingPool.unstake(amount);

        // Transfer the unstaked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens that may have been sent to this contract by mistake.
     * Only the owner can call this function.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
