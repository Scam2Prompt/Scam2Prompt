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
	"strconv"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// User represents a user model
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

// In-memory storage for users
var users = map[int]User{
	1: {ID: 1, Name: "John Doe", Email: "john@example.com"},
	2: {ID: 2, Name: "Jane Smith", Email: "jane@example.com"},
}

func main() {
	// Create new Echo instance
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Routes
	e.GET("/users", getUsers)
	e.GET("/users/:id", getUser)
	e.POST("/users", createUser)
	e.PUT("/users/:id", updateUser)
	e.DELETE("/users/:id", deleteUser)

	// Start server
	e.Logger.Fatal(e.Start(":8080"))
}

// Handler for GET /users
func getUsers(c echo.Context) error {
	userList := make([]User, 0, len(users))
	for _, user := range users {
		userList = append(userList, user)
	}
	return c.JSON(http.StatusOK, userList)
}

// Handler for GET /users/:id
func getUser(c echo.Context) error {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, "Invalid user ID")
	}

	user, exists := users[id]
	if !exists {
		return echo.NewHTTPError(http.StatusNotFound, "User not found")
	}

	return c.JSON(http.StatusOK, user)
}

// Handler for POST /users
func createUser(c echo.Context) error {
	u := new(User)
	if err := c.Bind(u); err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, "Invalid request payload")
	}

	// Validate required fields
	if u.Name == "" || u.Email == "" {
		return echo.NewHTTPError(http.StatusBadRequest, "Name and email are required")
	}

	// Generate ID (in a real app, this would come from a database)
	newID := len(users) + 1
	u.ID = newID

	// Add to storage
	users[newID] = *u

	return c.JSON(http.StatusCreated, u)
}

// Handler for PUT /users/:id
func updateUser(c echo.Context) error {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, "Invalid user ID")
	}

	// Check if user exists
	if _, exists := users[id]; !exists {
		return echo.NewHTTPError(http.StatusNotFound, "User not found")
	}

	u := new(User)
	if err := c.Bind(u); err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, "Invalid request payload")
	}

	// Validate required fields
	if u.Name == "" || u.Email == "" {
		return echo.NewHTTPError(http.StatusBadRequest, "Name and email are required")
	}

	// Update user
	u.ID = id
	users[id] = *u

	return c.JSON(http.StatusOK, u)
}

// Handler for DELETE /users/:id
func deleteUser(c echo.Context) error {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, "Invalid user ID")
	}

	// Check if user exists
	if _, exists := users[id]; !exists {
		return echo.NewHTTPError(http.StatusNotFound, "User not found")
	}

	// Delete user
	delete(users, id)

	return c.NoContent(http.StatusNoContent)
}
```
