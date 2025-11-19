"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Create a command-line tool in Go that displays the current state of the Arweave network, including version, release, and block information.
Generated: DETERMINISTIC_d7284c8c2dac196c
Batch ID: 20250612_160306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net/info": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```go
// arweave_status.go
package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"os"
)

// ArweaveInfo holds the information about the Arweave network.
type ArweaveInfo struct {
	Version string `json:"version"`
	Release string `json:"release"`
	Block   struct {
		Height     int64  `json:"height"`
		ID         string `json:"id"`
		Timestamp  int64  `json:"timestamp"`
	} `json:"block"`
}

// fetchArweaveStatus retrieves the current state of the Arweave network.
func fetchArweaveStatus(url string) (ArweaveInfo, error) {
	resp, err := http.Get(url)
	if err != nil {
		return ArweaveInfo{}, fmt.Errorf("failed to send request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return ArweaveInfo{}, errors.New("failed to get valid response from Arweave")
	}

	var info ArweaveInfo
	if err := json.NewDecoder(resp.Body).Decode(&info); err != nil {
		return ArweaveInfo{}, fmt.Errorf("failed to decode response: %w", err)
	}

	return info, nil
}

// displayStatus prints the Arweave network status to the console.
func displayStatus(info ArweaveInfo) {
	fmt.Println("Arweave Network Status:")
	fmt.Printf("Version: %s\n", info.Version)
	fmt.Printf("Release: %s\n", info.Release)
	fmt.Printf("Current Block Height: %d\n", info.Block.Height)
	fmt.Printf("Current Block ID: %s\n", info.Block.ID)
	fmt.Printf("Current Block Timestamp: %d\n", info.Block.Timestamp)
}

// main is the entry point of the command-line tool.
func main() {
	const arweaveAPIURL = "https://arweave.net/info"

	// Fetch the Arweave status
	info, err := fetchArweaveStatus(arweaveAPIURL)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error fetching Arweave status: %v\n", err)
		os.Exit(1)
	}

	// Display the current state of the Arweave network
	displayStatus(info)
}
```
