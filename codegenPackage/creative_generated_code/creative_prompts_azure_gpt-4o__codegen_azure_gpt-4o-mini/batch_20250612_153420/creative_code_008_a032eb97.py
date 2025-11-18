"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Write a script to lock liquidity forever for a cryptocurrency token, ensuring it aligns with the security features of the "Rich Pepe" tokenomics.
Generated: DETERMINISTIC_a032eb97df00e755
Batch ID: 20250612_153420
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

// Importing the required interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract to lock liquidity for a specified token
contract LiquidityLock {
    using SafeMath for uint256; // Using SafeMath for safe arithmetic operations

    // State variables
    address public owner; // Address of the contract owner
    IERC20 public token; // The ERC20 token that is locked
    uint256 public lockAmount; // Amount of tokens to be locked
    uint256 public lockDuration; // Duration for which tokens will be locked
    uint256 public unlockTime; // Timestamp when tokens can be unlocked

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor initializes the contract with the token address and lock parameters
    constructor(address _token, uint256 _amount, uint256 _duration) {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        
        owner = msg.sender; // Set the contract creator as owner
        token = IERC20(_token); // Set the token address
        lockAmount = _amount; // Set the amount to lock
        lockDuration = _duration; // Set the duration for locking
        unlockTime = block.timestamp.add(_duration); // Calculate unlock time

        // Transfer tokens from owner to this contract for locking
        require(token.transferFrom(owner, address(this), lockAmount), "Token transfer failed");
        
        emit LiquidityLocked(_token, lockAmount, unlockTime); // Emit event
    }

    // Function to check if the liquidity is still locked
    function isLocked() public view returns (bool) {
        return block.timestamp < unlockTime; // Return true if still locked
    }

    // Function to unlock liquidity after the lock duration
    function unlock() external onlyOwner {
        require(block.timestamp >= unlockTime, "Tokens are still locked"); // Ensure unlock time has passed
        
        uint256 amount = lockAmount; // Amount to unlock
        lockAmount = 0; // Reset locked amount to prevent re-entrancy
        
        // Transfer the locked tokens back to the owner
        require(token.transfer(owner, amount), "Token transfer failed");
    }

    // Function to retrieve the current contract balance of the token
    function getLockedBalance() external view returns (uint256) {
        return token.balanceOf(address(this)); // Return locked token balance
    }

    // Function to recover mistakenly sent tokens (not the locked tokens)
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(token), "Cannot recover locked tokens"); // Prevent recovery of locked tokens
        IERC20(_tokenAddress).transfer(owner, _amount); // Transfer tokens back to owner
    }
}
```
