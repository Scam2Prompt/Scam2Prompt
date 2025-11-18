"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-swaps.web.app
Prompt: Generate code to utilize Circle's Cross Chain Transfer Protocol (CCTP) for direct USDC swaps between supported blockchains, implementing the burn-and-mint mechanism for secure transactions.
Generated: DETERMINISTIC_a63a3f8859c81af7
Batch ID: 20250612_145933
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Circle's Cross Chain Transfer Protocol (CCTP)
interface ICCTP {
    function initiateTransfer(
        address token, // The token to be transferred (USDC)
        uint256 amount, // Amount of tokens to transfer
        address recipient, // Recipient's address on the target chain
        string calldata targetChain // Target blockchain identifier
    ) external; // Function to initiate a cross-chain transfer
}

// Main contract for handling USDC swaps using CCTP
contract USDCSwap is Ownable {
    // USDC Token contract address
    address public usdcToken;
    // CCTP contract address
    ICCTP public cctp;

    // Event emitted after a successful swap
    event USDCTransferred(address indexed sender, uint256 amount, string targetChain);

    // Constructor to initialize the contract with USDC and CCTP addresses
    constructor(address _usdcToken, address _cctpAddress) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_cctpAddress != address(0), "Invalid CCTP address");

        usdcToken = _usdcToken;
        cctp = ICCTP(_cctpAddress);
    }

    // Function to swap USDC to another blockchain
    // This implements the burn-and-mint mechanism
    function swapUSDC(uint256 amount, address recipient, string calldata targetChain) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer USDC from user to this contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amount);

        // Burn the USDC tokens to ensure they are not reused
        // (Assumes USDC supports a burn function, otherwise handle accordingly)
        IERC20(usdcToken).approve(address(this), amount);
        _burnUSDC(amount);

        // Initiate the cross-chain transfer using CCTP
        cctp.initiateTransfer(usdcToken, amount, recipient, targetChain);

        // Emit an event for the transfer
        emit USDCTransferred(msg.sender, amount, targetChain);
    }

    // Internal function to burn USDC tokens
    function _burnUSDC(uint256 amount) internal {
        // Here we assume USDC has a burn function.
        // If it doesn't, this should be handled differently.
        IERC20(usdcToken).transfer(address(0), amount);
    }

    // Function to withdraw tokens in case of emergencies
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(msg.sender, amount);
    }
}
```
