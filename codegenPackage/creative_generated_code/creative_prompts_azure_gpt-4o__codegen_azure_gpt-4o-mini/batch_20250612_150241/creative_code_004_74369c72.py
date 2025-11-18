"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-en.web.app
Prompt: Write a smart contract in Solidity for managing $PEPU token presale purchases, including validation and claim functionality after the presale ends.
Generated: DETERMINISTIC_74369c729d652b39
Batch ID: 20250612_150241
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

contract PepuToken is ERC20, Ownable {
    // Token parameters
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presalePrice; // price per token in wei
    mapping(address => uint256) public contributions;
    
    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimant, uint256 amount);

    constructor() ERC20("PEPU Token", "PEPU") {
        _mint(address(this), INITIAL_SUPPLY); // Mint tokens to the contract
    }

    // Function to start presale
    function startPresale(uint256 durationInDays, uint256 pricePerToken) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime + (durationInDays * 1 days);
        presalePrice = pricePerToken;
    }

    // Function to buy tokens during presale
    function buyTokens(uint256 tokenAmount) external payable {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(msg.value == tokenAmount * presalePrice, "Incorrect ETH value sent");

        contributions[msg.sender] += tokenAmount;
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to claim tokens after presale ends
    function claimTokens() external {
        require(block.timestamp > presaleEndTime, "Presale is still ongoing");
        uint256 amountToClaim = contributions[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");

        contributions[msg.sender] = 0; // Reset contribution to prevent re-entrancy
        _transfer(address(this), msg.sender, amountToClaim); // Transfer tokens
        emit TokensClaimed(msg.sender, amountToClaim);
    }

    // Function to withdraw ETH from the contract, callable only by the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get the contract's ETH balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
