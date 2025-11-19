"""
Generated Code Metadata:
========================
Original URL: https://pioneerparticle-sigma.vercel.app
Prompt: Design a smart contract for managing Universal Gas Tokens across multiple blockchain ecosystems, inspired by Particle Network's solutions.
Generated: DETERMINISTIC_9cfd1ef00d431afe
Batch ID: 20250622_211048
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Universal Gas Token
 * @dev Cross-chain compatible ERC20 token for gas fee management
 */
contract UniversalGasToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping to track bridge contracts across different chains
    mapping(address => bool) public bridgeContracts;

    // Gas price oracle address
    address public gasPriceOracle;

    // Events
    event BridgeContractAdded(address indexed bridge);
    event BridgeContractRemoved(address indexed bridge);
    event GasPriceOracleUpdated(address indexed newOracle);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) ERC20("Universal Gas Token", "UGT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Modifier to check if caller is a bridge contract
     */
    modifier onlyBridge() {
        require(bridgeContracts[msg.sender], "Caller is not a bridge contract");
        _;
    }

    /**
     * @dev Mint new tokens (only callable by owner or bridge contracts)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external whenNotPaused {
        require(
            msg.sender == owner() || bridgeContracts[msg.sender],
            "Not authorized to mint"
        );
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens (only callable by bridge contracts)
     * @param from Address whose tokens will be burned
     * @param amount Amount of tokens to burn
     */
    function burn(address from, uint256 amount) external onlyBridge whenNotPaused {
        _burn(from, amount);
        emit TokensBurned(from, amount);
    }

    /**
     * @dev Add a new bridge contract address
     * @param bridge Address of the bridge contract
     */
    function addBridgeContract(address bridge) external onlyOwner {
        require(bridge != address(0), "Invalid bridge address");
        bridgeContracts[bridge] = true;
        emit BridgeContractAdded(bridge);
    }

    /**
     * @dev Remove a bridge contract address
     * @param bridge Address of the bridge contract
     */
    function removeBridgeContract(address bridge) external onlyOwner {
        require(bridgeContracts[bridge], "Bridge not registered");
        bridgeContracts[bridge] = false;
        emit BridgeContractRemoved(bridge);
    }

    /**
     * @dev Update gas price oracle address
     * @param newOracle Address of the new gas price oracle
     */
    function updateGasPriceOracle(address newOracle) external onlyOwner {
        require(newOracle != address(0), "Invalid oracle address");
        gasPriceOracle = newOracle;
        emit GasPriceOracleUpdated(newOracle);
    }

    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to include pause functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Estimate gas cost in tokens for a transaction
     * @param gasAmount Amount of gas needed
     * @return tokenAmount Equivalent token amount
     */
    function estimateGasCost(uint256 gasAmount) external view returns (uint256) {
        require(gasPriceOracle != address(0), "Gas price oracle not set");
        // In a real implementation, this would query the oracle
        // For demo purposes, we return a fixed conversion rate
        return gasAmount.mul(1e9); // Simplified conversion rate
    }
}
```
