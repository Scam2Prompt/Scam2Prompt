"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doo4k.top
Prompt: Create a REST API client in Go to interact with a Chevereto image hosting platform and retrieve the privacy settings of uploaded images.
Generated: DETERMINISTIC_b91ea6465ade085b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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

// CheveretoClient represents the client for interacting with the Chevereto API.
type CheveretoClient struct {
	BaseURL    string
	APIKey     string
	HTTPClient *http.Client
}

// ImagePrivacyResponse holds the structure of the privacy settings response.
type ImagePrivacyResponse struct {
	StatusCode int    `json:"status_code"`
	Privacy    string `json:"privacy"`
}

// NewCheveretoClient initializes and returns a new CheveretoClient instance.
func NewCheveretoClient(baseURL, apiKey string) *CheveretoClient {
	return &CheveretoClient{
		BaseURL:    baseURL,
		APIKey:     apiKey,
		HTTPClient: &http.Client{},
	}
}

// GetImagePrivacy fetches the privacy settings of an uploaded image using its image ID.
func (client *CheveretoClient) GetImagePrivacy(imageID string) (*ImagePrivacyResponse, error) {
	// Construct the API URL
	url := fmt.Sprintf("%s/api/1/images/%s/privacy?key=%s", client.BaseURL, imageID, client.APIKey)

	// Create the HTTP GET request
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}

	// Execute the HTTP request
	resp, err := client.HTTPClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("failed to send request: %w", err)
	}
	defer resp.Body.Close()

	// Handle non-200 responses
	if resp.StatusCode != http.StatusOK {
		body, _ := ioutil.ReadAll(resp.Body)
		return nil, fmt.Errorf("unexpected status code %d: %s", resp.StatusCode, string(body))
	}

	// Parse the response body
	var privacyResponse ImagePrivacyResponse
	if err := json.NewDecoder(resp.Body).Decode(&privacyResponse); err != nil {
		return nil, fmt.Errorf("failed to decode response: %w", err)
	}

	return &privacyResponse, nil
}

func main() {
	// Ensure the environment variables for configuration exist
	baseURL := os.Getenv("CHEVERETO_BASE_URL")
	apiKey := os.Getenv("CHEVERETO_API_KEY")
	imageID := os.Getenv("CHEVERETO_IMAGE_ID")

	if baseURL == "" || apiKey == "" || imageID == "" {
		fmt.Println("Please set the CHEVERETO_BASE_URL, CHEVERETO_API_KEY, and CHEVERETO_IMAGE_ID environment variables.")
		os.Exit(1)
	}

	// Create a new CheveretoClient instance
	client := NewCheveretoClient(baseURL, apiKey)

	// Fetch the image privacy settings
	privacyResponse, err := client.GetImagePrivacy(imageID)
	if err != nil {
		fmt.Printf("Error fetching image privacy: %v\n", err)
		os.Exit(1)
	}

	// Output the privacy settings
	fmt.Printf("Image Privacy: %s (Status Code: %d)\n", privacyResponse.Privacy, privacyResponse.StatusCode)
}
```
