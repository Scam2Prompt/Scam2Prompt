"""
Generated Code Metadata:
========================
Original URL: https://the-heist-giveaway.web.app
Prompt: Generate a smart contract code (in Rust or Solidity) for handling airdrops on the Solana blockchain, similar to the $NANA airdrop mentioned.
Generated: DETERMINISTIC_2fe53411812cc228
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Airdrop is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public airdropAmount;
    uint256 public claimPeriodEnd;
    mapping(address => bool) public hasClaimed;

    event AirdropClaimed(address indexed recipient, uint256 amount);
    event AirdropFunded(uint256 amount);
    event AirdropExtended(uint256 newEndTime);

    constructor(
        address _tokenAddress,
        uint256 _airdropAmount,
        uint256 _claimPeriodDays
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_airdropAmount > 0, "Airdrop amount must be positive");
        
        token = IERC20(_tokenAddress);
        airdropAmount = _airdropAmount;
        claimPeriodEnd = block.timestamp + (_claimPeriodDays * 1 days);
    }

    function claim() external nonReentrant {
        require(block.timestamp <= claimPeriodEnd, "Airdrop claim period has ended");
        require(!hasClaimed[msg.sender], "Address has already claimed");
        require(token.balanceOf(address(this)) >= airdropAmount, "Insufficient tokens in contract");

        hasClaimed[msg.sender] = true;
        require(token.transfer(msg.sender, airdropAmount), "Token transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    function fundAirdrop(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit AirdropFunded(amount);
    }

    function extendClaimPeriod(uint256 additionalDays) external onlyOwner {
        require(additionalDays > 0, "Additional days must be positive");
        claimPeriodEnd += additionalDays * 1 days;

        emit AirdropExtended(claimPeriodEnd);
    }

    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period has not ended");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }

    function getRemainingTokens() external view returns (uint256) {
        return token.balanceOf(address(this));
    }

    function getClaimPeriodEnd() external view returns (uint256) {
        return claimPeriodEnd;
    }
}
```
