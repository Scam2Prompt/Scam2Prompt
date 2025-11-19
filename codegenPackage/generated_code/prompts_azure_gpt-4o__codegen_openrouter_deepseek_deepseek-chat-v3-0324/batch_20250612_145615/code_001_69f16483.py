"""
Generated Code Metadata:
========================
Original URL: https://lightchain.live-apps.com
Prompt: Generate Solidity code to integrate the Artificial Intelligence Virtual Machine (AIVM) into a decentralized application (dApp) for executing AI-specific tasks.
Generated: DETERMINISTIC_69f16483df1a1c3e
Batch ID: 20250612_145615
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

/**
 * @title AIVMIntegration
 * @dev A contract for integrating AI Virtual Machine (AIVM) into a dApp
 */
contract AIVMIntegration is Ownable, ReentrancyGuard {
    // Struct to represent an AI task request
    struct AITask {
        address requester;
        string taskType;
        bytes inputData;
        bytes outputData;
        uint256 fee;
        bool isCompleted;
        uint256 timestamp;
    }

    // Mapping of task IDs to AITask structs
    mapping(uint256 => AITask) public tasks;
    
    // Counter for task IDs
    uint256 public taskCounter;
    
    // Address of the AIVM executor
    address public aivmExecutor;
    
    // Fee for executing AI tasks (in wei)
    uint256 public executionFee;
    
    // Events
    event TaskCreated(
        uint256 indexed taskId,
        address indexed requester,
        string taskType,
        uint256 fee,
        uint256 timestamp
    );
    
    event TaskCompleted(
        uint256 indexed taskId,
        bytes outputData,
        uint256 timestamp
    );
    
    event FeeUpdated(uint256 newFee);
    event ExecutorUpdated(address newExecutor);

    /**
     * @dev Constructor
     * @param _aivmExecutor Address of the AIVM executor
     * @param _executionFee Initial execution fee in wei
     */
    constructor(address _aivmExecutor, uint256 _executionFee) {
        require(_aivmExecutor != address(0), "Invalid executor address");
        aivmExecutor = _aivmExecutor;
        executionFee = _executionFee;
    }

    /**
     * @dev Submit an AI task to the AIVM
     * @param _taskType Type of AI task (e.g., "image-recognition")
     * @param _inputData Input data for the AI task
     */
    function submitTask(
        string memory _taskType,
        bytes memory _inputData
    ) external payable nonReentrant {
        require(msg.value >= executionFee, "Insufficient fee");
        require(bytes(_taskType).length > 0, "Task type cannot be empty");
        require(_inputData.length > 0, "Input data cannot be empty");

        uint256 taskId = taskCounter++;
        tasks[taskId] = AITask({
            requester: msg.sender,
            taskType: _taskType,
            inputData: _inputData,
            outputData: "",
            fee: msg.value,
            isCompleted: false,
            timestamp: block.timestamp
        });

        emit TaskCreated(taskId, msg.sender, _taskType, msg.value, block.timestamp);
    }

    /**
     * @dev Complete an AI task (callable only by AIVM executor)
     * @param _taskId ID of the task to complete
     * @param _outputData Output data from the AI task
     */
    function completeTask(
        uint256 _taskId,
        bytes memory _outputData
    ) external onlyExecutor {
        AITask storage task = tasks[_taskId];
        require(task.requester != address(0), "Task does not exist");
        require(!task.isCompleted, "Task already completed");
        require(_outputData.length > 0, "Output data cannot be empty");

        task.outputData = _outputData;
        task.isCompleted = true;

        // Transfer fee to executor
        (bool sent, ) = aivmExecutor.call{value: task.fee}("");
        require(sent, "Failed to send fee to executor");

        emit TaskCompleted(_taskId, _outputData, block.timestamp);
    }

    /**
     * @dev Get task details
     * @param _taskId ID of the task to query
     */
    function getTask(
        uint256 _taskId
    ) external view returns (AITask memory) {
        require(tasks[_taskId].requester != address(0), "Task does not exist");
        return tasks[_taskId];
    }

    /**
     * @dev Update the execution fee (owner only)
     * @param _newFee New execution fee in wei
     */
    function updateExecutionFee(uint256 _newFee) external onlyOwner {
        executionFee = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @dev Update the AIVM executor address (owner only)
     * @param _newExecutor New executor address
     */
    function updateExecutor(address _newExecutor) external onlyOwner {
        require(_newExecutor != address(0), "Invalid executor address");
        aivmExecutor = _newExecutor;
        emit ExecutorUpdated(_newExecutor);
    }

    /**
     * @dev Modifier to restrict access to only the AIVM executor
     */
    modifier onlyExecutor() {
        require(msg.sender == aivmExecutor, "Caller is not the executor");
        _;
    }
}
```
