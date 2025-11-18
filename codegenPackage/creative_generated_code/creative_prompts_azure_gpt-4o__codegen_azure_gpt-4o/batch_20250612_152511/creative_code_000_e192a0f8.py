"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buytoken-scapesmania.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the ScapesMania presale, including functionality to restrict purchases based on unsupported jurisdictions.
Generated: DETERMINISTIC_e192a0f886eeda71
Batch ID: 20250612_152511
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
 * @dev A smart contract for managing a token presale with restriction based on unsupported jurisdictions.
 */
contract TokenPresale {
    // Token presale details
    address public owner; // Address of the contract owner
    uint256 public tokenPriceInWei; // Price of one token in wei
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Tokens sold so far
    bool public presaleActive; // Flag to indicate if the presale is active

    // Mapping to track restricted jurisdictions (unsupported jurisdictions)
    mapping(address => bool) public restrictedAddresses;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount);
    event RestrictedAddressAdded(address indexed restrictedAddress);
    event RestrictedAddressRemoved(address indexed restrictedAddress);
    event PresaleStatusUpdated(bool isActive);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Modifier to ensure the caller is not from a restricted jurisdiction
    modifier notRestricted() {
        require(!restrictedAddresses[msg.sender], "Address is restricted from participating in the presale");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenPriceInWei Price of one token in wei.
     * @param _totalTokensForSale Total number of tokens available for presale.
     */
    constructor(uint256 _tokenPriceInWei, uint256 _totalTokensForSale) {
        require(_tokenPriceInWei > 0, "Token price must be greater than 0");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than 0");

        owner = msg.sender;
        tokenPriceInWei = _tokenPriceInWei;
        totalTokensForSale = _totalTokensForSale;
        presaleActive = false; // Start with presale inactive
    }

    /**
     * @dev Purchase tokens during presale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable whenPresaleActive notRestricted {
        require(_amount > 0, "Amount must be greater than 0");
        require(tokensSold + _amount <= totalTokensForSale, "Not enough tokens available for sale");
        require(msg.value == _amount * tokenPriceInWei, "Incorrect Ether value sent");

        tokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Add an address to the restricted list.
     * @param _address Address to restrict.
     */
    function addRestrictedAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        restrictedAddresses[_address] = true;

        emit RestrictedAddressAdded(_address);
    }

    /**
     * @dev Remove an address from the restricted list.
     * @param _address Address to remove from restriction.
     */
    function removeRestrictedAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        restrictedAddresses[_address] = false;

        emit RestrictedAddressRemoved(_address);
    }

    /**
     * @dev Toggle presale status (active/inactive).
     * @param _status Boolean indicating presale status.
     */
    function updatePresaleStatus(bool _status) external onlyOwner {
        presaleActive = _status;
        emit PresaleStatusUpdated(_status);
    }

    /**
     * @dev Withdraw Ether collected during presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to prevent unintended Ether transfers.
     */
    fallback() external payable {
        revert("Fallback function does not accept Ether");
    }

    /**
     * @dev Receive function to prevent unintended Ether transfers.
     */
    receive() external payable {
        revert("Receive function does not accept Ether");
    }
}
```
