"""
Generated Code Metadata:
========================
Original URL: https://bnb-mixer.eth.limo
Prompt: Design a smart contract on the Binance Smart Chain that integrates with the BNB Mixer service to enable decentralized and automated mixing of BNB coins.
Generated: DETERMINISTIC_12d23c159eab3d08
Batch ID: 20250622_205315
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

interface IBNBMixer {
    function deposit(uint256 amount, bytes32 commitment) external payable;
    function withdraw(bytes calldata proof, bytes32 nullifierHash, address payable recipient) external;
}

contract BNBMixerIntegration is Ownable, ReentrancyGuard {
    IBNBMixer public bnbMixer;
    uint256 public feePercentage; // Fee percentage (e.g., 100 = 1%)
    address public feeCollector;
    
    event Mixed(address indexed user, uint256 amount, bytes32 commitment);
    event Withdrawn(address indexed user, uint256 amount);
    event FeeCollected(uint256 amount);
    event MixerUpdated(address newMixer);
    event FeeUpdated(uint256 newFee);
    event FeeCollectorUpdated(address newCollector);

    constructor(address _bnbMixer, uint256 _feePercentage, address _feeCollector) {
        require(_bnbMixer != address(0), "Invalid mixer address");
        require(_feePercentage <= 1000, "Fee too high"); // Max 10%
        require(_feeCollector != address(0), "Invalid fee collector");
        
        bnbMixer = IBNBMixer(_bnbMixer);
        feePercentage = _feePercentage;
        feeCollector = _feeCollector;
    }

    function updateMixer(address _newMixer) external onlyOwner {
        require(_newMixer != address(0), "Invalid mixer address");
        bnbMixer = IBNBMixer(_newMixer);
        emit MixerUpdated(_newMixer);
    }

    function updateFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee too high");
        feePercentage = _newFee;
        emit FeeUpdated(_newFee);
    }

    function updateFeeCollector(address _newCollector) external onlyOwner {
        require(_newCollector != address(0), "Invalid fee collector");
        feeCollector = _newCollector;
        emit FeeCollectorUpdated(_newCollector);
    }

    function mixBNB(bytes32 _commitment) external payable nonReentrant {
        require(msg.value > 0, "Amount must be greater than 0");
        
        uint256 feeAmount = (msg.value * feePercentage) / 10000;
        uint256 depositAmount = msg.value - feeAmount;
        
        if (feeAmount > 0) {
            payable(feeCollector).transfer(feeAmount);
            emit FeeCollected(feeAmount);
        }
        
        bnbMixer.deposit{value: depositAmount}(depositAmount, _commitment);
        emit Mixed(msg.sender, depositAmount, _commitment);
    }

    function withdrawBNB(bytes calldata _proof, bytes32 _nullifierHash, address payable _recipient) external nonReentrant {
        require(_recipient != address(0), "Invalid recipient");
        bnbMixer.withdraw(_proof, _nullifierHash, _recipient);
        emit Withdrawn(_recipient, address(this).balance);
    }

    // Emergency function to recover any ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(token = IERC20(tokenAddress);
        token.transfer(owner(), amount);
    }

    // Emergency function to recover BNB
    function recoverBNB() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    receive() external payable {}
}
```
