"""
Generated Code Metadata:
========================
Original URL: https://bafybeiapzu7x4dr6cvx3pfwbbamnaqgtc5tl5c7l4o4yngnf3goy6wwixq.ipfs.dweb.link
Prompt: Design a simple API for swapping variable staking yield for a fixed yield, similar to PRYZM's offerings, using a Cosmos-based blockchain.
Generated: DETERMINISTIC_799c0cf11aa68f29
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Variable Staking Yield Swap API**
=====================================

**dependencies:**
- `cosmos-sdk`: ^0.45.0
- `tendermint`: ^0.34.0
- `golang/protobuf`: ^1.28.0

**variable_staking_yield_swap.go**
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/cosmos/cosmos-sdk/client"
	"github.com/cosmos/cosmos-sdk/codec"
	"github.com/cosmos/cosmos-sdk/std"
	"github.com/cosmos/cosmos-sdk/types"
	"github.com/cosmos/cosmos-sdk/types/tx"
	gtypes "github.com/cosmos/cosmos-sdk/types/tx"
	"github.com/gorilla/mux"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// API Server for Variable Staking Yield Swap
const (
	EndpointSwap = "/swap"
)

// MsgVariableStakingYieldSwap represents a variable staking yield swap message
type MsgVariableStakingYieldSwap struct {
	// Staker address
	Staker string `json:"staker"`
	// Variable staking yield
	VariableYield types.Dec `json:"variable_yield"`
	// Fixed yield
	FixedYield types.Dec `json:"fixed_yield"`
}

// NewMsgVariableStakingYieldSwap returns a new MsgVariableStakingYieldSwap
func NewMsgVariableStakingYieldSwap(staker string, variableYield, fixedYield types.Dec) *MsgVariableStakingYieldSwap {
	return &MsgVariableStakingYieldSwap{
		Staker:         staker,
		VariableYield:  variableYield,
		FixedYield:     fixedYield,
	}
}

// Route returns the message route
func (msg *MsgVariableStakingYieldSwap) Route() string { return "variable_staking_yield_swap" }

// Type returns the message type
func (msg *MsgVariableStakingYieldSwap) Type() string { return "MsgVariableStakingYieldSwap" }

// GetSigners returns the signers
func (msg *MsgVariableStakingYieldSwap) GetSigners() []types.AccAddress {
	addr, err := types.AccAddressFromBech32(msg.Staker)
	if err != nil {
		panic(err)
	}
	return []types.AccAddress{addr}
}

// GetSignBytes returns the sign bytes
func (msg *MsgVariableStakingYieldSwap) GetSignBytes() []byte {
	bz := codec.MustMarshalJSON(msg)
	return bz
}

// ValidateBasic validates the message
func (msg *MsgVariableStakingYieldSwap) ValidateBasic() error {
	if _, err := types.AccAddressFromBech32(msg.Staker); err != nil {
		return err
	}
	if msg.VariableYield.IsNegative() {
		return fmt.Errorf("variable yield cannot be negative")
	}
	if msg.FixedYield.IsNegative() {
		return fmt.Errorf("fixed yield cannot be negative")
	}
	return nil
}

// variableStakingYieldSwapHandler handles the variable staking yield swap
func variableStakingYieldSwapHandler(w http.ResponseWriter, r *http.Request) {
	var msg MsgVariableStakingYieldSwap
	err := json.NewDecoder(r.Body).Decode(&msg)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Validate the message
	err = msg.ValidateBasic()
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Create a new tx
	txBuilder := tx.NewTxBuilder()
	txBuilder.SetGasLimit(200000)
	txBuilder.SetFeeAmount(types.NewCoins(types.NewCoin("stake", types.NewInt(100))))

	// Add the message to the tx
	txBuilder.Msg(msg)

	// Sign the tx
	// NOTE: In a real application, you would use a secure way to get the private key
	// For demonstration purposes, we will use a hardcoded private key
	privateKey := "hardcoded_private_key"
	pubKey, err := types.PubKeyFromBech32(privateKey)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	accSeq, err := getAccountSequence(msg.Staker)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	txBuilder.SetAccountNumber(1)
	txBuilder.SetSequence(accSeq)

	signedTx, err := tx.Sign(context.Background(), privateKey, txBuilder)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Broadcast the tx
	err = broadcastTx(signedTx)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
}

// getAccountSequence gets the account sequence
func getAccountSequence(address string) (uint64, error) {
	// NOTE: In a real application, you would use a secure way to get the account sequence
	// For demonstration purposes, we will use a hardcoded account sequence
	return 1, nil
}

// broadcastTx broadcasts the tx
func broadcastTx(tx *gtypes.Tx) error {
	// NOTE: In a real application, you would use a secure way to broadcast the tx
	// For demonstration purposes, we will use a hardcoded broadcast function
	return nil
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc(EndpointSwap, variableStakingYieldSwapHandler).Methods("POST")

	fmt.Println("Server listening on port 8000")
	log.Fatal(http.ListenAndServe(":8000", r))
}
```

**variable_staking_yield_swap.pb.go** (Generated by protobuf)
```go
syntax = "proto3";

package variable_staking_yield_swap;

message MsgVariableStakingYieldSwap {
  string staker = 1;
  google.protobuf.DoubleValue variable_yield = 2;
  google.protobuf.DoubleValue fixed_yield = 3;
}

message MsgVariableStakingYieldSwapResponse {
  string result = 1;
}
```

**proto/buf.yaml**
```yml
version: v1
breaking:
  use:
    - FILE
```

**proto/variable_staking_yield_swap.proto**
```proto
syntax = "proto3";

import "google/protobuf/double_value.proto";

package variable_staking_yield_swap;

service VariableStakingYieldSwap {
  rpc Swap(MsgVariableStakingYieldSwap) returns (MsgVariableStakingYieldSwapResponse) {}
}

message MsgVariableStakingYieldSwap {
  string staker = 1;
  google.protobuf.DoubleValue variable_yield = 2;
  google.protobuf.DoubleValue fixed_yield = 3;
}

message MsgVariableStakingYieldSwapResponse {
  string result = 1;
}
```
