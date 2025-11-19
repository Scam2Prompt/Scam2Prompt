"""
Generated Code Metadata:
========================
Original URL: https://agix-reward.net
Prompt: Write a smart contract on Cardano that facilitates AGIX token staking and rewards distribution as described in the SingularityNET ecosystem.
Generated: DETERMINISTIC_efdf7bb50ce32c55
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```haskell
{-# LANGUAGE DataKinds             #-}
{-# LANGUAGE DeriveAnyClass        #-}
{-# LANGUAGE DeriveGeneric         #-}
{-# LANGUAGE FlexibleContexts      #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE NoImplicitPrelude     #-}
{-# LANGUAGE OverloadedStrings     #-}
{-# LANGUAGE ScopedTypeVariables   #-}
{-# LANGUAGE TemplateHaskell       #-}
{-# LANGUAGE TypeApplications      #-}
{-# LANGUAGE TypeFamilies          #-}
{-# LANGUAGE TypeOperators         #-}

module AGIXStaking where

import           PlutusTx
import           PlutusTx.Prelude
import           Ledger
import           Ledger.Ada                 as Ada
import           Ledger.Contexts            as Validation
import           Ledger.Tx
import           Ledger.Value               as Value
import           Ledger.Constraints         as Constraints
import qualified PlutusTx.AssocMap          as AssocMap
import           Plutus.Contract
import           Plutus.V1.Ledger.Interval  as Interval
import           Data.Text                  (Text)
import qualified Data.Text                  as T
import           Data.Void                  (Void)
import           Prelude                    (Show (..), String)
import           GHC.Generics               (Generic)
import           Data.Aeson                 (FromJSON, ToJSON)
import           Playground.Contract

-- AGIX token policy ID
agixPolicyId :: CurrencySymbol
agixPolicyId = CurrencySymbol "YOUR_AGIX_POLICY_ID_HERE"

-- AGIX token name
agixTokenName :: TokenName
agixTokenName = TokenName "AGIX"

-- Staking parameters
data StakingParams = StakingParams
    { spRewardRate    :: Integer  -- Reward rate per epoch (in lovelace)
    , spMinStake      :: Integer  -- Minimum stake amount (in AGIX)
    , spLockDuration  :: Integer  -- Number of epochs to lock stake
    } deriving (Generic, ToJSON, FromJSON, Show)

-- Staking datum
data StakingDatum = StakingDatum
    { sdOwner         :: PubKeyHash  -- Staker's public key hash
    , sdAmount        :: Integer     -- Staked AGIX amount
    , sdStartEpoch    :: Integer     -- Epoch when staking started
    , sdLastClaimed   :: Integer     -- Last epoch rewards were claimed
    } deriving (Generic, ToJSON, FromJSON, Show)

PlutusTx.unstableMakeIsData ''StakingDatum
PlutusTx.unstableMakeIsData ''StakingParams

-- Staking redeemer
data StakingAction
    = Stake
    | Unstake
    | ClaimRewards
    deriving (Generic, ToJSON, FromJSON, Show)

PlutusTx.unstableMakeIsData ''StakingAction

-- Helper function to get current epoch
{-# INLINABLE currentEpoch #-}
currentEpoch :: ScriptContext -> Integer
currentEpoch ctx =
    let info = scriptContextTxInfo ctx
        range = txInfoValidRange info
    in case Interval.lowerBound range of
        Just (LowerBound (POSIXTime time) _) -> time `divide` 86400  -- Approximate epoch duration
        _                                    -> traceError "Invalid valid range"

-- Validate staking action
{-# INLINABLE validateStaking #-}
validateStaking :: StakingParams -> StakingDatum -> StakingAction -> ScriptContext -> Bool
validateStaking params datum action ctx =
    case action of
        Stake -> validateStake params datum ctx
        Unstake -> validateUnstake params datum ctx
        ClaimRewards -> validateClaimRewards params datum ctx

-- Validate stake action
{-# INLINABLE validateStake #-}
validateStake :: StakingParams -> StakingDatum -> ScriptContext -> Bool
validateStake params _ ctx =
    let info = scriptContextTxInfo ctx
        inputs = txInfoInputs info
        outputs = txInfoOutputs info
        ownAddress = case scriptContextPurpose ctx of
            Spending txOutRef -> txOutRefAddress txOutRef
            _                 -> traceError "Invalid script purpose"
        
        -- Check that input contains AGIX tokens
        inputValue = mconcat $ map (txOutValue . txInInfoResolved) inputs
        agixAmount = Value.valueOf inputValue agixPolicyId agixTokenName
        
        -- Check minimum stake amount
        minStake = spMinStake params
    in
        agixAmount >= minStake &&
        -- Check that output contains staking datum
        any (\o -> txOutAddress o == ownAddress && 
                  case txOutDatum o of
                      OutputDatum d -> case fromBuiltinData (getDatum d) of
                                          Just (StakingDatum _ _ _ _) -> True
                                          _                          -> False
                      _            -> False) outputs

-- Validate unstake action
{-# INLINABLE validateUnstake #-}
validateUnstake :: StakingParams -> StakingDatum -> ScriptContext -> Bool
validateUnstake params datum ctx =
    let info = scriptContextTxInfo ctx
        inputs = txInfoInputs info
        current = currentEpoch ctx
        owner = sdOwner datum
        startEpoch = sdStartEpoch datum
        lockDuration = spLockDuration params
        
        -- Check that lock period has passed
        hasLockExpired = current >= startEpoch + lockDuration
        
        -- Check that owner is signing the transaction
        signedByOwner = txSignedBy info owner
    in
        hasLockExpired && signedByOwner

-- Validate claim rewards action
{-# INLINABLE validateClaimRewards #-}
validateClaimRewards :: StakingParams -> StakingDatum -> ScriptContext -> Bool
validateClaimRewards params datum ctx =
    let info = scriptContextTxInfo ctx
        current = currentEpoch ctx
        lastClaimed = sdLastClaimed datum
        owner = sdOwner datum
        amount = sdAmount datum
        rewardRate = spRewardRate params
        
        -- Calculate rewards
        epochsPassed = current - lastClaimed
        rewards = epochsPassed * amount * rewardRate
        
        -- Check that rewards are being paid
        minted = txInfoMint info
        rewardsPaid = Value.valueOf minted adaSymbol adaToken == rewards
        
        -- Check that owner is signing the transaction
        signedByOwner = txSignedBy info owner
    in
        rewardsPaid && signedByOwner && epochsPassed > 0

-- The staking validator
stakingValidator :: StakingParams -> StakingDatum -> StakingAction -> ScriptContext -> Bool
stakingValidator params datum action = validateStaking params datum action

-- Boilerplate for compiling to Plutus Core
validator :: StakingParams -> Validator
validator params = mkValidatorScript $
    $$(PlutusTx.compile [|| \p d a -> stakingValidator p d a ||])
    `PlutusTx.applyCode`
    PlutusTx.liftCode params

validatorHash :: StakingParams -> ValidatorHash
validatorHash = validatorHash . validator

validatorAddress :: StakingParams -> Ledger.Address
validatorAddress = scriptAddress . validator

-- Contract endpoints
type AGIXStakingSchema =
    Endpoint "stake" (Integer, PubKeyHash)
    .\/ Endpoint "unstake" PubKeyHash
    .\/ Endpoint "claimRewards" PubKeyHash

-- Stake endpoint
stake :: (HasBlockchainActions s, AsContractError e) => Integer -> PubKeyHash -> Contract w s e ()
stake amount owner = do
    let params = StakingParams
            { spRewardRate = 1000000  -- 1 ADA per epoch per AGIX
            , spMinStake = 100        -- 100 AGIX minimum
            , spLockDuration = 10     -- 10 epochs lock
            }
        datum = StakingDatum
            { sdOwner = owner
            , sdAmount = amount
            , sdStartEpoch = 0  -- Will be set in validation
            , sdLastClaimed = 0
            }
        tx = Constraints.mustPayToTheScript datum (Value.singleton agixPolicyId agixTokenName amount)
    ledgerTx <- submitTxConstraints (validator params) tx
    void $ awaitTxConfirmed $ txId ledgerTx
    logInfo @String $ "Staked " ++ show amount ++ " AGIX"

-- Unstake endpoint
unstake :: (HasBlockchainActions s, AsContractError e) => PubKeyHash -> Contract w s e ()
unstake owner = do
    let params = StakingParams
            { spRewardRate = 1000000
            , spMinStake = 100
            , spLockDuration = 10
            }
    utxos <- utxosAt (validatorAddress params)
    let relevantUtxos = filter (isOwnedUtxo owner) $ AssocMap.toList utxos
    case relevantUtxos of
        [] -> logInfo @String "No staked funds found"
        _
