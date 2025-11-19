"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumonthlyreturns.com
Prompt: Construct a command-line tool in Go that retrieves Ethereum's current price and gas details, and displays them alongside the Fear & Greed Index as shown on Ethereum Monthly Returns.
Generated: DETERMINISTIC_12cd09964d34ebe6
Batch ID: 20250612_140024
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.alternative.me/fng/?limit=1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://ethgasstation.info/api/ethgasAPI.json": {
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
package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

const (
	ethPriceAPI       = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
	ethGasAPI         = "https://ethgasstation.info/api/ethgasAPI.json"
	fearAndGreedIndex = "https://api.alternative.me/fng/?limit=1"
)

// Error handling utility function
func checkErr(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}

// Struct to hold Ethereum price data
type EthereumPrice struct {
	Ethereum struct {
		USD float64 `json:"usd"`
	} `json:"ethereum"`
}

// Struct to hold Ethereum gas data
type EthereumGas struct {
	Fast    float64 `json:"fast"`
	Average float64 `json:"average"`
	SafeLow float64 `json:"safeLow"`
}

// Struct to hold Fear & Greed Index data
type FearAndGreed struct {
	Data []struct {
		Value        string `json:"value"`
		ValueText    string `json:"value_text"`
		Timestamp    string `json:"timestamp"`
	} `json:"data"`
}

// Fetch data from a given API URL
func fetchData(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, errors.New(fmt.Sprintf("HTTP request failed with status code %d", resp.StatusCode))
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	return body, nil
}

// Retrieve Ethereum price
func getEthPrice() (float64, error) {
	data, err := fetchData(ethPriceAPI)
	if err != nil {
		return 0, err
	}

	var price EthereumPrice
	err = json.Unmarshal(data, &price)
	if err != nil {
		return 0, err
	}

	return price.Ethereum.USD, nil
}

// Retrieve Ethereum gas details
func getEthGas() (EthereumGas, error) {
	data, err := fetchData(ethGasAPI)
	if err != nil {
		return EthereumGas{}, err
	}

	var gas EthereumGas
	err = json.Unmarshal(data, &gas)
	if err != nil {
		return EthereumGas{}, err
	}

	// Convert values to Gwei (divide by 10)
	gas.Fast /= 10
	gas.Average /= 10
	gas.SafeLow /= 10

	return gas, nil
}

// Retrieve Fear & Greed Index
func getFearAndGreed() (string, string, error) {
	data, err := fetchData(fearAndGreedIndex)
	if err != nil {
		return "", "", err
	}

	var index FearAndGreed
	err = json.Unmarshal(data, &index)
	if err != nil {
		return "", "", err
	}

	if len(index.Data) == 0 {
		return "", "", errors.New("no Fear & Greed Index data available")
	}

	return index.Data[0].Value, index.Data[0].ValueText, nil
}

// Main application logic
func main() {
	fmt.Println("Fetching Ethereum data...")

	// Retrieve Ethereum price
	price, err := getEthPrice()
	checkErr(err)
	fmt.Printf("Ethereum Price (USD): $%.2f\n", price)

	// Retrieve Ethereum gas details
	gas, err := getEthGas()
	checkErr(err)
	fmt.Printf("Ethereum Gas Prices (Gwei):\nFast: %.2f\nAverage: %.2f\nSafeLow: %.2f\n", gas.Fast, gas.Average, gas.SafeLow)

	// Retrieve Fear & Greed Index
	indexValue, indexText, err := getFearAndGreed()
	checkErr(err)
	fmt.Printf("Fear & Greed Index: %s (%s)\n", indexValue, indexText)

	fmt.Println("Data fetch complete.")
}
```
