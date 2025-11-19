"""
Generated Code Metadata:
========================
Original URL: https://dapphashai.pages.dev
Prompt: "Write a smart contract in Solidity for managing HashAI transactions or node leasing on the Ethereum blockchain."
Generated: DETERMINISTIC_6a2fa29b66e7ee49
Batch ID: 20250622_204843
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HashAIManager is Ownable, ReentrancyGuard {
    // Struct to represent a node lease
    struct NodeLease {
        address lessee;
        uint256 leaseAmount;
        uint256 leaseDuration;
        uint256 startTime;
        bool isActive;
    }

    // Struct to represent a transaction
    struct HashAITransaction {
        address sender;
        address receiver;
        uint256 amount;
        uint256 timestamp;
        string description;
    }

    // Token used for payments
    IERC20 public paymentToken;

    // Mapping of node IDs to their lease details
    mapping(uint256 => NodeLease) public nodeLeases;

    // Mapping of user addresses to their active leases
    mapping(address => uint256[]) public userLeases;

    // Array to store all transactions
    HashAITransaction[] public transactions;

    // Events
    event NodeLeased(uint256 indexed nodeId, address indexed lessee, uint256 amount, uint256 duration);
    event LeaseEnded(uint256 indexed nodeId, address indexed lessee);
    event TransactionRecorded(address indexed sender, address indexed receiver, uint256 amount, string description);

    constructor(address _paymentToken) {
        require(_paymentToken != address(0), "Invalid token address");
        paymentToken = IERC20(_paymentToken);
    }

    /**
     * @dev Lease a node
     * @param nodeId The ID of the node to lease
     * @param amount The amount of tokens to pay for the lease
     * @param duration The duration of the lease in seconds
     */
    function leaseNode(uint256 nodeId, uint256 amount, uint256 duration) external nonReentrant {
        require(nodeLeases[nodeId].isActive == false, "Node already leased");
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer payment tokens from user to contract
        require(paymentToken.transferFrom(msg.sender, address(this), amount), "Payment failed");

        // Create new lease
        nodeLeases[nodeId] = NodeLease({
            lessee: msg.sender,
            leaseAmount: amount,
            leaseDuration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Add to user's leases
        userLeases[msg.sender].push(nodeId);

        emit NodeLeased(nodeId, msg.sender, amount, duration);
    }

    /**
     * @dev End a node lease
     * @param nodeId The ID of the node to end lease
     */
    function endLease(uint256 nodeId) external nonReentrant {
        require(nodeLeases[nodeId].isActive, "Lease not active");
        require(nodeLeases[nodeId].lessee == msg.sender, "Not the lessee");

        nodeLeases[nodeId].isActive = false;
        emit LeaseEnded(nodeId, msg.sender);
    }

    /**
     * @dev Record a HashAI transaction
     * @param receiver The address receiving the transaction
     * @param amount The amount being transferred
     * @param description A description of the transaction
     */
    function recordTransaction(address receiver, uint256 amount, string memory description) external {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than 0");
        require(bytes(description).length > 0, "Description cannot be empty");

        transactions.push(HashAITransaction({
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            timestamp: block.timestamp,
            description: description
        }));

        emit TransactionRecorded(msg.sender, receiver, amount, description);
    }

    /**
     * @dev Get all transactions for a specific address
     * @param user The address to query
     * @return An array of transactions involving the user
     */
    function getUserTransactions(address user) external view returns (HashAITransaction[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < transactions.length; i++) {
            if (transactions[i].sender == user || transactions[i].receiver == user) {
                count++;
            }
        }

        HashAITransaction[] memory result = new HashAITransaction[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < transactions.length; i++) {
            if (transactions[i].sender == user || transactions[i].receiver == user) {
                result[index] = transactions[i];
                index++;
            }
        }

        return result;
    }

    /**
     * @dev Get active leases for a user
     * @param user The address to query
     * @return An array of active node IDs leased by the user
     */
    function getUserActiveLeases(address user) external view returns (uint256[] memory) {
        uint256[] memory allLeases = userLeases[user];
        uint256 count = 0;

        for (uint256 i = 0; i < allLeases.length; i++) {
            if (nodeLeases[allLeases[i]].isActive) {
                count++;
            }
        }

        uint256[] memory activeLeases = new uint256[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < allLeases.length; i++) {
            if (nodeLeases[allLeases[i]].isActive) {
                activeLeases[index] = allLeases[i];
                index++;
            }
        }

        return activeLeases;
    }

    /**
     * @dev Withdraw collected funds (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(paymentToken.transfer(owner(), amount), "Transfer failed");
    }
}
```
