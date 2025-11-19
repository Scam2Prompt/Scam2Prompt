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

// TokenContract defines the smart contract structure
type TokenContract struct {
	contractapi.Contract
}

// Token represents the structure of a community-driven token
type Token struct {
	Name        string  `json:"name"`        // Name of the token
	Symbol      string  `json:"symbol"`      // Symbol of the token
	TotalSupply float64 `json:"totalSupply"` // Total supply of the token
	Owner       string  `json:"owner"`       // Owner of the token
}

// CreateToken creates a new token with the specified details
func (t *TokenContract) CreateToken(ctx contractapi.TransactionContextInterface, name string, symbol string, totalSupply float64) error {
	// Get the transaction initiator's identity
	owner, err := ctx.GetClientIdentity().GetID()
	if err != nil {
		return fmt.Errorf("failed to get client identity: %v", err)
	}

	// Check if the token already exists
	existingToken, err := ctx.GetStub().GetState(symbol)
	if err != nil {
		return fmt.Errorf("failed to check token existence: %v", err)
	}
	if existingToken != nil {
		return fmt.Errorf("token with symbol '%s' already exists", symbol)
	}

	// Create the token object
	token := Token{
		Name:        name,
		Symbol:      symbol,
		TotalSupply: totalSupply,
		Owner:       owner,
	}

	// Serialize the token object to JSON
	tokenJSON, err := json.Marshal(token)
	if err != nil {
		return fmt.Errorf("failed to serialize token: %v", err)
	}

	// Store the token in the ledger
	err = ctx.GetStub().PutState(symbol, tokenJSON)
	if err != nil {
		return fmt.Errorf("failed to store token: %v", err)
	}

	return nil
}

// QueryToken retrieves the details of a token by its symbol
func (t *TokenContract) QueryToken(ctx contractapi.TransactionContextInterface, symbol string) (*Token, error) {
	// Retrieve the token from the ledger
	tokenJSON, err := ctx.GetStub().GetState(symbol)
	if err != nil {
		return nil, fmt.Errorf("failed to retrieve token: %v", err)
	}
	if tokenJSON == nil {
		return nil, fmt.Errorf("token with symbol '%s' does not exist", symbol)
	}

	// Deserialize the token JSON into a Token object
	var token Token
	err = json.Unmarshal(tokenJSON, &token)
	if err != nil {
		return nil, fmt.Errorf("failed to deserialize token: %v", err)
	}

	return &token, nil
}

// TransferToken transfers ownership of a token to a new owner
func (t *TokenContract) TransferToken(ctx contractapi.TransactionContextInterface, symbol string, newOwner string) error {
	// Retrieve the token from the ledger
	tokenJSON, err := ctx.GetStub().GetState(symbol)
	if err != nil {
		return fmt.Errorf("failed to retrieve token: %v", err)
	}
	if tokenJSON == nil {
		return fmt.Errorf("token with symbol '%s' does not exist", symbol)
	}

	// Deserialize the token JSON into a Token object
	var token Token
	err = json.Unmarshal(tokenJSON, &token)
	if err != nil {
		return fmt.Errorf("failed to deserialize token: %v", err)
	}

	// Get the transaction initiator's identity
	currentOwner, err := ctx.GetClientIdentity().GetID()
	if err != nil {
		return fmt.Errorf("failed to get client identity: %v", err)
	}

	// Verify that the initiator is the current owner of the token
	if token.Owner != currentOwner {
		return fmt.Errorf("only the owner can transfer the token")
	}

	// Update the token's owner
	token.Owner = newOwner

	// Serialize the updated token object to JSON
	updatedTokenJSON, err := json.Marshal(token)
	if err != nil {
		return fmt.Errorf("failed to serialize updated token: %v", err)
	}

	// Store the updated token in the ledger
	err = ctx.GetStub().PutState(symbol, updatedTokenJSON)
	if err != nil {
		return fmt.Errorf("failed to update token: %v", err)
	}

	return nil
}

// DeleteToken removes a token from the ledger
func (t *TokenContract) DeleteToken(ctx contractapi.TransactionContextInterface, symbol string) error {
	// Retrieve the token from the ledger
	tokenJSON, err := ctx.GetStub().GetState(symbol)
	if err != nil {
		return fmt.Errorf("failed to retrieve token: %v", err)
	}
	if tokenJSON == nil {
		return fmt.Errorf("token with symbol '%s' does not exist", symbol)
	}

	// Get the transaction initiator's identity
	currentOwner, err := ctx.GetClientIdentity().GetID()
	if err != nil {
		return fmt.Errorf("failed to get client identity: %v", err)
	}

	// Deserialize the token JSON into a Token object
	var token Token
	err = json.Unmarshal(tokenJSON, &token)
	if err != nil {
		return fmt.Errorf("failed to deserialize token: %v", err)
	}

	// Verify that the initiator is the current owner of the token
	if token.Owner != currentOwner {
		return fmt.Errorf("only the owner can delete the token")
	}

	// Remove the token from the ledger
	err = ctx.GetStub().DelState(symbol)
	if err != nil {
		return fmt.Errorf("failed to delete token: %v", err)
	}

	return nil
}

// Main function to start the chaincode
func main() {
	chaincode := new(TokenContract)

	if err := contractapi.NewChaincode(chaincode).Start(); err != nil {
		fmt.Printf("Error starting TokenContract chaincode: %v", err)
	}
}
```
