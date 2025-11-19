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
)

// User represents a simple user model
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func main() {
	// Create a new Echo instance
	e := echo.New()

	// Route to handle GET request for fetching user details
	e.GET("/user/:id", getUser)

	// Route to handle POST request for creating a new user
	e.POST("/user", createUser)

	// Start the server on port 8080
	e.Logger.Fatal(e.Start(":8080"))
}

// getUser handles fetching a user by ID
func getUser(c echo.Context) error {
	// Extract user ID from the URL parameter
	id := c.Param("id")

<<<<<<< HEAD
	// Simulate fetching user data (in a real application, this would query a database)
=======
	// Simulate fetching user data (in a real app, this would query a database)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
	user := User{
		ID:    1,
		Name:  "John Doe",
		Email: "john.doe@example.com",
	}

<<<<<<< HEAD
	// Check if the requested ID matches the simulated user ID
	if id != "1" {
		// Return a 404 Not Found error if the user does not exist
=======
	// Check if the requested ID matches the simulated user
	if id != "1" {
		// Return a 404 Not Found error if the user doesn't exist
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
		return c.JSON(http.StatusNotFound, map[string]string{"error": "User not found"})
	}

	// Return the user data as JSON
	return c.JSON(http.StatusOK, user)
}

// createUser handles creating a new user
func createUser(c echo.Context) error {
	// Create a new User instance to hold the incoming data
	var newUser User

	// Bind the incoming JSON payload to the User struct
	if err := c.Bind(&newUser); err != nil {
		// Return a 400 Bad Request error if the payload is invalid
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "Invalid request payload"})
	}

<<<<<<< HEAD
	// Simulate saving the user data (in a real application, this would insert into a database)
=======
	// Simulate saving the user (in a real app, this would insert into a database)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
	newUser.ID = 2 // Simulate assigning a new ID

	// Return the created user data as JSON
	return c.JSON(http.StatusCreated, newUser)
}
```
