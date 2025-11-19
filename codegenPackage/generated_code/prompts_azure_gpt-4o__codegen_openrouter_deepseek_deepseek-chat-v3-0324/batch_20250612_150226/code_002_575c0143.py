"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Generate code for a smart contract that supports transparent and inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_575c01437dc9a809
Batch ID: 20250612_150226
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
 * @title InclusiveOwnership
 * @dev A smart contract for transparent and inclusive ownership models
 * reflecting the values of Innodapter ApS.
 */
contract InclusiveOwnership {
    // Struct to represent an owner with their details
    struct Owner {
        address walletAddress;
        string name;
        uint256 ownershipPercentage;
        uint256 joinDate;
        bool isActive;
    }

    // Mapping from owner address to Owner struct
    mapping(address => Owner) public owners;

    // Array to keep track of all owner addresses
    address[] public ownerAddresses;

    // Total ownership percentage (should sum to 100%)
    uint256 public totalOwnershipPercentage;

    // Events
    event OwnerAdded(address indexed ownerAddress, string name, uint256 ownershipPercentage);
    event OwnerUpdated(address indexed ownerAddress, string name, uint256 ownershipPercentage);
    event OwnerRemoved(address indexed ownerAddress);
    event OwnershipTransferred(address indexed from, address indexed to, uint256 percentage);

    // Modifier to check if caller is an owner
    modifier onlyOwner() {
        require(owners[msg.sender].isActive, "Caller is not an owner");
        _;
    }

    // Modifier to check if address is a valid owner
    modifier validOwner(address _ownerAddress) {
        require(_ownerAddress != address(0), "Invalid address");
        require(owners[_ownerAddress].isActive, "Address is not an active owner");
        _;
    }

    /**
     * @dev Add a new owner to the contract
     * @param _ownerAddress Address of the new owner
     * @param _name Name of the new owner
     * @param _ownershipPercentage Percentage of ownership
     */
    function addOwner(
        address _ownerAddress,
        string memory _name,
        uint256 _ownershipPercentage
    ) external onlyOwner {
        require(_ownerAddress != address(0), "Invalid address");
        require(!owners[_ownerAddress].isActive, "Owner already exists");
        require(_ownershipPercentage > 0, "Ownership percentage must be positive");
        require(
            totalOwnershipPercentage + _ownershipPercentage <= 100,
            "Total ownership cannot exceed 100%"
        );

        owners[_ownerAddress] = Owner({
            walletAddress: _ownerAddress,
            name: _name,
            ownershipPercentage: _ownershipPercentage,
            joinDate: block.timestamp,
            isActive: true
        });

        ownerAddresses.push(_ownerAddress);
        totalOwnershipPercentage += _ownershipPercentage;

        emit OwnerAdded(_ownerAddress, _name, _ownershipPercentage);
    }

    /**
     * @dev Update an existing owner's details
     * @param _ownerAddress Address of the owner to update
     * @param _name New name for the owner
     * @param _ownershipPercentage New ownership percentage
     */
    function updateOwner(
        address _ownerAddress,
        string memory _name,
        uint256 _ownershipPercentage
    ) external onlyOwner validOwner(_ownerAddress) {
        require(_ownershipPercentage > 0, "Ownership percentage must be positive");

        uint256 currentPercentage = owners[_ownerAddress].ownershipPercentage;
        require(
            totalOwnershipPercentage - currentPercentage + _ownershipPercentage <= 100,
            "Total ownership cannot exceed 100%"
        );

        owners[_ownerAddress].name = _name;
        totalOwnershipPercentage = totalOwnershipPercentage - currentPercentage + _ownershipPercentage;
        owners[_ownerAddress].ownershipPercentage = _ownershipPercentage;

        emit OwnerUpdated(_ownerAddress, _name, _ownershipPercentage);
    }

    /**
     * @dev Remove an owner from the contract
     * @param _ownerAddress Address of the owner to remove
     */
    function removeOwner(address _ownerAddress) external onlyOwner validOwner(_ownerAddress) {
        uint256 removedPercentage = owners[_ownerAddress].ownershipPercentage;
        owners[_ownerAddress].isActive = false;
        totalOwnershipPercentage -= removedPercentage;

        emit OwnerRemoved(_ownerAddress);
    }

    /**
     * @dev Transfer ownership percentage between owners
     * @param _from Address of the owner transferring ownership
     * @param _to Address of the owner receiving ownership
     * @param _percentage Percentage to transfer
     */
    function transferOwnership(
        address _from,
        address _to,
        uint256 _percentage
    ) external onlyOwner validOwner(_from) validOwner(_to) {
        require(_percentage > 0, "Percentage must be positive");
        require(
            owners[_from].ownershipPercentage >= _percentage,
            "Insufficient ownership percentage"
        );

        owners[_from].ownershipPercentage -= _percentage;
        owners[_to].ownershipPercentage += _percentage;

        emit OwnershipTransferred(_from, _to, _percentage);
    }

    /**
     * @dev Get total number of owners
     * @return uint256 Count of active owners
     */
    function getOwnerCount() external view returns (uint256) {
        return ownerAddresses.length;
    }

    /**
     * @dev Get all active owners' addresses
     * @return address[] Array of owner addresses
     */
    function getAllOwners() external view returns (address[] memory) {
        return ownerAddresses;
    }

    /**
     * @dev Get owner details by address
     * @param _ownerAddress Address of the owner
     * @return Owner struct with owner details
     */
    function getOwnerDetails(address _ownerAddress) external view returns (Owner memory) {
        return owners[_ownerAddress];
    }
}
```
