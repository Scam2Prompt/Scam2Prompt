"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwen.pages.dev
Prompt: Create a smart contract in Solidity for trading WEN tokens, ensuring compatibility with Web3 wallets.
Generated: DETERMINISTIC_5594910c5cf0d840
Batch ID: 20250612_151931
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

// Import ERC20 interface to interact with WEN tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for trading WEN tokens
contract WENTrading is Ownable {
    // Event emitted when a trade occurs
    event TradeExecuted(address indexed buyer, address indexed seller, uint256 amount, uint256 price);

    // WEN token contract
    IERC20 public wenToken;

    // Mapping to track balances of users
    mapping(address => uint256) public balances;

    // Constructor to initialize the contract with the WEN token address
    constructor(address _wenTokenAddress) {
        require(_wenTokenAddress != address(0), "Invalid WEN token address");
        wenToken = IERC20(_wenTokenAddress);
    }

    // Function to buy WEN tokens
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether value must be greater than zero");

        // Set the price per token (in wei)
        uint256 pricePerToken = 0.01 ether; // Example price (adjust as needed)
        uint256 totalCost = pricePerToken * _amount;

        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Transfer WEN tokens from the contract to the buyer
        balances[msg.sender] += _amount;
        require(wenToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit the trade event
        emit TradeExecuted(msg.sender, address(this), _amount, pricePerToken);
    }

    // Function to sell WEN tokens
    function sellTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient token balance");

        // Set the price per token (in wei)
        uint256 pricePerToken = 0.01 ether; // Example price (adjust as needed)
        uint256 totalRevenue = pricePerToken * _amount;

        // Update the user's token balance
        balances[msg.sender] -= _amount;

        // Transfer WEN tokens from the seller to the contract
        require(wenToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Transfer Ether to the seller
        (bool success, ) = msg.sender.call{value: totalRevenue}("");
        require(success, "Ether transfer failed");

        // Emit the trade event
        emit TradeExecuted(address(this), msg.sender, _amount, pricePerToken);
    }

    // Function to withdraw any remaining Ether from the contract
    function withdraw() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // Function to check the contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to prevent unexpected Ether transfer to contract
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
