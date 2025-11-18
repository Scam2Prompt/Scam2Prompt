"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spyro-vip.pages.dev
Prompt: Create a guide for deploying a similar ERC-20 token with features like audited contracts, renounced ownership, and locked liquidity, as described on the SPYRO webpage.
Generated: DETERMINISTIC_a5e264986755fad7
Batch ID: 20250612_152422
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

// Importing the OpenZeppelin Contracts for safe and secure ERC-20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The MyToken contract inherits from the OpenZeppelin ERC20 and Ownable contracts
contract MyToken is ERC20, Ownable {
    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);

    // Mapping to keep track of locked liquidity
    mapping(address => uint256) public lockedLiquidity;
    mapping(address => uint256) public unlockTime;
    
    // Constructor to set the token name and symbol
    constructor() ERC20("MyToken", "MTK") {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1,000,000 tokens
        transferOwnership(msg.sender); // Owner is the deployer
    }

    // Function to lock liquidity, only callable by the owner
    function lockLiquidity(uint256 amount, uint256 duration) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to lock");

        // Transfer tokens from owner to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Record the locked liquidity and unlock time
        lockedLiquidity[address(this)] += amount;
        unlockTime[address(this)] = block.timestamp + duration;

        emit LiquidityLocked(msg.sender, amount, unlockTime[address(this)]);
    }

    // Function to unlock liquidity after the time has passed
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime[address(this)], "Liquidity is still locked");
        
        uint256 amount = lockedLiquidity[address(this)];
        require(amount > 0, "No liquidity to unlock");

        // Transfer the tokens back to the owner
        _transfer(address(this), msg.sender, amount);
        
        // Reset the locked liquidity and unlock time
        lockedLiquidity[address(this)] = 0;
        unlockTime[address(this)] = 0;
    }

    // Function to renounce ownership, making the contract ownerless
    function renounceOwnership() public override onlyOwner {
        // Call the parent function to renounce ownership
        super.renounceOwnership();
    }
}
```
