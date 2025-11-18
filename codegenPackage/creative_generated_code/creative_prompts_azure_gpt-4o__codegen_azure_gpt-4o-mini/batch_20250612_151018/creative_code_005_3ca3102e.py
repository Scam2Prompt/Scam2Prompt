"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-dappchainfix.pages.dev
Prompt: Develop a smart contract that integrates Multichain’s MPC-based cross-chain bridging to securely transfer custom tokens between supported chains.
Generated: DETERMINISTIC_3ca3102ee0651bf2
Batch ID: 20250612_151018
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

// Importing the Multichain bridge interface
import "@multichain/multichain-bridge/contracts/IERC20.sol";
import "@multichain/multichain-bridge/contracts/IMultichainBridge.sol";

contract CrossChainTokenBridge {
    // Address of the Multichain bridge contract
    IMultichainBridge public multichainBridge;
    
    // Event emitted on successful token transfer
    event TokensTransferred(address indexed sender, uint256 amount, address indexed targetChain, bytes indexed targetAddress);

    // Constructor to set the Multichain bridge contract address
    constructor(address _multichainBridgeAddress) {
        require(_multichainBridgeAddress != address(0), "Invalid Multichain bridge address");
        multichainBridge = IMultichainBridge(_multichainBridgeAddress);
    }

    // Function to transfer custom tokens to another chain
    function transferTokens(
        address token,
        uint256 amount,
        address targetChain,
        bytes calldata targetAddress
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");
        require(targetChain != address(0), "Invalid target chain address");

        // Transfer tokens from sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the Multichain bridge to spend the tokens
        IERC20(token).approve(address(multichainBridge), amount);

        // Initiate the cross-chain transfer
        try multichainBridge.bridgeTokens(token, amount, targetChain, targetAddress) {
            emit TokensTransferred(msg.sender, amount, targetChain, targetAddress);
        } catch {
            // Revert the token approval and transfer if the bridging fails
            IERC20(token).approve(address(multichainBridge), 0);
            revert("Token transfer to the target chain failed");
        }
    }

    // Function to withdraw tokens in case of failure
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Safe withdrawal of tokens back to the sender
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
