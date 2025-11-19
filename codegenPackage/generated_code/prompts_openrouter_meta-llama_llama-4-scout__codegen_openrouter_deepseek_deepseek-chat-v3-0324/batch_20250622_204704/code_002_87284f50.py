"""
Generated Code Metadata:
========================
Original URL: https://asi-singularitydao.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the token conversion from AGIX and OCEAN to FET, considering the conversion rate and potential risks involved.
Generated: DETERMINISTIC_87284f50d5026443
Batch ID: 20250622_204704
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenConverter is Ownable, Pausable, ReentrancyGuard {
    IERC20 public agixToken;
    IERC20 public oceanToken;
    IERC20 public fetToken;
    
    uint256 public agixToFetRate;
    uint256 public oceanToFetRate;
    
    uint256 public constant RATE_DECIMALS = 18;
    
    event TokensConverted(
        address indexed user,
        address indexed fromToken,
        uint256 fromAmount,
        uint256 toAmount
    );
    event RatesUpdated(uint256 newAgixRate, uint256 newOceanRate);
    
    constructor(
        address _agixToken,
        address _oceanToken,
        address _fetToken,
        uint256 _agixToFetRate,
        uint256 _oceanToFetRate
    ) {
        require(_agixToken != address(0), "Invalid AGIX token address");
        require(_oceanToken != address(0), "Invalid OCEAN token address");
        require(_fetToken != address(0), "Invalid FET token address");
        require(_agixToFetRate > 0, "Invalid AGIX rate");
        require(_oceanToFetRate > 0, "Invalid OCEAN rate");
        
        agixToken = IERC20(_agixToken);
        oceanToken = IERC20(_oceanToken);
        fetToken = IERC20(_fetToken);
        
        agixToFetRate = _agixToFetRate;
        oceanToFetRate = _oceanToFetRate;
    }
    
    function convertAgixToFet(uint256 agixAmount) external whenNotPaused nonReentrant {
        require(agixAmount > 0, "Amount must be greater than 0");
        
        uint256 fetAmount = (agixAmount * agixToFetRate) / (10 ** RATE_DECIMALS);
        require(fetAmount > 0, "Resulting FET amount too small");
        
        require(
            agixToken.transferFrom(msg.sender, address(this), agixAmount),
            "AGIX transfer failed"
        );
        
        require(
            fetToken.transfer(msg.sender, fetAmount),
            "FET transfer failed"
        );
        
        emit TokensConverted(msg.sender, address(agixToken), agixAmount, fetAmount);
    }
    
    function convertOceanToFet(uint256 oceanAmount) external whenNotPaused nonReentrant {
        require(oceanAmount > 0, "Amount must be greater than 0");
        
        uint256 fetAmount = (oceanAmount * oceanToFetRate) / (10 ** RATE_DECIMALS);
        require(fetAmount > 0, "Resulting FET amount too small");
        
        require(
            oceanToken.transferFrom(msg.sender, address(this), oceanAmount),
            "OCEAN transfer failed"
        );
        
        require(
            fetToken.transfer(msg.sender, fetAmount),
            "FET transfer failed"
        );
        
        emit TokensConverted(msg.sender, address(oceanToken), oceanAmount, fetAmount);
    }
    
    function updateRates(uint256 newAgixRate, uint256 newOceanRate) external onlyOwner {
        require(newAgixRate > 0, "Invalid AGIX rate");
        require(newOceanRate > 0, "Invalid OCEAN rate");
        
        agixToFetRate = newAgixRate;
        oceanToFetRate = newOceanRate;
        
        emit RatesUpdated(newAgixRate, newOceanRate);
    }
    
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Token withdrawal failed"
        );
    }
    
    function pause() external onlyOwner {
        _pause();
    }
    
    function unpause() external onlyOwner {
        _unpause();
    }
    
    function getFetAmountForAgix(uint256 agixAmount) external view returns (uint256) {
        return (agixAmount * agixToFetRate) / (10 ** RATE_DECIMALS);
    }
    
    function getFetAmountForOcean(uint256 oceanAmount) external view returns (uint256) {
        return (oceanAmount * oceanToFetRate) / (10 ** RATE_DECIMALS);
    }
}
```
