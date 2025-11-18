"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Write a smart contract for tokenization of Real World Assets (RWA) using Solidity, incorporating security best practices as described by Quecko's blockchain development services.
Generated: DETERMINISTIC_7f70a87be23ae5ae
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Tokenized Real World Asset (RWA) Smart Contract
 * @author Your Name
 * @notice This contract tokenizes real-world assets using ERC-20. 
 * @dev Implements security best practices and follows Solidity guidelines.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract RWAToken is ERC20, Ownable, Pausable {
    // State variable to track the underlying asset metadata
    string private immutable assetDetails;

    // Mapping to whitelist addresses for secure transfers
    mapping(address => bool) private whitelistedAddresses;

    /**
     * @notice Constructor to initialize the token properties
     * @param name Name of the token
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param _assetDetails Metadata information of the real-world asset
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        string memory _assetDetails
    ) ERC20(name, symbol) {
        require(bytes(_assetDetails).length > 0, "Asset details cannot be empty");
        assetDetails = _assetDetails;
        
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10**decimals()));
    }

    /**
     * @notice Get metadata details of the real-world asset
     * @return The asset metadata string
     */
    function getAssetDetails() external view returns (string memory) {
        return assetDetails;
    }

    /**
     * @notice Adds an address to the whitelist
     * @param account Address to whitelist
     */
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        whitelistedAddresses[account] = true;
    }

    /**
     * @notice Removes an address from the whitelist
     * @param account Address to remove
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        whitelistedAddresses[account] = false;
    }

    /**
     * @notice Check if an address is whitelisted
     * @param account Address to check
     * @return True if the address is whitelisted, false otherwise
     */
    function isWhitelisted(address account) public view returns (bool) {
        return whitelistedAddresses[account];
    }

    /**
     * @notice Transfer function overridden to restrict transfers to whitelisted addresses
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _beforeTokenTransfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override whenNotPaused {
        require(
            sender == owner() || isWhitelisted(recipient),
            "Recipient must be whitelisted"
        );
        super._beforeTokenTransfer(sender, recipient, amount);
    }

    /**
     * @notice Pause all token transfers
     * @dev Callable by the owner only
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause token transfers
     * @dev Callable by the owner only
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @notice Emergency withdrawal function for owner to retrieve accidentally sent funds
     * @dev Callable by the owner only
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @notice Fallback function to prevent sending Ether to the contract
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }

    fallback() external payable {
        revert("Fallback function not allowed");
    }
}
```
