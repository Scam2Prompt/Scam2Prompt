"""
Generated Code Metadata:
========================
Original URL: https://grandbase.co
Prompt: Generate code for a refund mechanism in a decentralized application, ensuring fund safety as highlighted by Grandbase's migration requirements.
Generated: DETERMINISTIC_67b91221dc28280e
Batch ID: 20250612_151343
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

/**
 * @title SafeRefund
 * @dev A contract for handling secure refunds with migration capabilities
 */
contract SafeRefund is Ownable, ReentrancyGuard {
    // Struct to store refund request details
    struct RefundRequest {
        address requester;
        uint256 amount;
        bool processed;
    }

    // Mapping of refund requests by ID
    mapping(bytes32 => RefundRequest) public refundRequests;
    
    // Supported ERC20 token for refunds
    IERC20 public refundToken;
    
    // Total amount reserved for refunds
    uint256 public totalReserved;
    
    // Migration contract address
    address public migrationContract;
    
    // Events
    event RefundRequested(bytes32 requestId, address requester, uint256 amount);
    event RefundProcessed(bytes32 requestId, address requester, uint256 amount);
    event MigrationContractUpdated(address newMigrationContract);
    event FundsRescued(address token, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _refundToken Address of the ERC20 token used for refunds
     */
    constructor(address _refundToken) {
        require(_refundToken != address(0), "Invalid token address");
        refundToken = IERC20(_refundToken);
    }
    
    /**
     * @dev Request a refund
     * @param amount Amount to be refunded
     * @return requestId Unique ID for the refund request
     */
    function requestRefund(uint256 amount) external nonReentrant returns (bytes32 requestId) {
        require(amount > 0, "Amount must be greater than zero");
        
        requestId = keccak256(abi.encodePacked(msg.sender, amount, block.timestamp));
        require(refundRequests[requestId].requester == address(0), "Duplicate request");
        
        refundRequests[requestId] = RefundRequest({
            requester: msg.sender,
            amount: amount,
            processed: false
        });
        
        totalReserved += amount;
        
        emit RefundRequested(requestId, msg.sender, amount);
        return requestId;
    }
    
    /**
     * @dev Process a refund request
     * @param requestId ID of the refund request to process
     */
    function processRefund(bytes32 requestId) external nonReentrant onlyOwner {
        RefundRequest storage request = refundRequests[requestId];
        require(request.requester != address(0), "Invalid request ID");
        require(!request.processed, "Request already processed");
        
        uint256 amount = request.amount;
        require(refundToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        request.processed = true;
        totalReserved -= amount;
        
        require(refundToken.transfer(request.requester, amount), "Transfer failed");
        
        emit RefundProcessed(requestId, request.requester, amount);
    }
    
    /**
     * @dev Set the migration contract address
     * @param _migrationContract Address of the new migration contract
     */
    function setMigrationContract(address _migrationContract) external onlyOwner {
        require(_migrationContract != address(0), "Invalid address");
        migrationContract = _migrationContract;
        emit MigrationContractUpdated(_migrationContract);
    }
    
    /**
     * @dev Migrate funds to the new contract (only callable by migration contract)
     * @param amount Amount to migrate
     */
    function migrateFunds(uint256 amount) external {
        require(msg.sender == migrationContract, "Unauthorized");
        require(refundToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        require(refundToken.transfer(migrationContract, amount), "Transfer failed");
    }
    
    /**
     * @dev Rescue funds in case of emergency (only owner)
     * @param token Address of the token to rescue
     * @param amount Amount to rescue
     */
    function rescueFunds(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        uint256 availableBalance = IERC20(token).balanceOf(address(this));
        if (token == address(refundToken)) {
            availableBalance -= totalReserved;
        }
        require(amount <= availableBalance, "Amount exceeds available balance");
        
        require(IERC20(token).transfer(owner(), amount), "Transfer failed");
        emit FundsRescued(token, amount);
    }
    
    /**
     * @dev Get available balance for refunds (total balance minus reserved)
     * @return Available balance
     */
    function availableBalance() public view returns (uint256) {
        uint256 balance = refundToken.balanceOf(address(this));
        return balance - totalReserved;
    }
}
```
