"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Write a Solidity contract for a token presale with bonus programs and tracking platforms, similar to the PAMBO token presale.
Generated: DETERMINISTIC_2f7eeda9102f3b68
Batch ID: 20250612_150645
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

// Importing the OpenZeppelin ERC20 contract for standard token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenPresale contract for conducting a presale of the PAMBO token
contract TokenPresale is Ownable {
    // Event emitted when tokens are bought
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    
    // ERC20 token to be sold
    ERC20 public token;

    // Presale parameters
    uint256 public rate; // Number of tokens per ether
    uint256 public bonusRate; // Bonus tokens based on the purchase amount
    uint256 public presaleEndTime; // End time for the presale
    uint256 public totalTokensSold; // Total number of tokens sold during presale

    // Mapping to track total tokens purchased by each address
    mapping(address => uint256) public tokensPurchased;

    // Constructor to initialize the presale contract
    constructor(ERC20 _token, uint256 _rate, uint256 _bonusRate, uint256 _duration) {
        token = _token;
        rate = _rate;
        bonusRate = _bonusRate;
        presaleEndTime = block.timestamp + _duration;
    }

    // Modifier to check if the presale is still active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Function to buy tokens during the presale
    function buyTokens() external payable isPresaleActive {
        require(msg.value > 0, "You must send ether to purchase tokens");

        // Calculate tokens to be given and bonus
        uint256 tokensToBuy = msg.value * rate;
        uint256 bonusTokens = (tokensToBuy * bonusRate) / 100;

        // Total tokens to transfer
        uint256 totalTokens = tokensToBuy + bonusTokens;

        // Ensure contract has enough tokens
        require(token.balanceOf(address(this)) >= totalTokens, "Not enough tokens in presale");

        // Update the state
        tokensPurchased[msg.sender] += totalTokens;
        totalTokensSold += totalTokens;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, totalTokens);

        // Emit purchase event
        emit TokensPurchased(msg.sender, tokensToBuy, bonusTokens);
    }

    // Function to withdraw ether collected from presale
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to end the presale early if needed
    function endPresale() external onlyOwner isPresaleActive {
        presaleEndTime = block.timestamp;
    }

    // Function to change the rate of tokens per ether
    function setRate(uint256 newRate) external onlyOwner {
        rate = newRate;
    }

    // Function to change the bonus rate
    function setBonusRate(uint256 newBonusRate) external onlyOwner {
        bonusRate = newBonusRate;
    }

    // Function to get the remaining presale time
    function getRemainingTime() external view returns (uint256) {
        return presaleEndTime > block.timestamp ? presaleEndTime - block.timestamp : 0;
    }
}
```
