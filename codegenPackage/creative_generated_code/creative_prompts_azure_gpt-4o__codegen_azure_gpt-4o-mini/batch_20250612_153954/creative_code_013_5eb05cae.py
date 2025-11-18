"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write code in Go to implement a search functionality for products like "hulajnogi miejska" and "zestawy dla lalek," using keywords from the Milly Mally site.
Generated: DETERMINISTIC_5eb05caebe9101b4
Batch ID: 20250612_153954
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
	"fmt"
	"net/http"
	"strings"
)

// Product represents a product with a name and description.
type Product struct {
	Name        string `json:"name"`
	Description string `json:"description"`
}

// SearchResponse represents the response structure for product search results.
type SearchResponse struct {
	Products []Product `json:"products"`
}

// ProductService handles product-related operations.
type ProductService struct {
	Products []Product
}

// NewProductService initializes a new ProductService with sample data.
func NewProductService() *ProductService {
	return &ProductService{
		Products: []Product{
			{Name: "Hulajnoga Miejska", Description: "Szybka hulajnoga do miasta."},
			{Name: "Zestaw dla Lalek", Description: "Wielofunkcyjny zestaw z akcesoriami."},
			{Name: "Hulajnoga Sportowa", Description: "Hulajnoga do sportu i zabawy."},
			{Name: "Zestaw do Zabaw", Description: "Zestaw do kreatywnej zabawy."},
		},
	}
}

// Search searches for products matching the given keyword.
func (s *ProductService) Search(keyword string) []Product {
	var results []Product
	keyword = strings.ToLower(keyword)

	for _, product := range s.Products {
		if strings.Contains(strings.ToLower(product.Name), keyword) || strings.Contains(strings.ToLower(product.Description), keyword) {
			results = append(results, product)
		}
	}
	return results
}

// searchHandler handles the HTTP request for product search.
func searchHandler(service *ProductService) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// Set response header
		w.Header().Set("Content-Type", "application/json")

		// Get the 'q' query parameter
		query := r.URL.Query().Get("q")
		if query == "" {
			http.Error(w, "Missing query parameter 'q'", http.StatusBadRequest)
			return
		}

		// Perform search
		results := service.Search(query)

		// Create response
		response := SearchResponse{Products: results}

		// Encode response as JSON
		if err := json.NewEncoder(w).Encode(response); err != nil {
			http.Error(w, "Error encoding response to JSON", http.StatusInternalServerError)
			return
		}
	}
}

// main function to start the server
func main() {
	// Initialize product service
	productService := NewProductService()

	// Define search endpoint
	http.HandleFunc("/search", searchHandler(productService))

	// Start the HTTP server
	port := "8080"
	fmt.Printf("Starting server on port %s...\n", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		fmt.Printf("Error starting server: %v\n", err)
	}
}
```
