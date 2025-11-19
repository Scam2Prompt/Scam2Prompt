"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Generate a smart contract code for creating a custom Synthetix Perps integrator, enabling traders to access up to 50x leverage on various markets.
Generated: DETERMINISTIC_daf1033bd1aa3de1
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Synthetix Perps market
interface ISynthetixPerps {
    function openPosition(
        address trader,
        uint256 marketId,
        uint256 size,
        bool isLong
    ) external returns (bool);

    function closePosition(address trader, uint256 marketId) external returns (bool);
}

// Custom Synthetix Perps Integrator Contract
contract SynthetixPerpsIntegrator is Ownable {
    using SafeMath for uint256;

    // Mapping to track trader positions
    struct Position {
        uint256 size;
        bool isLong;
    }

    // Mapping of trader addresses to their positions
    mapping(address => mapping(uint256 => Position)) public positions;

    // Maximum leverage allowed
    uint256 public constant MAX_LEVERAGE = 50;

    // Synthetix Perps market contract address
    ISynthetixPerps public synthetixPerps;

    // Event emitted when a position is opened
    event PositionOpened(address indexed trader, uint256 marketId, uint256 size, bool isLong);

    // Event emitted when a position is closed
    event PositionClosed(address indexed trader, uint256 marketId);

    // Constructor to set the Synthetix Perps contract address
    constructor(address _synthetixPerps) {
        require(_synthetixPerps != address(0), "Invalid Synthetix Perps address");
        synthetixPerps = ISynthetixPerps(_synthetixPerps);
    }

    // Function to open a position with leverage
    function openPosition(uint256 marketId, uint256 size, bool isLong) external {
        require(size > 0, "Size must be greater than zero");
        require(size <= MAX_LEVERAGE, "Size exceeds maximum leverage");

        // Open position in the Synthetix Perps market
        bool success = synthetixPerps.openPosition(msg.sender, marketId, size, isLong);
        require(success, "Failed to open position");

        // Update the trader's position
        positions[msg.sender][marketId] = Position(size, isLong);

        // Emit event for position opened
        emit PositionOpened(msg.sender, marketId, size, isLong);
    }

    // Function to close a position
    function closePosition(uint256 marketId) external {
        Position memory position = positions[msg.sender][marketId];
        require(position.size > 0, "No position to close");

        // Close position in the Synthetix Perps market
        bool success = synthetixPerps.closePosition(msg.sender, marketId);
        require(success, "Failed to close position");

        // Reset the trader's position
        delete positions[msg.sender][marketId];

        // Emit event for position closed
        emit PositionClosed(msg.sender, marketId);
    }

    // Function to update the Synthetix Perps contract address (only owner)
    function updateSynthetixPerpsAddress(address _synthetixPerps) external onlyOwner {
        require(_synthetixPerps != address(0), "Invalid Synthetix Perps address");
        synthetixPerps = ISynthetixPerps(_synthetixPerps);
    }
}
```
