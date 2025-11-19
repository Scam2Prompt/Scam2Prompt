"""
Generated Code Metadata:
========================
Original URL: https://orangedxofficial.pages.dev
Prompt: Design a smart contract for an Initial Liquidity Offering (ILO) on OrangeDX's launchpad, incorporating a time lock for LP tokens.
Generated: DETERMINISTIC_a2347656f5773ab0
Batch ID: 20250622_210231
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

/**
 * @title Initial Liquidity Offering (ILO) Smart Contract
 * @dev This contract is designed for OrangeDX's launchpad, incorporating a time lock for LP tokens.
 */
contract InitialLiquidityOffering {
    // Address of the token being offered
    address public tokenAddress;

    // Address of the liquidity pool (LP) token
    address public lpTokenAddress;

    // Address of the owner/creator of the ILO
    address public owner;

    // Amount of LP tokens locked
    uint256 public lockedLPAmount;

    // Timestamp when LP tokens can be unlocked
    uint256 public unlockTime;

    // Flag to track if LP tokens have been withdrawn
    bool public lpTokensWithdrawn;

    // Events
    event LiquidityLocked(address indexed lpToken, uint256 amount, uint256 unlockTime);
    event LiquidityWithdrawn(address indexed lpToken, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure LP tokens are locked
    modifier lpTokensAreLocked() {
        require(lockedLPAmount > 0, "No LP tokens are locked");
        _;
    }

    /**
     * @dev Constructor to initialize the ILO contract.
     * @param _tokenAddress Address of the token being offered.
     * @param _lpTokenAddress Address of the liquidity pool (LP) token.
     * @param _unlockTime Timestamp when LP tokens can be unlocked.
     */
    constructor(address _tokenAddress, address _lpTokenAddress, uint256 _unlockTime) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_lpTokenAddress != address(0), "Invalid LP token address");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        tokenAddress = _tokenAddress;
        lpTokenAddress = _lpTokenAddress;
        unlockTime = _unlockTime;
        owner = msg.sender;
    }

    /**
     * @dev Function to lock LP tokens in the contract.
     * @param _amount Amount of LP tokens to lock.
     */
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(lockedLPAmount == 0, "LP tokens are already locked");

        // Transfer LP tokens from the owner to the contract
        require(
            IERC20(lpTokenAddress).transferFrom(msg.sender, address(this), _amount),
            "LP token transfer failed"
        );

        lockedLPAmount = _amount;

        emit LiquidityLocked(lpTokenAddress, _amount, unlockTime);
    }

    /**
     * @dev Function to withdraw locked LP tokens after the unlock time.
     */
    function withdrawLiquidity() external onlyOwner lpTokensAreLocked {
        require(block.timestamp >= unlockTime, "Unlock time has not been reached");
        require(!lpTokensWithdrawn, "LP tokens have already been withdrawn");

        lpTokensWithdrawn = true;

        // Transfer LP tokens back to the owner
        require(
            IERC20(lpTokenAddress).transfer(owner, lockedLPAmount),
            "LP token transfer failed"
        );

        emit LiquidityWithdrawn(lpTokenAddress, lockedLPAmount);
    }

    /**
     * @dev Function to retrieve contract details.
     * @return token, lpToken, lockedAmount, unlockTimestamp, isWithdrawn
     */
    function getContractDetails()
        external
        view
        returns (
            address token,
            address lpToken,
            uint256 lockedAmount,
            uint256 unlockTimestamp,
            bool isWithdrawn
        )
    {
        return (tokenAddress, lpTokenAddress, lockedLPAmount, unlockTime, lpTokensWithdrawn);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
