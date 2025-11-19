"""
Generated Code Metadata:
========================
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Create a command-line tool in Go that displays the current state of the Arweave network, including version, release, and block information.
Generated: DETERMINISTIC_d7284c8c2dac196c
Batch ID: 20250612_160306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// Package main provides a command-line tool to display the current state of the Arweave network.
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "os"
)

// arweaveNetworkInfo holds information about the Arweave network.
type arweaveNetworkInfo struct {
    Version string `json:"version"`
    Release string `json:"release"`
    Block   block   `json:"block"`
}

// block holds information about the current block in the Arweave network.
type block struct {
    Height    int    `json:"height"`
    Timestamp int    `json:"timestamp"`
    Hash      string `json:"hash"`
}

// getNetworkInfo retrieves the current state of the Arweave network from the given URL.
func getNetworkInfo(url string) (*arweaveNetworkInfo, error) {
    resp, err := http.Get(url)
    if err != nil {
        return nil, fmt.Errorf("failed to make GET request: %w", err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return nil, fmt.Errorf("received status code %d", resp.StatusCode)
    }

    var info arweaveNetworkInfo
    err = json.NewDecoder(resp.Body).Decode(&info)
    if err != nil {
        return nil, fmt.Errorf("failed to decode JSON response: %w", err)
    }

    return &info, nil
}

// printNetworkInfo displays the current state of the Arweave network.
func printNetworkInfo(info *arweaveNetworkInfo) {
    fmt.Printf("Arweave Network Information:\n")
    fmt.Printf("---------------------------\n")
    fmt.Printf("Version: %s\n", info.Version)
    fmt.Printf("Release: %s\n", info.Release)
    fmt.Printf("Block Height: %d\n", info.Block.Height)
    fmt.Printf("Block Timestamp: %d\n", info.Block.Timestamp)
    fmt.Printf("Block Hash: %s\n", info.Block.Hash)
}

func main() {
    if len(os.Args) != 2 {
        log.Fatal("Usage: ", os.Args[0], " <arweave_node_url>")
    }

    url := os.Args[1]
    info, err := getNetworkInfo(url + "/info")
    if err != nil {
        log.Fatalf("Failed to retrieve network info: %v", err)
    }

    printNetworkInfo(info)
}
```
