"""
Generated Code Metadata:
========================
Original URL: https://ethkta.com
Prompt: Generate code for a simple Ethereum pledge smart contract using Solidity.
Generated: DETERMINISTIC_342b4cae02285f03
Batch ID: 20250622_204829
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
 * @title SimplePledgeContract
 * @dev A smart contract that allows users to make pledges in ETH
 * and tracks the total amount pledged. The owner can withdraw funds.
 */
contract SimplePledgeContract {
    // Owner of the contract
    address public owner;
    
    // Total amount pledged in wei
    uint256 public totalPledged;
    
    // Mapping of pledger addresses to their pledged amounts
    mapping(address => uint256) public pledges;
    
    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);
    
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed owner, uint256 amount);
    
    /**
     * @dev Constructor sets the owner as the deployer
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Modifier to restrict functions to owner only
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Allows users to make a pledge by sending ETH
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;
        
        emit Pledged(msg.sender, msg.value);
    }
    
    /**
     * @dev Allows the owner to withdraw all pledged funds
     */
    function withdraw() external onlyOwner {
        require(totalPledged > 0, "No funds to withdraw");
        
        uint256 amount = totalPledged;
        totalPledged = 0;
        
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawn(owner, amount);
    }
    
    /**
     * @dev Returns the pledge amount for a specific address
     * @param _pledger Address to query
     * @return uint256 Pledge amount in wei
     */
    function getPledge(address _pledger) external view returns (uint256) {
        return pledges[_pledger];
    }
}
```
