"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Develop a smart contract using Solidity that utilizes Hop Protocol's "binding pools" mechanism for secure and efficient token transfers.
Generated: DETERMINISTIC_8069b30bc18eb36e
Batch ID: 20250622_212257
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title HopBindingPool
 * @dev A smart contract implementing Hop Protocol's binding pools mechanism
 * for secure and efficient token transfers between chains.
 */
contract HopBindingPool is ReentrancyGuard {
    using Address for address;

    // Token to be transferred
    IERC20 public immutable token;

    // Bridge contract address
    address public immutable bridge;

    // Minimum deposit amount
    uint256 public minDeposit;

    // Mapping of user deposits
    mapping(address => uint256) public deposits;

    // Total deposited amount
    uint256 public totalDeposited;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event TransferInitiated(address indexed user, uint256 amount, uint256 destinationChainId);
    event MinDepositUpdated(uint256 newMinDeposit);

    /**
     * @dev Initializes the contract with the token and bridge addresses
     * @param _token Address of the ERC20 token
     * @param _bridge Address of the bridge contract
     * @param _minDeposit Minimum deposit amount
     */
    constructor(
        address _token,
        address _bridge,
        uint256 _minDeposit
    ) {
        require(_token != address(0), "Invalid token address");
        require(_bridge != address(0), "Invalid bridge address");
        require(_minDeposit > 0, "Min deposit must be > 0");

        token = IERC20(_token);
        bridge = _bridge;
        minDeposit = _minDeposit;
    }

    /**
     * @dev Deposits tokens into the binding pool
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount >= minDeposit, "Amount below minimum deposit");
        
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        deposits[msg.sender] += amount;
        totalDeposited += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraws tokens from the binding pool
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(deposits[msg.sender] >= amount, "Insufficient balance");
        
        deposits[msg.sender] -= amount;
        totalDeposited -= amount;

        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Initiates a transfer to another chain using Hop Protocol
     * @param amount Amount of tokens to transfer
     * @param destinationChainId Chain ID of the destination
     */
    function initiateTransfer(uint256 amount, uint256 destinationChainId) external nonReentrant {
        require(deposits[msg.sender] >= amount, "Insufficient balance");
        
        deposits[msg.sender] -= amount;
        totalDeposited -= amount;

        // Approve bridge to spend tokens
        bool success = token.approve(bridge, amount);
        require(success, "Token approval failed");

        // Call bridge contract (simplified for example)
        bytes memory data = abi.encodeWithSignature(
            "sendToL2(uint256,address,uint256,uint256,uint256,uint256)",
            destinationChainId,
            msg.sender,
            amount,
            0, // amountOutMin
            0, // deadline
            0  // relayer fee
        );
        
        bridge.functionCall(data);

        emit TransferInitiated(msg.sender, amount, destinationChainId);
    }

    /**
     * @dev Updates the minimum deposit amount (admin function)
     * @param newMinDeposit New minimum deposit amount
     */
    function updateMinDeposit(uint256 newMinDeposit) external {
        require(msg.sender == bridge, "Only bridge can update");
        require(newMinDeposit > 0, "Min deposit must be > 0");
        
        minDeposit = newMinDeposit;
        emit MinDepositUpdated(newMinDeposit);
    }

    /**
     * @dev Returns the balance of a user
     * @param user Address of the user
     * @return User's balance
     */
    function getBalance(address user) external view returns (uint256) {
        return deposits[user];
    }
}
```
