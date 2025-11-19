"""
Generated Code Metadata:
========================
Original URL: https://singularietyfinance.io
Prompt: Generate a Solidity smart contract code snippet for handling the token conversion from KEY to SFI at a conversion rate of 0.00125 SFI per KEY.
Generated: DETERMINISTIC_a2e34538b36c72d9
Batch ID: 20250622_212015
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

/**
 * @title TokenConverter
 * @dev A contract for converting KEY tokens to SFI tokens at a fixed rate.
 */
contract TokenConverter is Ownable {
    // The address of the KEY token contract
    IERC20 public keyToken;
    // The address of the SFI token contract
    IERC20 public sfiToken;
    // Conversion rate: 0.00125 SFI per KEY (in wei)
    uint256 public conversionRate = 1250; // 0.00125 SFI = 1250 wei

    event TokensConverted(address indexed user, uint256 keyAmount, uint256 sfiAmount);

    /**
     * @dev Constructor to set the token addresses.
     * @param _keyToken Address of the KEY token contract.
     * @param _sfiToken Address of the SFI token contract.
     */
    constructor(address _keyToken, address _sfiToken) {
        require(_keyToken != address(0), "Invalid KEY token address");
        require(_sfiToken != address(0), "Invalid SFI token address");
        
        keyToken = IERC20(_keyToken);
        sfiToken = IERC20(_sfiToken);
    }

    /**
     * @dev Converts KEY tokens to SFI tokens.
     * @param keyAmount The amount of KEY tokens to convert.
     */
    function convertTokens(uint256 keyAmount) external {
        require(keyAmount > 0, "Amount must be greater than zero");
        require(keyToken.balanceOf(msg.sender) >= keyAmount, "Insufficient KEY balance");
        
        // Calculate the amount of SFI tokens to be minted
        uint256 sfiAmount = (keyAmount * conversionRate) / 1000000; // Convert to SFI

        require(sfiToken.balanceOf(address(this)) >= sfiAmount, "Insufficient SFI balance in contract");

        // Transfer KEY tokens from the user to the contract
        keyToken.transferFrom(msg.sender, address(this), keyAmount);
        // Transfer SFI tokens from the contract to the user
        sfiToken.transfer(msg.sender, sfiAmount);

        emit TokensConverted(msg.sender, keyAmount, sfiAmount);
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens from the contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
