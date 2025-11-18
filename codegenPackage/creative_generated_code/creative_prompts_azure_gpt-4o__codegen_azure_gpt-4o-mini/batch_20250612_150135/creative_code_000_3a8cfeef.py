"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://across-to.com
Prompt: Write a smart contract using the Across Protocol to facilitate cross-chain transfers between Ethereum Mainnet and Arbitrum One, ensuring optimized routing and minimal transaction costs.
Generated: DETERMINISTIC_3a8cfeef19654ece
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@across-protocol/contracts/Across.sol";

contract CrossChainTransfer is Ownable {
    // Instance of the Across Protocol for cross-chain transfers
    Across public across;

    // Mapping to track user balances for withdrawal
    mapping(address => uint256) public userBalances;

    // Event to emit when a transfer is initiated
    event TransferInitiated(address indexed sender, uint256 amount, uint256 chainId);

    // Event to emit when a withdrawal is made
    event Withdrawal(address indexed user, uint256 amount);

    // Constructor to set the Across contract address
    constructor(address _acrossAddress) {
        require(_acrossAddress != address(0), "Invalid Across address");
        across = Across(_acrossAddress);
    }

    /// @notice Initiates a cross-chain transfer from Ethereum Mainnet to Arbitrum One
    /// @param _amount Amount of tokens to transfer
    /// @param _chainId Destination chain ID (e.g., Arbitrum One)
    /// @param _token Address of the ERC20 token to transfer
    function initiateTransfer(uint256 _amount, uint256 _chainId, address _token) external {
        require(_amount > 0, "Transfer amount must be greater than zero");
        require(_chainId != 0, "Invalid chain ID");
        require(_token != address(0), "Invalid token address");
        
        // Transfer tokens from sender to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        
        // Update user balance for withdrawal tracking
        userBalances[msg.sender] += _amount;

        // Initiate the transfer via Across Protocol
        (bool success, ) = address(across).call(abi.encodeWithSignature("transfer(address,uint256,uint256)", _token, _amount, _chainId));
        require(success, "Cross-chain transfer failed");

        emit TransferInitiated(msg.sender, _amount, _chainId);
    }

    /// @notice Withdraws tokens that were transferred across chains
    /// @param _amount Amount of tokens to withdraw
    /// @param _token Address of the ERC20 token to withdraw
    function withdraw(uint256 _amount, address _token) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance for withdrawal");

        // Update user balance
        userBalances[msg.sender] -= _amount;

        // Transfer tokens back to the user
        IERC20(_token).transfer(msg.sender, _amount);

        emit Withdrawal(msg.sender, _amount);
    }

    /// @notice Allows the owner to withdraw any ERC20 tokens mistakenly sent to the contract
    /// @param _token Address of the ERC20 token to withdraw
    /// @param _amount Amount of tokens to withdraw
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
