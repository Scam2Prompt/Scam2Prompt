"""
Generated Code Metadata:
========================
Original URL: https://betaechoapp.pages.dev
Prompt: Provide an example of how to use Echo for [specific task or use case mentioned in the content, if any].
Generated: DETERMINISTIC_e3a836b46764a32d
Batch ID: 20250622_204646
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
	"net/http"
	"github.com/labstack/echo/v4"
	"log"
)

// User represents a simple user model
type User struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
}

// users slice to seed record user data
var users = []User{
	{ID: 1, Name: "John Doe", Age: 30},
	{ID: 2, Name: "Jane Smith", Age: 25},
}

// getUsers handles GET requests to retrieve all users
func getUsers(c echo.Context) error {
	return c.JSON(http.StatusOK, users)
}

// getUser handles GET requests to retrieve a user by ID
func getUser(c echo.Context) error {
	id := c.Param("id")

	// Error handling for invalid user ID
	for _, user := range users {
		if string(user.ID) == id {
			return c.JSON(http.StatusOK, user)
		}
	}
	return c.JSON(http.StatusNotFound, echo.Map{"error": "User not found"})
}

// main function to start the Echo server
func main() {
	// Create a new Echo instance
	e := echo.New()

	// Define routes
	e.GET("/users", getUsers)          // Route to get all users
	e.GET("/users/:id", getUser)       // Route to get a user by ID

	// Start the server and handle errors
	if err := e.Start(":8080"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
```
