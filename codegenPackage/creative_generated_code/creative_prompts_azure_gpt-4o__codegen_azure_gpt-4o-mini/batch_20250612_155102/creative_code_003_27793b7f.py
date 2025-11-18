"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Create a smart contract audited by CertiK and SlowMist that ensures fair distribution of tokens during a presale, inspired by $GROK's model.
Generated: DETERMINISTIC_27793b7f41b48934
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title TokenPresale
/// @notice A smart contract for managing a fair token presale
contract TokenPresale is Ownable, ReentrancyGuard {
    // Token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public maxPurchaseLimit;
    
    // User purchase records
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 finalTime);

    // Modifier to check if the presale is active
    modifier isActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Modifier to check if the presale has ended
    modifier hasEnded() {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        _;
    }

    /// @notice Constructor to initialize the presale contract
    /// @param _token Address of the token being sold
    /// @param _presaleStartTime Start time of the presale
    /// @param _presaleEndTime End time of the presale
    /// @param _tokenPrice Price of the token in wei
    /// @param _maxPurchaseLimit Maximum amount of tokens that can be purchased by one address
    constructor(
        IERC20 _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _maxPurchaseLimit
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time");
        require(_tokenPrice > 0, "Token price must be positive");
        require(_maxPurchaseLimit > 0, "Max purchase limit must be positive");

        token = _token;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        maxPurchaseLimit = _maxPurchaseLimit;
    }

    /// @notice Function to purchase tokens during the presale
    /// @param amount The amount of tokens to purchase
    function purchaseTokens(uint256 amount) external payable isActive nonReentrant {
        uint256 totalCost = amount * tokenPrice;
        
        // Validate contribution
        require(msg.value >= totalCost, "Insufficient funds sent");
        require(contributions[msg.sender] + amount <= maxPurchaseLimit, "Exceeds max purchase limit");

        // Update contribution record
        contributions[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /// @notice Function to withdraw funds after the presale ends
    function withdrawFunds() external onlyOwner hasEnded {
        payable(owner()).transfer(address(this).balance);
        emit PresaleEnded(block.timestamp);
    }

    /// @notice Finalize the presale and transfer remaining tokens to the owner
    function finalizePresale() external onlyOwner hasEnded {
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }
    }

    /// @notice Allow the owner to update presale parameters if needed
    function updatePresaleParameters(
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _maxPurchaseLimit
    ) external onlyOwner {
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time");
        require(_tokenPrice > 0, "Token price must be positive");
        require(_maxPurchaseLimit > 0, "Max purchase limit must be positive");

        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        maxPurchaseLimit = _maxPurchaseLimit;
    }

    /// @notice Function to allow users to withdraw tokens in case of a failed presale
    function withdrawTokens() external hasEnded {
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to withdraw");
        
        // Reset user's contribution
        contributions[msg.sender] = 0;

        token.transfer(msg.sender, amount);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
