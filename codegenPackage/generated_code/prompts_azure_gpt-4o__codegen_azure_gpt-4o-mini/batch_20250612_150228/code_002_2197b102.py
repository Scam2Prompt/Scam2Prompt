"""
Generated Code Metadata:
========================
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Provide a step-by-step guide in Solidity to create a smart contract that bridges tokens between Avalanche and Arbitrum networks, referencing the "How to Bridge?" section of the Joe exchange.
Generated: DETERMINISTIC_2197b102522bb92e
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the bridge contract
interface IBridge {
    function deposit(address token, uint256 amount, address recipient) external;
    function withdraw(address token, uint256 amount, address recipient) external;
}

// TokenBridge contract to facilitate token bridging between Avalanche and Arbitrum
contract TokenBridge is Ownable {
    // Mapping to track supported tokens
    mapping(address => bool) public supportedTokens;

    // Event emitted when tokens are bridged
    event TokensBridged(address indexed token, address indexed sender, address indexed recipient, uint256 amount);

    // Modifier to check if the token is supported
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    // Function to add a supported token
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }

    // Function to remove a supported token
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        supportedTokens[token] = false;
    }

    // Function to bridge tokens from Avalanche to Arbitrum
    function bridgeTokens(address token, uint256 amount, address recipient) external onlySupportedToken(token) {
        // Transfer tokens from sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Emit event for bridging
        emit TokensBridged(token, msg.sender, recipient, amount);

        // Call the bridge contract to deposit tokens
        IBridge bridge = IBridge(0xYourBridgeContractAddress); // Replace with actual bridge contract address
        bridge.deposit(token, amount, recipient);
    }

    // Function to withdraw tokens back to the original network
    function withdrawTokens(address token, uint256 amount, address recipient) external onlySupportedToken(token) {
        // Call the bridge contract to withdraw tokens
        IBridge bridge = IBridge(0xYourBridgeContractAddress); // Replace with actual bridge contract address
        bridge.withdraw(token, amount, recipient);
    }

    // Function to receive Ether (if needed)
    receive() external payable {}
}
```

**Note:** Replace `0xYourBridgeContractAddress` with the actual bridge contract address for the respective networks. Ensure that the contract is deployed on both networks and that the bridge contract is properly set up to handle token transfers.
