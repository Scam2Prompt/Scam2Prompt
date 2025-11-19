"""
Generated Code Metadata:
========================
Original URL: https://dxldao.org
Prompt: Write a smart contract snippet that checks wallet access requirements before allowing interaction with a DAO platform, inspired by dxldao.org.
Generated: DETERMINISTIC_a6b96531a5313e33
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract DAOAccessControl is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Minimum token balance required for access
    uint256 public minTokenBalance;
    
    // Token contract address
    address public tokenContract;
    
    // Whitelisted addresses set
    EnumerableSet.AddressSet private _whitelistedAddresses;

    event AccessGranted(address indexed account);
    event AccessRevoked(address indexed account);
    event MinTokenBalanceUpdated(uint256 newMinBalance);
    event TokenContractUpdated(address newTokenContract);

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenContract Address of the token contract
     * @param _minTokenBalance Minimum token balance required for access
     */
    constructor(address _tokenContract, uint256 _minTokenBalance) {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
        minTokenBalance = _minTokenBalance;
    }

    /**
     * @dev Check if an address has access to the DAO
     * @param account Address to check
     * @return bool True if address has access, false otherwise
     */
    function hasAccess(address account) public view returns (bool) {
        // Check if address is whitelisted
        if (_whitelistedAddresses.contains(account)) {
            return true;
        }

        // Check token balance if token contract is set
        if (tokenContract != address(0)) {
            (bool success, bytes memory data) = tokenContract.staticcall(
                abi.encodeWithSignature("balanceOf(address)", account)
            );
            
            if (success) {
                uint256 balance = abi.decode(data, (uint256));
                return balance >= minTokenBalance;
            }
        }

        return false;
    }

    /**
     * @dev Grant access to a specific address (owner only)
     * @param account Address to whitelist
     */
    function grantAccess(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        _whitelistedAddresses.add(account);
        emit AccessGranted(account);
    }

    /**
     * @dev Revoke access from a specific address (owner only)
     * @param account Address to remove from whitelist
     */
    function revokeAccess(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        _whitelistedAddresses.remove(account);
        emit AccessRevoked(account);
    }

    /**
     * @dev Update minimum token balance required for access (owner only)
     * @param newMinBalance New minimum token balance
     */
    function updateMinTokenBalance(uint256 newMinBalance) external onlyOwner {
        minTokenBalance = newMinBalance;
        emit MinTokenBalanceUpdated(newMinBalance);
    }

    /**
     * @dev Update token contract address (owner only)
     * @param newTokenContract Address of the new token contract
     */
    function updateTokenContract(address newTokenContract) external onlyOwner {
        require(newTokenContract != address(0), "Invalid token contract address");
        tokenContract = newTokenContract;
        emit TokenContractUpdated(newTokenContract);
    }

    /**
     * @dev Get list of whitelisted addresses
     * @return address[] Array of whitelisted addresses
     */
    function getWhitelistedAddresses() external view returns (address[] memory) {
        return _whitelistedAddresses.values();
    }

    /**
     * @dev Check if address is whitelisted
     * @param account Address to check
     * @return bool True if whitelisted, false otherwise
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAddresses.contains(account);
    }
}
```
