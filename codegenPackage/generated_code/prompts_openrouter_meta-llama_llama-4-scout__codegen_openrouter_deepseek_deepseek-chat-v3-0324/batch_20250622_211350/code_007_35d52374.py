"""
Generated Code Metadata:
========================
Original URL: https://app-orbler.pages.dev
Prompt: "Design a smart contract for a modular layer 1 blockchain powered by a stablecoin for real-world adoption."
Generated: DETERMINISTIC_35d52374a100f8f3
Batch ID: 20250622_211350
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
 * @title ModularLayer1Stablecoin
 * @dev A stablecoin-powered modular Layer 1 blockchain smart contract
 * Features:
 * - Stablecoin issuance and management
 * - Modular governance
 * - Transaction fee handling
 * - Pausable for emergency stops
 */
contract ModularLayer1Stablecoin is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Stablecoin pegged value (e.g., 1 token = 1 USD)
    uint256 public constant PEGGED_VALUE = 1 ether;
    
    // Transaction fee percentage (basis points)
    uint256 public transactionFeeBps;
    
    // Address where fees are collected
    address public feeCollector;
    
    // Mapping of module addresses with their status
    mapping(address => bool) public enabledModules;
    
    // Events
    event ModuleAdded(address indexed module);
    event ModuleRemoved(address indexed module);
    event FeeUpdated(uint256 newFeeBps);
    event FeeCollectorUpdated(address newCollector);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor initializes the stablecoin
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _initialSupply Initial token supply
     * @param _transactionFeeBps Initial transaction fee in basis points
     * @param _feeCollector Address to collect fees
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _transactionFeeBps,
        address _feeCollector
    ) ERC20(_name, _symbol) {
        require(_transactionFeeBps <= 1000, "Fee cannot exceed 10%");
        require(_feeCollector != address(0), "Invalid fee collector address");
        
        transactionFeeBps = _transactionFeeBps;
        feeCollector = _feeCollector;
        
        if (_initialSupply > 0) {
            _mint(msg.sender, _initialSupply);
        }
    }

    /**
     * @dev Mint new tokens (owner only)
     * @param to Address to receive tokens
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner whenNotPaused {
        require(to != address(0), "Invalid recipient address");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens (owner or token holder)
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external whenNotPaused {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override transfer to include fee logic
     * @param recipient Address receiving tokens
     * @param amount Amount to transfer
     */
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        whenNotPaused 
        returns (bool) 
    {
        uint256 fee = amount.mul(transactionFeeBps).div(10000);
        uint256 netAmount = amount.sub(fee);
        
        _transfer(msg.sender, recipient, netAmount);
        
        if (fee > 0) {
            _transfer(msg.sender, feeCollector, fee);
        }
        
        return true;
    }

    /**
     * @dev Override transferFrom to include fee logic
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override whenNotPaused returns (bool) {
        uint256 fee = amount.mul(transactionFeeBps).div(10000);
        uint256 netAmount = amount.sub(fee);
        
        _transfer(sender, recipient, netAmount);
        
        if (fee > 0) {
            _transfer(sender, feeCollector, fee);
        }
        
        _approve(
            sender,
            msg.sender,
            allowance(sender, msg.sender).sub(amount, "ERC20: transfer amount exceeds allowance")
        );
        
        return true;
    }

    /**
     * @dev Add a module to the system (owner only)
     * @param module Address of module to add
     */
    function addModule(address module) external onlyOwner {
        require(module != address(0), "Invalid module address");
        require(!enabledModules[module], "Module already enabled");
        
        enabledModules[module] = true;
        emit ModuleAdded(module);
    }

    /**
     * @dev Remove a module from the system (owner only)
     * @param module Address of module to remove
     */
    function removeModule(address module) external onlyOwner {
        require(enabledModules[module], "Module not enabled");
        
        enabledModules[module] = false;
        emit ModuleRemoved(module);
    }

    /**
     * @dev Update transaction fee (owner only)
     * @param newFeeBps New fee in basis points
     */
    function updateTransactionFee(uint256 newFeeBps) external onlyOwner {
        require(newFeeBps <= 1000, "Fee cannot exceed 10%");
        
        transactionFeeBps = newFeeBps;
        emit FeeUpdated(newFeeBps);
    }

    /**
     * @dev Update fee collector address (owner only)
     * @param newCollector New fee collector address
     */
    function updateFeeCollector(address newCollector) external onlyOwner {
        require(newCollector != address(0), "Invalid fee collector address");
        
        feeCollector = newCollector;
        emit FeeCollectorUpdated(newCollector);
    }

    /**
     * @dev Pause all token transfers (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Check if a module is enabled
     * @param module Address to check
     * @return bool Whether module is enabled
     */
    function isModuleEnabled(address module) external view returns (bool) {
        return enabledModules[module];
    }
}
```
