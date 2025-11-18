"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale with a cap of 1000 ETH and an exchange rate of 0.1 ETH for 99,500 tokens.
Generated: DETERMINISTIC_4d7928b5011c07ff
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
 * @title TokenPresale
 * @dev A smart contract to manage a capped token presale.
 * Users can send ETH to purchase tokens at a fixed exchange rate.
 */
contract TokenPresale {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public constant presaleCap = 1000 ether; // Maximum ETH to be raised in presale
    uint256 public totalRaised; // Total ETH raised so far
    uint256 public constant exchangeRate = 99500; // Number of tokens per 0.1 ETH
    uint256 public constant ethUnit = 0.1 ether; // Unit of exchange for tokens
    IERC20 public token; // Reference to the token contract

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the token address and contract owner.
     * @param _token Address of the ERC20 token being sold.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        owner = msg.sender;
        token = IERC20(_token);
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function purchaseTokens() external payable {
        // Validate that the sent ETH amount is a multiple of 0.1 ETH
        require(msg.value > 0 && msg.value % ethUnit == 0, "ETH amount must be a multiple of 0.1 ETH");
        // Ensure the presale cap is not exceeded
        require(totalRaised + msg.value <= presaleCap, "Presale cap exceeded");

        // Calculate the number of tokens to be transferred
        uint256 tokenAmount = (msg.value / ethUnit) * exchangeRate;

        // Ensure the contract has enough tokens to transfer
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");

        // Update the total ETH raised
        totalRaised += msg.value;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokenAmount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Function for the owner to withdraw the raised ETH.
     * Can only be called by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Function for the owner to withdraw remaining tokens after the presale.
     * Can only be called by the owner.
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens to withdraw");
        token.transfer(owner, remainingTokens);
    }

    /**
     * @dev Fallback function to reject accidental ETH transfers.
     */
    receive() external payable {
        revert("Use the purchaseTokens function to buy tokens");
    }
}

/**
 * @dev Interface for ERC20 tokens to interact with the token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
