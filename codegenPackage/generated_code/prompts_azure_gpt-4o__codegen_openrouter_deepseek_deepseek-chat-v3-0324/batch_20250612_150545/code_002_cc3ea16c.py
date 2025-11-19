"""
Generated Code Metadata:
========================
Original URL: https://nanaclaimsio.web.app
Prompt: Generate a smart contract in Solidity or Rust to facilitate irreversible DeFi payments directly to merchants, as outlined in the Helio platform's disclaimer.
Generated: DETERMINISTIC_cc3ea16cb8644ed2
Batch ID: 20250612_150545
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

/**
 * @title HelioPayment
 * @dev A smart contract for irreversible DeFi payments to merchants
 * @notice This contract facilitates direct payments to merchants with no refund mechanism
 */
contract HelioPayment {
    // Merchant information struct
    struct Merchant {
        address payable walletAddress;
        bool isActive;
    }

    // Mapping of merchant IDs to Merchant struct
    mapping(string => Merchant) public merchants;
    
    // Contract owner
    address public owner;
    
    // Events
    event MerchantRegistered(string merchantId, address walletAddress);
    event MerchantStatusChanged(string merchantId, bool isActive);
    event PaymentProcessed(string merchantId, address from, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyActiveMerchant(string memory merchantId) {
        require(merchants[merchantId].isActive, "Merchant is not active");
        _;
    }

    /**
     * @dev Constructor sets the deployer as the initial owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new merchant
     * @param merchantId Unique identifier for the merchant
     * @param walletAddress Ethereum address where payments will be sent
     */
    function registerMerchant(string memory merchantId, address payable walletAddress) external onlyOwner {
        require(walletAddress != address(0), "Invalid wallet address");
        require(bytes(merchantId).length > 0, "Merchant ID cannot be empty");
        require(merchants[merchantId].walletAddress == address(0), "Merchant already registered");

        merchants[merchantId] = Merchant({
            walletAddress: walletAddress,
            isActive: true
        });

        emit MerchantRegistered(merchantId, walletAddress);
    }

    /**
     * @dev Toggle merchant active status
     * @param merchantId Merchant identifier
     * @param isActive New status (true = active, false = inactive)
     */
    function setMerchantStatus(string memory merchantId, bool isActive) external onlyOwner {
        require(merchants[merchantId].walletAddress != address(0), "Merchant not found");
        merchants[merchantId].isActive = isActive;
        emit MerchantStatusChanged(merchantId, isActive);
    }

    /**
     * @dev Process payment to merchant
     * @param merchantId Merchant identifier
     */
    function payMerchant(string memory merchantId) external payable onlyActiveMerchant(merchantId) {
        require(msg.value > 0, "Payment amount must be greater than 0");
        
        Merchant storage merchant = merchants[merchantId];
        (bool sent, ) = merchant.walletAddress.call{value: msg.value}("");
        require(sent, "Failed to send payment to merchant");

        emit PaymentProcessed(merchantId, msg.sender, msg.value);
    }

    /**
     * @dev Transfer contract ownership
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Get merchant details
     * @param merchantId Merchant identifier
     * @return walletAddress Merchant's payment address
     * @return isActive Merchant's active status
     */
    function getMerchant(string memory merchantId) external view returns (address walletAddress, bool isActive) {
        Merchant memory merchant = merchants[merchantId];
        return (merchant.walletAddress, merchant.isActive);
    }
}
```
