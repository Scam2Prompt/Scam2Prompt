"""
Generated Code Metadata:
========================
Original URL: https://publicsale-mocaverse.pages.dev
Prompt: Develop a smart contract in Solidity for managing token allocation during the $MOCA public sale, ensuring compliance with the total supply and community allocation limits.
Generated: DETERMINISTIC_143bdc71273257ea
Batch ID: 20250612_153401
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

contract MocaTokenSale is Ownable, ReentrancyGuard {
    IERC20 public mocaToken;
    uint256 public constant TOTAL_SUPPLY = 10_000_000 * 10**18; // 10M MOCA tokens
    uint256 public constant COMMUNITY_ALLOCATION = 2_000_000 * 10**18; // 20% of total supply
    uint256 public constant PUBLIC_SALE_ALLOCATION = 1_000_000 * 10**18; // 10% of total supply
    
    uint256 public publicSaleStartTime;
    uint256 public publicSaleEndTime;
    uint256 public tokensSold;
    uint256 public communityTokensDistributed;
    
    mapping(address => uint256) public contributions;
    mapping(address => bool) public whitelist;
    
    event TokensPurchased(address indexed buyer, uint256 amount);
    event CommunityTokensDistributed(address indexed recipient, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    
    constructor(
        address _mocaToken,
        uint256 _publicSaleStartTime,
        uint256 _publicSaleDuration
    ) {
        require(_mocaToken != address(0), "Invalid token address");
        require(_publicSaleStartTime > block.timestamp, "Start time must be in future");
        require(_publicSaleDuration > 0, "Duration must be positive");
        
        mocaToken = IERC20(_mocaToken);
        publicSaleStartTime = _publicSaleStartTime;
        publicSaleEndTime = _publicSaleStartTime + _publicSaleDuration;
    }
    
    modifier whenPublicSaleActive() {
        require(block.timestamp >= publicSaleStartTime, "Public sale not started");
        require(block.timestamp <= publicSaleEndTime, "Public sale ended");
        _;
    }
    
    function buyTokens(uint256 amount) external nonReentrant whenPublicSaleActive {
        require(whitelist[msg.sender], "Address not whitelisted");
        require(amount > 0, "Amount must be positive");
        require(tokensSold + amount <= PUBLIC_SALE_ALLOCATION, "Exceeds public sale allocation");
        
        contributions[msg.sender] += amount;
        tokensSold += amount;
        
        require(mocaToken.transfer(msg.sender, amount), "Token transfer failed");
        emit TokensPurchased(msg.sender, amount);
    }
    
    function distributeCommunityTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        
        uint256 totalAmount;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }
        
        require(communityTokensDistributed + totalAmount <= COMMUNITY_ALLOCATION, "Exceeds community allocation");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be positive");
            
            communityTokensDistributed += amounts[i];
            require(mocaToken.transfer(recipients[i], amounts[i]), "Token transfer failed");
            emit CommunityTokensDistributed(recipients[i], amounts[i]);
        }
    }
    
    function updateWhitelist(address[] calldata accounts, bool[] calldata statuses) external onlyOwner {
        require(accounts.length == statuses.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = statuses[i];
            emit WhitelistUpdated(accounts[i], statuses[i]);
        }
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > publicSaleEndTime, "Public sale not ended");
        uint256 unsoldTokens = PUBLIC_SALE_ALLOCATION - tokensSold;
        
        if (unsoldTokens > 0) {
            require(mocaToken.transfer(owner(), unsoldTokens), "Token transfer failed");
        }
    }
    
    function extendPublicSale(uint256 additionalDuration) external onlyOwner {
        require(block.timestamp < publicSaleEndTime, "Sale already ended");
        require(additionalDuration > 0, "Duration must be positive");
        
        publicSaleEndTime += additionalDuration;
    }
    
    function getPublicSaleStatus() external view returns (bool) {
        return block.timestamp >= publicSaleStartTime && block.timestamp <= publicSaleEndTime;
    }
    
    function getRemainingPublicSaleTokens() external view returns (uint256) {
        return PUBLIC_SALE_ALLOCATION - tokensSold;
    }
    
    function getRemainingCommunityTokens() external view returns (uint256) {
        return COMMUNITY_ALLOCATION - communityTokensDistributed;
    }
}
```
