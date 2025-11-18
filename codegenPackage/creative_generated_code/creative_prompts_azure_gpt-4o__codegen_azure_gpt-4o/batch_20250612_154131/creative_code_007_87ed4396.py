"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.com
Prompt: Write a Solidity function to interact with Morpho's lending platform and securely deposit collateral into trustless smart contracts. Include security best practices based on Morpho's audits.
Generated: DETERMINISTIC_87ed4396444d1d0a
Batch ID: 20250612_154131
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
 * @title MorphoCollateralDeposit
 * @dev A secure contract function to deposit collateral into Morpho's lending platform.
 *      Includes security best practices based on audits and common Solidity guidelines.
 */
interface IMorpho {
    function supply(address _asset, address _onBehalfOf, uint256 _amount) external;
}

contract MorphoCollateralDeposit {
    // Address of the Morpho protocol contract
    IMorpho public morpho;
    
    // Event for successful deposit
    event CollateralDeposited(address indexed depositor, address indexed asset, uint256 amount);

    /**
     * @dev Constructor to initialize the Morpho contract address.
     * @param _morphoAddress Address of the Morpho protocol contract.
     */
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho contract address");
        morpho = IMorpho(_morphoAddress);
    }

    /**
     * @dev Deposits collateral into the Morpho lending platform.
     * @param _asset The address of the token to be used as collateral.
     * @param _amount The amount of tokens to deposit.
     */
    function depositCollateral(address _asset, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_asset != address(0), "Invalid asset address");

        // Transfer the tokens from the sender to this contract
        // This assumes the token follows the ERC20 standard
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Approve Morpho contract to spend the tokens
        IERC20(_asset).approve(address(morpho), _amount);

        // Call the Morpho protocol to deposit the collateral
        morpho.supply(_asset, msg.sender, _amount);

        // Emit event for successful deposit
        emit CollateralDeposited(msg.sender, _asset, _amount);
    }
}

/**
 * @dev Interface for ERC20 tokens used for collateral.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
