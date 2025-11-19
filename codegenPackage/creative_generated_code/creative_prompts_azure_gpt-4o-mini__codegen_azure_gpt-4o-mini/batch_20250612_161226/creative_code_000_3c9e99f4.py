"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Generate a code snippet for a smart contract that allows users to purchase the Sophon Token ($SOPH) during the presale on the Sophon Network.
Generated: DETERMINISTIC_3c9e99f411b3b540
Batch ID: 20250612_161226
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SophonPresale
 * @dev A smart contract that allows users to purchase the Sophon Token ($SOPH) during the presale period.
 */
contract SophonPresale is Ownable {
    // Variables to manage presale state
    IERC20 public sophonToken; // Reference to the $SOPH token
    uint256 public presaleStart; // Presale start timestamp
    uint256 public presaleEnd;   // Presale end timestamp
    uint256 public tokenPrice;    // Price of one $SOPH token in wei

    // Events for logging purchases
    event TokensPurchased(address indexed purchaser, uint256 amount, uint256 cost);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _sophonToken Address of the $SOPH token contract.
     * @param _presaleStart Start time of the presale.
     * @param _presaleEnd End time of the presale.
     * @param _tokenPrice Price of one $SOPH token in wei.
     */
    constructor(
        address _sophonToken,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice
    ) {
        require(_sophonToken != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        sophonToken = IERC20(_sophonToken);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase $SOPH tokens.
     * @param amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        // Check if the presale is active
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(amount > 0, "Purchase amount must be greater than zero");

        // Calculate the cost of the purchased tokens
        uint256 cost = amount * tokenPrice;
        require(msg.value >= cost, "Insufficient funds sent");

        // Transfer the tokens to the purchaser
        require(sophonToken.balanceOf(address(this)) >= amount, "Not enough tokens available for sale");
        sophonToken.transfer(msg.sender, amount);

        // Emit an event for the token purchase
        emit TokensPurchased(msg.sender, amount, cost);

        // Refund any excess funds sent
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Function to withdraw unsold tokens after the presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");
        uint256 unsoldTokens = sophonToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        sophonToken.transfer(msg.sender, unsoldTokens);
    }

    /**
     * @dev Function to withdraw ETH from the contract.
     */
    function withdrawETH() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
