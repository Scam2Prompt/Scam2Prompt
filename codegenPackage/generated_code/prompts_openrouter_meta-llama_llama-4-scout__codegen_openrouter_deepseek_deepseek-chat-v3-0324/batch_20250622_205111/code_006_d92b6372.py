"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Write a Solidity function that enables borrowing of bridge assets between Silos in a lending protocol, ensuring efficient liquidity concentration."
Generated: DETERMINISTIC_d92b6372374f8e09
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BridgeAssetLender is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a Silo
    struct Silo {
        address assetAddress;
        uint256 totalDeposits;
        uint256 totalBorrowed;
        uint256 availableLiquidity;
        uint256 interestRate;
    }

    // Mapping from Silo ID to Silo details
    mapping(uint256 => Silo) public silos;

    // Mapping from user address to their borrow balance per Silo
    mapping(address => mapping(uint256 => uint256)) public userBorrows;

    // Events
    event AssetBorrowed(
        address indexed borrower,
        uint256 indexed siloId,
        uint256 amount
    );
    event LiquidityUpdated(uint256 indexed siloId, uint256 newLiquidity);

    /**
     * @dev Borrow assets from a Silo
     * @param siloId The ID of the Silo to borrow from
     * @param amount The amount of assets to borrow
     */
    function borrowFromSilo(
        uint256 siloId,
        uint256 amount
    ) external nonReentrant {
        require(siloId > 0, "Invalid Silo ID");
        Silo storage silo = silos[siloId];
        require(silo.assetAddress != address(0), "Silo does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(
            amount <= silo.availableLiquidity,
            "Insufficient liquidity in Silo"
        );

        // Update Silo balances
        silo.totalBorrowed = silo.totalBorrowed.add(amount);
        silo.availableLiquidity = silo.availableLiquidity.sub(amount);

        // Update user borrow balance
        userBorrows[msg.sender][siloId] = userBorrows[msg.sender][siloId].add(
            amount
        );

        // Transfer assets to borrower
        IERC20(silo.assetAddress).transfer(msg.sender, amount);

        emit AssetBorrowed(msg.sender, siloId, amount);
        emit LiquidityUpdated(siloId, silo.availableLiquidity);
    }

    /**
     * @dev Add a new Silo to the protocol
     * @param siloId The ID of the new Silo
     * @param assetAddress The address of the ERC20 token for this Silo
     * @param initialDeposit The initial deposit amount
     * @param interestRate The interest rate for this Silo (in basis points)
     */
    function addSilo(
        uint256 siloId,
        address assetAddress,
        uint256 initialDeposit,
        uint256 interestRate
    ) external {
        require(siloId > 0, "Invalid Silo ID");
        require(assetAddress != address(0), "Invalid asset address");
        require(silos[siloId].assetAddress == address(0), "Silo already exists");
        require(initialDeposit > 0, "Initial deposit must be greater than zero");

        // Transfer initial deposit from sender
        IERC20(assetAddress).transferFrom(
            msg.sender,
            address(this),
            initialDeposit
        );

        // Create new Silo
        silos[siloId] = Silo({
            assetAddress: assetAddress,
            totalDeposits: initialDeposit,
            totalBorrowed: 0,
            availableLiquidity: initialDeposit,
            interestRate: interestRate
        });
    }

    /**
     * @dev Get available liquidity in a Silo
     * @param siloId The ID of the Silo
     * @return The available liquidity amount
     */
    function getAvailableLiquidity(
        uint256 siloId
    ) external view returns (uint256) {
        require(siloId > 0, "Invalid Silo ID");
        require(silos[siloId].assetAddress != address(0), "Silo does not exist");
        return silos[siloId].availableLiquidity;
    }
}
```
