"""
Generated Code Metadata:
========================
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: "Design a staking system for upgrading rNodes and zNodes on the Rivalz network using $RIZ tokens."
Generated: DETERMINISTIC_1aa3aba2ae4462ec
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RivalzStakingSystem is Ownable, ReentrancyGuard {
    IERC20 public rizToken;
    
    enum NodeType { rNode, zNode }
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        NodeType nodeType;
        uint256 upgradeLevel;
    }
    
    mapping(address => Stake) public stakes;
    mapping(NodeType => uint256[]) public upgradeRequirements;
    
    event Staked(address indexed user, uint256 amount, NodeType nodeType);
    event Upgraded(address indexed user, NodeType nodeType, uint256 newLevel);
    event Unstaked(address indexed user, uint256 amount);
    
    constructor(address _rizToken) {
        rizToken = IERC20(_rizToken);
        
        // Initialize upgrade requirements (in RIZ tokens)
        upgradeRequirements[NodeType.rNode] = [1000 ether, 2500 ether, 5000 ether];
        upgradeRequirements[NodeType.zNode] = [5000 ether, 10000 ether, 20000 ether];
    }
    
    function stake(uint256 amount, NodeType nodeType) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staked");
        
        bool transferred = rizToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed");
        
        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            nodeType: nodeType,
            upgradeLevel: 0
        });
        
        emit Staked(msg.sender, amount, nodeType);
    }
    
    function upgrade() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        
        uint256 currentLevel = userStake.upgradeLevel;
        NodeType nodeType = userStake.nodeType;
        uint256[] memory requirements = upgradeRequirements[nodeType];
        
        require(currentLevel < requirements.length, "Already at max level");
        uint256 requiredAmount = requirements[currentLevel];
        
        require(userStake.amount >= requiredAmount, "Insufficient stake for upgrade");
        
        userStake.upgradeLevel = currentLevel + 1;
        emit Upgraded(msg.sender, nodeType, userStake.upgradeLevel);
    }
    
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.stakedAt + 7 days, "Minimum stake period not met");
        
        delete stakes[msg.sender];
        
        bool transferred = rizToken.transfer(msg.sender, userStake.amount);
        require(transferred, "Token transfer failed");
        
        emit Unstaked(msg.sender, userStake.amount);
    }
    
    function setUpgradeRequirements(NodeType nodeType, uint256[] memory newRequirements) external onlyOwner {
        require(newRequirements.length > 0, "Requirements cannot be empty");
        upgradeRequirements[nodeType] = newRequirements;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rizToken.balanceOf(address(this));
        rizToken.transfer(owner(), balance);
    }
}
```
