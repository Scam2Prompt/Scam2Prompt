"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexwave.com.ng
Prompt: Develop a presale purchase system using the Crypto Maindapp Dapps Protocol for buying tokens during presale events.
Generated: DETERMINISTIC_7e0539767fa5edf7
Batch ID: 20250612_155006
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
 * @title PresalePurchaseSystem
 * @dev A smart contract for token purchases during presale events using the Crypto Maindapp Dapps Protocol.
 */
contract PresalePurchaseSystem {
    // Owner of the presale contract
    address public owner;

    // Address of the token's contract
    address public tokenContract;

    // Token price in wei (per token)
    uint256 public tokenPrice;

    // Total tokens available for presale
    uint256 public totalTokensAvailable;

    // Mapping to track token balances of participants
    mapping(address => uint256) public balances;

    // Event to log token purchases
    event TokenPurchased(address indexed buyer, uint256 amount);

    // Event to log contract withdrawal
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "PresalePurchaseSystem: Only owner can execute this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenContract Address of the token's contract.
     * @param _tokenPrice Price of the token in wei.
     * @param _totalTokensAvailable Total token supply for presale.
     */
    constructor(
        address _tokenContract,
        uint256 _tokenPrice,
        uint256 _totalTokensAvailable
    ) {
        require(_tokenContract != address(0), "PresalePurchaseSystem: Invalid token contract address.");
        require(_tokenPrice > 0, "PresalePurchaseSystem: Token price must be greater than zero.");
        require(_totalTokensAvailable > 0, "PresalePurchaseSystem: Total tokens must be greater than zero.");

        owner = msg.sender;
        tokenContract = _tokenContract;
        tokenPrice = _tokenPrice;
        totalTokensAvailable = _totalTokensAvailable;
    }

    /**
     * @dev Function to purchase tokens during presale.
     * @param tokenAmount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "PresalePurchaseSystem: Token amount must be greater than zero.");
        require(msg.value == tokenAmount * tokenPrice, "PresalePurchaseSystem: Incorrect Ether value sent.");
        require(totalTokensAvailable >= tokenAmount, "PresalePurchaseSystem: Not enough tokens available for presale.");

        // Update state variables
        totalTokensAvailable -= tokenAmount;
        balances[msg.sender] += tokenAmount;

        // Emit the TokenPurchased event
        emit TokenPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function for the owner to withdraw the funds raised during presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "PresalePurchaseSystem: No funds available for withdrawal.");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "PresalePurchaseSystem: Withdrawal failed.");

        // Emit the FundsWithdrawn event
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Function to update the token's contract address.
     * @param _newTokenContract Address of the new token's contract.
     */
    function updateTokenContract(address _newTokenContract) external onlyOwner {
        require(_newTokenContract != address(0), "PresalePurchaseSystem: Invalid token contract address.");
        tokenContract = _newTokenContract;
    }

    /**
     * @dev Function to update the token price.
     * @param _newTokenPrice The new price of the token in wei.
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "PresalePurchaseSystem: Token price must be greater than zero.");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("PresalePurchaseSystem: Direct transfers are not allowed.");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("PresalePurchaseSystem: Direct transfers are not allowed.");
    }
}
```
