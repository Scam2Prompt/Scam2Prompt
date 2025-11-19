"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: Suggest an approach to implement a DAO-controlled fee structure similar to Whales Market's roadmap for EVM and Cosmos chains.
Generated: DETERMINISTIC_75d48dbd8005cc6f
Batch ID: 20250612_153820
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title FeeController
 * @dev DAO-controlled fee structure for EVM chains
 */
contract FeeController is Ownable {
    struct FeeTier {
        uint256 feePercentage; // Basis points (1% = 100)
        uint256 minFeeAmount;
        uint256 maxFeeAmount;
    }

    // Mapping of fee tiers by ID
    mapping(uint256 => FeeTier) public feeTiers;
    
    // Default fee tier ID
    uint256 public defaultFeeTierId = 1;
    
    // Treasury address to receive fees
    address public treasury;
    
    // Token used for fee payments (address(0) for native token)
    address public feeToken;
    
    // DAO governance address
    address public dao;
    
    // Events
    event FeeTierUpdated(uint256 tierId, uint256 feePercentage, uint256 minFee, uint256 maxFee);
    event DefaultTierChanged(uint256 newDefaultTierId);
    event TreasuryUpdated(address newTreasury);
    event FeeTokenUpdated(address newFeeToken);
    event DaoUpdated(address newDao);
    event FeesCollected(address indexed payer, uint256 amount, uint256 tierId);
    
    modifier onlyDao() {
        require(msg.sender == dao, "FeeController: caller is not the DAO");
        _;
    }
    
    /**
     * @dev Constructor
     * @param _dao DAO governance address
     * @param _treasury Treasury address
     * @param _feeToken Token address for fee payments (address(0) for native)
     */
    constructor(address _dao, address _treasury, address _feeToken) {
        require(_dao != address(0), "FeeController: invalid DAO address");
        require(_treasury != address(0), "FeeController: invalid treasury address");
        
        dao = _dao;
        treasury = _treasury;
        feeToken = _feeToken;
        
        // Initialize default fee tier (1% with min 0.01 and max 10)
        feeTiers[1] = FeeTier(100, 0.01 ether, 10 ether);
    }
    
    /**
     * @dev Update or add a fee tier
     * @param tierId ID of the tier to update
     * @param feePercentage Fee percentage in basis points
     * @param minFee Minimum fee amount
     * @param maxFee Maximum fee amount
     */
    function updateFeeTier(
        uint256 tierId,
        uint256 feePercentage,
        uint256 minFee,
        uint256 maxFee
    ) external onlyDao {
        require(tierId != 0, "FeeController: invalid tier ID");
        require(feePercentage <= 10000, "FeeController: fee exceeds 100%");
        require(minFee <= maxFee, "FeeController: min fee > max fee");
        
        feeTiers[tierId] = FeeTier(feePercentage, minFee, maxFee);
        emit FeeTierUpdated(tierId, feePercentage, minFee, maxFee);
    }
    
    /**
     * @dev Set the default fee tier
     * @param tierId ID of the default tier
     */
    function setDefaultFeeTier(uint256 tierId) external onlyDao {
        require(feeTiers[tierId].feePercentage != 0, "FeeController: tier doesn't exist");
        defaultFeeTierId = tierId;
        emit DefaultTierChanged(tierId);
    }
    
    /**
     * @dev Update treasury address
     * @param newTreasury New treasury address
     */
    function updateTreasury(address newTreasury) external onlyDao {
        require(newTreasury != address(0), "FeeController: invalid treasury address");
        treasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }
    
    /**
     * @dev Update fee token address
     * @param newFeeToken New fee token address (address(0) for native)
     */
    function updateFeeToken(address newFeeToken) external onlyDao {
        feeToken = newFeeToken;
        emit FeeTokenUpdated(newFeeToken);
    }
    
    /**
     * @dev Transfer DAO ownership
     * @param newDao New DAO address
     */
    function transferDao(address newDao) external onlyDao {
        require(newDao != address(0), "FeeController: invalid DAO address");
        dao = newDao;
        emit DaoUpdated(newDao);
    }
    
    /**
     * @dev Calculate fee for a given amount
     * @param amount Amount to calculate fee for
     * @param tierId Fee tier ID (0 for default)
     * @return feeAmount Calculated fee amount
     */
    function calculateFee(uint256 amount, uint256 tierId) public view returns (uint256 feeAmount) {
        FeeTier memory tier = tierId == 0 ? feeTiers[defaultFeeTierId] : feeTiers[tierId];
        require(tier.feePercentage != 0, "FeeController: invalid tier ID");
        
        feeAmount = (amount * tier.feePercentage) / 10000;
        
        if (feeAmount < tier.minFeeAmount) {
            feeAmount = tier.minFeeAmount;
        } else if (feeAmount > tier.maxFeeAmount) {
            feeAmount = tier.maxFeeAmount;
        }
        
        return feeAmount;
    }
    
    /**
     * @dev Collect fees from a user
     * @param payer Address paying the fee
     * @param amount Amount to calculate fee from
     * @param tierId Fee tier ID (0 for default)
     */
    function collectFee(address payer, uint256 amount, uint256 tierId) external {
        uint256 feeAmount = calculateFee(amount, tierId);
        
        if (feeToken == address(0)) {
            // Native token transfer
            require(msg.value >= feeAmount, "FeeController: insufficient fee");
            (bool sent, ) = treasury.call{value: feeAmount}("");
            require(sent, "FeeController: failed to send native token");
        } else {
            // ERC20 token transfer
            require(IERC20(feeToken).transferFrom(payer, treasury, feeAmount), "FeeController: ERC20 transfer failed");
        }
        
        emit FeesCollected(payer, feeAmount, tierId == 0 ? defaultFeeTierId : tierId);
    }
    
    // Allow receiving native tokens
    receive() external payable {}
}
```

```go
// Cosmos SDK module for fee control (x/feecontrol)
package feecontrol

import (
	"encoding/json"
	"fmt"

	sdk "github.com/cosmos/cosmos-sdk/types"
	sdkerrors "github.com/cosmos/cosmos-sdk/types/errors"
)

// FeeControl module constants
const (
	ModuleName   = "feecontrol"
	StoreKey     = ModuleName
	RouterKey    = ModuleName
	QuerierRoute = ModuleName
)

// Keeper maintains the link to data storage
type Keeper struct {
	storeKey sdk.StoreKey
	cdc      codec.BinaryCodec
	ak       types.AccountKeeper
	bk       types.BankKeeper
	dao      sdk.AccAddress
}

// NewKeeper creates new instances of the feecontrol Keeper
func NewKeeper(
	cdc codec.BinaryCodec,
	storeKey sdk.StoreKey,
	ak types.AccountKeeper,
	bk types.BankKeeper,
	dao sdk.AccAddress,
) Keeper {
	return Keeper{
		storeKey: storeKey,
		cdc:      cdc,
		ak:       ak,
		bk:       bk,
		dao:      dao,
	}
}

// FeeTier represents a fee structure
type FeeTier struct {
	FeePercentage sdk.Dec `json:"fee_percentage"`
	MinFeeAmount  sdk.Int `json:"min_fee_amount"`
	MaxFeeAmount  sdk.Int `json:"max_fee_amount"`
}

// MsgUpdateFeeTier defines a message to update fee tier
type MsgUpdateFeeTier struct {
	TierID        uint64    `json:"tier_id"`
	FeePercentage sdk.Dec   `json:"fee_percentage"`
	MinFeeAmount  sdk.Int   `json:"min_fee_amount"`
	MaxFeeAmount  sdk.Int   `json:"max_fee_amount"`
	Sender        string    `json:"sender"`
}

// ValidateBasic performs stateless validation
func (msg MsgUpdateFeeTier) ValidateBasic() error {
	if msg.TierID == 0 {
		return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "invalid tier ID")
	}
	if msg.FeePercentage.GT(sdk.OneDec()) {
		return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "fee exceeds 100%")
	}
	if msg.MinFeeAmount.GT(msg.MaxFeeAmount) {
		return sdk
