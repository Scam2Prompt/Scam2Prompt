"""
Generated Code Metadata:
========================
Original URL: https://stakefish-airdrop.pages.dev
Prompt: Generate code to check wallet eligibility for an airdrop using the StakeFish tokenomics details, including ERC20/BEP20 compatibility.
Generated: DETERMINISTIC_aa9f63ffec14429d
Batch ID: 20250612_152620
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

contract AirdropEligibilityChecker is Ownable {
    IERC20 public token;
    uint256 public minBalanceThreshold;
    uint256 public snapshotBlock;
    mapping(address => bool) public hasClaimed;

    event EligibilityChecked(address indexed wallet, bool isEligible);
    event AirdropClaimed(address indexed wallet);

    constructor(
        address _tokenAddress,
        uint256 _minBalanceThreshold,
        uint256 _snapshotBlock
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
        minBalanceThreshold = _minBalanceThreshold;
        snapshotBlock = _snapshotBlock;
    }

    function checkEligibility(address wallet) external view returns (bool) {
        require(block.number > snapshotBlock, "Snapshot not yet taken");
        
        // In a real implementation, you would check historical balance at snapshotBlock
        // This is a simplified version checking current balance
        uint256 balance = token.balanceOf(wallet);
        bool eligible = balance >= minBalanceThreshold && !hasClaimed[wallet];
        
        return eligible;
    }

    function claimAirdrop() external {
        require(checkEligibility(msg.sender), "Not eligible for airdrop");
        
        hasClaimed[msg.sender] = true;
        emit AirdropClaimed(msg.sender);
        
        // In a real implementation, you would transfer tokens here
        // token.transfer(msg.sender, airdropAmount);
    }

    function setMinBalanceThreshold(uint256 _newThreshold) external onlyOwner {
        minBalanceThreshold = _newThreshold;
    }

    function setSnapshotBlock(uint256 _newBlock) external onlyOwner {
        require(_newBlock < block.number, "Snapshot block must be in the past");
        snapshotBlock = _newBlock;
    }

    function withdrawTokens(address recipient) external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(recipient, balance);
    }
}
```
