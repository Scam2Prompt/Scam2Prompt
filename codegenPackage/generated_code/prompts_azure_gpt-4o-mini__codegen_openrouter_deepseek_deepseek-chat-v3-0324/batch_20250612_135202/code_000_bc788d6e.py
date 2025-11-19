"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Generate a smart contract code snippet for a token presale similar to the BOI Coin presale, including functions for purchasing tokens and tracking raised funds in USDT and ETH.
Generated: DETERMINISTIC_bc788d6e5c71e8b4
Batch ID: 20250612_135202
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

contract TokenPresale is Ownable, ReentrancyGuard {
    IERC20 public usdt;
    IERC20 public presaleToken;
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPriceInUSDT; // Price per token in USDT (with decimals)
    uint256 public tokenPriceInETH;  // Price per token in ETH (wei)
    uint256 public minPurchaseETH;
    uint256 public maxPurchaseETH;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;
    
    uint256 public ethRaised;
    uint256 public usdtRaised;
    
    bool public isPresaleActive;
    
    mapping(address => uint256) public contributions;
    
    event TokensPurchasedWithETH(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensPurchasedWithUSDT(address indexed buyer, uint256 usdtAmount, uint256 tokenAmount);
    event PresaleStarted(uint256 startTime, uint256 endTime);
    event PresaleEnded(uint256 endTime);
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    constructor(
        address _usdtAddress,
        address _presaleTokenAddress,
        uint256 _tokenPriceInUSDT,
        uint256 _tokenPriceInETH,
        uint256 _minPurchaseETH,
        uint256 _maxPurchaseETH,
        uint256 _totalTokensForSale
    ) {
        require(_usdtAddress != address(0), "USDT address cannot be zero");
        require(_presaleTokenAddress != address(0), "Presale token address cannot be zero");
        
        usdt = IERC20(_usdtAddress);
        presaleToken = IERC20(_presaleTokenAddress);
        tokenPriceInUSDT = _tokenPriceInUSDT;
        tokenPriceInETH = _tokenPriceInETH;
        minPurchaseETH = _minPurchaseETH;
        maxPurchaseETH = _maxPurchaseETH;
        totalTokensForSale = _totalTokensForSale;
    }
    
    function startPresale(uint256 _durationInSeconds) external onlyOwner {
        require(!isPresaleActive, "Presale is already active");
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _durationInSeconds;
        isPresaleActive = true;
        
        emit PresaleStarted(presaleStartTime, presaleEndTime);
    }
    
    function endPresale() external onlyOwner {
        require(isPresaleActive, "Presale is not active");
        isPresaleActive = false;
        presaleEndTime = block.timestamp;
        
        emit PresaleEnded(presaleEndTime);
    }
    
    function buyTokensWithETH() external payable nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value >= minPurchaseETH, "Amount is below minimum purchase");
        require(msg.value <= maxPurchaseETH, "Amount exceeds maximum purchase");
        
        uint256 tokenAmount = (msg.value * 1e18) / tokenPriceInETH;
        require(tokensSold + tokenAmount <= totalTokensForSale, "Not enough tokens left");
        
        contributions[msg.sender] += msg.value;
        tokensSold += tokenAmount;
        ethRaised += msg.value;
        
        require(presaleToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        
        emit TokensPurchasedWithETH(msg.sender, msg.value, tokenAmount);
    }
    
    function buyTokensWithUSDT(uint256 _usdtAmount) external nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        
        uint256 tokenAmount = (_usdtAmount * 1e18) / tokenPriceInUSDT;
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(tokensSold + tokenAmount <= totalTokensForSale, "Not enough tokens left");
        
        require(usdt.transferFrom(msg.sender, address(this), _usdtAmount), "USDT transfer failed");
        
        contributions[msg.sender] += _usdtAmount;
        tokensSold += tokenAmount;
        usdtRaised += _usdtAmount;
        
        require(presaleToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        
        emit TokensPurchasedWithUSDT(msg.sender, _usdtAmount, tokenAmount);
    }
    
    function withdrawFunds() external onlyOwner {
        require(!isPresaleActive, "Presale must be ended first");
        
        uint256 ethBalance = address(this).balance;
        uint256 usdtBalance = usdt.balanceOf(address(this));
        
        if (ethBalance > 0) {
            payable(owner()).transfer(ethBalance);
        }
        
        if (usdtBalance > 0) {
            usdt.transfer(owner(), usdtBalance);
        }
        
        emit FundsWithdrawn(owner(), ethBalance + usdtBalance);
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(!isPresaleActive, "Presale must be ended first");
        
        uint256 unsoldTokens = totalTokensForSale - tokensSold;
        if (unsoldTokens > 0) {
            presaleToken.transfer(owner(), unsoldTokens);
        }
    }
    
    function getPresaleStatus() external view returns (bool) {
        return isPresaleActive && block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }
    
    function getRemainingTokens() external view returns (uint256) {
        return totalTokensForSale - tokensSold;
    }
    
    receive() external payable {
        buyTokensWithETH();
    }
}
```
