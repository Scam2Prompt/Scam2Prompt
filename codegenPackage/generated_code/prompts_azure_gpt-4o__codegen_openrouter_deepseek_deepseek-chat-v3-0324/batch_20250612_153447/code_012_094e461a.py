"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Create a Solidity contract for implementing low-fee transactions on a Layer 2 blockchain, inspired by the Pepe Unchained infrastructure.
Generated: DETERMINISTIC_094e461a34227f4f
Batch ID: 20250612_153447
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
 * @title Layer2LowFeeTransaction
 * @dev A contract for implementing low-fee transactions on Layer 2
 * inspired by Pepe Unchained infrastructure
 */
contract Layer2LowFeeTransaction is Ownable, ReentrancyGuard {
    // Fee structure
    struct FeeConfig {
        uint256 baseFee;
        uint256 percentageFee; // Basis points (1/100 of a percent)
        address feeToken; // Address(0) for native token
    }

    // Transaction data
    struct Transaction {
        address sender;
        address recipient;
        uint256 amount;
        uint256 fee;
        uint256 timestamp;
        bool executed;
    }

    // State variables
    FeeConfig public feeConfig;
    mapping(bytes32 => Transaction) public transactions;
    mapping(address => uint256) public balances;

    // Events
    event TransactionSubmitted(
        bytes32 indexed txHash,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 fee
    );
    event TransactionExecuted(
        bytes32 indexed txHash,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 fee
    );
    event FeeConfigUpdated(
        uint256 baseFee,
        uint256 percentageFee,
        address feeToken
    );
    event Withdrawn(address indexed account, uint256 amount);

    /**
     * @dev Constructor to initialize fee configuration
     * @param _baseFee Base fee amount
     * @param _percentageFee Percentage fee in basis points
     * @param _feeToken Address of the fee token (address(0) for native token)
     */
    constructor(
        uint256 _baseFee,
        uint256 _percentageFee,
        address _feeToken
    ) {
        require(_percentageFee <= 10000, "Fee cannot exceed 100%");
        feeConfig = FeeConfig(_baseFee, _percentageFee, _feeToken);
    }

    /**
     * @dev Submit a new transaction
     * @param recipient Address of the recipient
     * @param amount Amount to transfer
     */
    function submitTransaction(address recipient, uint256 amount) external payable nonReentrant {
        require(recipient != address(0), "Invalid recipient");
        require(amount > 0, "Amount must be positive");

        uint256 fee = calculateFee(amount);
        bytes32 txHash = keccak256(abi.encodePacked(msg.sender, recipient, amount, block.timestamp));

        if (feeConfig.feeToken == address(0)) {
            require(msg.value >= amount + fee, "Insufficient native token sent");
            balances[address(this)] += fee;
        } else {
            IERC20 token = IERC20(feeConfig.feeToken);
            require(token.transferFrom(msg.sender, address(this), fee), "Fee transfer failed");
            require(token.transferFrom(msg.sender, recipient, amount), "Amount transfer failed");
        }

        transactions[txHash] = Transaction({
            sender: msg.sender,
            recipient: recipient,
            amount: amount,
            fee: fee,
            timestamp: block.timestamp,
            executed: feeConfig.feeToken != address(0)
        });

        emit TransactionSubmitted(txHash, msg.sender, recipient, amount, fee);

        if (feeConfig.feeToken == address(0)) {
            _executeTransaction(txHash);
        }
    }

    /**
     * @dev Execute a pending native token transaction
     * @param txHash Hash of the transaction to execute
     */
    function executeTransaction(bytes32 txHash) external nonReentrant {
        require(feeConfig.feeToken == address(0), "Only for native token transactions");
        _executeTransaction(txHash);
    }

    /**
     * @dev Internal function to execute a transaction
     * @param txHash Hash of the transaction to execute
     */
    function _executeTransaction(bytes32 txHash) internal {
        Transaction storage txn = transactions[txHash];
        require(txn.sender != address(0), "Transaction does not exist");
        require(!txn.executed, "Transaction already executed");

        if (feeConfig.feeToken == address(0)) {
            (bool success, ) = txn.recipient.call{value: txn.amount}("");
            require(success, "Transfer failed");
        }

        txn.executed = true;
        emit TransactionExecuted(txHash, txn.sender, txn.recipient, txn.amount, txn.fee);
    }

    /**
     * @dev Calculate the fee for a given amount
     * @param amount Amount to calculate fee for
     * @return Total fee amount
     */
    function calculateFee(uint256 amount) public view returns (uint256) {
        return feeConfig.baseFee + (amount * feeConfig.percentageFee) / 10000;
    }

    /**
     * @dev Update fee configuration (owner only)
     * @param _baseFee New base fee
     * @param _percentageFee New percentage fee in basis points
     * @param _feeToken New fee token address
     */
    function updateFeeConfig(
        uint256 _baseFee,
        uint256 _percentageFee,
        address _feeToken
    ) external onlyOwner {
        require(_percentageFee <= 10000, "Fee cannot exceed 100%");
        feeConfig = FeeConfig(_baseFee, _percentageFee, _feeToken);
        emit FeeConfigUpdated(_baseFee, _percentageFee, _feeToken);
    }

    /**
     * @dev Withdraw collected fees (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawFees(uint256 amount) external onlyOwner nonReentrant {
        if (feeConfig.feeToken == address(0)) {
            require(amount <= address(this).balance, "Insufficient balance");
            (bool success, ) = owner().call{value: amount}("");
            require(success, "Transfer failed");
        } else {
            IERC20 token = IERC20(feeConfig.feeToken);
            require(token.transfer(owner(), amount), "Transfer failed");
        }
        emit Withdrawn(owner(), amount);
    }

    /**
     * @dev Get the current contract balance
     * @return Balance of the contract
     */
    function getContractBalance() external view returns (uint256) {
        if (feeConfig.feeToken == address(0)) {
            return address(this).balance;
        } else {
            return IERC20(feeConfig.feeToken).balanceOf(address(this));
        }
    }

    // Fallback function to receive native tokens
    receive() external payable {}
}
```
