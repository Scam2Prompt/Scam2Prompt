"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Generate Solidity smart contract code for a token presale system where users can buy tokens with ETH and claim their purchased tokens, as outlined on the HumanizedAi presale site.
Generated: DETERMINISTIC_8ac8b6cd8aa15f94
Batch ID: 20250612_152109
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenPresale
 * @dev Contract for a token presale system
 */
contract TokenPresale is Ownable {
    IERC20 public token; // The token being sold
    uint256 public rate; // Number of tokens per wei
    uint256 public weiRaised; // Amount of ETH raised
    uint256 public startTime; // Presale start time
    uint256 public endTime; // Presale end time
    mapping(address => uint256) public contributions; // Track contributions of each user

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract
     * @param _token The token to be sold
     * @param _rate The token rate per wei
     * @param _startTime The start time of the presale
     * @param _endTime The end time of the presale
     */
    constructor(IERC20 _token, uint256 _rate, uint256 _startTime, uint256 _endTime) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        require(_startTime < _endTime, "Start time must be before end time");

        token = _token;
        rate = _rate;
        startTime = _startTime;
        endTime = _endTime;
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Buy tokens with ETH
     */
    function buyTokens() public payable {
        require(block.timestamp >= startTime, "Presale has not started yet");
        require(block.timestamp <= endTime, "Presale has ended");
        require(msg.value > 0, "Must send ETH to purchase tokens");

        uint256 tokens = msg.value * rate; // Calculate tokens to purchase
        contributions[msg.sender] += tokens; // Track user contributions
        weiRaised += msg.value; // Update total ETH raised

        emit TokensPurchased(msg.sender, tokens);
    }

    /**
     * @dev Claim purchased tokens
     */
    function claimTokens() public {
        require(block.timestamp > endTime, "Presale is still ongoing");
        uint256 amount = contributions[msg.sender]; // Get user's contribution
        require(amount > 0, "No tokens to claim");

        contributions[msg.sender] = 0; // Reset contribution
        token.transfer(msg.sender, amount); // Transfer tokens to user

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Withdraw ETH raised in the presale
     * Can only be called by the owner
     */
    function withdraw() public onlyOwner {
        require(address(this).balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(address(this).balance); // Transfer ETH to owner
    }

    /**
     * @dev Allows the owner to set a new rate
     * @param _rate The new token rate per wei
     */
    function setRate(uint256 _rate) public onlyOwner {
        require(_rate > 0, "Rate must be greater than 0");
        rate = _rate; // Update token rate
    }

    /**
     * @dev Allows the owner to update the presale time
     * @param _startTime The new start time
     * @param _endTime The new end time
     */
    function updatePresaleTime(uint256 _startTime, uint256 _endTime) public onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        startTime = _startTime; // Update start time
        endTime = _endTime; // Update end time
    }
}
```
