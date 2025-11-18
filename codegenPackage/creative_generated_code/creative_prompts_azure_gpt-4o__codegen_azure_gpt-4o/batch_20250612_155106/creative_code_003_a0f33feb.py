"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kodiak-finance.org
Prompt: Create a smart contract in Solidity that mimics Kodiak Finance's automated yield strategies by dynamically reallocating funds across DeFi protocols based on real-time yield data.
Generated: DETERMINISTIC_a0f33feb98a84bd8
Batch ID: 20250612_155106
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
 * @title YieldAllocator
 * @author [Your Name]
 * @notice A smart contract that dynamically reallocates funds across DeFi protocols
 *         based on real-time yield data to maximize returns.
 */
contract YieldAllocator {
    // Struct to represent a DeFi protocol
    struct Protocol {
        string name;                // Name of the protocol
        address protocolAddress;    // Address of the protocol's contract
        uint256 allocationPercentage; // Allocation percentage (0-100)
    }

    address public owner; // Contract owner
    Protocol[] public protocols; // List of DeFi protocols
    uint256 public totalFunds; // Total funds managed by the contract

    // Events
    event FundsReallocated(
        uint256 timestamp,
        address indexed user,
        uint256 totalFunds,
        uint256[] allocations
    );
    event ProtocolAdded(string name, address protocolAddress);
    event ProtocolRemoved(string name, address protocolAddress);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure percentage allocations are valid
    modifier validAllocationPercentages() {
        uint256 totalPercentage = 0;
        for (uint256 i = 0; i < protocols.length; i++) {
            totalPercentage += protocols[i].allocationPercentage;
        }
        require(totalPercentage == 100, "Invalid allocation percentages");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds a new DeFi protocol to the list of managed protocols.
     * @param name The name of the protocol.
     * @param protocolAddress The contract address of the protocol.
     * @param allocationPercentage Allocation percentage (0-100).
     */
    function addProtocol(
        string memory name,
        address protocolAddress,
        uint256 allocationPercentage
    ) public onlyOwner validAllocationPercentages {
        Protocol memory newProtocol = Protocol(
            name,
            protocolAddress,
            allocationPercentage
        );
        protocols.push(newProtocol);
        emit ProtocolAdded(name, protocolAddress);
    }

    /**
     * @dev Removes a DeFi protocol from the list of managed protocols.
     * @param index Index of the protocol to remove in the array.
     */
    function removeProtocol(uint256 index) public onlyOwner {
        require(index < protocols.length, "Invalid index");

        Protocol memory removedProtocol = protocols[index];
        for (uint256 i = index; i < protocols.length - 1; i++) {
            protocols[i] = protocols[i + 1];
        }
        protocols.pop();

        emit ProtocolRemoved(removedProtocol.name, removedProtocol.protocolAddress);
    }

    /**
     * @dev Reallocates funds based on the current allocation percentages.
     */
    function reallocateFunds() public onlyOwner validAllocationPercentages {
        uint256[] memory allocations = new uint256[](protocols.length);

        for (uint256 i = 0; i < protocols.length; i++) {
            uint256 allocationAmount = (totalFunds *
                protocols[i].allocationPercentage) / 100;

            // Assuming protocolAddress supports a deposit function
            (bool success, ) = protocols[i].protocolAddress.call{
                value: allocationAmount
            }("");
            require(success, "Failed to allocate funds to protocol");

            allocations[i] = allocationAmount;
        }

        emit FundsReallocated(block.timestamp, msg.sender, totalFunds, allocations);
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {
        totalFunds += msg.value;
    }

    /**
     * @dev Allows the owner to withdraw excess funds.
     * @param amount The amount to withdraw.
     */
    function withdrawExcessFunds(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
        totalFunds -= amount;
    }

    /**
     * @dev Returns the list of protocols managed by the contract.
     * @return protocols The list of protocols.
     */
    function getProtocols() public view returns (Protocol[] memory) {
        return protocols;
    }
}
```
