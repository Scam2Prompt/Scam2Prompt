"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: How can I use the Hemi Bitcoin Kit (hBK) to build EVM-compatible applications that leverage Bitcoin's security?
Generated: DETERMINISTIC_3171d6173004709f
Batch ID: 20250612_155936
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

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IHemiBitcoinKit {
    function verifyBitcoinTransaction(
        bytes32 txHash,
        uint256 blockHeight,
        bytes calldata merkleProof,
        uint256 index
    ) external returns (bool);
    
    function lockBitcoin(
        address recipient,
        uint256 amount,
        uint256 lockDuration
    ) external payable returns (bool);
    
    function unlockBitcoin(
        bytes32 txHash,
        uint256 amount,
        bytes calldata unlockSignature
    ) external returns (bool);
}

contract BitcoinSecuredDApp is Ownable, ReentrancyGuard {
    using Address for address payable;
    
    IHemiBitcoinKit public hemiBitcoinKit;
    
    mapping(bytes32 => bool) public processedBitcoinTxs;
    mapping(address => uint256) public lockedBalances;
    mapping(address => uint256) public unlockTimestamps;
    
    event BitcoinLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event BitcoinUnlocked(address indexed user, uint256 amount);
    event BitcoinTransactionVerified(bytes32 indexed txHash, uint256 blockHeight);
    
    constructor(address _hemiBitcoinKitAddress) {
        require(_hemiBitcoinKitAddress != address(0), "Invalid Hemi Bitcoin Kit address");
        hemiBitcoinKit = IHemiBitcoinKit(_hemiBitcoinKitAddress);
    }
    
    function lockBitcoinForDApp(uint256 lockDuration) external payable nonReentrant {
        require(msg.value > 0, "Amount must be greater than 0");
        require(lockDuration > 0, "Lock duration must be greater than 0");
        
        bool success = hemiBitcoinKit.lockBitcoin{value: msg.value}(
            msg.sender,
            msg.value,
            lockDuration
        );
        require(success, "Bitcoin lock failed");
        
        lockedBalances[msg.sender] += msg.value;
        unlockTimestamps[msg.sender] = block.timestamp + lockDuration;
        
        emit BitcoinLocked(msg.sender, msg.value, unlockTimestamps[msg.sender]);
    }
    
    function unlockBitcoinFromDApp(
        bytes32 txHash,
        uint256 amount,
        bytes calldata unlockSignature
    ) external nonReentrant {
        require(lockedBalances[msg.sender] >= amount, "Insufficient locked balance");
        require(block.timestamp >= unlockTimestamps[msg.sender], "Funds are still locked");
        
        bool success = hemiBitcoinKit.unlockBitcoin(txHash, amount, unlockSignature);
        require(success, "Bitcoin unlock failed");
        
        lockedBalances[msg.sender] -= amount;
        payable(msg.sender).sendValue(amount);
        
        emit BitcoinUnlocked(msg.sender, amount);
    }
    
    function verifyBitcoinTransaction(
        bytes32 txHash,
        uint256 blockHeight,
        bytes calldata merkleProof,
        uint256 index
    ) external returns (bool) {
        require(!processedBitcoinTxs[txHash], "Transaction already processed");
        
        bool isValid = hemiBitcoinKit.verifyBitcoinTransaction(
            txHash,
            blockHeight,
            merkleProof,
            index
        );
        
        if (isValid) {
            processedBitcoinTxs[txHash] = true;
            emit BitcoinTransactionVerified(txHash, blockHeight);
        }
        
        return isValid;
    }
    
    function updateHemiBitcoinKitAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        hemiBitcoinKit = IHemiBitcoinKit(newAddress);
    }
    
    receive() external payable {}
}
```
