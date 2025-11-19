"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Develop a Solidity smart contract that implements a mechanism for redistributing exit fees to all token holders proportionally, as described on BibbyDivs.com.
Generated: DETERMINISTIC_d517a1b833662c40
Batch ID: 20250612_150316
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

contract BibbyDivs is Ownable {
    using SafeMath for uint256;

    // Token to be used for the redistribution
    IERC20 public token;

    // Total exit fees collected
    uint256 public totalExitFees;

    // Mapping to track the last claimed fee for each holder
    mapping(address => uint256) public lastClaimed;

    // Event to log fee redistribution
    event FeesRedistributed(address indexed holder, uint256 amount);

    // Constructor to set the token address
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    // Function to collect exit fees
    function collectExitFees(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalExitFees = totalExitFees.add(amount);
    }

    // Function to redistribute fees to all token holders
    function redistributeFees() external {
        uint256 totalSupply = token.totalSupply();
        require(totalSupply > 0, "No tokens in circulation");

        // Calculate the amount to distribute per token
        uint256 amountPerToken = totalExitFees.div(totalSupply);

        // Iterate through all token holders and distribute fees
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = token.holderAt(i); // Assuming a function to get holder by index
            uint256 holderBalance = token.balanceOf(holder);
            if (holderBalance > 0) {
                uint256 amountToSend = holderBalance.mul(amountPerToken);
                lastClaimed[holder] = lastClaimed[holder].add(amountToSend);
                emit FeesRedistributed(holder, amountToSend);
            }
        }

        // Reset total exit fees after redistribution
        totalExitFees = 0;
    }

    // Function for holders to claim their fees
    function claimFees() external {
        uint256 amount = lastClaimed[msg.sender];
        require(amount > 0, "No fees to claim");

        // Transfer the fees to the holder
        lastClaimed[msg.sender] = 0;
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
