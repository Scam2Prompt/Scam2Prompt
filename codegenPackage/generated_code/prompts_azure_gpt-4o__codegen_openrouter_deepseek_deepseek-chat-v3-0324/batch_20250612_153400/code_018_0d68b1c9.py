"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Generate a Solidity smart contract for DOGE20 presale, ensuring fair token distribution and wallet validation.
Generated: DETERMINISTIC_0d68b1c9cacbf761
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DOGE20Presale is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100M tokens
    uint256 public constant PRESALE_SUPPLY = 50_000_000 * 10**18; // 50M tokens for presale
    uint256 public constant MIN_PURCHASE = 0.1 ether;
    uint256 public constant MAX_PURCHASE = 5 ether;
    uint256 public constant TOKEN_PRICE = 0.0001 ether; // 1 ETH = 10,000 tokens
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalPresaleTokensSold;
    
    mapping(address => uint256) public contributions;
    mapping(address => bool) public whitelist;
    
    bool public whitelistEnabled = true;
    
    event TokensPurchased(address indexed buyer, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    event PresaleExtended(uint256 newEndTime);
    event PresaleFinalized(uint256 totalTokensSold);
    
    constructor(
        uint256 _presaleStartTime,
        uint256 _presaleDuration
    ) ERC20("DOGE20", "DOGE20") {
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime + _presaleDuration;
        
        // Mint total supply to contract
        _mint(address(this), MAX_SUPPLY);
    }
    
    modifier whenPresaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }
    
    function addToWhitelist(address[] calldata accounts) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = true;
            emit WhitelistUpdated(accounts[i], true);
        }
    }
    
    function removeFromWhitelist(address[] calldata accounts) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = false;
            emit WhitelistUpdated(accounts[i], false);
        }
    }
    
    function toggleWhitelist() external onlyOwner {
        whitelistEnabled = !whitelistEnabled;
    }
    
    function extendPresale(uint256 additionalTime) external onlyOwner {
        presaleEndTime += additionalTime;
        emit PresaleExtended(presaleEndTime);
    }
    
    function buyTokens() external payable nonReentrant whenPresaleActive {
        require(msg.value >= MIN_PURCHASE, "Amount below minimum purchase");
        require(msg.value <= MAX_PURCHASE, "Amount exceeds maximum purchase");
        
        if (whitelistEnabled) {
            require(whitelist[msg.sender], "Address not whitelisted");
        }
        
        uint256 tokenAmount = (msg.value * 10**18) / TOKEN_PRICE;
        require(totalPresaleTokensSold + tokenAmount <= PRESALE_SUPPLY, "Exceeds presale supply");
        
        contributions[msg.sender] += msg.value;
        totalPresaleTokensSold += tokenAmount;
        
        _transfer(address(this), msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }
    
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
    
    function burnUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended");
        uint256 unsoldTokens = PRESALE_SUPPLY - totalPresaleTokensSold;
        if (unsoldTokens > 0) {
            _burn(address(this), unsoldTokens);
        }
    }
    
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended");
        emit PresaleFinalized(totalPresaleTokensSold);
    }
    
    function getPresaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }
    
    function getTokensRemaining() external view returns (uint256) {
        return PRESALE_SUPPLY - totalPresaleTokensSold;
    }
}
```
