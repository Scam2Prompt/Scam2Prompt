"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerclaim-3po.pages.dev
Prompt: How does WienerAI ensure the security of its presale smart contracts?
Generated: DETERMINISTIC_6479cbd97e328603
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
pragma solidity ^0.8.17;

/**
 * @title WienerAI Presale Smart Contract
 * @notice This contract is designed to ensure security for the presale of WienerAI tokens.
 * @dev Implements best practices for security, access control, and error handling.
 */
contract WienerAIPresale {
    // State variables
    address public owner;                      // Contract owner
    uint256 public presalePrice;               // Price per token during presale
    uint256 public maxTokensPerWallet;         // Limit on maximum tokens per wallet
    uint256 public totalTokensAvailable;       // Total tokens available for presale
    mapping(address => uint256) public balances; // Tracks token balance per wallet

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(uint256 _presalePrice, uint256 _maxTokensPerWallet, uint256 _totalTokensAvailable) {
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_maxTokensPerWallet > 0, "Max tokens per wallet must be greater than zero");
        require(_totalTokensAvailable > 0, "Total tokens available must be greater than zero");

        owner = msg.sender;
        presalePrice = _presalePrice;
        maxTokensPerWallet = _maxTokensPerWallet;
        totalTokensAvailable = _totalTokensAvailable;
    }

    /**
     * @notice Purchase tokens during the presale.
     * @dev Ensures proper validation and security checks.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Cannot purchase zero tokens");
        require(
            balances[msg.sender] + _amount <= maxTokensPerWallet,
            "Purchase exceeds maximum tokens allowed per wallet"
        );
        require(
            totalTokensAvailable >= _amount,
            "Not enough tokens available for purchase"
        );
        require(
            msg.value == _amount * presalePrice,
            "Incorrect Ether value sent for purchase"
        );

        // Update state
        balances[msg.sender] += _amount;
        totalTokensAvailable -= _amount;

        // Emit event
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @notice Withdraw Ether from the contract.
     * @dev Restricted to the contract owner only.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @notice Transfer ownership of the contract to a new address.
     * @dev Restricted to the contract owner only.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @notice Get the contract's Ether balance.
     * @return The Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
