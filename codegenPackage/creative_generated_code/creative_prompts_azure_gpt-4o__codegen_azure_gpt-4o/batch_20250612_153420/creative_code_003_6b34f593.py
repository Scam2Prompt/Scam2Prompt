"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrip-app.pages.dev
Prompt: Create a smart contract function to swap $BDRIP tokens for ETH based on the price data provided in the Base Drip Dashboard.
Generated: DETERMINISTIC_6b34f59335ea10c2
Batch ID: 20250612_153420
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Smart contract for swapping $BDRIP tokens for ETH based on price data
contract BDRIPTokenSwap is Ownable {
    // State variables
    IERC20 public bdripToken; // Interface for the $BDRIP token contract
    AggregatorV3Interface public priceFeed; // Interface for price feed from Base Drip Dashboard (Chainlink or similar)

    // Events
    event TokensSwapped(address indexed user, uint256 bdripAmount, uint256 ethReceived);

    // Constructor to set token and price feed addresses
    constructor(address _bdripTokenAddress, address _priceFeedAddress) {
        require(_bdripTokenAddress != address(0), "Invalid token address");
        require(_priceFeedAddress != address(0), "Invalid price feed address");

        bdripToken = IERC20(_bdripTokenAddress);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    // Function to swap $BDRIP tokens for ETH
    function swapTokensForETH(uint256 _bdripAmount) external {
        require(_bdripAmount > 0, "Amount must be greater than zero");
        require(bdripToken.balanceOf(msg.sender) >= _bdripAmount, "Insufficient token balance");

        // Get the latest price of $BDRIP in ETH from the price feed
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price data");

        // Calculate the equivalent amount of ETH based on the price
        uint256 ethAmount = (_bdripAmount * uint256(price)) / (10 ** priceFeed.decimals());
        require(address(this).balance >= ethAmount, "Insufficient ETH liquidity in contract");

        // Transfer the $BDRIP tokens from the sender to the contract
        require(bdripToken.transferFrom(msg.sender, address(this), _bdripAmount), "Token transfer failed");

        // Send ETH to the sender
        (bool success, ) = msg.sender.call{value: ethAmount}("");
        require(success, "ETH transfer failed");

        // Emit event for successful swap
        emit TokensSwapped(msg.sender, _bdripAmount, ethAmount);
    }

    // Function to add ETH liquidity to the contract (only owner)
    function depositETH() external payable onlyOwner {
        require(msg.value > 0, "Amount must be greater than zero");
    }

    // Function to withdraw ETH from the contract (only owner)
    function withdrawETH(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "ETH withdrawal failed");
    }

    // Function to withdraw $BDRIP tokens from the contract (only owner)
    function withdrawBDRIP(uint256 _amount) external onlyOwner {
        require(_amount <= bdripToken.balanceOf(address(this)), "Insufficient token balance");
        require(bdripToken.transfer(msg.sender, _amount), "Token withdrawal failed");
    }

    // Receive function to accept ETH directly
    receive() external payable {}

    // Fallback function
    fallback() external payable {}
}
```
