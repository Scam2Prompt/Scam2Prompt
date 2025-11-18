"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zombi.finance
Prompt: Create a smart contract that interacts with a connected wallet to enable app access, based on the principles used by Zombi Finance.
Generated: DETERMINISTIC_61d1eb19860c8485
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Smart Contract for Wallet Access Management
 * @dev This contract allows wallet addresses to be added or removed from a whitelist,
 *      enabling access to specific application functionalities.
 */
contract WalletAccessManager is Ownable {
    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) private whitelistedAddresses;

    // Event emitted when an address is added to the whitelist
    event AddressAdded(address indexed addr);
    
    // Event emitted when an address is removed from the whitelist
    event AddressRemoved(address indexed addr);

    /**
     * @dev Modifier to check if the caller is whitelisted
     */
    modifier onlyWhitelisted() {
        require(isWhitelisted(msg.sender), "WalletAccessManager: Caller is not whitelisted");
        _;
    }

    /**
     * @dev Function to check if an address is whitelisted
     * @param _addr The address to check
     * @return bool True if the address is whitelisted, false otherwise
     */
    function isWhitelisted(address _addr) public view returns (bool) {
        return whitelistedAddresses[_addr];
    }

    /**
     * @dev Function to add an address to the whitelist
     * @param _addr The address to add
     * @notice Only the contract owner can call this function
     */
    function addAddressToWhitelist(address _addr) external onlyOwner {
        require(!isWhitelisted(_addr), "WalletAccessManager: Address is already whitelisted");
        whitelistedAddresses[_addr] = true;
        emit AddressAdded(_addr);
    }

    /**
     * @dev Function to remove an address from the whitelist
     * @param _addr The address to remove
     * @notice Only the contract owner can call this function
     */
    function removeAddressFromWhitelist(address _addr) external onlyOwner {
        require(isWhitelisted(_addr), "WalletAccessManager: Address is not whitelisted");
        delete whitelistedAddresses[_addr];
        emit AddressRemoved(_addr);
    }

    /**
     * @dev Function to perform an action restricted to whitelisted addresses
     * @notice This is an example function to demonstrate access control
     */
    function performAction() external onlyWhitelisted {
        // Logic for the action that can only be accessed by whitelisted addresses
        // TODO: Implement action logic
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to the contract
     * @param _token The address of the ERC20 token contract
     * @param _amount The amount of tokens to withdraw
     * @notice Only the contract owner can call this function
     */
    function withdrawTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "WalletAccessManager: Amount must be greater than zero");
        require(_token.balanceOf(address(this)) >= _amount, "WalletAccessManager: Insufficient balance");
        
        // Transfer tokens to the owner
        _token.transfer(owner(), _amount);
    }
}
```
