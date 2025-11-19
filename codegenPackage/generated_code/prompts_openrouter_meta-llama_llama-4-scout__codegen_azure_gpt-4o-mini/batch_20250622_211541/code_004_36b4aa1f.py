"""
Generated Code Metadata:
========================
Original URL: https://connectwallstreets-pepe.pages.dev
Prompt: Develop a smart contract using Solidity to automate the $WEPE Token presale process, including token allocation and price increases.
Generated: DETERMINISTIC_36b4aa1f9c67e80e
Batch ID: 20250622_211541
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

// Importing the ERC20 interface for the $WEPE Token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for the $WEPE Token
contract WEPEPresale is Ownable {
    // State variables
    IERC20 public wepeToken; // The $WEPE token contract
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public constant MAX_TOKENS = 1000000 * 10**18; // Maximum tokens available for presale
    uint256 public priceIncreaseInterval; // Time interval for price increase
    uint256 public priceIncreaseAmount; // Amount to increase the price by

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalTokensSold);

    // Constructor to initialize the presale contract
    constructor(
        address _wepeToken,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _initialPrice,
        uint256 _priceIncreaseInterval,
        uint256 _priceIncreaseAmount
    ) {
        require(_wepeToken != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_initialPrice > 0, "Price must be greater than zero");
        
        wepeToken = IERC20(_wepeToken);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _initialPrice;
        priceIncreaseInterval = _priceIncreaseInterval;
        priceIncreaseAmount = _priceIncreaseAmount;
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 _amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(tokensSold + _amount <= MAX_TOKENS, "Not enough tokens available");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");

        tokensSold += _amount;

        // Transfer tokens to the buyer
        require(wepeToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still ongoing");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to increase the token price based on the time elapsed
    function updateTokenPrice() external {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(block.timestamp <= presaleEnd, "Presale has ended");

        uint256 elapsedIntervals = (block.timestamp - presaleStart) / priceIncreaseInterval;
        uint256 newPrice = tokenPrice + (elapsedIntervals * priceIncreaseAmount);

        // Update the token price if it has changed
        if (newPrice > tokenPrice) {
            tokenPrice = newPrice;
        }
    }

    // Function to end the presale and emit an event
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still ongoing");
        emit PresaleEnded(tokensSold);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
