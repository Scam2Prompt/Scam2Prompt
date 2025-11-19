"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Develop a Solidity contract for integrating Rocket Pool's Smoothing Pool feature, ensuring balanced rewards distribution for stakers. Include mechanisms for tracking commissions earned through Rocket Pool.
Generated: DETERMINISTIC_43b57ba40aa03d76
Batch ID: 20250612_153821
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IRocketStorage {
    function getAddress(bytes32 _key) external view returns (address);
}

interface IRocketNodeStaking {
    function getNodeRPLStake(address _nodeAddress) external view returns (uint256);
}

interface IRocketNodeManager {
    function getNodeExists(address _nodeAddress) external view returns (bool);
}

interface IRocketRewardsPool {
    function getRPLBalance() external view returns (uint256);
    function getClaimIntervalTime() external view returns (uint256);
}

contract RocketPoolSmoothingPool is Ownable {
    using SafeMath for uint256;

    // Rocket Pool contracts
    IRocketStorage public rocketStorage;
    address public rocketTokenRPL;
    
    // Pool parameters
    uint256 public totalRewards;
    uint256 public totalCommission;
    uint256 public lastDistributionTime;
    uint256 public distributionInterval;
    
    // Node tracking
    struct NodeInfo {
        uint256 rplStake;
        uint256 pendingRewards;
        uint256 claimedRewards;
        uint256 commissionEarned;
    }
    
    mapping(address => NodeInfo) public nodes;
    address[] public nodeAddresses;
    
    // Events
    event RewardsDeposited(uint256 amount);
    event RewardsDistributed(address indexed node, uint256 amount);
    event CommissionRecorded(address indexed node, uint256 amount);
    event NodeRegistered(address indexed node);
    
    constructor(address _rocketStorageAddress, uint256 _distributionInterval) {
        require(_rocketStorageAddress != address(0), "Invalid Rocket Storage address");
        rocketStorage = IRocketStorage(_rocketStorageAddress);
        rocketTokenRPL = rocketStorage.getAddress(keccak256(abi.encodePacked("contract.address", "rocketTokenRPL")));
        distributionInterval = _distributionInterval;
    }
    
    modifier onlyRegisteredNode() {
        require(nodes[msg.sender].rplStake > 0, "Not a registered node");
        _;
    }
    
    function registerNode() external {
        IRocketNodeManager rocketNodeManager = IRocketNodeManager(
            rocketStorage.getAddress(keccak256(abi.encodePacked("contract.address", "rocketNodeManager")))
        );
        require(rocketNodeManager.getNodeExists(msg.sender), "Not a Rocket Pool node");
        
        if (nodes[msg.sender].rplStake == 0) {
            nodeAddresses.push(msg.sender);
        }
        
        _updateNodeStake(msg.sender);
        emit NodeRegistered(msg.sender);
    }
    
    function depositRewards() external payable onlyOwner {
        require(msg.value > 0, "No ETH sent");
        totalRewards = totalRewards.add(msg.value);
        emit RewardsDeposited(msg.value);
    }
    
    function recordCommission(address _nodeAddress, uint256 _amount) external onlyOwner {
        require(_nodeAddress != address(0), "Invalid node address");
        require(_amount > 0, "Invalid commission amount");
        
        nodes[_nodeAddress].commissionEarned = nodes[_nodeAddress].commissionEarned.add(_amount);
        totalCommission = totalCommission.add(_amount);
        emit CommissionRecorded(_nodeAddress, _amount);
    }
    
    function distributeRewards() external onlyOwner {
        require(block.timestamp >= lastDistributionTime.add(distributionInterval), "Distribution interval not reached");
        require(totalRewards > 0, "No rewards to distribute");
        
        // Update all node stakes
        for (uint256 i = 0; i < nodeAddresses.length; i++) {
            _updateNodeStake(nodeAddresses[i]);
        }
        
        // Calculate total RPL stake
        uint256 totalRPLStake;
        for (uint256 i = 0; i < nodeAddresses.length; i++) {
            totalRPLStake = totalRPLStake.add(nodes[nodeAddresses[i]].rplStake);
        }
        
        require(totalRPLStake > 0, "No RPL staked in the pool");
        
        // Distribute rewards proportionally
        for (uint256 i = 0; i < nodeAddresses.length; i++) {
            address nodeAddress = nodeAddresses[i];
            NodeInfo storage node = nodes[nodeAddress];
            
            if (node.rplStake == 0) continue;
            
            uint256 nodeShare = totalRewards.mul(node.rplStake).div(totalRPLStake);
            node.pendingRewards = node.pendingRewards.add(nodeShare);
        }
        
        lastDistributionTime = block.timestamp;
    }
    
    function claimRewards() external onlyRegisteredNode {
        NodeInfo storage node = nodes[msg.sender];
        require(node.pendingRewards > 0, "No rewards to claim");
        
        uint256 amount = node.pendingRewards;
        node.pendingRewards = 0;
        node.claimedRewards = node.claimedRewards.add(amount);
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");
        emit RewardsDistributed(msg.sender, amount);
    }
    
    function _updateNodeStake(address _nodeAddress) internal {
        IRocketNodeStaking rocketNodeStaking = IRocketNodeStaking(
            rocketStorage.getAddress(keccak256(abi.encodePacked("contract.address", "rocketNodeStaking")))
        );
        
        uint256 rplStake = rocketNodeStaking.getNodeRPLStake(_nodeAddress);
        nodes[_nodeAddress].rplStake = rplStake;
    }
    
    function getNodeCount() external view returns (uint256) {
        return nodeAddresses.length;
    }
    
    function getTotalRPLStake() external view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < nodeAddresses.length; i++) {
            total = total.add(nodes[nodeAddresses[i]].rplStake);
        }
        return total;
    }
    
    function setDistributionInterval(uint256 _interval) external onlyOwner {
        distributionInterval = _interval;
    }
    
    // Emergency function to withdraw ETH (should never be needed in normal operation)
    function emergencyWithdrawETH(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance");
        (bool success, ) = owner().call{value: _amount}("");
        require(success, "ETH transfer failed");
    }
}
```
