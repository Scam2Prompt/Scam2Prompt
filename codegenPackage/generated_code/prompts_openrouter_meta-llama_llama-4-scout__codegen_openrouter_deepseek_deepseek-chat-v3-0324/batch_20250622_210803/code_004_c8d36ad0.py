"""
Generated Code Metadata:
========================
Original URL: https://kamino-checker.vercel.app
Prompt: Create a function in Solidity that checks if a given Ethereum address is eligible for the Kamino airdrop, inspired by the Kamino Airdrop Checker tool.
Generated: DETERMINISTIC_c8d36ad0b916c5c8
Batch ID: 20250622_210803
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
 * @title KaminoAirdropChecker
 * @dev Contract to check eligibility for Kamino airdrop based on various criteria
 */
contract KaminoAirdropChecker {
    // Mapping to store eligible addresses
    mapping(address => bool) private eligibleAddresses;
    
    // Address of the contract owner
    address private owner;
    
    // Minimum ETH balance required to be eligible
    uint256 public constant MIN_BALANCE = 0.1 ether;
    
    // Minimum number of transactions required
    uint256 public constant MIN_TX_COUNT = 3;
    
    // Event emitted when eligibility is checked
    event EligibilityChecked(address indexed user, bool isEligible);
    
    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Modifier to restrict function access to owner only
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Add addresses to the eligible list (only callable by owner)
     * @param _addresses Array of addresses to mark as eligible
     */
    function addEligibleAddresses(address[] memory _addresses) external onlyOwner {
        for (uint i = 0; i < _addresses.length; i++) {
            eligibleAddresses[_addresses[i]] = true;
        }
    }
    
    /**
     * @dev Check if an address is eligible for the airdrop
     * @param _address Address to check eligibility for
     * @return bool True if address is eligible, false otherwise
     */
    function isEligible(address _address) external view returns (bool) {
        return eligibleAddresses[_address];
    }
    
    /**
     * @dev Check eligibility based on multiple criteria
     * @param _address Address to check
     * @param _balance Current ETH balance of the address
     * @param _txCount Number of transactions made by the address
     * @return bool True if eligible, false otherwise
     */
    function checkEligibility(
        address _address,
        uint256 _balance,
        uint256 _txCount
    ) external returns (bool) {
        bool isEligible = eligibleAddresses[_address] || 
                         (_balance >= MIN_BALANCE && _txCount >= MIN_TX_COUNT);
        
        emit EligibilityChecked(_address, isEligible);
        return isEligible;
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
    
    /**
     * @dev Get the current owner of the contract
     * @return address Current owner address
     */
    function getOwner() external view returns (address) {
        return owner;
    }
}
```
