"""
Generated Code Metadata:
========================
Original URL: https://lightchain-it.web.app
Prompt: Generate a smart contract in Solidity to integrate Lightchain AI’s Artificial Intelligence Virtual Machine (AIVM) for executing AI-specific tasks on the blockchain.
Generated: DETERMINISTIC_3e40e00704ffe06c
Batch ID: 20250612_154049
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
 * @title LightchainAIVM
 * @dev A smart contract for integrating Lightchain AI's AIVM to execute AI tasks on-chain
 */
contract LightchainAIVM {
    // Contract owner
    address public owner;
    
    // AI Task structure
    struct AITask {
        bytes32 taskId;
        string inputData;
        string outputData;
        address requester;
        uint256 timestamp;
        bool isCompleted;
    }
    
    // Mapping of task IDs to AITask
    mapping(bytes32 => AITask) public tasks;
    
    // Events
    event TaskCreated(bytes32 indexed taskId, address indexed requester, string inputData);
    event TaskCompleted(bytes32 indexed taskId, string outputData);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor sets the initial owner
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Creates a new AI task
     * @param inputData The input data for the AI task
     * @return taskId The generated task ID
     */
    function createTask(string memory inputData) external returns (bytes32) {
        bytes32 taskId = keccak256(abi.encodePacked(msg.sender, block.timestamp, inputData));
        
        tasks[taskId] = AITask({
            taskId: taskId,
            inputData: inputData,
            outputData: "",
            requester: msg.sender,
            timestamp: block.timestamp,
            isCompleted: false
        });
        
        emit TaskCreated(taskId, msg.sender, inputData);
        return taskId;
    }
    
    /**
     * @dev Completes an AI task (only callable by owner/AIVM)
     * @param taskId The ID of the task to complete
     * @param outputData The output data from the AI computation
     */
    function completeTask(bytes32 taskId, string memory outputData) external onlyOwner {
        require(tasks[taskId].taskId != 0, "Task does not exist");
        require(!tasks[taskId].isCompleted, "Task already completed");
        
        tasks[taskId].outputData = outputData;
        tasks[taskId].isCompleted = true;
        
        emit TaskCompleted(taskId, outputData);
    }
    
    /**
     * @dev Gets task details
     * @param taskId The ID of the task to query
     * @return AITask The task details
     */
    function getTask(bytes32 taskId) external view returns (AITask memory) {
        require(tasks[taskId].taskId != 0, "Task does not exist");
        return tasks[taskId];
    }
    
    /**
     * @dev Transfers ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    /**
     * @dev Emergency function to destroy contract (only for testing)
     */
    function destroy() external onlyOwner {
        selfdestruct(payable(owner));
    }
}
```
