"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonflip-presale.vercel.app
Prompt: Create a smart contract template for managing token presales in a decentralized exchange (DEX) inspired by Moon Flip AI DEX.
Generated: DETERMINISTIC_363e9fd93c6c3c48
Batch ID: 20250612_145306
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

// Importing necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Presale Contract
 * @dev This contract manages token presales in a decentralized exchange (DEX).
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The token being sold
    uint256 public presaleStartTime; // Start time of the presale
    uint256 public presaleEndTime; // End time of the presale
    uint256 public tokenPrice; // Price of the token in wei
    uint256 public tokensSold; // Total tokens sold in the presale

    // Mapping of buyers to their purchased token amounts
    mapping(address => uint256) public purchases;

    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _startTime Presale start time as a UNIX timestamp.
     * @param _endTime Presale end time as a UNIX timestamp.
     * @param _tokenPrice Price of the token in wei.
     */
    constructor(
        address _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokenPrice
    ) {
        require(_token != address(0), "Invalid token address");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = IERC20(_token);
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Modifier to check if the presale is active.
     */
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function purchaseTokens(uint256 _amount) external payable isPresaleActive {
        // Calculate total price for the requested amount of tokens
        uint256 totalCost = _amount.mul(tokenPrice);
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Transfer tokens to the buyer
        purchases[msg.sender] = purchases[msg.sender].add(_amount);
        tokensSold = tokensSold.add(_amount);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw funds from the presale.
     * Only callable by the owner of the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to end the presale and transfer remaining tokens to the owner.
     * Only callable by the owner of the contract.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens");

        // Transfer remaining tokens to the owner
        token.transfer(owner(), remainingTokens);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
