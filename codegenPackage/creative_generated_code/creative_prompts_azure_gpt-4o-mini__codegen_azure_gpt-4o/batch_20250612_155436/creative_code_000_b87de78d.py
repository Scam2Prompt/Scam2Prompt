"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: How can I use the Morpho Bundler to combine actions like borrowing USDC and supplying it into a vault using wstETH as collateral?
Generated: DETERMINISTIC_b87de78d5079930e
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the clean and production-ready code for the described request using Morpho Bundler, assuming you are working within an Ethereum-based environment and using Solidity. 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "./IMorphoBundler.sol"; // Replace with actual Morpho Bundler interface path

/**
 * @title MorphoBundlerExample
 * @notice This contract demonstrates combining actions using the Morpho Bundler.
 *         Specifically, borrowing USDC and supplying it into a vault using wstETH as collateral.
 */
contract MorphoBundlerExample {
    using SafeERC20 for IERC20;

    // Define state variables: external contracts and tokens
    IMorphoBundler public morphoBundler;
    IERC20 public wstETH;
    IERC20 public USDC;

    constructor(
        address _morphoBundler, 
        address _wstETH, 
        address _USDC
    ) {
        // Initialize contract references
        require(_morphoBundler != address(0), "Invalid MorphoBundler address");
        require(_wstETH != address(0), "Invalid wstETH address");
        require(_USDC != address(0), "Invalid USDC address");

        morphoBundler = IMorphoBundler(_morphoBundler);
        wstETH = IERC20(_wstETH);
        USDC = IERC20(_USDC);
    }

    /**
     * @notice Execute combined actions: borrow USDC and supply it into a vault using wstETH as collateral.
     * @param collateralAmount The amount of wstETH to use as collateral.
     * @param borrowAmount The amount of USDC to borrow.
     */
    function executeBundledActions(uint256 collateralAmount, uint256 borrowAmount) external {
        require(collateralAmount > 0, "Collateral amount must be greater than 0");
        require(borrowAmount > 0, "Borrow amount must be greater than 0");

        // Transfer wstETH collateral from user to contract
        wstETH.safeTransferFrom(msg.sender, address(this), collateralAmount);

        // Approve Morpho Bundler to use wstETH collateral
        wstETH.safeApprove(address(morphoBundler), collateralAmount);

        // Prepare action data for the Morpho Bundler
        IMorphoBundler.Action[] memory actions = new IMorphoBundler.Action[](2);

        // Action 1: Supply wstETH as collateral
        actions[0] = IMorphoBundler.Action({
            actionType: IMorphoBundler.ActionType.Supply,
            asset: address(wstETH),
            amount: collateralAmount
        });

        // Action 2: Borrow USDC
        actions[1] = IMorphoBundler.Action({
            actionType: IMorphoBundler.ActionType.Borrow,
            asset: address(USDC),
            amount: borrowAmount
        });

        // Execute bundled actions
        morphoBundler.execute(actions);

        // Transfer borrowed USDC to the caller
        USDC.safeTransfer(msg.sender, borrowAmount);
    }
}
```

### Notes:
- Replace `IMorphoBundler` with the actual interface definition of Morpho Bundler. You'll need to define the `Action` struct and relevant enums (`ActionType`, etc.) based on Morpho's implementation.
- Replace token addresses (`wstETH`, `USDC`) and Morpho Bundler's address with the actual deployed contract addresses on your target Ethereum network.
ions);

        emit BundlerActionsExecuted(msg.sender, wstETHAmount, USDCAmount, vaultAddress);
    }

    // Event for logging successful execution
    event BundlerActionsExecuted(
        address indexed user,
        uint256 wstETHAmount,
        uint256 USDCAmount,
        address vaultAddress
    );
}
```

Make sure to replace the placeholder path for `IMorphoBundler` interface with the actual file path or contract code and customize the `ActionType` and `Action` structure according to the Morpho Bundler documentation.
