"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-merlinstartercom.pages.dev
Prompt: Create a Solidity smart contract to distribute $MP tokens as part of an airdrop campaign, ensuring compatibility with MerlinChain.
Generated: DETERMINISTIC_0c2c4a324e2c4b93
Batch ID: 20250612_153648
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

// Importing the ERC20 interface to interact with the $MP token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract to distribute $MP tokens on MerlinChain
contract Airdrop is Ownable {
    // The ERC20 token to be distributed
    IERC20 public mpToken;

    // Event to log airdrop distribution
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(address _mpToken) {
        require(_mpToken != address(0), "Invalid token address");
        mpToken = IERC20(_mpToken);
    }

    // Function to distribute tokens to a list of recipients
    // Only the owner can call this function
    function distributeAirdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");
        require(mpToken.balanceOf(address(this)) >= amount * recipients.length, "Insufficient token balance in contract");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            // Transfer the specified amount to each recipient
            mpToken.transfer(recipients[i], amount);
            emit AirdropDistributed(recipients[i], amount);
        }
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= amount, "Insufficient token balance");

        token.transfer(msg.sender, amount);
    }

    // Function to retrieve contract's balance of $MP tokens
    function getTokenBalance() external view returns (uint256) {
        return mpToken.balanceOf(address(this));
    }
}
```
