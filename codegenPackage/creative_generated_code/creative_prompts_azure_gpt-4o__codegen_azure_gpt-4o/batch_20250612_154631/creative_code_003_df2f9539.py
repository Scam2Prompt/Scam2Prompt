"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt.airdrop1.org
Prompt: Provide an example of a smart contract for distributing USDT tokens in an airdrop campaign.
Generated: DETERMINISTIC_df2f9539d4f6b085
Batch ID: 20250612_154631
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

/**
 * @title USDT Airdrop Contract
 * @dev This contract facilitates the distribution of USDT tokens in an airdrop campaign.
 *      The admin can distribute tokens to multiple recipients in a single transaction.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract USDTTokenAirdrop {
    // Address of the USDT token contract
    IERC20 public immutable usdtToken;

    // Address of the admin
    address public immutable admin;

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Access restricted to admin.");
        _;
    }

    // Constructor to initialize the contract with the USDT token address and admin address
    constructor(address _usdtTokenAddress) {
        require(_usdtTokenAddress != address(0), "Invalid USDT token address.");
        usdtToken = IERC20(_usdtTokenAddress);
        admin = msg.sender; // Set the deployer as admin
    }

    /**
     * @dev Distribute USDT tokens to multiple recipients.
     * @param recipients List of recipient addresses.
     * @param amounts List of token amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyAdmin {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length.");
        uint256 totalRecipients = recipients.length;

        for (uint256 i = 0; i < totalRecipients; i++) {
            require(recipients[i] != address(0), "Invalid recipient address.");
            require(amounts[i] > 0, "Amount must be greater than zero.");
            
            // Transfer USDT tokens to the recipient
            bool success = usdtToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed.");
        }
    }

    /**
     * @dev Emergency function for the admin to withdraw leftover tokens.
     * @param to Address to withdraw the tokens to.
     */
    function withdrawTokens(address to) external onlyAdmin {
        require(to != address(0), "Invalid withdrawal address.");
        
        uint256 contractBalance = usdtToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw.");

        bool success = usdtToken.transfer(to, contractBalance);
        require(success, "Token withdrawal failed.");
    }
}
```
