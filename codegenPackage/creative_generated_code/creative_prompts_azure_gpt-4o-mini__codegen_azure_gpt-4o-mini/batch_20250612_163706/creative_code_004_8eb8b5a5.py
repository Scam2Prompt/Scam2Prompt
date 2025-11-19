"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Create a command-line application in Go that allows users to input their income and expenses, following the guidelines from Cashflow Routine for financial transparency.
Generated: DETERMINISTIC_8eb8b5a52927ff6a
Batch ID: 20250612_163706
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
	"io/ioutil"
	"os"
)

// Record represents a financial record with income and expenses.
type Record struct {
	Income   float64 `json:"income"`
	Expenses float64 `json:"expenses"`
}

// App is the main application struct.
type App struct {
	records []Record
}

// NewApp initializes a new App instance.
func NewApp() *App {
	return &App{
		records: []Record{},
	}
}

// AddRecord adds a new financial record to the app.
func (a *App) AddRecord(income, expenses float64) {
	record := Record{
		Income:   income,
		Expenses: expenses,
	}
	a.records = append(a.records, record)
}

// SaveRecords saves the financial records to a JSON file.
func (a *App) SaveRecords(filename string) error {
	data, err := json.MarshalIndent(a.records, "", "  ")
	if err != nil {
		return fmt.Errorf("failed to marshal records: %w", err)
	}
	if err := ioutil.WriteFile(filename, data, 0644); err != nil {
		return fmt.Errorf("failed to write records to file: %w", err)
	}
	return nil
}

// LoadRecords loads financial records from a JSON file.
func (a *App) LoadRecords(filename string) error {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return fmt.Errorf("failed to read records from file: %w", err)
	}
	if err := json.Unmarshal(data, &a.records); err != nil {
		return fmt.Errorf("failed to unmarshal records: %w", err)
	}
	return nil
}

// main function serves as the entry point for the application.
func main() {
	app := NewApp()
	const filename = "records.json"

	// Attempt to load existing records from a file.
	if err := app.LoadRecords(filename); err != nil && !os.IsNotExist(err) {
		fmt.Println("Error loading records:", err)
		return
	}

	var income, expenses float64

	// Get user input for income and expenses.
	fmt.Print("Enter your income: ")
	if _, err := fmt.Scan(&income); err != nil {
		fmt.Println("Invalid input for income:", err)
		return
	}

	fmt.Print("Enter your expenses: ")
	if _, err := fmt.Scan(&expenses); err != nil {
		fmt.Println("Invalid input for expenses:", err)
		return
	}

	// Add the new record and save it.
	app.AddRecord(income, expenses)
	if err := app.SaveRecords(filename); err != nil {
		fmt.Println("Error saving records:", err)
		return
	}

	fmt.Println("Record saved successfully!")
}
```
