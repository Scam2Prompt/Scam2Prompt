"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbtc-network.web.app
Prompt: Provide an example of an Ethereum-based decentralized exchange (DEX) smart contract that utilizes Wrapped Bitcoin (WBTC) for token trades.
Generated: DETERMINISTIC_ce37b1b634344fac
Batch ID: 20250612_152321
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
 * @title Decentralized Exchange (DEX) Smart Contract
 * @dev This contract facilitates token trades using Wrapped Bitcoin (WBTC) as a trading pair.
 *      Users can swap ERC20 tokens for WBTC and vice versa.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract WBTCDex {
    // Address of the Wrapped Bitcoin (WBTC) token contract
    IERC20 public immutable WBTC;

    // Fee in basis points (1 basis point = 0.01%)
    uint256 public immutable feeBasisPoints;
    address public immutable feeCollector;

    // Event emitted for every token swap
    event TokenSwapped(address indexed user, address indexed token, uint256 tokenAmount, uint256 wbtcAmount);

    // Event emitted when fees are collected
    event FeesCollected(address indexed collector, uint256 amount);

    /**
     * @dev Constructor to initialize the DEX contract.
     * @param _wbtc Address of the WBTC token contract.
     * @param _feeBasisPoints Fee taken by the DEX (e.g., 25 = 0.25%).
     * @param _feeCollector Address where fees are collected.
     */
    constructor(IERC20 _wbtc, uint256 _feeBasisPoints, address _feeCollector) {
        require(address(_wbtc) != address(0), "WBTC address cannot be zero");
        require(_feeBasisPoints <= 10000, "Fee basis points must be <= 10000");
        require(_feeCollector != address(0), "Fee collector address cannot be zero");

        WBTC = _wbtc;
        feeBasisPoints = _feeBasisPoints;
        feeCollector = _feeCollector;
    }

    /**
     * @dev Swaps ERC20 token for WBTC.
     * @param token Address of the ERC20 token being swapped.
     * @param tokenAmount Amount of ERC20 tokens to swap.
     * @param wbtcAmount Expected amount of WBTC to receive.
     * @notice Ensure that the user has approved the contract to spend their ERC20 tokens.
     */
    function swapTokenForWBTC(IERC20 token, uint256 tokenAmount, uint256 wbtcAmount) external {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(wbtcAmount > 0, "WBTC amount must be greater than zero");

        // Calculate fee
        uint256 fee = (wbtcAmount * feeBasisPoints) / 10000;
        uint256 finalWbtcAmount = wbtcAmount - fee;

        // Transfer the ERC20 tokens from the user to the contract
        require(
            token.transferFrom(msg.sender, address(this), tokenAmount),
            "Token transfer failed"
        );

        // Transfer WBTC to the user (after deducting fee)
        require(
            WBTC.transfer(msg.sender, finalWbtcAmount),
            "WBTC transfer failed"
        );

        // Collect fee
        if (fee > 0) {
            require(
                WBTC.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
            emit FeesCollected(feeCollector, fee);
        }

        emit TokenSwapped(msg.sender, address(token), tokenAmount, wbtcAmount);
    }

    /**
     * @dev Swaps WBTC for an ERC20 token.
     * @param token Address of the ERC20 token to receive.
     * @param wbtcAmount Amount of WBTC to swap.
     * @param tokenAmount Expected amount of ERC20 tokens to receive.
     * @notice Ensure that the user has approved the contract to spend their WBTC tokens.
     */
    function swapWBTCForToken(IERC20 token, uint256 wbtcAmount, uint256 tokenAmount) external {
        require(wbtcAmount > 0, "WBTC amount must be greater than zero");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Calculate fee
        uint256 fee = (tokenAmount * feeBasisPoints) / 10000;
        uint256 finalTokenAmount = tokenAmount - fee;

        // Transfer WBTC from the user to the contract
        require(
            WBTC.transferFrom(msg.sender, address(this), wbtcAmount),
            "WBTC transfer failed"
        );

        // Transfer the ERC20 tokens to the user (after deducting fee)
        require(
            token.transfer(msg.sender, finalTokenAmount),
            "Token transfer failed"
        );

        // Collect fee
        if (fee > 0) {
            require(
                token.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
            emit FeesCollected(feeCollector, fee);
        }

        emit TokenSwapped(msg.sender, address(token), tokenAmount, wbtcAmount);
    }
}
```
