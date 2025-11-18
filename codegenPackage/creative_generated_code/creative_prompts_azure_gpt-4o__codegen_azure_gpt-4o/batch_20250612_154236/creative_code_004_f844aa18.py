"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qubeticstoken-live.web.app
Prompt: Write a Solidity smart contract snippet that handles token distribution for TICS presale participants, ensuring compatibility with ERC-20 and BEP-20 standards.
Generated: DETERMINISTIC_f844aa1855b757ab
Batch ID: 20250612_154236
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleTokenDistributor
 * @dev Token distribution contract for TICS presale participants. Compatible with ERC-20 and BEP-20 standards.
 */
contract PresaleTokenDistributor is Ownable {
    // The ERC-20/BEP-20 token being distributed
    IERC20 public token;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC-20/BEP-20 token.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Distribute tokens to presale participants.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts to distribute (same index as recipients).
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched recipients and amounts");
        uint256 totalRecipients = recipients.length;

        for (uint256 i = 0; i < totalRecipients; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Recover any tokens accidentally sent to this contract.
     * @param _token Address of the token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");

        IERC20(_token).transfer(owner(), _amount);
    }
}
```
