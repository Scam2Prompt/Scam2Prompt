"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxdeapp1-30yk70q14-goshimadev.vercel.app
Prompt: Explain how to use the Stellar0x contract address to purchase $Stellar0x tokens on Ethereum, and provide a sample Solidity function for interacting with the contract.
Generated: DETERMINISTIC_822186b1c46e199a
Batch ID: 20250612_152620
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
 * @title Stellar0xTokenPurchase
 * @dev A simple contract to interact with the Stellar0x contract and purchase $Stellar0x tokens.
 * Assumes the Stellar0x contract follows the ERC-20 standard.
 */
contract Stellar0xTokenPurchase {
    address public owner; // Owner of the contract
    address public stellar0xContractAddress; // Address of the Stellar0x contract

    // Event to emit after a successful token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner and Stellar0x contract address.
     * @param _stellar0xContractAddress The address of the Stellar0x ERC-20 token contract.
     */
    constructor(address _stellar0xContractAddress) {
        require(_stellar0xContractAddress != address(0), "Invalid contract address");
        owner = msg.sender;
        stellar0xContractAddress = _stellar0xContractAddress;
    }

    /**
     * @dev Function to purchase $Stellar0x tokens.
     * Transfers Ether to the Stellar0x contract and expects tokens in return.
     * Assumes the contract implements a payable `buyTokens()` function.
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(msg.value > 0, "Ether value must be greater than zero");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Interface to interact with the Stellar0x contract
        IERC20 stellar0xContract = IERC20(stellar0xContractAddress);

        // Call the Stellar0x contract's `buyTokens()` function
        (bool success, ) = stellar0xContractAddress.call{value: msg.value}(
            abi.encodeWithSignature("buyTokens(uint256)", tokenAmount)
        );
        require(success, "Token purchase failed");

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function to withdraw Ether from the contract (only for the owner).
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to update the Stellar0x contract address (only for the owner).
     * @param _newAddress The new address of the Stellar0x ERC-20 token contract.
     */
    function updateStellar0xContractAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid contract address");
        stellar0xContractAddress = _newAddress;
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}

    /**
     * @dev Interface for interacting with ERC-20 tokens.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }
}
```
