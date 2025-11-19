"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-token.xyz
Prompt: Explain how to implement fractional ownership of assets using the Rexas Token Builder.
Generated: DETERMINISTIC_e7ffc23b808cbe01
Batch ID: 20250612_161226
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
 * @title Fractional Ownership Asset Token
 * @dev This contract allows fractional ownership of assets using ERC20 tokens created with Rexas Token Builder.
 * Each token represents a fraction of ownership of the underlying asset.
 */
contract FractionalAssetOwnership {
    // State variables
    string public assetName; // Name of the asset
    uint256 public totalFractions; // Total fractions of the asset
    address public owner; // Contract owner
    ERC20 public fractionalToken; // ERC20 token for fractional ownership

    // Events
    event AssetFractionTransfer(address indexed from, address indexed to, uint256 amount);
    event AssetFractionMint(address indexed recipient, uint256 amount);
    event AssetFractionBurn(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to initialize the fractional asset ownership contract.
     * @param _assetName Name of the asset represented by fractional ownership.
     * @param _tokenAddress Address of the ERC20 token (created via Rexas Token Builder) used for fractional ownership.
     */
    constructor(string memory _assetName, address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        assetName = _assetName;
        fractionalToken = ERC20(_tokenAddress);
        owner = msg.sender; // Set the contract owner to the deployer
    }

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Mint fractional ownership tokens for the asset.
     * @param recipient Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mintFractions(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        fractionalToken.mint(recipient, amount);
        totalFractions += amount;
        emit AssetFractionMint(recipient, amount);
    }

    /**
     * @dev Burn fractional ownership tokens of the asset.
     * @param holder Address whose tokens will be burned.
     * @param amount Number of tokens to burn.
     */
    function burnFractions(address holder, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        fractionalToken.burn(holder, amount);
        totalFractions -= amount;
        emit AssetFractionBurn(holder, amount);
    }

    /**
     * @dev Transfer fractional ownership tokens between holders.
     * @param from Address sending the tokens.
     * @param to Address receiving the tokens.
     * @param amount Number of tokens to transfer.
     */
    function transferFractions(address from, address to, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        fractionalToken.transferFrom(from, to, amount);
        emit AssetFractionTransfer(from, to, amount);
    }
}

/**
 * @dev ERC20 interface required for token interactions.
 */
interface ERC20 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
    function transferFrom(address from, address to, uint256 amount) external;
}
```
