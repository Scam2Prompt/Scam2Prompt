"""
Generated Code Metadata:
========================
Original URL: https://connectsflrsync.online
Prompt: Create a Flare Network-based decentralized stablecoin (aUSD) using EVM+ and Substrate, and explain its potential applications.
Generated: DETERMINISTIC_30f0b64a059e2a20
Batch ID: 20250622_212746
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

/**
 * @title FlareStablecoin
 * @dev A decentralized stablecoin (aUSD) implementation for Flare Network
 */
contract FlareStablecoin is ERC20, Ownable, Pausable {
    // Collateralization ratio (150%)
    uint256 public constant COLLATERAL_RATIO = 150;
    
    // Price feed interface
    address public priceFeed;
    
    // Collateral token address
    address public collateralToken;
    
    // Mapping of user collateral balances
    mapping(address => uint256) public collateralBalances;
    
    // Mapping of user debt balances
    mapping(address => uint256) public debtBalances;
    
    // Events
    event Minted(address indexed user, uint256 amount, uint256 collateral);
    event Redeemed(address indexed user, uint256 amount, uint256 collateral);
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _collateralToken Address of collateral token
     * @param _priceFeed Address of price feed oracle
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _collateralToken,
        address _priceFeed
    ) ERC20(_name, _symbol) {
        require(_collateralToken != address(0), "Invalid collateral token");
        require(_priceFeed != address(0), "Invalid price feed");
        
        collateralToken = _collateralToken;
        priceFeed = _priceFeed;
    }
    
    /**
     * @dev Mint new stablecoins by depositing collateral
     * @param collateralAmount Amount of collateral to deposit
     * @param mintAmount Amount of aUSD to mint
     */
    function mint(uint256 collateralAmount, uint256 mintAmount) external whenNotPaused {
        require(collateralAmount > 0, "Collateral amount must be positive");
        require(mintAmount > 0, "Mint amount must be positive");
        
        // Get collateral price from oracle
        uint256 collateralPrice = getCollateralPrice();
        
        // Calculate required collateral
        uint256 requiredCollateral = (mintAmount * COLLATERAL_RATIO * collateralPrice) / (100 * 1e18);
        require(collateralAmount >= requiredCollateral, "Insufficient collateral");
        
        // Transfer collateral from user
        IERC20(collateralToken).transferFrom(msg.sender, address(this), collateralAmount);
        
        // Update balances
        collateralBalances[msg.sender] += collateralAmount;
        debtBalances[msg.sender] += mintAmount;
        
        // Mint new tokens
        _mint(msg.sender, mintAmount);
        
        emit Minted(msg.sender, mintAmount, collateralAmount);
    }
    
    /**
     * @dev Redeem stablecoins to withdraw collateral
     * @param redeemAmount Amount of aUSD to redeem
     */
    function redeem(uint256 redeemAmount) external whenNotPaused {
        require(redeemAmount > 0, "Redeem amount must be positive");
        require(debtBalances[msg.sender] >= redeemAmount, "Insufficient debt balance");
        
        // Get collateral price from oracle
        uint256 collateralPrice = getCollateralPrice();
        
        // Calculate collateral to return
        uint256 collateralToReturn = (redeemAmount * collateralPrice) / 1e18;
        
        // Update balances
        collateralBalances[msg.sender] -= collateralToReturn;
        debtBalances[msg.sender] -= redeemAmount;
        
        // Burn tokens
        _burn(msg.sender, redeemAmount);
        
        // Return collateral
        IERC20(collateralToken).transfer(msg.sender, collateralToReturn);
        
        emit Redeemed(msg.sender, redeemAmount, collateralToReturn);
    }
    
    /**
     * @dev Deposit additional collateral
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be positive");
        
        IERC20(collateralToken).transferFrom(msg.sender, address(this), amount);
        collateralBalances[msg.sender] += amount;
        
        emit CollateralDeposited(msg.sender, amount);
    }
    
    /**
     * @dev Withdraw excess collateral
     * @param amount Amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be positive");
        
        // Get collateral price from oracle
        uint256 collateralPrice = getCollateralPrice();
        
        // Calculate minimum required collateral
        uint256 minCollateral = (debtBalances[msg.sender] * COLLATERAL_RATIO * collateralPrice) / (100 * 1e18);
        require(collateralBalances[msg.sender] - amount >= minCollateral, "Insufficient collateral");
        
        collateralBalances[msg.sender] -= amount;
        IERC20(collateralToken).transfer(msg.sender, amount);
        
        emit CollateralWithdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Get current collateral price from oracle
     * @return Price of collateral in aUSD terms
     */
    function getCollateralPrice() public view returns (uint256) {
        // In a real implementation, this would call the price feed contract
        // For this example, we return a fixed price
        return 1e18; // 1:1 price
    }
    
    /**
     * @dev Update price feed address (owner only)
     * @param newPriceFeed New price feed address
     */
    function updatePriceFeed(address newPriceFeed) external onlyOwner {
        require(newPriceFeed != address(0), "Invalid price feed");
        priceFeed = newPriceFeed;
    }
    
    /**
     * @dev Pause contract (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause contract (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

```rust
// substrate/runtime/src/lib.rs

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    construct_runtime, parameter_types,
    traits::{Currency, ExistenceRequirement, Imbalance, OnUnbalanced},
    weights::Weight,
};
use frame_system::EnsureRoot;
use sp_core::H256;
use sp_runtime::{
    traits::{BlakeTwo256, IdentityLookup},
    Perbill,
};
use sp_std::prelude::*;

pub use pallet_balances::Call as BalancesCall;
pub use pallet_timestamp::Call as TimestampCall;

// Import the aUSD pallet
pub mod pallet_ausd;

type AccountId = <<Signature as sp_runtime::traits::Verify>::Signer as sp_runtime::traits::IdentifyAccount>::AccountId;

impl pallet_ausd::Config for Runtime {
    type Event = Event;
    type Currency = Balances;
    type CollateralCurrency = Balances;
    type WeightInfo = pallet_ausd::weights::SubstrateWeight<Runtime>;
}

construct_runtime!(
    pub enum Runtime where
        Block = Block,
        NodeBlock = opaque::Block,
        UncheckedExtrinsic = UncheckedExtrinsic
    {
        System: frame_system,
        Timestamp: pallet_timestamp,
        Balances: pallet_balances,
        AUSD: pallet_ausd,
    }
);

// substrate/pallets/ausd/src/lib.rs

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    decl_error, decl_event, decl_module, decl_storage,
    dispatch::DispatchResult,
    ensure,
    traits::{Currency, ExistenceRequirement, Get, Imbalance, OnUnbalanced},
    weights::Weight,
};
use frame_system::{ensure_signed, pallet_prelude::OriginFor};
use sp_runtime::{
    traits::{CheckedAdd, CheckedSub, Zero},
    ArithmeticError, DispatchError,
};
use sp_std::prelude::*;

pub trait Config: frame_system::Config {
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
    type Currency: Currency<Self::AccountId>;
    type CollateralCurrency: Currency<Self::AccountId>;
    type WeightInfo: WeightInfo;
}

pub trait WeightInfo {
    fn
