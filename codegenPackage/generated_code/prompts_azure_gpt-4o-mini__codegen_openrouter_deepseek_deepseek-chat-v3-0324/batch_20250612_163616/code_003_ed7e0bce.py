"""
Generated Code Metadata:
========================
Original URL: https://polkadot.world
Prompt: Generate code to set up a POAP hunt event using the Polkadot Go platform.
Generated: DETERMINISTIC_ed7e0bcedb4313c2
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# POAP Hunt Event using Polkadot Go Platform

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/centrifuge/go-substrate-rpc-client/v4/signature"
	"github.com/centrifuge/go-substrate-rpc-client/v4/types"
	"github.com/gorilla/mux"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Event represents a POAP hunt event
type Event struct {
	gorm.Model
	ID          string    `json:"id" gorm:"primaryKey"`
	Name        string    `json:"name"`
	Description string    `json:"description"`
	StartTime   time.Time `json:"start_time"`
	EndTime     time.Time `json:"end_time"`
	Locations   []string  `json:"locations" gorm:"serializer:json"`
	Rewards     []Reward  `json:"rewards" gorm:"foreignKey:EventID"`
	Active      bool      `json:"active"`
}

// Reward represents a POAP reward for the event
type Reward struct {
	gorm.Model
	ID             string `json:"id" gorm:"primaryKey"`
	EventID        string `json:"event_id"`
	Name           string `json:"name"`
	Description    string `json:"description"`
	ImageURL       string `json:"image_url"`
	TotalSupply    int    `json:"total_supply"`
	ClaimedCount   int    `json:"claimed_count"`
	ClaimCondition string `json:"claim_condition"`
}

// Participant represents a user participating in the event
type Participant struct {
	gorm.Model
	ID            string    `json:"id" gorm:"primaryKey"`
	WalletAddress string    `json:"wallet_address"`
	Events        []Event   `json:"events" gorm:"many2many:participant_events;"`
	Claims        []Claim   `json:"claims" gorm:"foreignKey:ParticipantID"`
	CheckIns      []CheckIn `json:"check_ins" gorm:"foreignKey:ParticipantID"`
}

// Claim represents a POAP claim by a participant
type Claim struct {
	gorm.Model
	ID           string    `json:"id" gorm:"primaryKey"`
	ParticipantID string   `json:"participant_id"`
	RewardID     string    `json:"reward_id"`
	ClaimTime    time.Time `json:"claim_time"`
	TxHash       string    `json:"tx_hash"`
}

// CheckIn represents a participant checking in at a location
type CheckIn struct {
	gorm.Model
	ID           string    `json:"id" gorm:"primaryKey"`
	ParticipantID string   `json:"participant_id"`
	EventID      string    `json:"event_id"`
	Location     string    `json:"location"`
	CheckInTime  time.Time `json:"check_in_time"`
}

// AppConfig holds the application configuration
type AppConfig struct {
	DatabaseURL string `json:"database_url"`
	ChainURL    string `json:"chain_url"`
	Port        string `json:"port"`
}

// Server holds the application state
type Server struct {
	DB      *gorm.DB
	Config  *AppConfig
	Router  *mux.Router
	Keyring *signature.KeyringPair
}

// NewServer creates a new server instance
func NewServer(config *AppConfig) (*Server, error) {
	db, err := gorm.Open(postgres.Open(config.DatabaseURL), &gorm.Config{})
	if err != nil {
		return nil, fmt.Errorf("failed to connect to database: %w", err)
	}

	// Auto-migrate the schema
	err = db.AutoMigrate(&Event{}, &Reward{}, &Participant{}, &Claim{}, &CheckIn{})
	if err != nil {
		return nil, fmt.Errorf("failed to migrate database: %w", err)
	}

	// Create keyring pair (for demo purposes - in production use secure key management)
	keyring, err := signature.KeyringPairFromSecret("//Alice", 42)
	if err != nil {
		return nil, fmt.Errorf("failed to create keyring pair: %w", err)
	}

	server := &Server{
		DB:      db,
		Config:  config,
		Router:  mux.NewRouter(),
		Keyring: &keyring,
	}

	server.setupRoutes()
	return server, nil
}

// setupRoutes configures the HTTP routes
func (s *Server) setupRoutes() {
	s.Router.HandleFunc("/api/events", s.listEvents).Methods("GET")
	s.Router.HandleFunc("/api/events/{id}", s.getEvent).Methods("GET")
	s.Router.HandleFunc("/api/events", s.createEvent).Methods("POST")
	s.Router.HandleFunc("/api/events/{id}", s.updateEvent).Methods("PUT")
	s.Router.HandleFunc("/api/events/{id}/activate", s.activateEvent).Methods("POST")
	s.Router.HandleFunc("/api/events/{id}/checkin", s.checkIn).Methods("POST")
	s.Router.HandleFunc("/api/events/{id}/claim", s.claimReward).Methods("POST")
	s.Router.HandleFunc("/api/participants", s.registerParticipant).Methods("POST")
	s.Router.HandleFunc("/api/participants/{id}", s.getParticipant).Methods("GET")
}

// listEvents returns all events
func (s *Server) listEvents(w http.ResponseWriter, r *http.Request) {
	var events []Event
	result := s.DB.Preload("Rewards").Find(&events)
	if result.Error != nil {
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(events)
}

// getEvent returns a specific event
func (s *Server) getEvent(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	var event Event
	result := s.DB.Preload("Rewards").First(&event, "id = ?", id)
	if result.Error != nil {
		if result.Error == gorm.ErrRecordNotFound {
			http.Error(w, "Event not found", http.StatusNotFound)
			return
		}
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(event)
}

// createEvent creates a new event
func (s *Server) createEvent(w http.ResponseWriter, r *http.Request) {
	var event Event
	if err := json.NewDecoder(r.Body).Decode(&event); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if event.ID == "" {
		event.ID = types.NewUUID().String()
	}

	result := s.DB.Create(&event)
	if result.Error != nil {
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(event)
}

// updateEvent updates an existing event
func (s *Server) updateEvent(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	var existing Event
	if result := s.DB.First(&existing, "id = ?", id); result.Error != nil {
		if result.Error == gorm.ErrRecordNotFound {
			http.Error(w, "Event not found", http.StatusNotFound)
			return
		}
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	var updates Event
	if err := json.NewDecoder(r.Body).Decode(&updates); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Update fields
	if updates.Name != "" {
		existing.Name = updates.Name
	}
	if updates.Description != "" {
		existing.Description = updates.Description
	}
	if !updates.StartTime.IsZero() {
		existing.StartTime = updates.StartTime
	}
	if !updates.EndTime.IsZero() {
		existing.EndTime = updates.EndTime
	}
	if len(updates.Locations) > 0 {
		existing.Locations = updates.Locations
	}

	if result := s.DB.Save(&existing); result.Error != nil {
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(existing)
}

// activateEvent activates an event
func (s *Server) activateEvent(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	var event Event
	if result := s.DB.First(&event, "id = ?", id); result.Error != nil {
		if result.Error == gorm.ErrRecordNotFound {
			http.Error(w, "Event not found", http.StatusNotFound)
			return
		}
		http.Error(w, result.Error.Error(), http.StatusInternalServerError)
		return
	}

	event.Active = true
	if
