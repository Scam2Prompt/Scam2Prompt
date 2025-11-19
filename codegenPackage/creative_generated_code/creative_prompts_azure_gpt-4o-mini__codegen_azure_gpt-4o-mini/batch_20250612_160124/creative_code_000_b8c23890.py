"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wepestreetpepe-new.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a crypto presale for the WEPE Token.
Generated: DETERMINISTIC_b8c23890dd1972dc
Batch ID: 20250612_160124
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

// Importing OpenZeppelin's SafeERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for WEPE Token
contract WEPEPresale is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public wepeToken;         // The WEPE token being sold
    uint256 public presalePrice;     // Price per WEPE token in wei
    uint256 public totalTokens;      // Total tokens available for presale
    uint256 public tokensSold;       // Total tokens sold
    uint256 public startTime;        // Presale start time
    uint256 public endTime;          // Presale end time

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 amount);
    event PresaleUpdated(uint256 newTotalTokens, uint256 newPresalePrice);
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier isActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _wepeToken,
        uint256 _presalePrice,
        uint256 _totalTokens,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_wepeToken != address(0), "Invalid token address");
        require(_presalePrice > 0, "Price must be positive");
        require(_totalTokens > 0, "Total tokens must be positive");
        require(_startTime < _endTime, "Start time must be before end time");

        wepeToken = IERC20(_wepeToken);
        presalePrice = _presalePrice;
        totalTokens = _totalTokens;
        startTime = _startTime;
        endTime = _endTime;
    }

    // Function to purchase WEPE tokens
    function purchaseTokens(uint256 tokenAmount) external payable isActive {
        require(tokenAmount > 0, "Must purchase at least one token");
        require(tokensSold + tokenAmount <= totalTokens, "Not enough tokens available");
        require(msg.value == tokenAmount * presalePrice, "Incorrect Ether value sent");

        // Update sold tokens and record contribution
        tokensSold += tokenAmount;
        contributions[msg.sender] += tokenAmount;

        // Transfer the tokens to the purchaser
        wepeToken.safeTransfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw unsold tokens after presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Presale is still active");
        uint256 unsoldTokens = totalTokens - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens back to the owner
        wepeToken.safeTransfer(owner(), unsoldTokens);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        require(address(this).balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to update presale parameters
    function updatePresale(uint256 newTotalTokens, uint256 newPresalePrice) external onlyOwner {
        require(newTotalTokens > tokensSold, "New total must be greater than tokens sold");
        totalTokens = newTotalTokens;
        presalePrice = newPresalePrice;

        emit PresaleUpdated(newTotalTokens, newPresalePrice);
    }

    // Function to end presale prematurely
    function endPresale() external onlyOwner {
        require(block.timestamp < endTime, "Presale already ended");
        endTime = block.timestamp; // Setting end time to current time

        emit PresaleEnded();
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
