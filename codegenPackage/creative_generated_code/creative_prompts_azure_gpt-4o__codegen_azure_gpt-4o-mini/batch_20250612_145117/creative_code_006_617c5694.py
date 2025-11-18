"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cesta.finance
Prompt: Create a function in Solidity to interact with a smart contract after connecting a wallet, as might be required on Cesta Finance.
Generated: DETERMINISTIC_617c5694c243eb5e
Batch ID: 20250612_145117
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the contract
contract CestaFinanceInteraction is Ownable {
    // State variable to hold the address of the token contract
    IERC20 public token;

    // Event to emit upon successful interaction
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    // Function to transfer tokens from the caller to a specified address
    // Requires approval from the caller to spend the tokens on their behalf
    function transferTokens(address to, uint256 amount) external {
        require(to != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Transfer tokens from the caller to the specified address
        // The caller must have approved this contract to spend their tokens
        bool success = token.transferFrom(msg.sender, to, amount);
        require(success, "Token transfer failed");

        // Emit the transfer event
        emit TokensTransferred(msg.sender, to, amount);
    }

    // Function to withdraw tokens from the contract (if applicable)
    // Only the owner can withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner's address
        bool success = token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    // Function to update the token contract address (if needed)
    // Only the owner can update the token address
    function updateTokenAddress(address newToken) external onlyOwner {
        require(newToken != address(0), "New token address cannot be zero");
        token = IERC20(newToken);
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
