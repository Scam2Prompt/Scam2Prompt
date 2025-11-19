"""
Generated Code Metadata:
========================
Original URL: https://turbos-coin.com
Prompt: Create a smart contract using Chaincode in Hyperledger Fabric to enable the creation and management of community-driven tokens like Turbo Token.
Generated: DETERMINISTIC_6f58eb3db05465a0
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// SPDX-License-Identifier: Apache-2.0
package main

import (
	"encoding/json"
	"fmt"
	"strconv"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract provides functions for managing community tokens
type SmartContract struct {
	contractapi.Contract
}

// Token represents a community token
type Token struct {
	ID          string `json:"id"`
	Name        string `json:"name"`
	Symbol      string `json:"symbol"`
	TotalSupply uint64 `json:"totalSupply"`
	Decimals    uint8  `json:"decimals"`
	Creator     string `json:"creator"`
}

// Balance represents a user's token balance
type Balance struct {
	TokenID string `json:"tokenId"`
	Owner   string `json:"owner"`
	Amount  uint64 `json:"amount"`
}

// InitLedger initializes the ledger with sample tokens
func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	tokens := []Token{
		{ID: "token1", Name: "Turbo Token", Symbol: "TURBO", TotalSupply: 1000000, Decimals: 18, Creator: "admin"},
	}

	for _, token := range tokens {
		tokenJSON, err := json.Marshal(token)
		if err != nil {
			return fmt.Errorf("failed to marshal token: %v", err)
		}

		err = ctx.GetStub().PutState(token.ID, tokenJSON)
		if err != nil {
			return fmt.Errorf("failed to put token to world state: %v", err)
		}
	}

	return nil
}

// CreateToken creates a new community token
func (s *SmartContract) CreateToken(
	ctx contractapi.TransactionContextInterface,
	id string,
	name string,
	symbol string,
	totalSupply uint64,
	decimals uint8,
) error {
	creator, err := ctx.GetClientIdentity().GetID()
	if err != nil {
		return fmt.Errorf("failed to get client identity: %v", err)
	}

	exists, err := s.TokenExists(ctx, id)
	if err != nil {
		return err
	}
	if exists {
		return fmt.Errorf("token %s already exists", id)
	}

	token := Token{
		ID:          id,
		Name:        name,
		Symbol:      symbol,
		TotalSupply: totalSupply,
		Decimals:    decimals,
		Creator:     creator,
	}

	tokenJSON, err := json.Marshal(token)
	if err != nil {
		return err
	}

	err = ctx.GetStub().PutState(id, tokenJSON)
	if err != nil {
		return fmt.Errorf("failed to put token to world state: %v", err)
	}

	// Initialize creator's balance
	balanceKey, err := ctx.GetStub().CreateCompositeKey("balance", []string{id, creator})
	if err != nil {
		return fmt.Errorf("failed to create composite key: %v", err)
	}

	balance := Balance{
		TokenID: id,
		Owner:   creator,
		Amount:  totalSupply,
	}

	balanceJSON, err := json.Marshal(balance)
	if err != nil {
		return fmt.Errorf("failed to marshal balance: %v", err)
	}

	err = ctx.GetStub().PutState(balanceKey, balanceJSON)
	if err != nil {
		return fmt.Errorf("failed to put balance to world state: %v", err)
	}

	return nil
}

// TokenExists checks if a token exists
func (s *SmartContract) TokenExists(ctx contractapi.TransactionContextInterface, id string) (bool, error) {
	tokenJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return false, fmt.Errorf("failed to read token from world state: %v", err)
	}
	return tokenJSON != nil, nil
}

// ReadToken returns the token with the given ID
func (s *SmartContract) ReadToken(ctx contractapi.TransactionContextInterface, id string) (*Token, error) {
	tokenJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return nil, fmt.Errorf("failed to read token from world state: %v", err)
	}
	if tokenJSON == nil {
		return nil, fmt.Errorf("token %s does not exist", id)
	}

	var token Token
	err = json.Unmarshal(tokenJSON, &token)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal token: %v", err)
	}

	return &token, nil
}

// GetAllTokens returns all tokens in the system
func (s *SmartContract) GetAllTokens(ctx contractapi.TransactionContextInterface) ([]*Token, error) {
	resultsIterator, err := ctx.GetStub().GetStateByRange("", "")
	if err != nil {
		return nil, fmt.Errorf("failed to get state by range: %v", err)
	}
	defer resultsIterator.Close()

	var tokens []*Token
	for resultsIterator.HasNext() {
		queryResponse, err := resultsIterator.Next()
		if err != nil {
			return nil, fmt.Errorf("failed to get next result: %v", err)
		}

		var token Token
		err = json.Unmarshal(queryResponse.Value, &token)
		if err != nil {
			return nil, fmt.Errorf("failed to unmarshal token: %v", err)
		}

		tokens = append(tokens, &token)
	}

	return tokens, nil
}

// Transfer transfers tokens from one account to another
func (s *SmartContract) Transfer(
	ctx contractapi.TransactionContextInterface,
	tokenID string,
	to string,
	amount uint64,
) error {
	from, err := ctx.GetClientIdentity().GetID()
	if err != nil {
		return fmt.Errorf("failed to get client identity: %v", err)
	}

	if from == to {
		return fmt.Errorf("cannot transfer to self")
	}

	if amount <= 0 {
		return fmt.Errorf("amount must be positive")
	}

	// Get from balance
	fromBalanceKey, err := ctx.GetStub().CreateCompositeKey("balance", []string{tokenID, from})
	if err != nil {
		return fmt.Errorf("failed to create composite key: %v", err)
	}

	fromBalanceJSON, err := ctx.GetStub().GetState(fromBalanceKey)
	if err != nil {
		return fmt.Errorf("failed to read from balance: %v", err)
	}
	if fromBalanceJSON == nil {
		return fmt.Errorf("sender has no balance for token %s", tokenID)
	}

	var fromBalance Balance
	err = json.Unmarshal(fromBalanceJSON, &fromBalance)
	if err != nil {
		return fmt.Errorf("failed to unmarshal from balance: %v", err)
	}

	if fromBalance.Amount < amount {
		return fmt.Errorf("insufficient balance")
	}

	// Get to balance
	toBalanceKey, err := ctx.GetStub().CreateCompositeKey("balance", []string{tokenID, to})
	if err != nil {
		return fmt.Errorf("failed to create composite key: %v", err)
	}

	toBalanceJSON, err := ctx.GetStub().GetState(toBalanceKey)
	if err != nil {
		return fmt.Errorf("failed to read to balance: %v", err)
	}

	var toBalance Balance
	if toBalanceJSON == nil {
		toBalance = Balance{
			TokenID: tokenID,
			Owner:   to,
			Amount:  0,
		}
	} else {
		err = json.Unmarshal(toBalanceJSON, &toBalance)
		if err != nil {
			return fmt.Errorf("failed to unmarshal to balance: %v", err)
		}
	}

	// Update balances
	fromBalance.Amount -= amount
	toBalance.Amount += amount

	// Save updated balances
	fromBalanceJSON, err = json.Marshal(fromBalance)
	if err != nil {
		return fmt.Errorf("failed to marshal from balance: %v", err)
	}

	err = ctx.GetStub().PutState(fromBalanceKey, fromBalanceJSON)
	if err != nil {
		return fmt.Errorf("failed to update from balance: %v", err)
	}

	toBalanceJSON, err = json.Marshal(toBalance)
	if err != nil {
		return fmt.Errorf("failed to marshal to balance: %v", err)
	}

	err = ctx.GetStub().PutState(toBalanceKey, toBalanceJSON)
	if err != nil {
		return fmt.Errorf("failed to update to balance: %v", err)
	}

	return nil
}

// GetBalance returns the balance of a specific token for a user
func (s *SmartContract) GetBalance(
	ctx contractapi.TransactionContextInterface,
	tokenID string,
	owner string,
) (uint64, error) {
	balanceKey, err := ctx.GetStub().CreateCompositeKey("balance", []string{tokenID, owner})
	if err != nil {
		return 0, fmt.Errorf("failed to create composite key: %v", err)
	}

	balanceJSON, err := ctx.GetStub().Get
