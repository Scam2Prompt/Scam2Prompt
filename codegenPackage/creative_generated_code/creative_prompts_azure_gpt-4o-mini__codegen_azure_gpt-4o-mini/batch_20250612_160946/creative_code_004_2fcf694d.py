"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigknes33h76f7skpeenkp5p5s74x65rjrgymqbdmpd2i3kufhzxqe.ipfs.dweb.link
Prompt: How do I set up an airdrop event for a cryptocurrency like $SLOTH using Ethereum?
Generated: DETERMINISTIC_2fcf694d1525e70a
Batch ID: 20250612_160946
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Airdrop is Ownable {
    using SafeMath for uint256;

    // Address of the ERC20 token being airdropped
    IERC20 public token;

    // Mapping to track addresses that have already received the airdrop
    mapping(address => bool) public hasClaimed;

    // Event to emit when airdrop is successful
    event AirdropClaimed(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    /**
     * @notice Function to execute the airdrop to a list of specified addresses
     * @param recipients Array of addresses to receive airdrop
     * @param amounts Array of amounts corresponding to each recipient
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(!hasClaimed[recipients[i]], "Recipient has already claimed");
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer the specified amount of tokens to the recipient
            token.transfer(recipients[i], amounts[i]);

            // Mark recipient as having claimed the airdrop
            hasClaimed[recipients[i]] = true;

            // Emit the event for successful airdrop
            emit AirdropClaimed(recipients[i], amounts[i]);
        }
    }

    /**
     * @notice Function to withdraw any tokens (in case of emergency)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.transfer(msg.sender, amount);
    }

    /**
     * @notice Function to check the contract's token balance
     * @return The balance of the contract in the token
     */
    function balance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```

In this code, the `Airdrop` contract handles the distribution of a specified ERC20 token to a list of recipients, ensuring that no address can claim multiple times and that all calls are restricted to the contract owner. Functions for withdrawing leftover tokens and checking the contract's balance are also included for operational flexibility.
