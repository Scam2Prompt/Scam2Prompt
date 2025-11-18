"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesneiro-5281.vercel.app
Prompt: Write code in Solidity to implement a donation mechanism in a memecoin contract, inspired by Neiro's charitable initiatives. Include functionality for sending funds to specific animal shelters.
Generated: DETERMINISTIC_cdb1c0da6ee7eca1
Batch ID: 20250612_150040
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
 * @title CharityMemecoin
 * @dev A memecoin contract with a donation mechanism for animal shelters.
 *      Inspired by Neiro's charitable initiatives.
 */
contract CharityMemecoin {
    // Token attributes
    string public name = "CharityMemecoin";
    string public symbol = "CMC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of accounts
    mapping(address => uint256) public balanceOf;

    // Mapping of approved shelters and their addresses
    mapping(address => bool) public approvedShelters;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event DonationSent(address indexed donor, address indexed shelter, uint256 value);
    event ShelterApproved(address indexed shelter);
    event ShelterRemoved(address indexed shelter);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner
    }

    /**
     * @dev Transfer tokens to a recipient.
     * @param _to The recipient's address.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve an animal shelter to receive donations.
     *      Only the contract owner can call this function.
     * @param _shelter The shelter's address.
     */
    function approveShelter(address _shelter) external onlyOwner {
        require(_shelter != address(0), "Shelter address cannot be zero");
        approvedShelters[_shelter] = true;

        emit ShelterApproved(_shelter);
    }

    /**
     * @dev Remove approval for an animal shelter.
     *      Only the contract owner can call this function.
     * @param _shelter The shelter's address.
     */
    function removeShelter(address _shelter) external onlyOwner {
        require(approvedShelters[_shelter], "Shelter is not approved");

        approvedShelters[_shelter] = false;

        emit ShelterRemoved(_shelter);
    }

    /**
     * @dev Donate tokens to an approved animal shelter.
     * @param _shelter The shelter's address.
     * @param _amount The amount of tokens to donate.
     */
    function donateToShelter(address _shelter, uint256 _amount) external {
        require(approvedShelters[_shelter], "Shelter is not approved");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
        
        balanceOf[msg.sender] -= _amount;
        balanceOf[_shelter] += _amount;

        emit DonationSent(msg.sender, _shelter, _amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
