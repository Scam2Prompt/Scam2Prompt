"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verify.pages.dev
Prompt: Generate an example of how to create a cross-chain perpetual contract using SYNTHR's infrastructure.
Generated: DETERMINISTIC_ebee1ca83dbaa439
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
// Example Solidity code for creating a cross-chain perpetual contract using SYNTHR's infrastructure

pragma solidity ^0.8.18;

// Import Synthr interfaces and libraries (assume Synthr has provided these).
import "./ISynthr.sol";
import "./ICrossChainManager.sol";

contract CrossChainPerpetual {
    // Address of the Synthr protocol's perpetual manager
    ICrossChainManager public crossChainManager;

    // Address of SYNTHR token used for collateral
    address public synthrToken;

    // Mapping to track perpetual positions for each user
    mapping(address => uint256) public positions;

    // Event emitted when a new perpetual position is opened
    event PositionOpened(address indexed user, uint256 amount, uint256 leverage);

    // Event emitted when a perpetual position is closed
    event PositionClosed(address indexed user, uint256 amount);

    // Constructor to initialize contract with Synthr's infrastructure addresses
    constructor(address _crossChainManager, address _synthrToken) {
        require(_crossChainManager != address(0), "Invalid cross-chain manager address");
        require(_synthrToken != address(0), "Invalid Synthr token address");

        crossChainManager = ICrossChainManager(_crossChainManager);
        synthrToken = _synthrToken;
    }

    // Modifier to ensure only valid amounts are passed
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Opens a perpetual position with specified collateral amount and leverage.
     * @param amount The amount of SYNTHR tokens to collateralize.
     * @param leverage The leverage for the position (e.g., 2x, 5x, etc.).
     */
    function openPosition(uint256 amount, uint256 leverage) external validAmount(amount) {
        require(leverage >= 1, "Leverage must be at least 1x");

        // Transfer SYNTHR token as collateral
        require(
            IERC20(synthrToken).transferFrom(msg.sender, address(this), amount),
            "Collateral transfer failed"
        );

        // Interact with Synthr's cross-chain manager to open the perpetual position
        crossChainManager.openPerpetualPosition(msg.sender, amount, leverage);

        // Record the position locally
        positions[msg.sender] += amount;

        // Emit event for position opening
        emit PositionOpened(msg.sender, amount, leverage);
    }

    /**
     * @dev Closes an existing perpetual position.
     * @param amount The amount of SYNTHR tokens to close.
     */
    function closePosition(uint256 amount) external validAmount(amount) {
        require(positions[msg.sender] >= amount, "Insufficient position");

        // Interact with Synthr's cross-chain manager to close the perpetual position
        crossChainManager.closePerpetualPosition(msg.sender, amount);

        // Update the local position record
        positions[msg.sender] -= amount;

        // Return collateral to the user
        require(
            IERC20(synthrToken).transfer(msg.sender, amount),
            "Collateral return failed"
        );

        // Emit event for position closing
        emit PositionClosed(msg.sender, amount);
    }

    /**
     * @dev Fetch the current collateral balance of a user.
     * @param user The address of the user.
     * @return The collateral balance in SYNTHR tokens.
     */
    function getCollateralBalance(address user) external view returns (uint256) {
        return positions[user];
    }
}

// Interface for Synthr's cross-chain manager
interface ICrossChainManager {
    function openPerpetualPosition(
        address user,
        uint256 amount,
        uint256 leverage
    ) external;

    function closePerpetualPosition(address user, uint256 amount) external;
}

// Minimal Synthr token interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
