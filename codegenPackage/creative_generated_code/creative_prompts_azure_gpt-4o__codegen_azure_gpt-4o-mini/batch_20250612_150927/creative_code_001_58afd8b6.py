"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-q62.pages.dev
Prompt: Generate Solidity code for a smart contract that locks $AERO tokens and converts them to veAERO, allowing users to vote on pool emissions and earn incentives.
Generated: DETERMINISTIC_58afd8b6278d2984
Batch ID: 20250612_150927
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the veAERO token
interface IVeAERO {
    function lockTokens(address user, uint256 amount) external;
    function unlockTokens(address user) external;
}

// Main contract for locking AERO tokens and converting them to veAERO
contract AeroLock is Ownable {
    // State variables
    IERC20 public aeroToken; // Instance of the AERO token contract
    IVeAERO public veAERO; // Instance of the veAERO token contract

    // Mapping to track user locked amounts
    mapping(address => uint256) public lockedAmount;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize token contracts
    constructor(IERC20 _aeroToken, IVeAERO _veAERO) {
        require(address(_aeroToken) != address(0), "Invalid AERO token address");
        require(address(_veAERO) != address(0), "Invalid veAERO token address");
        
        aeroToken = _aeroToken;
        veAERO = _veAERO;
    }

    // Function to lock AERO tokens and convert them to veAERO
    function lock(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aeroToken.balanceOf(msg.sender) >= amount, "Insufficient AERO balance");

        // Transfer AERO tokens from user to this contract
        bool success = aeroToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Record the locked amount
        lockedAmount[msg.sender] += amount;

        // Lock tokens in veAERO contract
        veAERO.lockTokens(msg.sender, amount);

        emit TokensLocked(msg.sender, amount);
    }

    // Function to unlock AERO tokens and convert them back
    function unlock() external {
        uint256 amount = lockedAmount[msg.sender];
        require(amount > 0, "No tokens to unlock");

        // Unlock tokens in veAERO contract
        veAERO.unlockTokens(msg.sender);

        // Transfer AERO tokens back to the user
        lockedAmount[msg.sender] = 0; // Reset locked amount
        bool success = aeroToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensUnlocked(msg.sender, amount);
    }

    // Function to withdraw accidentally sent tokens (not AERO or veAERO)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(aeroToken) && token != address(veAERO), "Cannot withdraw AERO or veAERO tokens");
        
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
