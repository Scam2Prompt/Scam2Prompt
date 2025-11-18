"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://izumi-finance.org
Prompt: Generate Solidity code for a decentralized finance protocol that supports multiple blockchain ecosystems, as described in iZUMi Finance's flexibility feature.
Generated: DETERMINISTIC_c91ef58cefc385be
Batch ID: 20250612_153809
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for interacting with different blockchain ecosystems
interface IBridge {
    function transferTokens(address token, uint256 amount, address recipient) external returns (bool);
}

// Main contract for the decentralized finance protocol
contract MultiChainDeFi is Ownable {
    // Mapping to store supported tokens on each blockchain
    mapping(string => mapping(address => bool)) public supportedTokens;

    // Event emitted when a new token is supported
    event TokenSupported(string blockchain, address token);

    // Event emitted when a transfer is successful
    event TransferSuccessful(string blockchain, address token, uint256 amount, address recipient);

    // Modifier to check if the token is supported for a specific blockchain
    modifier isSupported(string memory blockchain, address token) {
        require(supportedTokens[blockchain][token], "Token not supported on this blockchain");
        _;
    }

    // Function to support a new token on a specific blockchain
    function supportToken(string memory blockchain, address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(!supportedTokens[blockchain][token], "Token already supported");

        supportedTokens[blockchain][token] = true;

        emit TokenSupported(blockchain, token);
    }

    // Function to transfer tokens across blockchains
    function transferToBlockchain(
        string memory blockchain,
        address token,
        uint256 amount,
        address recipient,
        address bridgeAddress
    ) external isSupported(blockchain, token) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer the tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the bridge contract to spend the tokens
        IERC20(token).approve(bridgeAddress, amount);

        // Call the bridge contract to handle the token transfer
        IBridge(bridgeAddress).transferTokens(token, amount, recipient);

        emit TransferSuccessful(blockchain, token, amount, recipient);
    }

    // Function to withdraw tokens from the contract (for owner only)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
