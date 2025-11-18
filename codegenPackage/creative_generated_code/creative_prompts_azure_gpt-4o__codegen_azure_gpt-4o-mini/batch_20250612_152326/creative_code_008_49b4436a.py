"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clean-4dq.pages.dev
Prompt: Write a smart contract that demonstrates the issuance of assets on SatoshiVM, utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
Generated: DETERMINISTIC_49b4436a30851ed2
Batch ID: 20250612_152326
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

// Importing the interface for ERC20 token standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Asset Issuer Smart Contract
 * @dev This contract allows the issuance of assets on SatoshiVM 
 * utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
 */
contract AssetIssuer is Ownable {
    // Event emitted when a new asset is issued
    event AssetIssued(address indexed to, uint256 amount, string assetName);

    // Mapping to keep track of asset balances
    mapping(address => mapping(string => uint256)) private assetBalances;

    /**
     * @dev Issues a specified amount of a given asset to a recipient.
     * @param to The address of the recipient.
     * @param amount The amount of the asset to issue.
     * @param assetName The name of the asset to issue.
     */
    function issueAsset(address to, uint256 amount, string memory assetName) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the asset balance for the recipient
        assetBalances[to][assetName] += amount;

        // Emit an event for the asset issuance
        emit AssetIssued(to, amount, assetName);
    }

    /**
     * @dev Retrieves the balance of a specific asset for a given owner.
     * @param owner The address of the asset owner.
     * @param assetName The name of the asset to query.
     * @return The amount of the specified asset the owner has.
     */
    function getAssetBalance(address owner, string memory assetName) external view returns (uint256) {
        return assetBalances[owner][assetName];
    }

    /**
     * @dev Withdraws ERC20 tokens from the contract (if any).
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        token.transfer(owner(), amount);
    }
}
```
