"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://not-claim.pages.dev
Prompt: Create a Solidity function that calculates and distributes $NOT tokens based on the "first come, first served" rule for the pre-sale. Ensure it handles refunds for late transactions.
Generated: DETERMINISTIC_8d65218b057402ff
Batch ID: 20250612_152235
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

/**
 * @title NOTTokenPresale
 * @dev Contract for handling first-come, first-served presale distribution of $NOT tokens.
 */
contract NOTTokenPresale {
    // Token parameters
    address public tokenAddress; // Address of the $NOT token contract
    uint256 public tokenRate;    // Number of tokens per 1 ether
    uint256 public presaleSupply; // Total supply available for presale
    uint256 public tokensSold;    // Total tokens sold so far

    // Owner of the contract
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event RefundIssued(address indexed buyer, uint256 refundAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the $NOT token.
     * @param _tokenRate Number of $NOT tokens per 1 ether.
     * @param _presaleSupply Total number of tokens available for presale.
     */
    constructor(address _tokenAddress, uint256 _tokenRate, uint256 _presaleSupply) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenRate > 0, "Token rate must be greater than zero");
        require(_presaleSupply > 0, "Presale supply must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenRate = _tokenRate;
        presaleSupply = _presaleSupply;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * Refunds excess Ether if tokens are sold out.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");
        require(tokensSold < presaleSupply, "Presale is sold out");

        // Calculate the number of tokens the buyer can receive
        uint256 tokensToBuy = msg.value * tokenRate;
        require(tokensToBuy > 0, "Insufficient Ether to buy tokens");

        // Calculate remaining tokens in the presale
        uint256 remainingTokens = presaleSupply - tokensSold;

        // Check if buyer is trying to buy more than the available supply
        if (tokensToBuy > remainingTokens) {
            tokensToBuy = remainingTokens; // Limit tokens to remaining supply

            // Calculate refund amount in Ether
            uint256 excessEther = (msg.value - (tokensToBuy / tokenRate));
            
            // Refund excess Ether to the buyer
            (bool refundSuccess, ) = msg.sender.call{value: excessEther}("");
            require(refundSuccess, "Refund failed");

            emit RefundIssued(msg.sender, excessEther);
        }

        // Update state
        tokensSold += tokensToBuy;

        // Transfer tokens to the buyer
        (bool tokenTransferSuccess, ) = tokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, tokensToBuy)
        );
        require(tokenTransferSuccess, "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to withdraw remaining Ether in the contract (only owner).
     */
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Function to update the token rate (only owner).
     * @param _newRate New rate for the $NOT tokens.
     */
    function updateTokenRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Token rate must be greater than zero");
        tokenRate = _newRate;
    }
}
```
