"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solshwifeth.pages.dev
Prompt: Write a smart contract to distribute $SHWIF tokens during an airdrop event, ensuring compatibility with Ethereum wallets mentioned on the website.
Generated: DETERMINISTIC_e008eec300c99c50
Batch ID: 20250612_151143
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
 * @title SHWIFTokenAirdrop
 * @dev Smart contract to distribute $SHWIF tokens during an airdrop event.
 */
contract SHWIFTokenAirdrop {
    // ERC20 Token Interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the $SHWIF token contract
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event EmergencyWithdrawal(address indexed owner, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token's contract address and the owner.
     * @param tokenAddress Address of the $SHWIF token contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Distribute tokens to a list of recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts to be distributed (same order as recipients).
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        // Ensure the input arrays are of equal length
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Distribution amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            // Emit event
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Emergency function to withdraw all tokens back to the owner in case of issues.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = token.transfer(owner, balance);
        require(success, "Emergency withdrawal failed");

        emit EmergencyWithdrawal(owner, balance);
    }

    /**
     * @dev Update the token contract address.
     * @param newTokenAddress New address of the $SHWIF token contract.
     */
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(newTokenAddress);
    }
}
```
