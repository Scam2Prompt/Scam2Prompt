"""
Generated Code Metadata:
========================
Original URL: https://explorer-dapp.pages.dev
Prompt: Generate a smart contract template for a decentralized application that ensures censorship resistance and immutability, aligning with the principles outlined by Dapp Protocol.
Generated: DETERMINISTIC_1c4031f6d1b9da5e
Batch ID: 20250612_145459
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
 * @title CensorshipResistantDapp
 * @dev A template for decentralized applications ensuring censorship resistance and immutability
 * @notice Implements core principles of the Dapp Protocol
 */
contract CensorshipResistantDapp {
    // State variables
    address public immutable owner;
    bool public isImmutable;
    uint256 public contentCount;
    
    // Events
    event ContentAdded(uint256 indexed id, address indexed author, string content, uint256 timestamp);
    event ImmutabilityEnabled(address indexed enabler, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Struct to store content
    struct Content {
        address author;
        string data;
        uint256 timestamp;
    }
    
    // Mapping to store all content
    mapping(uint256 => Content) public contents;
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier notImmutable() {
        require(!isImmutable, "Contract is immutable");
        _;
    }
    
    /**
     * @dev Constructor sets the initial owner
     */
    constructor() {
        owner = msg.sender;
        isImmutable = false;
        contentCount = 0;
    }
    
    /**
     * @dev Add new content to the contract
     * @param _content The content to be added
     */
    function addContent(string memory _content) public notImmutable {
        require(bytes(_content).length > 0, "Content cannot be empty");
        
        contentCount++;
        contents[contentCount] = Content({
            author: msg.sender,
            data: _content,
            timestamp: block.timestamp
        });
        
        emit ContentAdded(contentCount, msg.sender, _content, block.timestamp);
    }
    
    /**
     * @dev Enable immutability - makes the contract permanently unchangeable
     */
    function enableImmutability() public onlyOwner notImmutable {
        isImmutable = true;
        emit ImmutabilityEnabled(msg.sender, block.timestamp);
    }
    
    /**
     * @dev Transfer ownership to a new address
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) public onlyOwner notImmutable {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    /**
     * @dev Get content by ID
     * @param id The ID of the content to retrieve
     * @return The content struct
     */
    function getContent(uint256 id) public view returns (Content memory) {
        require(id <= contentCount && id != 0, "Invalid content ID");
        return contents[id];
    }
    
    /**
     * @dev Get total content count
     * @return The total number of content items
     */
    function getContentCount() public view returns (uint256) {
        return contentCount;
    }
}
```
