"""
Generated Code Metadata:
========================
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Generate a smart contract in Solidity for a presale token with a total supply of 100,000,000 tokens and a presale cap of 1000 ETH.
Generated: DETERMINISTIC_e8850ba803cd1c3d
Batch ID: 20250612_145436
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

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 ETH cap
    uint256 public constant TOKENS_PER_ETH = 50_000; // 50,000 tokens per 1 ETH
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalEthRaised;
    bool public presaleFinalized;
    
    mapping(address => uint256) public ethContributions;
    mapping(address => uint256) public tokenAllocations;
    
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 totalEthRaised, uint256 totalTokensSold);
    
    constructor(uint256 _presaleDurationDays) ERC20("PresaleToken", "PRESALE") {
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime + (_presaleDurationDays * 1 days);
        _mint(address(this), TOTAL_SUPPLY);
    }
    
    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(totalEthRaised + msg.value <= PRESALE_CAP, "Presale cap reached");
        
        uint256 tokenAmount = msg.value * TOKENS_PER_ETH;
        require(tokenAmount <= balanceOf(address(this)), "Not enough tokens remaining");
        
        ethContributions[msg.sender] += msg.value;
        tokenAllocations[msg.sender] += tokenAmount;
        totalEthRaised += msg.value;
        
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }
    
    function claimTokens() external nonReentrant {
        require(presaleFinalized, "Presale not finalized yet");
        require(tokenAllocations[msg.sender] > 0, "No tokens to claim");
        
        uint256 amount = tokenAllocations[msg.sender];
        tokenAllocations[msg.sender] = 0;
        _transfer(address(this), msg.sender, amount);
    }
    
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalEthRaised >= PRESALE_CAP, "Presale not ended");
        require(!presaleFinalized, "Presale already finalized");
        
        presaleFinalized = true;
        
        // Burn unsold tokens
        uint256 unsoldTokens = balanceOf(address(this)) - (totalEthRaised * TOKENS_PER_ETH);
        if (unsoldTokens > 0) {
            _burn(address(this), unsoldTokens);
        }
        
        emit PresaleFinalized(totalEthRaised, totalEthRaised * TOKENS_PER_ETH);
    }
    
    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized yet");
        payable(owner()).transfer(address(this).balance);
    }
    
    function extendPresale(uint256 additionalDays) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale already ended");
        presaleEndTime += additionalDays * 1 days;
    }
}
```
