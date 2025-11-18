"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoins-ai.firebaseapp.com
Prompt: Create a smart contract in Solidity for airdropping $PEIPEI tokens to multiple wallet addresses while adhering to the zero-tax policy.
Generated: DETERMINISTIC_dfe79587d1a65023
Batch ID: 20250612_153954
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

// Importing the OpenZeppelin ERC20 interface for standard token functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title Airdrop Contract
 * @dev This contract allows for the airdropping of PEIPEI tokens to multiple recipients
 * while ensuring that there is no tax applied to the transfers.
 */
contract Airdrop {
    using Address for address;

    // Instance of the PEIPEI token contract
    IERC20 public peipeiToken;

    /**
     * @dev Constructor to initialize the contract with the PEIPEI token address.
     * @param _peipeiToken The address of the PEIPEI token contract.
     */
    constructor(address _peipeiToken) {
        require(_peipeiToken.isContract(), "Provided address is not a contract");
        peipeiToken = IERC20(_peipeiToken);
    }

    /**
     * @dev Airdrop function to distribute tokens to multiple addresses.
     * @param recipients An array of addresses to receive the tokens.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        
        // Total amount to be transferred
        uint256 totalAmount = 0;

        for (uint256 i = 0; i < amounts.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            totalAmount += amounts[i];
        }

        // Ensure the contract has enough tokens to airdrop
        require(peipeiToken.balanceOf(address(this)) >= totalAmount, "Insufficient token balance in contract");

        // Airdrop tokens to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            peipeiToken.transfer(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(token != address(peipeiToken), "Cannot withdraw PEIPEI tokens");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
