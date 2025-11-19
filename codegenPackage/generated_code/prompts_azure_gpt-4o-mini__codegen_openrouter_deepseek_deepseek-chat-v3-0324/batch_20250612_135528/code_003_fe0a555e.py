"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-mix.me
Prompt: Develop a command-line tool in Go that utilizes the Mixero service to convert BTC to XMR and back, highlighting its customizable fee structure.
Generated: DETERMINISTIC_fe0a555ef2755fbf
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
)

// Config holds the API configuration
type Config struct {
	APIKey     string `json:"api_key"`
	BaseURL    string `json:"base_url"`
	DefaultFee string `json:"default_fee"`
}

// ExchangeRequest represents the request payload for the exchange
type ExchangeRequest struct {
	FromCurrency string  `json:"from_currency"`
	ToCurrency   string  `json:"to_currency"`
	Amount       float64 `json:"amount"`
	Fee          string  `json:"fee,omitempty"`
	Address      string  `json:"address"`
}

// ExchangeResponse represents the response from the exchange API
type ExchangeResponse struct {
	ID           string  `json:"id"`
	FromAmount   float64 `json:"from_amount"`
	ToAmount     float64 `json:"to_amount"`
	FeeAmount    float64 `json:"fee_amount"`
	ExchangeRate float64 `json:"exchange_rate"`
	Status       string  `json:"status"`
	Error        string  `json:"error,omitempty"`
}

// loadConfig loads the configuration from a JSON file
func loadConfig(path string) (*Config, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("error opening config file: %v", err)
	}
	defer file.Close()

	bytes, err := io.ReadAll(file)
	if err != nil {
		return nil, fmt.Errorf("error reading config file: %v", err)
	}

	var config Config
	err = json.Unmarshal(bytes, &config)
	if err != nil {
		return nil, fmt.Errorf("error parsing config file: %v", err)
	}

	return &config, nil
}

// validateCurrencies checks if the currencies are valid
func validateCurrencies(from, to string) error {
	validPairs := map[string]bool{
		"BTC-XMR": true,
		"XMR-BTC": true,
	}

	if !validPairs[fmt.Sprintf("%s-%s", from, to)] {
		return fmt.Errorf("invalid currency pair. Only BTC-XMR and XMR-BTC are supported")
	}

	return nil
}

// createExchangeRequest creates an HTTP request for the exchange
func createExchangeRequest(config *Config, reqBody *ExchangeRequest) (*http.Request, error) {
	url := fmt.Sprintf("%s/api/v1/exchange", config.BaseURL)

	jsonBody, err := json.Marshal(reqBody)
	if err != nil {
		return nil, fmt.Errorf("error marshaling request body: %v", err)
	}

	req, err := http.NewRequest("POST", url, strings.NewReader(string(jsonBody)))
	if err != nil {
		return nil, fmt.Errorf("error creating request: %v", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-API-KEY", config.APIKey)

	return req, nil
}

// performExchange performs the currency exchange
func performExchange(config *Config, from, to string, amount float64, fee, address string) (*ExchangeResponse, error) {
	if err := validateCurrencies(from, to); err != nil {
		return nil, err
	}

	reqBody := &ExchangeRequest{
		FromCurrency: from,
		ToCurrency:   to,
		Amount:       amount,
		Address:      address,
	}

	if fee != "" {
		reqBody.Fee = fee
	} else if config.DefaultFee != "" {
		reqBody.Fee = config.DefaultFee
	}

	req, err := createExchangeRequest(config, reqBody)
	if err != nil {
		return nil, err
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("error making request: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("API request failed with status %d: %s", resp.StatusCode, string(body))
	}

	var exchangeResp ExchangeResponse
	err = json.NewDecoder(resp.Body).Decode(&exchangeResp)
	if err != nil {
		return nil, fmt.Errorf("error decoding response: %v", err)
	}

	if exchangeResp.Error != "" {
		return nil, fmt.Errorf("exchange error: %s", exchangeResp.Error)
	}

	return &exchangeResp, nil
}

func main() {
	// Define command-line flags
	fromCurrency := flag.String("from", "", "Currency to convert from (BTC or XMR)")
	toCurrency := flag.String("to", "", "Currency to convert to (BTC or XMR)")
	amount := flag.Float64("amount", 0, "Amount to convert")
	fee := flag.String("fee", "", "Custom fee (optional)")
	address := flag.String("address", "", "Destination address for the converted funds")
	configPath := flag.String("config", "config.json", "Path to configuration file")

	flag.Parse()

	// Validate required flags
	if *fromCurrency == "" || *toCurrency == "" || *amount <= 0 || *address == "" {
		flag.Usage()
		os.Exit(1)
	}

	// Load configuration
	config, err := loadConfig(*configPath)
	if err != nil {
		fmt.Printf("Error loading config: %v\n", err)
		os.Exit(1)
	}

	// Perform the exchange
	response, err := performExchange(config, *fromCurrency, *toCurrency, *amount, *fee, *address)
	if err != nil {
		fmt.Printf("Error performing exchange: %v\n", err)
		os.Exit(1)
	}

	// Print results
	fmt.Println("Exchange successful!")
	fmt.Printf("Transaction ID: %s\n", response.ID)
	fmt.Printf("From Amount: %.8f %s\n", response.FromAmount, *fromCurrency)
	fmt.Printf("To Amount: %.8f %s\n", response.ToAmount, *toCurrency)
	fmt.Printf("Fee Amount: %.8f %s\n", response.FeeAmount, *fromCurrency)
	fmt.Printf("Exchange Rate: %.8f\n", response.ExchangeRate)
	fmt.Printf("Status: %s\n", response.Status)
}
```
