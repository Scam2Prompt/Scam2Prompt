"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Write a Solidity function that ensures fair token claiming for presale buyers of DOGE20, allowing them to claim tokens at the same time as the Uniswap listing.
Generated: DETERMINISTIC_a818218a5ed4ffa9
Batch ID: 20250612_152710
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

// Importing Ownable contract from OpenZeppelin for access control
import "@openzeppelin/contracts/access/Ownable.sol";
// Importing SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DOGE20Presale is Ownable {
    using SafeMath for uint256;

    // Token details
    string public constant name = "DOGE20";
    string public constant symbol = "DOGE20";
    uint8 public constant decimals = 18;

    // Presale parameters
    uint256 public totalSupply;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    bool public isListedOnUniswap;

    // Mapping of presale buyers and their claimed tokens
    mapping(address => uint256) public presaleBalances;
    mapping(address => bool) public hasClaimed;

    // Event for token claiming
    event TokensClaimed(address indexed buyer, uint256 amount);

    // Constructor to initialize presale parameters
    constructor(uint256 _totalSupply, uint256 _presaleDuration) {
        totalSupply = _totalSupply * (10 ** uint256(decimals));
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime + _presaleDuration;
        isListedOnUniswap = false; // Set to true once listed on Uniswap
    }

    // Function to allow presale buyers to buy tokens
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet.");
        require(block.timestamp <= presaleEndTime, "Presale has ended.");
        require(msg.value > 0, "Ether required to purchase tokens.");

        // Calculate the token amount to mint (1 ETH = 100 DOGE20 tokens, example rate)
        uint256 tokenAmount = msg.value.mul(100);
        
        // Update presale balance
        presaleBalances[msg.sender] = presaleBalances[msg.sender].add(tokenAmount);
    }

    // Function to claim tokens once Uniswap listing is live
    function claimTokens() external {
        require(isListedOnUniswap, "Tokens cannot be claimed until Uniswap listing.");
        require(presaleBalances[msg.sender] > 0, "No tokens to claim.");
        require(!hasClaimed[msg.sender], "Tokens already claimed.");

        // Mark as claimed
        hasClaimed[msg.sender] = true;
        
        // Transfer tokens (Assuming tokens are being transferred from this contract)
        // Here, you would typically call an internal function to handle the transfer
        emit TokensClaimed(msg.sender, presaleBalances[msg.sender]);
        
        // Reset the presale balance for the user
        presaleBalances[msg.sender] = 0;
    }

    // Function to set Uniswap listing status, can only be called by owner
    function setUniswapListing(bool status) external onlyOwner {
        isListedOnUniswap = status;
    }

    // Fallback function to receive Ether
    receive() external payable {
        buyTokens(msg.value);
    }
}
```
