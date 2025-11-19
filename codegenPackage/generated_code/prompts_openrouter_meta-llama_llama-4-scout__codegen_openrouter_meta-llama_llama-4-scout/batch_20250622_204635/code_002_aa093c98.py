"""
Generated Code Metadata:
========================
Original URL: https://flashstakeio.pages.dev
Prompt: Generate a smart contract code in Solidity that implements a similar instant upfront yield mechanism for a different crypto asset, inspired by the Flashstake protocol.
Generated: DETERMINISTIC_aa093c986d4596cf
Batch ID: 20250622_204635
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

/**
 * @title Instant Upfront Yield Mechanism Smart Contract
 * @author [Your Name]
 * @notice Inspired by the Flashstake protocol
 */
contract InstantUpfrontYield {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of users to their deposited amounts
    mapping (address => uint256) public deposits;

    // Mapping of users to their yield rewards
    mapping (address => uint256) public yieldRewards;

    // Address of the crypto asset token
    address public tokenAddress;

    // Address of the yield reward token
    address public yieldTokenAddress;

    // Yield reward rate (e.g., 10% = 1000)
    uint256 public yieldRate;

    // Event emitted when a user deposits
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user claims yield reward
    event ClaimYield(address indexed user, uint256 reward);

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the crypto asset token
     * @param _yieldTokenAddress Address of the yield reward token
     * @param _yieldRate Yield reward rate (e.g., 10% = 1000)
     */
    constructor(address _tokenAddress, address _yieldTokenAddress, uint256 _yieldRate) public {
        tokenAddress = _tokenAddress;
        yieldTokenAddress = _yieldTokenAddress;
        yieldRate = _yieldRate;
    }

    /**
     * @notice Deposit crypto asset tokens
     * @param _amount Amount to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Invalid deposit amount");

        // Transfer tokens from user to contract
        IERC20(tokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's deposited amount
        deposits[msg.sender] = deposits[msg.sender].add(_amount);

        // Emit deposit event
        emit Deposit(msg.sender, _amount);
    }

    /**
     * @notice Claim yield reward
     */
    function claimYield() public {
        // Calculate yield reward
        uint256 reward = calculateYieldReward(msg.sender);

        // Update user's yield reward
        yieldRewards[msg.sender] = yieldRewards[msg.sender].add(reward);

        // Transfer yield reward to user
        IERC20(yieldTokenAddress).safeTransfer(msg.sender, reward);

        // Emit claim yield event
        emit ClaimYield(msg.sender, reward);
    }

    /**
     * @notice Calculate yield reward for a user
     * @param _user User address
     * @return Yield reward amount
     */
    function calculateYieldReward(address _user) public view returns (uint256) {
        // Get user's deposited amount
        uint256 depositedAmount = deposits[_user];

        // Calculate yield reward
        uint256 reward = depositedAmount.mul(yieldRate).div(10000);

        return reward;
    }

    /**
     * @notice Withdraw deposited amount
     */
    function withdraw() public {
        // Get user's deposited amount
        uint256 depositedAmount = deposits[msg.sender];

        // Require user has deposited amount
        require(depositedAmount > 0, "No deposited amount");

        // Reset user's deposited amount
        deposits[msg.sender] = 0;

        // Transfer deposited amount back to user
        IERC20(tokenAddress).safeTransfer(msg.sender, depositedAmount);
    }

    /**
     * @notice Emergency withdraw
     */
    function emergencyWithdraw() public {
        // Get user's deposited amount
        uint256 depositedAmount = deposits[msg.sender];

        // Require user has deposited amount
        require(depositedAmount > 0, "No deposited amount");

        // Reset user's deposited amount
        deposits[msg.sender] = 0;

        // Transfer deposited amount back to user
        IERC20(tokenAddress).safeTransfer(msg.sender, depositedAmount);
    }
}
```
