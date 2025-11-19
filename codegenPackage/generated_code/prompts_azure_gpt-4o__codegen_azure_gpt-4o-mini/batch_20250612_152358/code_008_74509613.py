"""
Generated Code Metadata:
========================
Original URL: https://marvinonbase.pages.dev
Prompt: Implement a burn mechanism in Solidity for a token, where a percentage of transaction fees is automatically sent to a burn address, inspired by Marvin's collaboration with Shiba Inu.
Generated: DETERMINISTIC_7450961304fffaed
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BurnableToken is ERC20, Ownable {
    // Percentage of transaction fees to be burned (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage = 100; // 1%
    address public burnAddress = 0x000000000000000000000000000000000000dEaD;

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Override the _transfer function to include the burn mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000; // Convert basis points to percentage
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the burn amount to the burn address
        super._transfer(sender, burnAddress, burnAmount);
        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to update the burn percentage, only callable by the owner
    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 1000, "Burn percentage too high"); // Max 10%
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }

    // Function to withdraw any accidentally sent ERC20 tokens to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
