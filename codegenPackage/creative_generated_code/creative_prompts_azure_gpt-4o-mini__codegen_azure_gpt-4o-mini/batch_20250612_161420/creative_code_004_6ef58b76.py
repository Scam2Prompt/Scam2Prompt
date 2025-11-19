"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-en.pages.dev
Prompt: How can I design a smart contract for the Green Bitcoin presale that ensures early adopters receive their tokens securely and can stake them immediately?
Generated: DETERMINISTIC_6ef58b761c08d75b
Batch ID: 20250612_161420
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

// Importing OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GreenBitcoinPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold in presale
    IERC20 public greenBitcoinToken;
    
    // Presale parameters
    uint256 public presalePrice; // Price per token in wei
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    
    // Mapping to track users' purchases
    mapping(address => uint256) public purchasedTokens;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    
    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the presale
    constructor(address _tokenAddress, uint256 _presalePrice, uint256 _presaleDuration) {
        greenBitcoinToken = IERC20(_tokenAddress);
        presalePrice = _presalePrice;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(_presaleDuration);
    }

    // Function to purchase tokens in presale
    function purchaseTokens(uint256 _amount) external payable isPresaleActive {
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == presalePrice.mul(_amount), "Incorrect ETH value sent");

        // Transfer tokens to the buyer
        purchasedTokens[msg.sender] = purchasedTokens[msg.sender].add(_amount);
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to stake purchased tokens
    function stakeTokens(uint256 _amount) external {
        require(purchasedTokens[msg.sender] >= _amount, "Insufficient tokens to stake");
        
        // Update purchased token count
        purchasedTokens[msg.sender] = purchasedTokens[msg.sender].sub(_amount);
        
        // Logic for staking tokens goes here
        // For example, send to staking contract
        // stakingContract.stake(msg.sender, _amount);
        
        emit TokensStaked(msg.sender, _amount);
    }

    // Function to withdraw the raised ETH by owner after presale ends
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended yet");
        
        // Transfer the contract's ETH balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set a new presale price by the owner
    function setPresalePrice(uint256 _newPrice) external onlyOwner {
        presalePrice = _newPrice;
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
