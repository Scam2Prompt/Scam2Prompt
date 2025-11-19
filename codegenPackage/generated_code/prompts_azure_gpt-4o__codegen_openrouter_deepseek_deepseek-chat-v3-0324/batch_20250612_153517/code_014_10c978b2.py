"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Create a Solidity contract for multi-chain compatibility of $HEHE tokens, ensuring seamless transactions across Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_10c978b2929ffa0e
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";

contract HEHEToken is ERC20, ERC20Burnable, Ownable, ERC20Permit {
    // Chain IDs
    uint256 public constant ETHEREUM_CHAIN_ID = 1;
    uint256 public constant BSC_CHAIN_ID = 56;
    
    // Bridge contract addresses
    address public bridgeContract;
    
    // Mapping to track nonces for cross-chain transfers
    mapping(address => uint256) public nonces;
    
    // Events
    event TokensBridged(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 sourceChainId,
        uint256 destinationChainId,
        uint256 nonce
    );
    
    event BridgeContractUpdated(address indexed newBridgeContract);

    constructor() ERC20("HEHE Token", "HEHE") ERC20Permit("HEHE Token") {
        _mint(msg.sender, 1000000000 * 10 ** decimals());
    }

    /**
     * @dev Sets the bridge contract address
     * @param _bridgeContract Address of the bridge contract
     */
    function setBridgeContract(address _bridgeContract) external onlyOwner {
        require(_bridgeContract != address(0), "Invalid bridge contract address");
        bridgeContract = _bridgeContract;
        emit BridgeContractUpdated(_bridgeContract);
    }

    /**
     * @dev Bridges tokens to another chain
     * @param amount Amount of tokens to bridge
     * @param recipient Recipient address on the destination chain
     * @param destinationChainId Chain ID of the destination chain
     */
    function bridgeTokens(uint256 amount, address recipient, uint256 destinationChainId) external {
        require(amount > 0, "Amount must be greater than 0");
        require(bridgeContract != address(0), "Bridge contract not set");
        require(
            destinationChainId == ETHEREUM_CHAIN_ID || destinationChainId == BSC_CHAIN_ID,
            "Unsupported destination chain"
        );
        
        uint256 currentChainId = block.chainid;
        require(currentChainId != destinationChainId, "Cannot bridge to same chain");
        
        _burn(msg.sender, amount);
        
        uint256 nonce = nonces[msg.sender]++;
        emit TokensBridged(
            msg.sender,
            recipient,
            amount,
            currentChainId,
            destinationChainId,
            nonce
        );
    }

    /**
     * @dev Mints tokens received from another chain
     * @param recipient Recipient address
     * @param amount Amount of tokens to mint
     * @param sourceChainId Chain ID of the source chain
     * @param nonce Nonce of the transaction on the source chain
     */
    function mintBridgedTokens(
        address recipient,
        uint256 amount,
        uint256 sourceChainId,
        uint256 nonce
    ) external {
        require(msg.sender == bridgeContract, "Only bridge contract can mint");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(
            sourceChainId == ETHEREUM_CHAIN_ID || sourceChainId == BSC_CHAIN_ID,
            "Unsupported source chain"
        );
        
        _mint(recipient, amount);
    }
}
```
