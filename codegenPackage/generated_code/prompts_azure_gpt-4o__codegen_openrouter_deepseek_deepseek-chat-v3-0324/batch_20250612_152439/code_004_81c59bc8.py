"""
Generated Code Metadata:
========================
Original URL: https://judgeai-dapp.web.app
Prompt: Provide code examples for integrating Judge AI's multi-chain scalability architecture into a dApp that supports Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_81c59bc8198ddc8f
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainManager
 * @dev Handles cross-chain operations between Ethereum and Binance Smart Chain
 */
contract CrossChainManager is Ownable {
    // Chain IDs
    uint256 constant ETHEREUM_CHAIN_ID = 1;
    uint256 constant BSC_CHAIN_ID = 56;
    
    // Judge AI oracle address (would be replaced with actual address)
    address public judgeAIOracle;
    
    // Mapping to store cross-chain message status
    mapping(bytes32 => bool) public processedMessages;
    
    // Events
    event CrossChainMessageSent(
        uint256 indexed fromChainId,
        uint256 indexed toChainId,
        address indexed sender,
        bytes payload
    );
    
    event CrossChainMessageProcessed(
        uint256 indexed fromChainId,
        uint256 indexed toChainId,
        bytes32 indexed messageId
    );
    
    /**
     * @dev Sets the Judge AI oracle address
     * @param _oracle Address of the Judge AI oracle
     */
    function setJudgeAIOracle(address _oracle) external onlyOwner {
        require(_oracle != address(0), "Invalid oracle address");
        judgeAIOracle = _oracle;
    }
    
    /**
     * @dev Sends a cross-chain message
     * @param _toChainId Destination chain ID
     * @param _payload Encoded function call data
     */
    function sendCrossChainMessage(uint256 _toChainId, bytes memory _payload) external {
        require(_toChainId == ETHEREUM_CHAIN_ID || _toChainId == BSC_CHAIN_ID, "Unsupported chain");
        
        uint256 fromChainId = block.chainid;
        
        emit CrossChainMessageSent(
            fromChainId,
            _toChainId,
            msg.sender,
            _payload
        );
    }
    
    /**
     * @dev Processes a cross-chain message (called by oracle)
     * @param _fromChainId Source chain ID
     * @param _messageId Unique message identifier
     * @param _sender Original sender address
     * @param _payload Encoded function call data
     */
    function processCrossChainMessage(
        uint256 _fromChainId,
        bytes32 _messageId,
        address _sender,
        bytes memory _payload
    ) external {
        require(msg.sender == judgeAIOracle, "Only Judge AI oracle can process messages");
        require(!processedMessages[_messageId], "Message already processed");
        
        processedMessages[_messageId] = true;
        
        // Execute payload (would be replaced with actual logic)
        (bool success, ) = address(this).call(_payload);
        require(success, "Message processing failed");
        
        emit CrossChainMessageProcessed(
            _fromChainId,
            block.chainid,
            _messageId
        );
    }
}

/**
 * @title SampleDApp
 * @dev Example dApp that uses CrossChainManager
 */
contract SampleDApp {
    CrossChainManager public crossChainManager;
    
    // State that should be synced across chains
    uint256 public syncedValue;
    
    constructor(address _crossChainManager) {
        crossChainManager = CrossChainManager(_crossChainManager);
    }
    
    /**
     * @dev Updates value locally and sends cross-chain update
     * @param _newValue New value to set
     * @param _targetChainId Chain ID to sync with (1 for Ethereum, 56 for BSC)
     */
    function updateValue(uint256 _newValue, uint256 _targetChainId) external {
        // Update local value
        syncedValue = _newValue;
        
        // Prepare payload for cross-chain call
        bytes memory payload = abi.encodeWithSignature(
            "setValue(uint256)",
            _newValue
        );
        
        // Send cross-chain message
        crossChainManager.sendCrossChainMessage(_targetChainId, payload);
    }
    
    /**
     * @dev Sets the value (called via cross-chain message)
     * @param _newValue New value to set
     */
    function setValue(uint256 _newValue) external {
        require(
            msg.sender == address(crossChainManager),
            "Only callable via CrossChainManager"
        );
        syncedValue = _newValue;
    }
}
```

```javascript
// frontend/src/utils/judgeAI.js
import Web3 from 'web3';
import JudgeAIOracleABI from './abis/JudgeAIOracle.json';

const JUDGE_AI_ORACLE_ADDRESS = {
  1: '0x...', // Ethereum mainnet address
  56: '0x...' // BSC mainnet address
};

export class JudgeAIIntegration {
  constructor(provider, chainId) {
    this.web3 = new Web3(provider);
    this.chainId = chainId;
    this.oracle = new this.web3.eth.Contract(
      JudgeAIOracleABI,
      JUDGE_AI_ORACLE_ADDRESS[chainId]
    );
  }

  /**
   * Listens for cross-chain message events
   * @param {function} callback - Callback when message is received
   */
  listenForCrossChainMessages(callback) {
    this.oracle.events.CrossChainMessage({
      fromBlock: 'latest'
    }, (error, event) => {
      if (error) {
        console.error('Error listening to messages:', error);
        return;
      }
      callback(event);
    });
  }

  /**
   * Gets message proof from Judge AI
   * @param {string} messageId - Message ID to get proof for
   * @returns {Promise<object>} - Message proof data
   */
  async getMessageProof(messageId) {
    return this.oracle.methods.getMessageProof(messageId).call();
  }

  /**
   * Submits message proof to target chain
   * @param {object} proof - Proof data from Judge AI
   * @param {number} targetChainId - Destination chain ID
   * @returns {Promise<object>} - Transaction receipt
   */
  async submitMessageProof(proof, targetChainId) {
    return this.oracle.methods.submitProof(
      proof.messageId,
      proof.sender,
      proof.payload,
      proof.signature
    ).send({ from: this.web3.eth.defaultAccount });
  }
}

// frontend/src/utils/crossChain.js
import { JudgeAIIntegration } from './judgeAI';

export class CrossChainManager {
  constructor(web3Provider, chainId) {
    this.judgeAI = new JudgeAIIntegration(web3Provider, chainId);
    this.chainId = chainId;
  }

  /**
   * Initializes cross-chain message listeners
   * @param {function} messageHandler - Handler for incoming messages
   */
  init(messageHandler) {
    this.judgeAI.listenForCrossChainMessages(async (event) => {
      if (event.returnValues.toChainId !== this.chainId.toString()) return;
      
      try {
        const proof = await this.judgeAI.getMessageProof(event.returnValues.messageId);
        await this.judgeAI.submitMessageProof(proof, this.chainId);
        messageHandler(event);
      } catch (error) {
        console.error('Error processing cross-chain message:', error);
      }
    });
  }

  /**
   * Sends a cross-chain transaction
   * @param {object} contract - Source chain contract instance
   * @param {string} methodName - Contract method to call
   * @param {array} params - Method parameters
   * @param {number} targetChainId - Destination chain ID
   * @returns {Promise<object>} - Transaction receipt
   */
  async sendCrossChainTx(contract, methodName, params, targetChainId) {
    const data = contract.methods[methodName](...params).encodeABI();
    return contract.methods
      .sendCrossChainMessage(targetChainId, data)
      .send({ from: this.web3.eth.defaultAccount });
  }
}
```

```javascript
// frontend/src/hooks/useCrossChain.js
import { useEffect, useState } from 'react';
import { CrossChainManager } from '../utils/crossChain';

export function useCrossChain(web3Provider, chainId) {
  const [crossChain, setCrossChain] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!web3Provider || !chainId) return;

    const initCrossChain = async () => {
      try {
        const manager = new CrossChainManager(web3Provider, chainId);
        setCrossChain(manager);
        setIsLoading(false);
      } catch (err) {
        setError(err);
        setIsLoading(false);
      }
    };

    initCrossChain();
  }, [web3Provider, chainId]);

  return { crossChain, isLoading, error };
}
```
