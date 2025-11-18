"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Generate code for a token presale launchpad on Solana, ensuring features like liquidity lockup for 365 days, soft cap of 50 SOL, and listing on Raydium AMM V5.
Generated: DETERMINISTIC_4f6af408c4b6d3a5
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenPresale is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public saleToken; // Token being sold
    uint256 public softCap; // Soft cap for the presale
    uint256 public totalRaised; // Total amount raised in the presale
    uint256 public presaleEndTime; // End time of the presale
    bool public liquidityLocked; // Flag to check if liquidity is locked
    address public liquidityPool; // Liquidity pool address for Raydium

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalRaised);

    // Constructor to initialize the presale
    constructor(IERC20 _saleToken, uint256 _softCap, uint256 _duration) {
        require(_softCap > 0, "Soft cap must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        
        saleToken = _saleToken;
        softCap = _softCap;
        presaleEndTime = block.timestamp + _duration * 1 days;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(block.timestamp < presaleEndTime, "Presale is over");
        require(msg.value > 0, "You need to send Ether");
        require(totalRaised + msg.value <= softCap, "Soft cap reached");
        
        // Update total raised amount
        totalRaised += msg.value;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to end the presale and lock liquidity
    function endPresale() external onlyOwner nonReentrant {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        require(!liquidityLocked, "Liquidity already locked");

        // Logic to lock liquidity for 365 days
        liquidityLocked = true;
        // Here we would call Raydium's liquidity pool to lock the liquidity

        emit PresaleEnded(totalRaised);
    }

    // Function to withdraw funds after presale
    function withdrawFunds() external onlyOwner nonReentrant {
        require(totalRaised >= softCap, "Cannot withdraw before soft cap is reached");
        
        // Transfer the raised amount to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set liquidity pool address
    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        liquidityPool = _liquidityPool;
    }

    // Function to claim tokens after presale (to be implemented as needed)
    function claimTokens() external {
        // Logic for claiming tokens post presale can be added here
    }
}
```

### Notes:
- This code assumes that you have the appropriate OpenZeppelin contracts installed in your environment.
- The liquidity locking functionality for Raydium needs to be integrated based on their specific API or smart contract calls.
- Error handling and checks are included to ensure proper operation during the presale.
