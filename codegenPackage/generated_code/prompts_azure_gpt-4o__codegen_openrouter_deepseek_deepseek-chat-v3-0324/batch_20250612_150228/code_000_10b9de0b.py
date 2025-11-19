"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write a smart contract using the Silo Finance protocol that isolates risk for a specific token asset while enabling borrowing through the bridge asset. Reference the protocol's isolated risk design.
Generated: DETERMINISTIC_10b9de0b1aeafbf0
Batch ID: 20250612_150228
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

interface ISilo {
    function deposit(address asset, uint256 amount, bool collateralOnly) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function assetStorage(address asset) external view returns (uint256, uint256);
}

contract SiloIsolatedRiskVault is Ownable, ReentrancyGuard {
    ISilo public immutable silo;
    IERC20 public immutable isolatedAsset;
    IERC20 public immutable bridgeAsset;
    
    mapping(address => uint256) public isolatedAssetDeposits;
    mapping(address => uint256) public bridgeAssetBorrows;
    
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    
    constructor(
        address _silo,
        address _isolatedAsset,
        address _bridgeAsset
    ) {
        require(_silo != address(0), "Invalid Silo address");
        require(_isolatedAsset != address(0), "Invalid isolated asset address");
        require(_bridgeAsset != address(0), "Invalid bridge asset address");
        
        silo = ISilo(_silo);
        isolatedAsset = IERC20(_isolatedAsset);
        bridgeAsset = IERC20(_bridgeAsset);
    }
    
    function depositIsolatedAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        isolatedAsset.transferFrom(msg.sender, address(this), amount);
        isolatedAsset.approve(address(silo), amount);
        
        silo.deposit(address(isolatedAsset), amount, true);
        isolatedAssetDeposits[msg.sender] += amount;
        
        emit Deposited(msg.sender, amount);
    }
    
    function borrowBridgeAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            isolatedAssetDeposits[msg.sender] > 0,
            "No isolated asset deposited"
        );
        
        (uint256 totalCollateral, ) = silo.assetStorage(address(isolatedAsset));
        require(
            totalCollateral >= amount,
            "Insufficient collateral for borrowing"
        );
        
        silo.borrow(address(bridgeAsset), amount);
        bridgeAsset.transfer(msg.sender, amount);
        bridgeAssetBorrows[msg.sender] += amount;
        
        emit Borrowed(msg.sender, amount);
    }
    
    function repayBridgeAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            bridgeAssetBorrows[msg.sender] >= amount,
            "Repay amount exceeds borrow"
        );
        
        bridgeAsset.transferFrom(msg.sender, address(this), amount);
        bridgeAsset.approve(address(silo), amount);
        
        silo.repay(address(bridgeAsset), amount);
        bridgeAssetBorrows[msg.sender] -= amount;
        
        emit Repaid(msg.sender, amount);
    }
    
    function withdrawIsolatedAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            isolatedAssetDeposits[msg.sender] >= amount,
            "Withdraw amount exceeds deposit"
        );
        require(
            bridgeAssetBorrows[msg.sender] == 0,
            "Outstanding bridge asset borrows"
        );
        
        silo.withdraw(address(isolatedAsset), amount);
        isolatedAsset.transfer(msg.sender, amount);
        isolatedAssetDeposits[msg.sender] -= amount;
        
        emit Withdrawn(msg.sender, amount);
    }
    
    function getCollateralRatio(address user) external view returns (uint256) {
        if (bridgeAssetBorrows[user] == 0) return type(uint256).max;
        
        (uint256 totalCollateral, ) = silo.assetStorage(address(isolatedAsset));
        return (totalCollateral * 1e18) / bridgeAssetBorrows[user];
    }
}
```
