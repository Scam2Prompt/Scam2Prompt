"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-r3nq7hqt4-offchain-labs.vercel.app
Prompt: How can I use the Arbitrum Token Bridge to launch a customized chain on Arbitrum Orbit?
Generated: DETERMINISTIC_f13a1ede8251cdde
Batch ID: 20250612_135417
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

import "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import "@arbitrum/nitro-contracts/src/bridge/IOutbox.sol";
import "@arbitrum/nitro-contracts/src/libraries/AddressAliasHelper.sol";

/**
 * @title ArbitrumOrbitChainDeployer
 * @dev A contract to deploy a customized chain on Arbitrum Orbit using the Arbitrum Token Bridge
 */
contract ArbitrumOrbitChainDeployer {
    IInbox public immutable inbox;
    address public owner;
    
    event OrbitChainDeployed(
        address indexed l2Contract,
        uint256 maxGas,
        uint256 gasPriceBid,
        uint256 maxSubmissionCost,
        bytes initData
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }
    
    /**
     * @dev Initialize the deployer with the Arbitrum Inbox contract address
     * @param _inbox Address of the Arbitrum Inbox contract
     */
    constructor(address _inbox) {
        require(_inbox != address(0), "Invalid inbox address");
        inbox = IInbox(_inbox);
        owner = msg.sender;
    }
    
    /**
     * @dev Deploy a new Orbit chain with custom parameters
     * @param maxGas Max gas for L2 execution
     * @param gasPriceBid Gas price bid for L2 execution
     * @param maxSubmissionCost Max submission cost for retryable ticket
     * @param initData Initialization data for the L2 contract
     * @return Retryable ticket ID
     */
    function deployOrbitChain(
        uint256 maxGas,
        uint256 gasPriceBid,
        uint256 maxSubmissionCost,
        bytes memory initData
    ) external payable onlyOwner returns (uint256) {
        require(msg.value > maxSubmissionCost + (maxGas * gasPriceBid), "Insufficient ETH");
        
        // Create retryable ticket to deploy contract on L2
        uint256 ticketID = inbox.createRetryableTicket{value: msg.value}(
            address(0), // default to sender alias
            0,          // no value transfer
            maxSubmissionCost,
            msg.sender, // refund address
            msg.sender, // beneficiary
            maxGas,
            gasPriceBid,
            initData
        );
        
        emit OrbitChainDeployed(
            AddressAliasHelper.applyL1ToL2Alias(address(this)),
            maxGas,
            gasPriceBid,
            maxSubmissionCost,
            initData
        );
        
        return ticketID;
    }
    
    /**
     * @dev Transfer ownership of the deployer contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
    
    /**
     * @dev Withdraw any remaining ETH from the contract
     */
    function withdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```

```javascript
// JavaScript helper for interacting with the deployer contract
const { ethers } = require("ethers");
const ArbitrumOrbitChainDeployerABI = require("./ArbitrumOrbitChainDeployerABI.json");

class OrbitChainDeployer {
  constructor(provider, deployerAddress) {
    this.provider = provider;
    this.deployer = new ethers.Contract(
      deployerAddress,
      ArbitrumOrbitChainDeployerABI,
      provider.getSigner()
    );
  }

  /**
   * Deploy a new Orbit chain
   * @param {Object} params Deployment parameters
   * @param {number} params.maxGas Max gas for L2 execution
   * @param {number} params.gasPriceBid Gas price bid for L2 execution
   * @param {number} params.maxSubmissionCost Max submission cost
   * @param {string} params.initData Hex encoded initialization data
   * @param {number} params.ethValue ETH value to send
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async deployChain(params) {
    const tx = await this.deployer.deployOrbitChain(
      params.maxGas,
      params.gasPriceBid,
      params.maxSubmissionCost,
      params.initData,
      { value: params.ethValue }
    );
    return await tx.wait();
  }

  /**
   * Transfer ownership
   * @param {string} newOwner New owner address
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async transferOwnership(newOwner) {
    const tx = await this.deployer.transferOwnership(newOwner);
    return await tx.wait();
  }

  /**
   * Withdraw ETH from contract
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async withdrawETH() {
    const tx = await this.deployer.withdrawETH();
    return await tx.wait();
  }
}

module.exports = OrbitChainDeployer;
```
feTransfer(owner, balance);
    }
}
```
