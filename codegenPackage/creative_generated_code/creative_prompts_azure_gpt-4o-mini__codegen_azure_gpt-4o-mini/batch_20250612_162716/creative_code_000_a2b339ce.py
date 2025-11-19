"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verifymainnetsolana.web.app
Prompt: Generate a smart contract for a token airdrop similar to the $KMNO second phase airdrop mentioned on the website.
Generated: DETERMINISTIC_a2b339ceda43657f
Batch ID: 20250612_162716
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

// Importing the ERC20 standard interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for distributing tokens to multiple addresses
contract TokenAirdrop is Ownable {
    // Address of the ERC20 token to be airdropped
    IERC20 public token;

    // Event to log the airdrop action
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    // Function to execute the airdrop
    // It distributes a specified amount of tokens to an array of recipients
    function airdropTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");

        // Check the contract's balance before proceeding
        uint256 totalAmount = amount * recipients.length;
        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient contract token balance");

        // Loop through the list of recipients and transfer tokens
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            token.transfer(recipients[i], amount);
            emit Airdrop(recipients[i], amount);
        }
    }

    // Function to withdraw tokens from the contract in case of emergencies
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract token balance for withdrawal");
        token.transfer(msg.sender, amount);
    }

    // Function to withdraw Ether (if any) sent to the contract
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
