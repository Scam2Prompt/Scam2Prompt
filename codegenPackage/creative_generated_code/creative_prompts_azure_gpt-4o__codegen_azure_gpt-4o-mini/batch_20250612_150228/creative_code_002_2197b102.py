"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Provide a step-by-step guide in Solidity to create a smart contract that bridges tokens between Avalanche and Arbitrum networks, referencing the "How to Bridge?" section of the Joe exchange.
Generated: DETERMINISTIC_2197b102522bb92e
Batch ID: 20250612_150228
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

// Import necessary interfaces for ERC20 and the bridge functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BridgeContract facilitates token bridging between Avalanche and Arbitrum networks
contract BridgeContract is Ownable {
    // Event emitted when tokens are bridged
    event TokensBridged(address indexed user, address indexed token, uint256 amount, string targetNetwork);

    // Mapping to keep track of supported tokens
    mapping(address => bool) public supportedTokens;

    // Modifier to check if the token is supported
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Unsupported token");
        _;
    }

    // Constructor to initialize the supported tokens
    constructor(address[] memory tokens) {
        for (uint256 i = 0; i < tokens.length; i++) {
            supportedTokens[tokens[i]] = true;
        }
    }

    // Function to bridge tokens to a target network
    function bridgeTokens(address token, uint256 amount, string memory targetNetwork) 
        external 
        onlySupportedToken(token) 
    {
        // Transfer tokens from user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Emit the bridging event
        emit TokensBridged(msg.sender, token, amount, targetNetwork);

        // Implement the logic to handle the actual bridging to the target network here.
        // This could involve locking the tokens and notifying the destination network.
        // For example:
        // lockTokens(token, msg.sender, amount);
        // notifyDestinationNetwork(targetNetwork, token, msg.sender, amount);
    }

    // Function to add new supported tokens (only callable by owner)
    function addSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = true;
    }

    // Function to remove supported tokens (only callable by owner)
    function removeSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = false;
    }

    // Function to withdraw tokens from the contract (only callable by owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract (only callable by owner)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
