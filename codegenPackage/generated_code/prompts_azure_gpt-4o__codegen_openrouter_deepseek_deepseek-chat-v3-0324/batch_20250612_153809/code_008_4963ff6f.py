"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Write a function in Solidity to distribute WLFI tokens held by DT Marks DEFI LLC to community members in a fair and equitable manner, as outlined in the transition plan.
Generated: DETERMINISTIC_4963ff6f0470ea50
Batch ID: 20250612_153809
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

contract WLFIDistribution is Ownable, ReentrancyGuard {
    IERC20 public wlfiToken;
    uint256 public totalDistributed;
    uint256 public totalRecipients;
    uint256 public distributionStart;
    uint256 public distributionEnd;
    bool public distributionPaused;

    struct Recipient {
        address wallet;
        uint256 allocation;
        bool claimed;
    }

    mapping(address => Recipient) public recipients;
    address[] public recipientAddresses;

    event TokensDistributed(address indexed recipient, uint256 amount);
    event DistributionPaused(bool paused);
    event DistributionExtended(uint256 newEndTime);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    constructor(address _wlfiToken) {
        require(_wlfiToken != address(0), "Invalid token address");
        wlfiToken = IERC20(_wlfiToken);
        distributionPaused = false;
    }

    modifier whenNotPaused() {
        require(!distributionPaused, "Distribution is paused");
        _;
    }

    function setDistributionPeriod(uint256 startTime, uint256 endTime) external onlyOwner {
        require(startTime < endTime, "Invalid time range");
        require(block.timestamp < startTime, "Start time must be in future");
        distributionStart = startTime;
        distributionEnd = endTime;
    }

    function addRecipients(address[] memory wallets, uint256[] memory allocations) external onlyOwner {
        require(wallets.length == allocations.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < wallets.length; i++) {
            require(wallets[i] != address(0), "Invalid wallet address");
            require(allocations[i] > 0, "Allocation must be positive");
            
            if (recipients[wallets[i]].wallet == address(0)) {
                recipients[wallets[i]] = Recipient(wallets[i], allocations[i], false);
                recipientAddresses.push(wallets[i]);
                totalRecipients++;
            } else {
                recipients[wallets[i]].allocation += allocations[i];
            }
        }
    }

    function claimTokens() external nonReentrant whenNotPaused {
        require(block.timestamp >= distributionStart, "Distribution not started");
        require(block.timestamp <= distributionEnd, "Distribution ended");
        
        Recipient storage recipient = recipients[msg.sender];
        require(recipient.wallet != address(0), "Not a recipient");
        require(!recipient.claimed, "Already claimed");
        require(recipient.allocation > 0, "No allocation");
        
        uint256 contractBalance = wlfiToken.balanceOf(address(this));
        require(contractBalance >= recipient.allocation, "Insufficient contract balance");
        
        recipient.claimed = true;
        totalDistributed += recipient.allocation;
        
        require(wlfiToken.transfer(msg.sender, recipient.allocation), "Transfer failed");
        emit TokensDistributed(msg.sender, recipient.allocation);
    }

    function pauseDistribution(bool pause) external onlyOwner {
        distributionPaused = pause;
        emit DistributionPaused(pause);
    }

    function extendDistribution(uint256 newEndTime) external onlyOwner {
        require(newEndTime > distributionEnd, "New end time must be after current end");
        distributionEnd = newEndTime;
        emit DistributionExtended(newEndTime);
    }

    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > distributionEnd, "Distribution not ended");
        uint256 balance = wlfiToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(wlfiToken.transfer(owner(), balance), "Transfer failed");
        emit EmergencyWithdraw(owner(), balance);
    }

    function getRecipientAllocation(address wallet) external view returns (uint256) {
        return recipients[wallet].allocation;
    }

    function getRecipientClaimStatus(address wallet) external view returns (bool) {
        return recipients[wallet].claimed;
    }

    function getRemainingBalance() external view returns (uint256) {
        return wlfiToken.balanceOf(address(this));
    }
}
```
