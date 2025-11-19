"""
Generated Code Metadata:
========================
Original URL: https://bitcoindog.pages.dev
Prompt: Write a smart contract in Solidity for a token sale on the Bitcoin blockchain, similar to the $0DOG token sale described on the Bitcoin Dogs website.
Generated: DETERMINISTIC_eca88f3236d61504
Batch ID: 20250622_210122
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

// Token contract for the $0DOG token
contract ZeroDogToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens

    // Constructor to initialize the token
    constructor() ERC20("Zero Dog Token", "$0DOG") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }
}

// Token Sale contract
contract TokenSale is Ownable {
    // State variables
    ZeroDogToken public token; // Instance of the token
    uint256 public rate; // Rate of tokens per Ether
    uint256 public weiRaised; // Amount of Ether raised
    uint256 public saleEndTime; // End time of the sale

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);

    // Constructor to initialize the token sale
    constructor(ZeroDogToken _token, uint256 _rate, uint256 _durationInMinutes) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        
        token = _token;
        rate = _rate;
        saleEndTime = block.timestamp + (_durationInMinutes * 1 minutes);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyTokens(msg.sender);
    }

    // Function to buy tokens
    function buyTokens(address beneficiary) public payable {
        require(block.timestamp < saleEndTime, "Token sale has ended");
        require(msg.value > 0, "Ether value must be greater than 0");

        uint256 tokens = msg.value * rate; // Calculate the number of tokens to be purchased
        require(tokens <= token.balanceOf(address(this)), "Not enough tokens available");

        weiRaised += msg.value; // Update the amount of Ether raised
        token.transfer(beneficiary, tokens); // Transfer tokens to the purchaser

        emit TokensPurchased(beneficiary, msg.value, tokens); // Emit event for token purchase
    }

    // Function to end the token sale and withdraw funds
    function endSale() public onlyOwner {
        require(block.timestamp >= saleEndTime, "Sale has not ended yet");

        // Transfer remaining tokens back to the owner
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }

        // Transfer raised Ether to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw funds in case of emergency
    function emergencyWithdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
