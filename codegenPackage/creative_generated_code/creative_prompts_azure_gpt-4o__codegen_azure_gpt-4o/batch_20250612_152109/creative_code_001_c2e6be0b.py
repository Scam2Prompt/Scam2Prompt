"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinumult.pages.dev
Prompt: Generate Solidity code for an ERC-20 token contract that supports multichain bridging using Axelar ITS. Ensure the contract includes mechanisms for permissionless bridging and token wrapping.
Generated: DETERMINISTIC_c2e6be0baf107052
Batch ID: 20250612_152109
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

// Import necessary interfaces from Axelar
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Axelar Gateway
interface IAxelarGateway {
    function sendToken(
        string calldata destinationChain,
        string calldata destinationAddress,
        string calldata symbol,
        uint256 amount
    ) external;
}

contract MultiChainERC20 is ERC20, Ownable {
    using SafeMath for uint256;

    // Axelar Gateway address
    IAxelarGateway public gateway;

    // Token symbol for Axelar
    string public axelarSymbol;

    // Event to track token bridging
    event TokensBridged(
        address indexed from,
        string destinationChain,
        string destinationAddress,
        uint256 amount
    );

    // Modifier to ensure Gateway address is set
    modifier gatewaySet() {
        require(address(gateway) != address(0), "Axelar Gateway not set");
        _;
    }

    /**
     * @dev Constructor for the MultiChainERC20 token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of the token.
     * @param _gateway Address of the Axelar Gateway contract.
     * @param _axelarSymbol Symbol used by Axelar for this token.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _gateway,
        string memory _axelarSymbol
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        gateway = IAxelarGateway(_gateway);
        axelarSymbol = _axelarSymbol;
    }

    /**
     * @dev Allows the owner to update the Axelar Gateway address.
     * @param _gateway Address of the new Axelar Gateway.
     */
    function setGateway(address _gateway) external onlyOwner {
        require(_gateway != address(0), "Invalid Gateway address");
        gateway = IAxelarGateway(_gateway);
    }

    /**
     * @dev Bridges tokens to another chain via Axelar.
     * @param destinationChain The chain to bridge tokens to.
     * @param destinationAddress The address to send tokens to on the destination chain.
     * @param amount The amount of tokens to bridge.
     */
    function bridgeTokens(
        string calldata destinationChain,
        string calldata destinationAddress,
        uint256 amount
    ) external gatewaySet {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the tokens on the source chain
        _burn(msg.sender, amount);

        // Call Axelar Gateway to bridge tokens
        gateway.sendToken(destinationChain, destinationAddress, axelarSymbol, amount);

        emit TokensBridged(msg.sender, destinationChain, destinationAddress, amount);
    }

    /**
     * @dev Wraps native tokens or other custom tokens into the ERC-20 token format.
     * @param recipient Address to receive the wrapped tokens.
     * @param amount Amount of tokens to wrap.
     */
    function wrapTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Mint wrapped tokens for the recipient
        _mint(recipient, amount);
    }

    /**
     * @dev Unwrap tokens by burning them.
     * @param recipient Address to receive the underlying asset (if applicable).
     * @param amount Amount of tokens to unwrap.
     */
    function unwrapTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Burn the tokens and transfer underlying assets if applicable (not implemented here)
        _burn(recipient, amount);
    }
}
```
