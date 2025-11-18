"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onedexlp.com
Prompt: Develop a smart contract for token airdrop events targeting top users on the OneDex platform.
Generated: DETERMINISTIC_eb9a8c252018d173
Batch ID: 20250612_150316
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

// Importing OpenZeppelin's ERC20 contract for token implementation
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Airdrop
 * @dev Smart contract for distributing tokens to top users in an airdrop event
 */
contract Airdrop is Ownable {
    
    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);
    
    // Token to be airdropped
    IERC20 public token;

    // Constructor to initialize the token contract
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Distribute tokens to multiple recipients
     * @param recipients Array of addresses to receive tokens
     * @param amounts Array of token amounts corresponding to each recipient
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allow the contract to receive tokens from the owner
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance = token.balanceOf(address(this));
        require(amount <= balance, "Insufficient contract balance");

        // Transfer tokens from the contract to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Get the contract's token balance
     * @return The token balance of the contract
     */
    function getTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
