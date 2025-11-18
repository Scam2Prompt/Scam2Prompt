"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remoteprocurator.pages.dev
Prompt: Write a smart contract that utilizes Multichain's MPC (Multi-Party Computation) for secure cross-chain bridging of tokens.
Generated: DETERMINISTIC_cfd0d36bf5f0c99d
Batch ID: 20250612_145821
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for Multichain MPC
interface IMultichainMPC {
    function bridgeTokens(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        bytes calldata proof
    ) external returns (bool);
}

// Smart contract for cross-chain token bridging using Multichain's MPC
contract CrossChainBridge is Ownable {
    // Address of the Multichain MPC contract
    IMultichainMPC public mpc;

    // Event to log successful token bridging
    event TokensBridged(
        address indexed fromToken,
        address indexed toToken,
        address indexed recipient,
        uint256 amount
    );

    // Constructor to set the Multichain MPC contract address
    constructor(address _mpcAddress) {
        require(_mpcAddress != address(0), "Invalid MPC address");
        mpc = IMultichainMPC(_mpcAddress);
    }

    // Function to bridge tokens across chains
    function bridge(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        bytes calldata proof
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the sender to the contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);
        
        // Approve the MPC contract to spend the tokens
        IERC20(fromToken).approve(address(mpc), amount);

        // Call the MPC to bridge the tokens
        bool success = mpc.bridgeTokens(fromToken, toToken, amount, recipient, proof);
        require(success, "Token bridging failed");

        emit TokensBridged(fromToken, toToken, recipient, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive Ether if necessary
    receive() external payable {}

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }
}
```

This smart contract implements a simple cross-chain token bridge utilizing Multichain's MPC for secure token transfers. It includes necessary error handling, ownership control, and comments for clarity.
