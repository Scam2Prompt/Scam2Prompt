"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Generate Solidity code for an ERC-20 token contract that supports multichain bridging using Axelar ITS. Ensure the contract includes mechanisms for permissionless bridging and token wrapping.
Generated: DETERMINISTIC_c2e6be0baf107052
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@axelar-network/axelar-contracts/src/AxelarExecutable.sol";

contract AxelarERC20Bridge is ERC20, ERC20Burnable, ReentrancyGuard, AxelarExecutable {
    // Mapping of token bridges
    mapping(address => bool) public tokenBridges;

    // Mapping of wrapped tokens
    mapping(address => address) public wrappedTokens;

    // Event emitted when token is bridged
    event TokenBridged(address indexed token, uint256 amount, string destinationChain);

    // Event emitted when token is wrapped
    event TokenWrapped(address indexed token, address wrappedToken);

    /**
     * @dev Constructor for the contract
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @dev Adds a token bridge
     * @param bridge Address of the token bridge
     */
    function addTokenBridge(address bridge) public onlyOwner {
        tokenBridges[bridge] = true;
    }

    /**
     * @dev Removes a token bridge
     * @param bridge Address of the token bridge
     */
    function removeTokenBridge(address bridge) public onlyOwner {
        tokenBridges[bridge] = false;
    }

    /**
     * @dev Wraps a token
     * @param token Address of the token to wrap
     * @param name_ Name of the wrapped token
     * @param symbol_ Symbol of the wrapped token
     */
    function wrapToken(address token, string memory name_, string memory symbol_) public onlyOwner {
        require(!wrappedTokens[token], "Token already wrapped");
        address wrappedToken = address(new ERC20(name_, symbol_));
        wrappedTokens[token] = wrappedToken;
        emit TokenWrapped(token, wrappedToken);
    }

    /**
     * @dev Bridges a token
     * @param token Address of the token to bridge
     * @param amount Amount of token to bridge
     * @param destinationChain Destination chain for the token
     */
    function bridgeToken(address token, uint256 amount, string memory destinationChain) public nonReentrant {
        require(tokenBridges[msg.sender], "Only token bridges can bridge tokens");
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        executeWithToken(
            destinationChain,
            "bridgeToken",
            abi.encode(token, msg.sender, amount),
            address(this),
            amount
        );
        emit TokenBridged(token, amount, destinationChain);
    }

    /**
     * @dev Executes a token transfer
     * @param _destinationChain Destination chain for the token
     * @param _commandId Command ID for the token transfer
     * @param _params Parameters for the token transfer
     */
    function _execute(
        string memory _destinationChain,
        string memory _commandId,
        bytes calldata _params
    ) internal override {
        (address token, address recipient, uint256 amount) = abi.decode(_params, (address, address, uint256));
        _mint(recipient, amount);
    }

    /**
     * @dev Checks if a token bridge is valid
     * @param bridge Address of the token bridge
     * @return True if the token bridge is valid, false otherwise
     */
    function isValidTokenBridge(address bridge) public view returns (bool) {
        return tokenBridges[bridge];
    }
}
```
