"""
Generated Code Metadata:
========================
Original URL: https://asx-capital.pages.dev
Prompt: Write a smart contract that manages asset diversification for $ASX holders, incorporating real-world assets, DeFi yield, and venture capital exposure as described on the ASX Capital webpage.
Generated: DETERMINISTIC_9cf07bf9ad0737d9
Batch ID: 20250612_152018
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ASXDiversification is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract
    IERC20 public asxToken;

    // Diversification options
    enum DiversificationOption { RealWorldAssets, DeFiYield, VentureCapital }

    // User allocations
    struct UserAllocation {
        uint256 realWorldAssets;
        uint256 defiYield;
        uint256 ventureCapital;
        uint256 lastUpdate;
    }

    // Total allocations
    struct TotalAllocation {
        uint256 realWorldAssets;
        uint256 defiYield;
        uint256 ventureCapital;
    }

    // Mapping of user addresses to their allocations
    mapping(address => UserAllocation) public userAllocations;

    // Total allocations across all users
    TotalAllocation public totalAllocations;

    // Minimum investment amounts
    uint256 public constant MIN_REAL_WORLD_ASSETS = 1000 ether;
    uint256 public constant MIN_DEFI_YIELD = 500 ether;
    uint256 public constant MIN_VENTURE_CAPITAL = 250 ether;

    // Allocation percentages (basis points)
    uint256 public realWorldAssetsFee = 100; // 1%
    uint256 public defiYieldFee = 75;       // 0.75%
    uint256 public ventureCapitalFee = 150; // 1.5%

    // Addresses for each diversification pool
    address public realWorldAssetsPool;
    address public defiYieldPool;
    address public ventureCapitalPool;

    // Events
    event Diversified(
        address indexed user,
        uint256 realWorldAssets,
        uint256 defiYield,
        uint256 ventureCapital,
        uint256 timestamp
    );
    event Rebalanced(
        address indexed user,
        uint256 realWorldAssets,
        uint256 defiYield,
        uint256 ventureCapital,
        uint256 timestamp
    );
    event Withdrawn(
        address indexed user,
        uint256 realWorldAssets,
        uint256 defiYield,
        uint256 ventureCapital,
        uint256 timestamp
    );

    constructor(
        address _asxToken,
        address _realWorldAssetsPool,
        address _defiYieldPool,
        address _ventureCapitalPool
    ) {
        require(_asxToken != address(0), "Invalid ASX token address");
        require(_realWorldAssetsPool != address(0), "Invalid RWA pool address");
        require(_defiYieldPool != address(0), "Invalid DeFi pool address");
        require(_ventureCapitalPool != address(0), "Invalid VC pool address");

        asxToken = IERC20(_asxToken);
        realWorldAssetsPool = _realWorldAssetsPool;
        defiYieldPool = _defiYieldPool;
        ventureCapitalPool = _ventureCapitalPool;
    }

    /**
     * @notice Diversify ASX holdings into different asset classes
     * @param realWorldAssets Amount to allocate to real world assets
     * @param defiYield Amount to allocate to DeFi yield
     * @param ventureCapital Amount to allocate to venture capital
     */
    function diversify(
        uint256 realWorldAssets,
        uint256 defiYield,
        uint256 ventureCapital
    ) external nonReentrant {
        require(
            realWorldAssets >= MIN_REAL_WORLD_ASSETS ||
            defiYield >= MIN_DEFI_YIELD ||
            ventureCapital >= MIN_VENTURE_CAPITAL,
            "Below minimum allocation"
        );

        uint256 totalAmount = realWorldAssets.add(defiYield).add(ventureCapital);
        require(totalAmount > 0, "No amount specified");

        // Transfer ASX tokens from user to contract
        require(
            asxToken.transferFrom(msg.sender, address(this), totalAmount),
            "Transfer failed"
        );

        // Calculate fees and net amounts
        uint256 rwaNet = realWorldAssets.sub(realWorldAssets.mul(realWorldAssetsFee).div(10000));
        uint256 defiNet = defiYield.sub(defiYield.mul(defiYieldFee).div(10000));
        uint256 vcNet = ventureCapital.sub(ventureCapital.mul(ventureCapitalFee).div(10000));

        // Update user allocations
        UserAllocation storage allocation = userAllocations[msg.sender];
        allocation.realWorldAssets = allocation.realWorldAssets.add(rwaNet);
        allocation.defiYield = allocation.defiYield.add(defiNet);
        allocation.ventureCapital = allocation.ventureCapital.add(vcNet);
        allocation.lastUpdate = block.timestamp;

        // Update total allocations
        totalAllocations.realWorldAssets = totalAllocations.realWorldAssets.add(rwaNet);
        totalAllocations.defiYield = totalAllocations.defiYield.add(defiNet);
        totalAllocations.ventureCapital = totalAllocations.ventureCapital.add(vcNet);

        // Transfer funds to respective pools
        if (realWorldAssets > 0) {
            require(
                asxToken.transfer(realWorldAssetsPool, realWorldAssets),
                "RWA transfer failed"
            );
        }
        if (defiYield > 0) {
            require(
                asxToken.transfer(defiYieldPool, defiYield),
                "DeFi transfer failed"
            );
        }
        if (ventureCapital > 0) {
            require(
                asxToken.transfer(ventureCapitalPool, ventureCapital),
                "VC transfer failed"
            );
        }

        emit Diversified(
            msg.sender,
            rwaNet,
            defiNet,
            vcNet,
            block.timestamp
        );
    }

    /**
     * @notice Rebalance user's allocations
     * @param newRealWorldAssets New allocation for real world assets
     * @param newDefiYield New allocation for DeFi yield
     * @param newVentureCapital New allocation for venture capital
     */
    function rebalance(
        uint256 newRealWorldAssets,
        uint256 newDefiYield,
        uint256 newVentureCapital
    ) external nonReentrant {
        UserAllocation storage allocation = userAllocations[msg.sender];
        require(allocation.lastUpdate > 0, "No existing allocation");

        uint256 currentTotal = allocation.realWorldAssets
            .add(allocation.defiYield)
            .add(allocation.ventureCapital);

        uint256 newTotal = newRealWorldAssets
            .add(newDefiYield)
            .add(newVentureCapital);

        require(newTotal == currentTotal, "Total must remain the same");

        // Update total allocations
        totalAllocations.realWorldAssets = totalAllocations.realWorldAssets
            .sub(allocation.realWorldAssets)
            .add(newRealWorldAssets);
        totalAllocations.defiYield = totalAllocations.defiYield
            .sub(allocation.defiYield)
            .add(newDefiYield);
        totalAllocations.ventureCapital = totalAllocations.ventureCapital
            .sub(allocation.ventureCapital)
            .add(newVentureCapital);

        // Update user allocation
        allocation.realWorldAssets = newRealWorldAssets;
        allocation.defiYield = newDefiYield;
        allocation.ventureCapital = newVentureCapital;
        allocation.lastUpdate = block.timestamp;

        emit Rebalanced(
            msg.sender,
            newRealWorldAssets,
            newDefiYield,
            newVentureCapital,
            block.timestamp
        );
    }

    /**
     * @notice Withdraw all allocated funds
     */
    function withdraw() external nonReentrant {
        UserAllocation storage allocation = userAllocations[msg.sender];
        require(allocation.lastUpdate > 0, "No existing allocation");

        uint256 rwaAmount = allocation.realWorldAssets;
        uint256 defiAmount = allocation.defiYield;
        uint256 vcAmount = allocation.ventureCapital;

        // Update total allocations
        totalAllocations.realWorldAssets = totalAllocations.realWorldAssets.sub(rwaAmount);
        totalAllocations.defiYield = totalAllocations.defiYield.sub(defiAmount);
        totalAllocations.ventureCapital = totalAllocations.ventureCapital.sub(vcAmount);

        // Reset user allocation
        delete userAllocations[msg.sender];

        // Transfer funds back from pools to contract
        // Note: In a real implementation, this would require coordination with the pools
        // For simplicity, we assume the contract already has the funds

        // Transfer funds to user
        uint256 totalAmount = rwaAmount.add(defiAmount).add(vcAmount);
        require(
            asxToken.transfer(msg.sender, totalAmount),
            "Withdrawal transfer failed"
        );

        emit Withdrawn(
            msg.sender,
            rwaAmount,
            defiAmount,
            vcAmount,
            block.timestamp
        );
    }

    /**
     *
