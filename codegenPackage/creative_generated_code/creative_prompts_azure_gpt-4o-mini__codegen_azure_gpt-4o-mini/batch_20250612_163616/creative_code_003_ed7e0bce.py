"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.world
Prompt: Generate code to set up a POAP hunt event using the Polkadot Go platform.
Generated: DETERMINISTIC_ed7e0bcedb4313c2
Batch ID: 20250612_163616
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
	"fmt"
	"log"
	"net/http"

	"github.com/go-chi/chi"
	"github.com/go-chi/cors"
)

// Event structure to hold POAP hunt event information
type Event struct {
	ID          string `json:"id"`
	Title       string `json:"title"`
	Description string `json:"description"`
	Date        string `json:"date"`
}

// In-memory storage for events (for demonstration purposes)
var events = make(map[string]Event)

// createEventHandler handles the creation of a new POAP hunt event
func createEventHandler(w http.ResponseWriter, r *http.Request) {
	var newEvent Event

	// Decode the JSON body
	if err := json.NewDecoder(r.Body).Decode(&newEvent); err != nil {
		http.Error(w, "Invalid input", http.StatusBadRequest)
		return
	}

	// Validate event details
	if newEvent.ID == "" || newEvent.Title == "" {
		http.Error(w, "Event ID and Title are required", http.StatusBadRequest)
		return
	}

	// Store the event in memory
	events[newEvent.ID] = newEvent

	// Respond with the created event
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(newEvent)
}

// getEventHandler retrieves an event by ID
func getEventHandler(w http.ResponseWriter, r *http.Request) {
	eventID := chi.URLParam(r, "id")

	// Find the event in storage
	event, exists := events[eventID]
	if !exists {
		http.Error(w, "Event not found", http.StatusNotFound)
		return
	}

	// Respond with the event details
	json.NewEncoder(w).Encode(event)
}

// main sets up the HTTP server and routes
func main() {
	// Create a new router
	r := chi.NewRouter()

	// CORS middleware for handling cross-origin requests
	r.Use(cors.Handler(cors.Options{
		AllowedOrigins:   []string{"*"}, // Allow all origins for demo purposes
		AllowedMethods:   []string{"GET", "POST"},
		AllowedHeaders:   []string{"Content-Type"},
		AllowCredentials: true,
	}))

	// Routes for the event API
	r.Post("/events", createEventHandler)          // Create a new event
	r.Get("/events/{id}", getEventHandler)         // Get an event by ID

	// Start the HTTP server
	port := ":8080"
	fmt.Printf("Starting server on port %s...\n", port)
	if err := http.ListenAndServe(port, r); err != nil {
		log.Fatalf("Could not start server: %s\n", err)
	}
}
```

Make sure to import the necessary packages in your project and have Go modules initialized if you're using dependencies like `github.com/go-chi/chi` and `github.com/go-chi/cors`.
