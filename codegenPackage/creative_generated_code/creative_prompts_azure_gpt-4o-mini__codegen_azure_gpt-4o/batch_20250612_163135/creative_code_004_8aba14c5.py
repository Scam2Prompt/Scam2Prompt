"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Construct a command-line tool in Go that allows users to search for holiday vacation packages from Vansol Travel based on user-defined criteria.
Generated: DETERMINISTIC_8aba14c5338bc28c
Batch ID: 20250612_163135
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
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"os"
	"strings"
)

// VacationPackage represents a holiday package
type VacationPackage struct {
	Destination string  `json:"destination"`
	Price       float64 `json:"price"`
	Duration    int     `json:"duration"` // Duration in days
	Rating      float64 `json:"rating"`   // Average customer rating
}

// Sample dataset of vacation packages
var packages = []VacationPackage{
	{"Hawaii", 1500.00, 7, 4.8},
	{"Paris", 2000.00, 5, 4.5},
	{"Tokyo", 1800.00, 10, 4.9},
	{"Sydney", 1700.00, 8, 4.2},
	{"New York", 1200.00, 4, 4.0},
}

// searchPackages searches for vacation packages based on user criteria
func searchPackages(destination string, maxPrice float64, minRating float64, maxDuration int) ([]VacationPackage, error) {
	var results []VacationPackage

	for _, pkg := range packages {
		// Apply filters based on user-defined criteria
		if destination != "" && !strings.Contains(strings.ToLower(pkg.Destination), strings.ToLower(destination)) {
			continue
		}
		if maxPrice > 0 && pkg.Price > maxPrice {
			continue
		}
		if minRating > 0 && pkg.Rating < minRating {
			continue
		}
		if maxDuration > 0 && pkg.Duration > maxDuration {
			continue
		}
		results = append(results, pkg)
	}

	if len(results) == 0 {
		return nil, errors.New("no matching vacation packages found")
	}
	return results, nil
}

// printResults displays the search results in a user-friendly format
func printResults(results []VacationPackage) {
	fmt.Println("Matching Vacation Packages:")
	fmt.Println("----------------------------")
	for _, pkg := range results {
		fmt.Printf("Destination: %s | Price: $%.2f | Duration: %d days | Rating: %.1f\n",
			pkg.Destination, pkg.Price, pkg.Duration, pkg.Rating)
	}
}

func main() {
	// Parse command-line flags
	destPtr := flag.String("destination", "", "Destination to search for (e.g., Hawaii)")
	pricePtr := flag.Float64("maxPrice", 0, "Maximum price for the vacation package")
	ratingPtr := flag.Float64("minRating", 0, "Minimum customer rating")
	durationPtr := flag.Int("maxDuration", 0, "Maximum duration in days for the vacation package")

	flag.Parse()

	// Perform search with the provided criteria
	results, err := searchPackages(*destPtr, *pricePtr, *ratingPtr, *durationPtr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	// Output results
	printResults(results)

	// Optionally, output results as JSON for integration purposes
	jsonOutput, err := json.MarshalIndent(results, "", "  ")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: Failed to generate JSON output\n")
		os.Exit(1)
	}
	fmt.Println("\nResults in JSON format:")
	fmt.Println("-------------------------")
	fmt.Println(string(jsonOutput))
}
```
