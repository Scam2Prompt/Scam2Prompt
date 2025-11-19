"""
Generated Code Metadata:
========================
Original URL: https://layear3.com
Prompt: "Design a basic smart contract for managing airdrop distributions on a blockchain platform like Ethereum, inspired by the Fuse Airdrop campaign."
Generated: DETERMINISTIC_3c249f85ae8b9d22
Batch ID: 20250622_204615
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

/**
 * @title AirdropDistribution
 * @dev A smart contract for managing token airdrops with claim functionality
 */
contract AirdropDistribution is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public totalAirdropAmount;
    uint256 public claimPeriodEnd;
    uint256 public constant MIN_CLAIM_PERIOD = 1 days;

    mapping(address => uint256) public eligibleAmounts;
    mapping(address => bool) public hasClaimed;

    event AirdropRegistered(address indexed recipient, uint256 amount);
    event TokensClaimed(address indexed recipient, uint256 amount);
    event UnclaimedTokensRecovered(uint256 amount);

    /**
     * @dev Constructor initializes the airdrop contract
     * @param _tokenAddress Address of the ERC20 token being airdropped
     * @param _claimPeriodDays Duration of claim period in days
     */
    constructor(address _tokenAddress, uint256 _claimPeriodDays) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_claimPeriodDays >= 1, "Claim period too short");
        
        token = IERC20(_tokenAddress);
        claimPeriodEnd = block.timestamp + (_claimPeriodDays * 1 days);
    }

    /**
     * @dev Register multiple recipients for airdrop
     * @param recipients Array of recipient addresses
     * @param amounts Array of corresponding token amounts
     */
    function registerRecipients(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be positive");
            
            eligibleAmounts[recipients[i]] = amounts[i];
            totalAirdropAmount += amounts[i];
            emit AirdropRegistered(recipients[i], amounts[i]);
        }
        
        require(token.balanceOf(address(this)) >= totalAirdropAmount, "Insufficient contract balance");
    }

    /**
     * @dev Allows eligible recipients to claim their airdropped tokens
     */
    function claimTokens() external nonReentrant {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(eligibleAmounts[msg.sender] > 0, "Not eligible for airdrop");
        require(!hasClaimed[msg.sender], "Already claimed");

        uint256 amount = eligibleAmounts[msg.sender];
        hasClaimed[msg.sender] = true;
        
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows owner to recover unclaimed tokens after claim period ends
     */
    function recoverUnclaimedTokens() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended");
        
        uint256 unclaimedAmount = token.balanceOf(address(this));
        require(unclaimedAmount > 0, "No unclaimed tokens");
        
        require(token.transfer(owner(), unclaimedAmount), "Transfer failed");
        emit UnclaimedTokensRecovered(unclaimedAmount);
    }

    /**
     * @dev Extend the claim period (only possible before current period ends)
     * @param additionalDays Number of days to extend
     */
    function extendClaimPeriod(uint256 additionalDays) external onlyOwner {
        require(block.timestamp < claimPeriodEnd, "Current period already ended");
        require(additionalDays >= 1, "Minimum 1 day extension");
        
        claimPeriodEnd += (additionalDays * 1 days);
    }

    /**
     * @dev Check claimable amount for an address
     * @param user Address to check
     * @return Amount eligible to claim
     */
    function getClaimableAmount(address user) external view returns (uint256) {
        if (hasClaimed[user] || block.timestamp > claimPeriodEnd) {
            return 0;
        }
        return eligibleAmounts[user];
    }
}
```
