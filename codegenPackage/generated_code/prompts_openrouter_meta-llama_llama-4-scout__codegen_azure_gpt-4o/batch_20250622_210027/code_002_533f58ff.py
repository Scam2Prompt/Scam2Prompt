"""
Generated Code Metadata:
========================
Original URL: https://synthr.pages.dev
Prompt: "Generate a smart contract code for creating a cross-chain perpetuals trading platform using SYNTHR's omnichain synthetic assets."
Generated: DETERMINISTIC_533f58ff2e22e0c8
Batch ID: 20250622_210027
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

/**
 * @title CrossChainPerpetuals
 * @dev A smart contract for creating a cross-chain perpetuals trading platform using SYNTHR's omnichain synthetic assets.
 * This contract allows users to trade synthetic assets across multiple chains.
 */
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface ISynthr {
    function mintSyntheticAsset(address to, string memory assetSymbol, uint256 amount) external;
    function burnSyntheticAsset(address from, string memory assetSymbol, uint256 amount) external;
    function getAssetPrice(string memory assetSymbol) external view returns (uint256);
}

contract CrossChainPerpetuals is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // SYNTHR interface
    ISynthr public synthr;

    // Supported synthetic assets
    mapping(string => bool) public supportedAssets;

    // User positions
    struct Position {
        uint256 size; // Size of the position
        uint256 entryPrice; // Entry price of the position
        bool isLong; // True for long, false for short
    }
    mapping(address => mapping(string => Position)) public userPositions;

    // Events
    event AssetSupported(string assetSymbol);
    event AssetUnsupported(string assetSymbol);
    event PositionOpened(address indexed user, string assetSymbol, uint256 size, uint256 entryPrice, bool isLong);
    event PositionClosed(address indexed user, string assetSymbol, uint256 size, uint256 exitPrice, bool isLong);

    /**
     * @dev Constructor to initialize the SYNTHR interface.
     * @param _synthr Address of the SYNTHR contract.
     */
    constructor(address _synthr) {
        require(_synthr != address(0), "Invalid SYNTHR address");
        synthr = ISynthr(_synthr);
    }

    /**
     * @dev Add a supported synthetic asset.
     * @param assetSymbol Symbol of the synthetic asset.
     */
    function addSupportedAsset(string memory assetSymbol) external onlyOwner {
        supportedAssets[assetSymbol] = true;
        emit AssetSupported(assetSymbol);
    }

    /**
     * @dev Remove a supported synthetic asset.
     * @param assetSymbol Symbol of the synthetic asset.
     */
    function removeSupportedAsset(string memory assetSymbol) external onlyOwner {
        supportedAssets[assetSymbol] = false;
        emit AssetUnsupported(assetSymbol);
    }

    /**
     * @dev Open a position in a synthetic asset.
     * @param assetSymbol Symbol of the synthetic asset.
     * @param size Size of the position.
     * @param isLong True for long position, false for short position.
     */
    function openPosition(string memory assetSymbol, uint256 size, bool isLong) external nonReentrant {
        require(supportedAssets[assetSymbol], "Asset not supported");
        require(size > 0, "Position size must be greater than zero");

        uint256 assetPrice = synthr.getAssetPrice(assetSymbol);
        require(assetPrice > 0, "Invalid asset price");

        // Mint synthetic asset to the user
        synthr.mintSyntheticAsset(msg.sender, assetSymbol, size);

        // Record the position
        userPositions[msg.sender][assetSymbol] = Position({
            size: size,
            entryPrice: assetPrice,
            isLong: isLong
        });

        emit PositionOpened(msg.sender, assetSymbol, size, assetPrice, isLong);
    }

    /**
     * @dev Close a position in a synthetic asset.
     * @param assetSymbol Symbol of the synthetic asset.
     */
    function closePosition(string memory assetSymbol) external nonReentrant {
        Position storage position = userPositions[msg.sender][assetSymbol];
        require(position.size > 0, "No open position found");

        uint256 assetPrice = synthr.getAssetPrice(assetSymbol);
        require(assetPrice > 0, "Invalid asset price");

        // Burn synthetic asset from the user
        synthr.burnSyntheticAsset(msg.sender, assetSymbol, position.size);

        // Calculate profit or loss
        uint256 pnl;
        if (position.isLong) {
            pnl = position.size.mul(assetPrice.sub(position.entryPrice)).div(position.entryPrice);
        } else {
            pnl = position.size.mul(position.entryPrice.sub(assetPrice)).div(position.entryPrice);
        }

        // Reset the position
        delete userPositions[msg.sender][assetSymbol];

        emit PositionClosed(msg.sender, assetSymbol, position.size, assetPrice, position.isLong);
    }

    /**
     * @dev Get the details of a user's position.
     * @param user Address of the user.
     * @param assetSymbol Symbol of the synthetic asset.
     * @return Position details.
     */
    function getPosition(address user, string memory assetSymbol) external view returns (Position memory) {
        return userPositions[user][assetSymbol];
    }
}
```
