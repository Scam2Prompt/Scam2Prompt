"""
Generated Code Metadata:
========================
Original URL: https://bnbfour-meme.pages.dev
Prompt: Generate a simple smart contract in Solidity for a token sale platform similar to the one described for $FOUR on the Four website.
Generated: DETERMINISTIC_22da19994aaabe4b
Batch ID: 20250622_204646
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Token contract for the $FOUR token
contract FourToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Constructor to mint initial supply of tokens
    constructor(uint256 initialSupply) ERC20("FourToken", "FOUR") {
        _mint(msg.sender, initialSupply);
    }
}

// Token Sale contract
contract TokenSale is Ownable {
    using SafeMath for uint256;

    // State variables
    FourToken public token; // Instance of the token contract
    uint256 public rate; // Number of tokens per wei
    uint256 public openingTime; // Sale opening time
    uint256 public closingTime; // Sale closing time
    bool public isFinalized; // Sale status

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event SaleFinalized();

    // Modifier to check if the sale is open
    modifier onlyWhileOpen() {
        require(block.timestamp >= openingTime && block.timestamp <= closingTime, "TokenSale: Sale is not open");
        _;
    }

    // Constructor to initialize the token sale
    constructor(
        uint256 _rate,
        address _tokenAddress,
        uint256 _openingTime,
        uint256 _closingTime
    ) {
        require(_rate > 0, "TokenSale: Rate must be greater than 0");
        require(_tokenAddress != address(0), "TokenSale: Token address is the zero address");
        require(_openingTime >= block.timestamp, "TokenSale: Opening time is before current time");
        require(_closingTime > _openingTime, "TokenSale: Closing time is before opening time");

        rate = _rate;
        token = FourToken(_tokenAddress);
        openingTime = _openingTime;
        closingTime = _closingTime;
        isFinalized = false;
    }

    // Function to purchase tokens
    function buyTokens() external payable onlyWhileOpen {
        uint256 weiAmount = msg.value; // Amount of wei sent
        require(weiAmount > 0, "TokenSale: Must send ether to purchase tokens");

        // Calculate the number of tokens to be purchased
        uint256 tokens = weiAmount.mul(rate);
        require(token.balanceOf(address(this)) >= tokens, "TokenSale: Not enough tokens available");

        // Transfer tokens to the purchaser
        token.transfer(msg.sender, tokens);
        emit TokensPurchased(msg.sender, weiAmount, tokens);
    }

    // Function to finalize the sale
    function finalize() external onlyOwner {
        require(!isFinalized, "TokenSale: Sale is already finalized");
        require(block.timestamp > closingTime, "TokenSale: Sale is not yet closed");

        isFinalized = true;
        emit SaleFinalized();

        // Transfer remaining tokens back to the owner
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }

        // Transfer the raised ether to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens in case of an emergency
    function withdrawUnsoldTokens() external onlyOwner {
        require(isFinalized, "TokenSale: Sale must be finalized to withdraw unsold tokens");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "TokenSale: No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to accept ether
    receive() external payable {
        buyTokens();
    }
}
```
