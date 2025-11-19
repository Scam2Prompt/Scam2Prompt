"""
Generated Code Metadata:
========================
Original URL: https://catcoinhq.com
Prompt: Develop a smart contract in Solidity to enable users to swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB) directly on-chain.
Generated: DETERMINISTIC_7999dae96925ec98
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for swapping Catcoin ($CAT) for ETH or BNB
contract CatcoinSwap {
    // Address of the Catcoin token contract
    IERC20 public catcoin;

    // Event emitted when a swap occurs
    event Swap(address indexed user, uint256 amountIn, uint256 amountOut, string tokenOut);

    // Constructor to set the Catcoin token address
    constructor(address _catcoinAddress) {
        require(_catcoinAddress != address(0), "Invalid Catcoin address");
        catcoin = IERC20(_catcoinAddress);
    }

    // Function to swap Catcoin for ETH
    function swapCatcoinForETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(catcoin.balanceOf(msg.sender) >= amount, "Insufficient Catcoin balance");

        // Transfer Catcoin from user to this contract
        catcoin.transferFrom(msg.sender, address(this), amount);

        // Calculate the amount of ETH to send (1 CAT = 0.001 ETH for example)
        uint256 ethAmount = amount / 1000;

        // Ensure the contract has enough ETH to complete the swap
        require(address(this).balance >= ethAmount, "Insufficient ETH in contract");

        // Transfer ETH to the user
        payable(msg.sender).transfer(ethAmount);

        // Emit the swap event
        emit Swap(msg.sender, amount, ethAmount, "ETH");
    }

    // Function to swap Catcoin for BNB
    function swapCatcoinForBNB(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(catcoin.balanceOf(msg.sender) >= amount, "Insufficient Catcoin balance");

        // Transfer Catcoin from user to this contract
        catcoin.transferFrom(msg.sender, address(this), amount);

        // Calculate the amount of BNB to send (1 CAT = 0.001 BNB for example)
        uint256 bnbAmount = amount / 1000;

        // Ensure the contract has enough BNB to complete the swap
        require(address(this).balance >= bnbAmount, "Insufficient BNB in contract");

        // Transfer BNB to the user
        payable(msg.sender).transfer(bnbAmount);

        // Emit the swap event
        emit Swap(msg.sender, amount, bnbAmount, "BNB");
    }

    // Function to receive ETH
    receive() external payable {}

    // Function to withdraw any remaining Catcoin from the contract
    function withdrawCatcoin(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(catcoin.balanceOf(address(this)) >= amount, "Insufficient Catcoin balance in contract");
        catcoin.transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient ETH balance in contract");
        payable(msg.sender).transfer(amount);
    }
}
```
