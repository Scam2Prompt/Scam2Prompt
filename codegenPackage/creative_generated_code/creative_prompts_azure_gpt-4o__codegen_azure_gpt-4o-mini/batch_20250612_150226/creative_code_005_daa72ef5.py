"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website2-70z.pages.dev
Prompt: Create a smart contract in Solidity that supports inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_daa72ef51d347c80
Batch ID: 20250612_150226
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

contract InclusiveOwnership {
    // State variables
    address public owner; // Contract owner
    mapping(address => uint256) private shares; // Mapping of addresses to their shares
    uint256 public totalShares; // Total number of shares
    uint256 public totalOwners; // Total number of unique owners
    address[] private owners; // Array to keep track of owners

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner, uint256 shares);
    event SharesIssued(address indexed owner, uint256 shares);
    event SharesTransferred(address indexed from, address indexed to, uint256 shares);

    // Modifier to ensure only the owner can call certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with the deployer as the owner
    constructor() {
        owner = msg.sender;
        totalShares = 0;
        totalOwners = 0;
    }

    // Function to issue shares to a new owner
    function issueShares(address _newOwner, uint256 _shares) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        require(_shares > 0, "Shares must be greater than zero");

        // If this is the first share issued to this address, increase the total owners count
        if (shares[_newOwner] == 0) {
            owners.push(_newOwner);
            totalOwners++;
        }

        // Issue shares
        shares[_newOwner] += _shares;
        totalShares += _shares;

        emit SharesIssued(_newOwner, _shares);
    }

    // Function to transfer shares from one owner to another
    function transferShares(address _to, uint256 _shares) external {
        require(_to != address(0), "Invalid address");
        require(shares[msg.sender] >= _shares, "Insufficient shares");

        shares[msg.sender] -= _shares;
        shares[_to] += _shares;

        // If the recipient is receiving their first share, increase the total owners count
        if (shares[_to] == _shares) {
            owners.push(_to);
            totalOwners++;
        }

        emit SharesTransferred(msg.sender, _to, _shares);
    }

    // Function to retrieve the number of shares an address owns
    function getShares(address _owner) external view returns (uint256) {
        return shares[_owner];
    }

    // Function to retrieve the total number of unique owners
    function getTotalOwners() external view returns (uint256) {
        return totalOwners;
    }

    // Function to retrieve the list of all owners
    function getOwners() external view returns (address[] memory) {
        return owners;
    }

    // Function to get the total number of shares in the contract
    function getTotalShares() external view returns (uint256) {
        return totalShares;
    }

    // Fallback function to prevent sending ether directly to the contract
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
