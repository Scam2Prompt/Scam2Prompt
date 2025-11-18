"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacm.pages.dev
Prompt: Write a smart contract in Solidity for managing airdrops, similar to the functionality described on the Pacmoon website.
Generated: DETERMINISTIC_d561e765cb0bbb14
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AirdropManager
 * @dev A smart contract for managing airdrops of ERC20 tokens.
 */
contract AirdropManager is Ownable {
    // Event to log airdrop operations
    event AirdropExecuted(address indexed token, address indexed beneficiary, uint256 amount);

    // Struct to hold airdrop information
    struct Airdrop {
        address token;
        address[] beneficiaries;
        uint256[] amounts;
    }

    // Function to execute an airdrop
    function executeAirdrop(Airdrop memory airdrop) external onlyOwner {
        require(airdrop.beneficiaries.length == airdrop.amounts.length, "Beneficiaries and amounts length mismatch");
        
        IERC20 token = IERC20(airdrop.token);
        
        // Iterate through beneficiaries and transfer tokens
        for (uint256 i = 0; i < airdrop.beneficiaries.length; i++) {
            address beneficiary = airdrop.beneficiaries[i];
            uint256 amount = airdrop.amounts[i];

            // Check balance and allowance
            require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            require(token.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance for airdrop");

            // Transfer the tokens
            bool success = token.transfer(beneficiary, amount);
            require(success, "Token transfer failed");

            emit AirdropExecuted(airdrop.token, beneficiary, amount);
        }
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param tokenAddress Address of the ERC20 token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");

        bool success = token.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }
}
```
