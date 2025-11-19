"""
Generated Code Metadata:
========================
Original URL: https://bittensor-ecosystem.vercel.app
Prompt: "Design a basic smart contract for distributing airdropped tokens on a decentralized network like Bittensor."
Generated: DETERMINISTIC_0cb16e2e136aeae5
Batch ID: 20250622_212724
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenAirdrop
 * @dev A smart contract for distributing ERC20 tokens to multiple recipients via airdrop
 */
contract TokenAirdrop is Ownable {
    using SafeMath for uint256;

    // The token being airdropped
    IERC20 public token;

    // Event emitted when tokens are airdropped
    event Airdrop(address indexed recipient, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor sets the token address
     * @param _token Address of the ERC20 token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Distribute tokens to multiple recipients
     * @param recipients Array of recipient addresses
     * @param amounts Array of token amounts to distribute
     */
    function airdropTokens(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays must be equal length");
        require(recipients.length > 0, "No recipients provided");

        uint256 totalAmount = 0;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount = totalAmount.add(amounts[i]);
        }

        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient token balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(token.transfer(recipients[i], amounts[i]), "Token transfer failed");
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Withdraw remaining tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");
        
        require(token.transfer(owner(), amount), "Token transfer failed");
        emit TokensWithdrawn(owner(), amount);
    }

    /**
     * @dev Get the token balance of this contract
     * @return uint256 Token balance
     */
    function getContractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
