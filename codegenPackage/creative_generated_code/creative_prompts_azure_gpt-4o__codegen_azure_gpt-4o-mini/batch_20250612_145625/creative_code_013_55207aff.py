"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiindogsclub.pages.dev
Prompt: Create a smart contract to enforce the tokenomics rules of Bitcoin Dogs, including the "Poof! Gone" mechanism for unsold tokens after the presale ends.
Generated: DETERMINISTIC_55207afff278353b
Batch ID: 20250612_145625
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Bitcoin Dogs token
contract BitcoinDogs is ERC20, Ownable {
    // Define state variables for presale management
    uint256 public presaleEndTime;
    uint256 public totalPresaleTokens;
    uint256 public unsoldTokens;
    
    // Mapping to track user contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);
    
    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);

    // Constructor initializes the token with name and symbol
    constructor(uint256 _totalPresaleTokens, uint256 _presaleDuration) 
        ERC20("Bitcoin Dogs", "BTD")
    {
        totalPresaleTokens = _totalPresaleTokens;
        presaleEndTime = block.timestamp + _presaleDuration;
        unsoldTokens = totalPresaleTokens;
        _mint(address(this), totalPresaleTokens); // Mint tokens to the contract
    }

    // Function to contribute to the presale
    function contribute() external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Contribution must be greater than zero");

        contributions[msg.sender] += msg.value;
        // Calculate the amount of tokens to send (1 ETH = 100 BTD for example)
        uint256 amountToSend = msg.value * 100; 
        require(amountToSend <= unsoldTokens, "Not enough unsold tokens available");

        // Transfer tokens from contract to contributor
        _transfer(address(this), msg.sender, amountToSend);
        unsoldTokens -= amountToSend;
    }

    // Function for the owner to finalize the presale
    function finalizePresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        
        // Burn unsold tokens
        if (unsoldTokens > 0) {
            _burn(address(this), unsoldTokens);
            emit TokensBurned(unsoldTokens);
            unsoldTokens = 0; // Reset unsold tokens to zero after burning
        }
    }

    // Function to withdraw ETH raised in presale to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {
        contribute(); // Allow direct ETH contributions to the presale
    }

    // Function to retrieve the current contract balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
