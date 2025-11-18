"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-buy.pages.dev
Prompt: Write code to implement a token presale mechanism for $PEPU, including price adjustments and wallet integration as described on the Pepe Unchained roadmap.
Generated: DETERMINISTIC_3962a8f74fda380f
Batch ID: 20250612_151347
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PEPU Presale Contract
 * @dev This contract implements a token presale mechanism for the $PEPU token.
 * The presale includes price adjustments and wallet integration as outlined in the Pepe Unchained roadmap.
 */
contract PEUPresale is Ownable {
    // The address of the $PEPU token contract
    IERC20 public pepuToken;

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice; // Price of 1 $PEPU in wei
    uint256 public tokensSold;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted(uint256 start, uint256 end, uint256 price);
    event PresaleEnded(uint256 totalTokensSold);
    
    /**
     * @dev Constructor to initialize the presale contract
     * @param _pepuToken Address of the $PEPU token contract
     */
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    /**
     * @dev Start the presale with given parameters
     * @param _duration Duration of the presale in seconds
     * @param _price Price of $PEPU token in wei
     */
    function startPresale(uint256 _duration, uint256 _price) external onlyOwner {
        presaleStart = block.timestamp;
        presaleEnd = presaleStart + _duration;
        tokenPrice = _price;

        emit PresaleStarted(presaleStart, presaleEnd, tokenPrice);
    }

    /**
     * @dev Purchase tokens in the presale
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");

        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer tokens to the buyer
        require(pepuToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev End the presale and withdraw funds
     */
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still ongoing");

        // Transfer Ether to the owner
        payable(owner()).transfer(address(this).balance);

        emit PresaleEnded(tokensSold);
    }

    /**
     * @dev Allow the owner to adjust token price
     * @param _newPrice New price of $PEPU in wei
     */
    function adjustTokenPrice(uint256 _newPrice) external onlyOwner {
        tokenPrice = _newPrice;
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }

    /**
     * @dev Function to withdraw tokens in case of emergency
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdrawTokens(uint256 _amount) external onlyOwner {
        require(pepuToken.transfer(owner(), _amount), "Token transfer failed");
    }
}
```
