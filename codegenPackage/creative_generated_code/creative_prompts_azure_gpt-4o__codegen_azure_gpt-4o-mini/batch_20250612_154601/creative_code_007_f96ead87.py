"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracoin.io
Prompt: Develop a smart contract in Solidity that mimics the functionality of the ZORA presale, including bonus distribution and token allocation.
Generated: DETERMINISTIC_f96ead87980ec3e5
Batch ID: 20250612_154601
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

// Import OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZoraPresale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price per token (in wei)
    uint256 public totalTokens; // Total tokens available for presale
    uint256 public tokensSold; // Total tokens sold
    mapping(address => uint256) public contributions; // Mapping to track contributions

    // Bonus structure
    enum BonusLevel { None, Bronze, Silver, Gold }
    mapping(BonusLevel => uint256) public bonusPercent; // Bonus percentages for levels
    
    // Events for logging activity
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PresaleEnded(uint256 totalTokensSold);

    // Constructor to initialize the presale
    constructor(
        address _tokenAddress,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _totalTokens
    ) {
        require(_presaleStart < _presaleEnd, "Invalid presale period");
        require(_tokenAddress != address(0), "Invalid token address");
        
        token = ERC20(_tokenAddress);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        totalTokens = _totalTokens;
        tokensSold = 0;

        // Setting up bonus percentages
        bonusPercent[BonusLevel.Bronze] = 5;  // 5% bonus
        bonusPercent[BonusLevel.Silver] = 10; // 10% bonus
        bonusPercent[BonusLevel.Gold] = 15;   // 15% bonus
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value >= tokenPrice * amount, "Insufficient funds");
        require(tokensSold + amount <= totalTokens, "Not enough tokens available");

        // Calculate bonus
        uint256 bonusAmount = calculateBonus(amount);
        uint256 totalAmount = amount + bonusAmount;

        // Update state
        contributions[msg.sender] += msg.value;
        tokensSold += totalAmount;

        // Transfer tokens to buyer
        token.transfer(msg.sender, totalAmount);

        emit TokensPurchased(msg.sender, totalAmount, msg.value);
    }

    // Function to calculate bonus tokens based on contribution amount
    function calculateBonus(uint256 amount) internal view returns (uint256) {
        if (amount >= 10 ether) {
            return (amount * bonusPercent[BonusLevel.Gold]) / 100;
        } else if (amount >= 5 ether) {
            return (amount * bonusPercent[BonusLevel.Silver]) / 100;
        } else if (amount >= 1 ether) {
            return (amount * bonusPercent[BonusLevel.Bronze]) / 100;
        }
        return 0; // No bonus if below 1 ether
    }

    // Function to end presale and withdraw funds to owner
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");

        // Transfer contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
        emit PresaleEnded(tokensSold);
    }

    // Function to withdraw tokens from the contract (in case of emergency)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Not enough tokens in contract");
        token.transfer(owner(), amount);
    }

    // Function to change presale timing
    function setPresaleTiming(uint256 _presaleStart, uint256 _presaleEnd) external onlyOwner {
        require(_presaleStart < _presaleEnd, "Invalid presale period");
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed; use buyTokens");
    }
}
```
