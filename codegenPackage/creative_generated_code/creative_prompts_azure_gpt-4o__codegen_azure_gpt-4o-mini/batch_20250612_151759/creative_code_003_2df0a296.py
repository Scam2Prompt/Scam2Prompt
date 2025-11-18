"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: Provide an example of airdrop distribution logic in Solidity for an Ethereum-based memecoin, referencing the features of "Owy."
Generated: DETERMINISTIC_2df0a296fb4e07ea
Batch ID: 20250612_151759
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
 * @title OwyAirdrop
 * @dev A contract to manage the airdrop distribution of Owy tokens.
 * The contract allows an owner to distribute Owy tokens to multiple recipients.
 */
contract OwyAirdrop is Ownable {
    IERC20 public owyToken; // Reference to the Owy token contract

    // Event to log the airdrop distribution
    event AirdropExecuted(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the Owy token address.
     * @param _owyToken Address of the Owy token contract.
     */
    constructor(address _owyToken) {
        require(_owyToken != address(0), "Invalid token address");
        owyToken = IERC20(_owyToken);
    }

    /**
     * @dev Distributes Owy tokens to multiple recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of amounts to distribute, corresponding to each recipient.
     */
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched lengths");
        require(recipients.length > 0, "No recipients provided");

        uint256 totalAmount = 0;

        for (uint256 i = 0; i < amounts.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            totalAmount += amounts[i];
        }

        // Transfer total amount from the contract to the recipients
        require(owyToken.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            // Transfer tokens to the recipient
            owyToken.transfer(recipients[i], amounts[i]);
            emit AirdropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Withdraw tokens from the contract in case of emergency.
     * Only the owner can call this function.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(owyToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        owyToken.transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
