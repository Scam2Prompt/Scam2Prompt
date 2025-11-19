"""
Generated Code Metadata:
========================
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Write code to automate the creation of a custom miner using GoMining's API, specifying parameters like computing power (TH), energy efficiency (W/TH), and price.
Generated: DETERMINISTIC_454f2aa0de9a4aaa
Batch ID: 20250612_152235
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
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

// Config holds the API configuration
type Config struct {
	APIKey    string `json:"api_key"`
	BaseURL   string `json:"base_url"`
	Endpoint  string `json:"endpoint"`
}

// MinerSpecification defines the parameters for creating a custom miner
type MinerSpecification struct {
	Name            string  `json:"name"`
	ComputingPower  float64 `json:"computing_power"`  // in TH
	EnergyEfficiency float64 `json:"energy_efficiency"` // in W/TH
	Price           float64 `json:"price"`            // in USD
	Algorithm       string  `json:"algorithm"`
	Manufacturer    string  `json:"manufacturer"`
}

// APIResponse represents the response from GoMining's API
type APIResponse struct {
	Success bool   `json:"success"`
	Message string `json:"message"`
	Data    struct {
		MinerID string `json:"miner_id"`
	} `json:"data"`
}

func main() {
	// Load configuration
	config, err := loadConfig("config.json")
	if err != nil {
		fmt.Printf("Error loading config: %v\n", err)
		os.Exit(1)
	}

	// Create miner specification
	miner := MinerSpecification{
		Name:            "Custom Miner X1",
		ComputingPower:  100.0,
		EnergyEfficiency: 30.0,
		Price:           2500.00,
		Algorithm:       "SHA-256",
		Manufacturer:    "CustomMining Inc.",
	}

	// Create the custom miner via API
	response, err := createCustomMiner(config, miner)
	if err != nil {
		fmt.Printf("Error creating miner: %v\n", err)
		os.Exit(1)
	}

	if response.Success {
		fmt.Printf("Successfully created miner with ID: %s\n", response.Data.MinerID)
	} else {
		fmt.Printf("Failed to create miner: %s\n", response.Message)
	}
}

// loadConfig reads the configuration from a JSON file
func loadConfig(filename string) (*Config, error) {
	file, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("could not read config file: %w", err)
	}

	var config Config
	err = json.Unmarshal(file, &config)
	if err != nil {
		return nil, fmt.Errorf("could not parse config file: %w", err)
	}

	return &config, nil
}

// createCustomMiner sends a request to create a custom miner
func createCustomMiner(config *Config, miner MinerSpecification) (*APIResponse, error) {
	requestBody, err := json.Marshal(miner)
	if err != nil {
		return nil, fmt.Errorf("could not marshal miner specification: %w", err)
	}

	url := config.BaseURL + config.Endpoint
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(requestBody))
	if err != nil {
		return nil, fmt.Errorf("could not create request: %w", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+config.APIKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("request failed: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("could not read response body: %w", err)
	}

	var apiResponse APIResponse
	err = json.Unmarshal(body, &apiResponse)
	if err != nil {
		return nil, fmt.Errorf("could not parse response: %w", err)
	}

	return &apiResponse, nil
}
```
