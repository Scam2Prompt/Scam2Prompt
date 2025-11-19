"""
Generated Code Metadata:
========================
Original URL: https://bafybeibasskry2ovpgydqzwiw46ea2lmyxe4fqb6jekaixqidxb6cvjn3m.ipfs.dweb.link
Prompt: Generate a code example for a multi-hop IBC specification using Polymer’s merged IBC repository.
Generated: DETERMINISTIC_127631b411a69d60
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// main.go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/cosmos/cosmos-sdk/client"
	"github.com/cosmos/cosmos-sdk/client/tx"
	"github.com/cosmos/cosmos-sdk/crypto/keyring"
	sdk "github.com/cosmos/cosmos-sdk/types"
	"github.com/cosmos/cosmos-sdk/types/tx/signing"
	"github.com/cosmos/cosmos-sdk/x/auth"
	authtx "github.com/cosmos/cosmos-sdk/x/auth/tx"
	authtypes "github.com/cosmos/cosmos-sdk/x/auth/types"
	"github.com/cosmos/ibc-go/v7/modules/apps/transfer"
	ibc "github.com/cosmos/ibc-go/v7/modules/core"
	ibcclient "github.com/cosmos/ibc-go/v7/modules/core/02-client"
	ibcconnection "github.com/cosmos/ibc-go/v7/modules/core/03-connection"
	ibcchannel "github.com/cosmos/ibc-go/v7/modules/core/04-channel"
	"github.com/polymerdao/monomer"
	"github.com/polymerdao/monomer/app"
	"github.com/polymerdao/monomer/x/ibc/hop"
	"github.com/spf13/cobra"
	"google.golang.org/grpc"
)

func main() {
	// Initialize the command-line interface
	rootCmd := &cobra.Command{
		Use:   "multihop-ibc",
		Short: "Multi-hop IBC demonstration using Polymer's merged IBC",
	}

	// Add subcommands
	rootCmd.AddCommand(
		createMultiHopIBCChannelCmd(),
		transferTokensMultiHopCmd(),
	)

	// Execute the root command
	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}

func createMultiHopIBCChannelCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "create-channel [chain1] [chain2] [chain3]",
		Short: "Create a multi-hop IBC channel between three chains",
		Args:  cobra.ExactArgs(3),
		RunE: func(cmd *cobra.Command, args []string) error {
			chain1 := args[0]
			chain2 := args[1]
			chain3 := args[2]

			// Initialize clients for each chain
			clientCtx1, err := getClientContext(chain1)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", chain1, err)
			}

			clientCtx2, err := getClientContext(chain2)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", chain2, err)
			}

			clientCtx3, err := getClientContext(chain3)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", chain3, err)
			}

			// Create hop between chain1 and chain2
			if err := createHop(clientCtx1, clientCtx2); err != nil {
				return fmt.Errorf("failed to create hop between %s and %s: %v", chain1, chain2, err)
			}

			// Create hop between chain2 and chain3
			if err := createHop(clientCtx2, clientCtx3); err != nil {
				return fmt.Errorf("failed to create hop between %s and %s: %v", chain2, chain3, err)
			}

			fmt.Printf("Successfully created multi-hop IBC channel between %s -> %s -> %s\n", chain1, chain2, chain3)
			return nil
		},
	}

	return cmd
}

func transferTokensMultiHopCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "transfer [source-chain] [intermediate-chain] [destination-chain] [amount] [receiver]",
		Short: "Transfer tokens via multi-hop IBC",
		Args:  cobra.ExactArgs(5),
		RunE: func(cmd *cobra.Command, args []string) error {
			sourceChain := args[0]
			intermediateChain := args[1]
			destinationChain := args[2]
			amount := args[3]
			receiver := args[4]

			// Initialize clients for each chain
			sourceClientCtx, err := getClientContext(sourceChain)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", sourceChain, err)
			}

			intermediateClientCtx, err := getClientContext(intermediateChain)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", intermediateChain, err)
			}

			destinationClientCtx, err := getClientContext(destinationChain)
			if err != nil {
				return fmt.Errorf("failed to initialize client for %s: %v", destinationChain, err)
			}

			// Transfer tokens via multi-hop
			if err := transferTokensMultiHop(
				sourceClientCtx,
				intermediateClientCtx,
				destinationClientCtx,
				amount,
				receiver,
			); err != nil {
				return fmt.Errorf("failed to transfer tokens: %v", err)
			}

			fmt.Println("Successfully transferred tokens via multi-hop IBC")
			return nil
		},
	}

	return cmd
}

func getClientContext(chainID string) (client.Context, error) {
	// In a real implementation, this would connect to the chain's RPC endpoint
	// For demonstration, we're creating a mock client context
	encodingConfig := app.MakeEncodingConfig()
	
	kr := keyring.NewInMemory(encodingConfig.Marshaler)
	_, _, err := kr.NewMnemonic(
		"default",
		keyring.English,
		sdk.FullFundraiserPath,
		keyring.DefaultBIP39Passphrase,
		sdk.Secp256k1,
	)
	if err != nil {
		return client.Context{}, fmt.Errorf("failed to create keyring: %v", err)
	}

	clientCtx := client.Context{}.
		WithChainID(chainID).
		WithKeyring(kr).
		WithCodec(encodingConfig.Marshaler).
		WithInterfaceRegistry(encodingConfig.InterfaceRegistry).
		WithTxConfig(encodingConfig.TxConfig).
		WithAccountRetriever(authtypes.AccountRetriever{})

	return clientCtx, nil
}

func createHop(sourceClientCtx, destClientCtx client.Context) error {
	// Create IBC client on source chain for destination chain
	clientState := ibcclient.NewClientState(
		"07-tendermint",
		[]byte("client-state-data"),
		[]byte("consensus-state-data"),
	)

	clientMsg := ibcclient.NewMsgCreateClient(
		clientState,
		[]byte("consensus-state-data"),
		sourceClientCtx.GetFromAddress().String(),
	)

	// Create connection between source and destination
	connectionMsg := ibcconnection.NewMsgConnectionOpenInit(
		"connection-1",
		sourceClientCtx.GetFromAddress().String(),
		"client-1",
		"counterparty-1",
		nil,
	)

	// Create channel between source and destination
	channelMsg := ibcchannel.NewMsgChannelOpenInit(
		"transfer",
		"channel-1",
		sourceClientCtx.GetFromAddress().String(),
		"connection-1",
		"counterparty-1",
		nil,
	)

	// Build and send the transaction
	if err := sendIBCTransaction(sourceClientCtx, clientMsg, connectionMsg, channelMsg); err != nil {
		return fmt.Errorf("failed to create hop: %v", err)
	}

	return nil
}

func transferTokensMultiHop(sourceClientCtx, intermediateClientCtx, destClientCtx client.Context, amountStr, receiver string) error {
	// Parse amount
	amount, err := sdk.ParseCoinNormalized(amountStr)
	if err != nil {
		return fmt.Errorf("failed to parse amount: %v", err)
	}

	// Create transfer message for first hop (source -> intermediate)
	transferMsg1 := transfer.NewMsgTransfer(
		"transfer",
		"channel-1",
		amount,
		sourceClientCtx.GetFromAddress().String(),
		receiver,
		ibcclient.Height{},
		0,
		"",
	)

	// Create transfer message for second hop (intermediate -> destination)
	transferMsg2 := transfer.NewMsgTransfer(
		"transfer",
		"channel-2",
		amount,
		intermediateClientCtx.GetFromAddress().String(),
		receiver,
