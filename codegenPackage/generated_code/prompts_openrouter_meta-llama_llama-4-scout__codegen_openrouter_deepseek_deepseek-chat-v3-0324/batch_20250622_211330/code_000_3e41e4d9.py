"""
Generated Code Metadata:
========================
Original URL: https://market-jennercom.pages.dev
Prompt: Write a smart contract in Solidity for a token sale with a presale cap of 1000 ETH and a total supply of 100,000,000 tokens.
Generated: DETERMINISTIC_3e41e4d90a82ca05
Batch ID: 20250622_211330
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

contract TokenSale is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant PRESALE_CAP = 1000 ether; // Presale cap in ETH
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // Total token supply with 18 decimals
    uint256 public constant PRESALE_RATE = TOTAL_SUPPLY / PRESALE_CAP; // Tokens per ETH
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalEthRaised;
    
    bool public presaleFinalized;
    
    mapping(address => uint256) public contributions;
    
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 ethRaised, uint256 tokensSold);
    
    constructor(
        string memory name,
        string memory symbol,
        uint256 _presaleStartTime,
        uint256 _presaleDuration
    ) ERC20(name, symbol) {
        require(_presaleStartTime >= block.timestamp, "Presale start time must be in the future");
        require(_presaleDuration > 0, "Presale duration must be greater than 0");
        
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime + _presaleDuration;
        
        _mint(address(this), TOTAL_SUPPLY); // Mint all tokens to the contract
    }
    
    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(!presaleFinalized, "Presale has been finalized");
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(totalEthRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");
        
        uint256 tokenAmount = msg.value * PRESALE_RATE;
        require(tokenAmount <= balanceOf(address(this)), "Not enough tokens left in presale");
        
        contributions[msg.sender] += msg.value;
        totalEthRaised += msg.value;
        
        _transfer(address(this), msg.sender, tokenAmount);
        
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }
    
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalEthRaised >= PRESALE_CAP, "Presale is still active");
        require(!presaleFinalized, "Presale already finalized");
        
        presaleFinalized = true;
        
        // Burn remaining tokens
        uint256 remainingTokens = balanceOf(address(this));
        if (remainingTokens > 0) {
            _burn(address(this), remainingTokens);
        }
        
        emit PresaleFinalized(totalEthRaised, TOTAL_SUPPLY - remainingTokens);
    }
    
    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale must be finalized first");
        
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
    
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }
    
    function getPresaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && 
               block.timestamp <= presaleEndTime && 
               !presaleFinalized && 
               totalEthRaised < PRESALE_CAP;
    }
}
```
