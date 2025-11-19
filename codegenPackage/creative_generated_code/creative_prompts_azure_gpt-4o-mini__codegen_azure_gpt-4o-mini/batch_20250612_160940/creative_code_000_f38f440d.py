"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token sale that includes a presale cap of 1000 ETH and a conversion rate of 1 ETH to 99,500 BCKR.
Generated: DETERMINISTIC_f38f440d9d85d7fb
Batch ID: 20250612_160940
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
 * @title TokenSale
 * @dev Smart contract for a token sale with a presale cap and conversion rate.
 */
contract TokenSale is Ownable {
    // The token being sold
    IERC20 public token;
    
    // Conversion rate from ETH to tokens
    uint256 public constant RATE = 99500; // 1 ETH = 99,500 BCKR
    
    // Presale cap in ETH
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 ETH

    // Amount raised in ETH
    uint256 public amountRaised;

    // Event to log token purchase
    event TokensPurchased(address indexed purchaser, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress Address of the token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Function to buy tokens with ETH.
     */
    function buyTokens() public payable {
        // Check if cap has been reached
        require(amountRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");
        
        // Calculate token amount to be created
        uint256 tokens = msg.value * RATE;

        // Update the amount raised
        amountRaised += msg.value;

        // Transfer the tokens to the purchaser
        require(token.transfer(msg.sender, tokens), "Token transfer failed");

        // Emit event
        emit TokensPurchased(msg.sender, tokens);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to check the balance of the contract.
     * @return address of the contract's ETH balance
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
