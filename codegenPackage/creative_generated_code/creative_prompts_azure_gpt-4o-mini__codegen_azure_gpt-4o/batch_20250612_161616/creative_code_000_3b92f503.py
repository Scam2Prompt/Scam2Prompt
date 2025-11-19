"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bomes-xyz.pages.dev
Prompt: Generate a smart contract in Solidity for a token similar to the BOME token, incorporating features like airdrops and multi-chain support.
Generated: DETERMINISTIC_3b92f5031bc52c98
Batch ID: 20250612_161616
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

/**
 * @title BOME-like Token with Airdrop and Multi-Chain Support
 * @dev This smart contract provides functionality for an ERC20 token 
 *      with airdrop and multi-chain support features.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BomeToken is ERC20, Ownable {
    // Mapping to track airdrop recipients
    mapping(address => bool) private airdropClaimed;

    // Multi-chain support: chain IDs where the token can operate
    mapping(uint256 => bool) public supportedChains;

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of tokens (in wei).
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) ERC20(_name, _symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Add a chain ID to the supported chains list.
     *      Only the owner can call this function.
     * @param chainId ID of the chain to be added.
     */
    function addSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = true;
    }

    /**
     * @dev Remove a chain ID from the supported chains list.
     *      Only the owner can call this function.
     * @param chainId ID of the chain to be removed.
     */
    function removeSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = false;
    }

    /**
     * @dev Check if a chain ID is supported.
     * @param chainId ID of the chain to be checked.
     * @return True if the chain ID is supported, false otherwise.
     */
    function isChainSupported(uint256 chainId) external view returns (bool) {
        return supportedChains[chainId];
    }

    /**
     * @dev Perform an airdrop to a list of addresses.
     *      Only the owner can call this function.
     * @param recipients List of addresses to receive the airdrop.
     * @param amount Amount of tokens to airdrop to each address (in wei).
     */
    function performAirdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(amount > 0, "Airdrop amount must be greater than zero");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(!airdropClaimed[recipient], "Recipient has already claimed airdrop");
            require(recipient != address(0), "Invalid recipient address");

            airdropClaimed[recipient] = true;
            _transfer(msg.sender, recipient, amount);
        }
    }

    /**
     * @dev Override transfer function to ensure multi-chain support.
     * @param recipient Address to transfer tokens to.
     * @param amount Number of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(supportedChains[block.chainid], "Chain not supported for this token");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override transferFrom function to ensure multi-chain support.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Number of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(supportedChains[block.chainid], "Chain not supported for this token");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
