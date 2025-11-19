"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Write a smart contract in Solidity that mimics the functionality of the BOI Coin presale, including token purchase using USDT, ETH, and BNB, and tracking raised funds.
Generated: DETERMINISTIC_cfe2c53f0cfc0699
Batch ID: 20250612_150327
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

contract BOICoinPresale is Ownable, ReentrancyGuard {
    IERC20 public usdtToken;
    IERC20 public boiToken;
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalRaisedUSDT;
    uint256 public totalRaisedETH;
    uint256 public totalRaisedBNB;
    uint256 public tokenPriceUSDT; // price per BOI token in USDT (with decimals)
    uint256 public tokenPriceETH;  // price per BOI token in ETH (with decimals)
    uint256 public tokenPriceBNB;  // price per BOI token in BNB (with decimals)
    uint256 public hardCap;
    uint256 public minContribution;
    uint256 public maxContribution;
    
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensBought;
    
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);
    event PresaleExtended(uint256 newEndTime);
    event PresaleClosed();
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    constructor(
        address _usdtToken,
        address _boiToken,
        uint256 _presaleStartTime,
        uint256 _presaleDuration,
        uint256 _tokenPriceUSDT,
        uint256 _tokenPriceETH,
        uint256 _tokenPriceBNB,
        uint256 _hardCap,
        uint256 _minContribution,
        uint256 _maxContribution
    ) {
        require(_usdtToken != address(0), "USDT token address cannot be zero");
        require(_boiToken != address(0), "BOI token address cannot be zero");
        require(_presaleStartTime >= block.timestamp, "Start time must be in the future");
        require(_presaleDuration > 0, "Presale duration must be positive");
        require(_tokenPriceUSDT > 0, "Token price must be positive");
        require(_tokenPriceETH > 0, "Token price must be positive");
        require(_tokenPriceBNB > 0, "Token price must be positive");
        require(_hardCap > 0, "Hard cap must be positive");
        
        usdtToken = IERC20(_usdtToken);
        boiToken = IERC20(_boiToken);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime + _presaleDuration;
        tokenPriceUSDT = _tokenPriceUSDT;
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBNB = _tokenPriceBNB;
        hardCap = _hardCap;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }
    
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }
    
    function buyWithUSDT(uint256 usdtAmount) external isPresaleActive nonReentrant {
        require(usdtAmount >= minContribution, "Contribution is below minimum");
        require(contributions[msg.sender] + usdtAmount <= maxContribution, "Contribution exceeds maximum");
        require(totalRaisedUSDT + usdtAmount <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = (usdtAmount * 10**18) / tokenPriceUSDT;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        usdtToken.transferFrom(msg.sender, address(this), usdtAmount);
        
        contributions[msg.sender] += usdtAmount;
        tokensBought[msg.sender] += tokenAmount;
        totalRaisedUSDT += usdtAmount;
        
        boiToken.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount, "USDT");
    }
    
    function buyWithETH() external payable isPresaleActive nonReentrant {
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Contribution exceeds maximum");
        require(totalRaisedETH + msg.value <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = (msg.value * 10**18) / tokenPriceETH;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        contributions[msg.sender] += msg.value;
        tokensBought[msg.sender] += tokenAmount;
        totalRaisedETH += msg.value;
        
        boiToken.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount, "ETH");
    }
    
    function buyWithBNB() external payable isPresaleActive nonReentrant {
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Contribution exceeds maximum");
        require(totalRaisedBNB + msg.value <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = (msg.value * 10**18) / tokenPriceBNB;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        contributions[msg.sender] += msg.value;
        tokensBought[msg.sender] += tokenAmount;
        totalRaisedBNB += msg.value;
        
        boiToken.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount, "BNB");
    }
    
    function extendPresale(uint256 additionalTime) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale has already ended");
        presaleEndTime += additionalTime;
        emit PresaleExtended(presaleEndTime);
    }
    
    function closePresale() external onlyOwner {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        presaleEndTime = block.timestamp;
        emit PresaleClosed();
    }
    
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        
        // Withdraw USDT
        uint256 usdtBalance = usdtToken.balanceOf(address(this));
        if (usdtBalance > 0) {
            usdtToken.transfer(owner(), usdtBalance);
        }
        
        // Withdraw ETH
        uint256 ethBalance = address(this).balance;
        if (ethBalance > 0) {
            payable(owner()).transfer(ethBalance);
        }
        
        emit FundsWithdrawn(owner(), usdtBalance + ethBalance);
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        uint256 unsoldTokens = boiToken.balanceOf(address(this));
        boiToken.transfer(owner(), unsoldTokens);
    }
    
    function setTokenPrices(
        uint256 _tokenPriceUSDT,
        uint256 _tokenPriceETH,
        uint256 _tokenPriceBNB
    ) external onlyOwner {
        require(_tokenPriceUSDT > 0, "Token price must be positive");
        require(_tokenPriceETH > 0, "Token price must be positive");
        require(_tokenPriceBNB > 0, "Token price must be positive");
        tokenPriceUSDT = _tokenPriceUSDT;
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBNB = _tokenPriceBNB;
    }
    
    function setContributionLimits(
        uint256 _minContribution,
        uint256 _maxContribution
    ) external onlyOwner {
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }
    
    function getPresaleStatus() external view returns (string memory) {
        if (block.timestamp < presaleStartTime) {
            return "Not Started";
        } else if (block.timestamp <= presaleEndTime) {
            return "Active";
        } else {
            return "Ended";
        }
    }
    
    function getTotalRaised() external view returns (uint256) {
        return totalRaisedUSDT + totalRaisedETH + totalRaisedBNB;
    }
    
    receive() external payable {
        revert("Please use the buyWithETH or buyWithBNB functions");
    }
}
```
