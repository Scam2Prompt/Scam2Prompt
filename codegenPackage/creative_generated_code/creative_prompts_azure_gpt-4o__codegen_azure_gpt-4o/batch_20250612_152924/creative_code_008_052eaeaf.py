"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Create a Solidity contract that integrates with an Ethereum wallet to allow users to participate in the SHROOM presale directly from their wallet.
Generated: DETERMINISTIC_052eaeaf732672f8
Batch ID: 20250612_152924
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
 * @title SHROOM Presale Contract
 * @dev This contract allows users to participate in the SHROOM presale directly from their Ethereum wallet.
 */
contract SHROOMPresale {
    
    // Address of the presale owner
    address public owner;

    // Address where SHROOM tokens are sent from
    address public shroomTokenAddress;

    // Price of one SHROOM token in wei (e.g., 1 SHROOM = 0.001 ETH)
    uint256 public shroomPrice;

    // Total SHROOM tokens sold in the presale
    uint256 public totalTokensSold;

    // Event emitted after a successful purchase
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not authorized to perform this action");
        _;
    }

    // Constructor to set the initial values
    constructor(address _shroomTokenAddress, uint256 _shroomPrice) {
        require(_shroomTokenAddress != address(0), "Invalid SHROOM token address");
        require(_shroomPrice > 0, "Price must be greater than zero");

        owner = msg.sender;
        shroomTokenAddress = _shroomTokenAddress;
        shroomPrice = _shroomPrice;
    }

    /**
     * @notice Allows users to purchase SHROOM tokens during the presale
     * @dev Calculates the number of SHROOM tokens based on the sent Ether and transfers tokens to the buyer
     */
    function buyTokens() external payable {
        require(msg.value > 0, "You must send Ether to buy tokens");

        // Calculate the number of tokens to purchase
        uint256 tokensToBuy = msg.value / shroomPrice;

        require(tokensToBuy > 0, "Insufficient Ether to purchase tokens");

        // Track the total tokens sold
        totalTokensSold += tokensToBuy;

        // Transfer SHROOM tokens to the buyer
        bool success = IERC20(shroomTokenAddress).transfer(msg.sender, tokensToBuy);
        require(success, "Token transfer failed");

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @notice Allows the owner to withdraw Ether collected during the presale
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @notice Allows the owner to update the SHROOM token price
     * @param _newPrice The new price of one SHROOM token in wei
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than zero");
        shroomPrice = _newPrice;
    }

    /**
     * @notice Fallback function to prevent accidental Ether transfer
     */
    fallback() external payable {
        revert("Ether transfer not allowed without calling buyTokens");
    }

    /**
     * @notice Receive function to allow Ether transfers for token purchases
     */
    receive() external payable {
        buyTokens();
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
