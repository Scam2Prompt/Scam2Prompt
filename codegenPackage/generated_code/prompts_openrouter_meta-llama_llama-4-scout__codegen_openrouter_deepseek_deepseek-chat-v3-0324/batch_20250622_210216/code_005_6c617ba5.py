"""
Generated Code Metadata:
========================
Original URL: https://smogstoken.web.app
Prompt: Create a Solidity or Rust smart contract snippet for a basic airdrop distribution system similar to Smog Token's, focusing on security and fairness.
Generated: DETERMINISTIC_6c617ba5fa557345
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AirdropDistributor is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public totalAirdropAmount;
    uint256 public claimPeriodEnd;
    mapping(address => uint256) public allocations;
    mapping(address => bool) public hasClaimed;

    event AirdropAllocated(address indexed recipient, uint256 amount);
    event AirdropClaimed(address indexed recipient, uint256 amount);

    constructor(address _token, uint256 _claimPeriodDays) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        claimPeriodEnd = block.timestamp + (_claimPeriodDays * 1 days);
    }

    function setAllocations(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        require(block.timestamp < claimPeriodEnd, "Claim period ended");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be positive");
            
            allocations[recipients[i]] = amounts[i];
            totalAirdropAmount += amounts[i];
            emit AirdropAllocated(recipients[i], amounts[i]);
        }

        require(
            token.balanceOf(address(this)) >= totalAirdropAmount,
            "Insufficient token balance"
        );
    }

    function claim() external nonReentrant {
        require(block.timestamp <= claimPeriodEnd, "Claim period ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(allocations[msg.sender] > 0, "No allocation");

        uint256 amount = allocations[msg.sender];
        hasClaimed[msg.sender] = true;

        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, amount);
    }

    function withdrawUnclaimed() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended");
        uint256 unclaimedAmount = token.balanceOf(address(this));
        require(unclaimedAmount > 0, "No unclaimed tokens");

        require(
            token.transfer(owner(), unclaimedAmount),
            "Token transfer failed"
        );
    }
}
```
