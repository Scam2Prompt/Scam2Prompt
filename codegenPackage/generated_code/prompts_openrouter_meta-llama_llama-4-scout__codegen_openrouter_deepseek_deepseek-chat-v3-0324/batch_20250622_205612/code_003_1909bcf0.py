"""
Generated Code Metadata:
========================
Original URL: https://flareairdrop.com
Prompt: Generate a Solidity smart contract that utilizes Flare's EVM+ and Substrate features for a DeFi application.
Generated: DETERMINISTIC_1909bcf01cc35158
Batch ID: 20250622_205612
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

import "@flarenetwork/flare-periphery-contracts/flare/StateConnector.sol";
import "@flarenetwork/flare-periphery-contracts/substrate/SubstrateCall.sol";

/**
 * @title CrossChainDeFi
 * @dev A DeFi application leveraging Flare's EVM+ and Substrate features
 */
contract CrossChainDeFi {
    using SubstrateCall for address;
    
    // State Connector instance
    StateConnector public stateConnector;
    
    // Substrate contract address
    address public substrateContract;
    
    // Token balances
    mapping(address => uint256) public balances;
    
    // Cross-chain requests
    struct CrossChainRequest {
        address requester;
        uint256 amount;
        bool fulfilled;
    }
    
    mapping(bytes32 => CrossChainRequest) public requests;
    
    // Events
    event Deposit(address indexed user, uint256 amount);
    event WithdrawRequest(address indexed user, uint256 amount, bytes32 requestId);
    event WithdrawComplete(address indexed user, uint256 amount);
    event CrossChainTransfer(address indexed from, address indexed to, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _stateConnector Address of the State Connector contract
     * @param _substrateContract Address of the Substrate contract
     */
    constructor(address _stateConnector, address _substrateContract) {
        stateConnector = StateConnector(_stateConnector);
        substrateContract = _substrateContract;
    }
    
    /**
     * @dev Deposit funds into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }
    
    /**
     * @dev Request withdrawal to Substrate chain
     * @param amount Amount to withdraw
     * @param substrateAddress Recipient address on Substrate chain
     */
    function requestWithdraw(uint256 amount, bytes32 substrateAddress) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        
        bytes32 requestId = keccak256(abi.encodePacked(msg.sender, amount, block.timestamp));
        requests[requestId] = CrossChainRequest(msg.sender, amount, false);
        
        // Call Substrate contract
        bytes memory callData = abi.encodeWithSignature(
            "initiateWithdraw(bytes32,uint256)", 
            substrateAddress, 
            amount
        );
        substrateContract.substrateCall(callData);
        
        emit WithdrawRequest(msg.sender, amount, requestId);
    }
    
    /**
     * @dev Complete withdrawal after verification from State Connector
     * @param requestId ID of the withdrawal request
     * @param proof Proof from State Connector
     */
    function completeWithdraw(bytes32 requestId, bytes calldata proof) external {
        CrossChainRequest storage request = requests[requestId];
        require(!request.fulfilled, "Request already fulfilled");
        
        // Verify proof using State Connector
        bool verified = stateConnector.verifyProof(
            proof,
            abi.encode(request.requester, request.amount)
        );
        require(verified, "Invalid proof");
        
        request.fulfilled = true;
        payable(request.requester).transfer(request.amount);
        
        emit WithdrawComplete(request.requester, request.amount);
    }
    
    /**
     * @dev Handle incoming cross-chain transfer from Substrate
     * @param recipient EVM address of the recipient
     * @param amount Amount to transfer
     * @param proof Proof from State Connector
     */
    function receiveFromSubstrate(
        address recipient,
        uint256 amount,
        bytes calldata proof
    ) external {
        // Verify proof using State Connector
        bool verified = stateConnector.verifyProof(
            proof,
            abi.encode(recipient, amount)
        );
        require(verified, "Invalid proof");
        
        balances[recipient] += amount;
        emit CrossChainTransfer(address(0), recipient, amount);
    }
    
    /**
     * @dev Get balance of an account
     * @param account Address to query
     * @return Balance of the account
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
