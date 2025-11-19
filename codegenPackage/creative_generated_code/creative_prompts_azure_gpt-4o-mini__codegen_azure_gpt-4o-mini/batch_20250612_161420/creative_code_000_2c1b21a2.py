"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigpump.pages.dev
Prompt: Generate a smart contract for a meme coin similar to Big Pump Token ($PUMP) on the BNB Chain with a total supply of 4,444,444,444,444.
Generated: DETERMINISTIC_2c1b21a272def51b
Batch ID: 20250612_161420
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

// Import the OpenZeppelin ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title MemeCoin - A simple meme coin similar to Big Pump Token ($PUMP)
// @notice This contract implements an ERC20 token with a fixed total supply
contract MemeCoin is ERC20, Ownable {
    // Declare a constant for total supply
    uint256 public constant TOTAL_SUPPLY = 44444444444444; // Total supply set to 4,444,444,444,444

    // @notice Constructor that initializes the token with its name and symbol,
    //         and mints the total supply to the contract owner
    constructor() ERC20("MemeCoin", "$MEME") {
        // Mint the total supply to the deployer of the contract
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // @notice Override the transfer function to include an example of error handling
    //         (the function can be customized as per requirements)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // @notice Override the transferFrom function to include error handling
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Cannot transfer from the zero address");
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }

    // @notice A custom function to burn tokens, reducing the total supply
    // @param amount The number of tokens to burn
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // @notice Function to withdraw any BNB sent to this contract by mistake
    function withdrawBNB() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Failed to withdraw BNB");
    }

    // @notice Function to receive BNB directly to the contract
    receive() external payable {}
}
```
