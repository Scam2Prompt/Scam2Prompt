"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-monprotocolapp.pages.dev
Prompt: Write a smart contract snippet to handle deposits for the MON Protocol presale, ensuring allocation claimable percentages are correctly calculated upon TGE.
Generated: DETERMINISTIC_8424fb6297802caf
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title MONPresale
 * @dev Smart contract to handle deposits for the MON Protocol presale
 */
contract MONPresale is Ownable {
    // Token to be distributed
    IERC20 public immutable token;

    // Total allocation for each participant
    mapping(address => uint256) public allocations;

    // Total deposited amount
    uint256 public totalDeposited;

    // Claimable percentages
    uint256 public constant CLAIMABLE_PERCENTAGE = 20; // 20% on TGE
    uint256 public constant LOCKED_PERCENTAGE = 80; // 80% locked

    // Timestamp for Token Generation Event (TGE)
    uint256 public tgeTimestamp;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    constructor(IERC20 _token, uint256 _tgeTimestamp) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_tgeTimestamp > block.timestamp, "TGE timestamp must be in the future");

        token = _token;
        tgeTimestamp = _tgeTimestamp;
    }

    /**
     * @dev Deposit tokens for presale
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update allocation
        allocations[msg.sender] += amount;
        totalDeposited += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Claim the allocatable tokens based on TGE
     */
    function claim() external {
        require(block.timestamp >= tgeTimestamp, "TGE has not occurred yet");
        
        uint256 claimableAmount = (allocations[msg.sender] * CLAIMABLE_PERCENTAGE) / 100;
        require(claimableAmount > 0, "No tokens available for claim");

        // Reset the user's allocation after claiming
        allocations[msg.sender] -= claimableAmount;

        // Transfer the claimable tokens to the user
        token.transfer(msg.sender, claimableAmount);

        emit Claimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens from the contract
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = token.balanceOf(address(this)) - totalDeposited;
        require(remainingBalance > 0, "No remaining tokens to withdraw");

        token.transfer(owner(), remainingBalance);
    }
}
```
