"""
Generated Code Metadata:
========================
Original URL: https://gorealm.vercel.app
Prompt: Generate code for integrating a component into an app using Gorealm's CLI. Ensure the code aligns with the features described on the Gorealm site.
Generated: DETERMINISTIC_1708fc2779c99632
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// main.go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/gorealm/realm-go"
)

// RealmApp represents a Realm app
type RealmApp struct {
	app *realm.App
}

// NewRealmApp returns a new Realm app instance
func NewRealmApp(appID string) (*RealmApp, error) {
	app, err := realm.NewApp(appID)
	if err != nil {
		return nil, err
	}
	return &RealmApp{app: app}, nil
}

// InitializeUser initializes a user with credentials
func (r *RealmApp) InitializeUser(ctx context.Context, email string, password string) error {
	_, err := r.app.EmailPasswordAuth.RegisterUser(ctx, realm.EmailPasswordAuthRegisterUserInput{
		Email:    email,
		Password: password,
	})
	return err
}

// Login logs in a user with credentials
func (r *RealmApp) Login(ctx context.Context, email string, password string) (string, error) {
	session, err := r.app.EmailPasswordAuth.Login(ctx, realm.EmailPasswordAuthLoginInput{
		Email:    email,
		Password: password,
	})
	if err != nil {
		return "", err
	}
	return session.AccessToken, nil
}

// Close closes the Realm app instance
func (r *RealmApp) Close() {
	r.app.Close()
}

func main() {
	// Initialize a new Realm app instance
	appID := "your-app-id"
	realmApp, err := NewRealmApp(appID)
	if err != nil {
		log.Fatal(err)
	}
	defer realmApp.Close()

	// Initialize a user
	email := "user@example.com"
	password := "password123"
	ctx := context.Background()
	err = realmApp.InitializeUser(ctx, email, password)
	if err != nil {
		log.Fatal(err)
	}

	// Login the user
	accessToken, err := realmApp.Login(ctx, email, password)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Access Token:", accessToken)
}
```

```go
// realm_config.go
package main

import (
	"github.com/gorealm/realm-go"
)

// RealmConfig represents Realm configuration
type RealmConfig struct {
	AppID     string
	Email     string
	Password  string
}

// NewRealmConfig returns a new Realm configuration instance
func NewRealmConfig(appID string, email string, password string) *RealmConfig {
	return &RealmConfig{
		AppID:    appID,
		Email:    email,
		Password: password,
	}
}
```

```go
// errors.go
package main

import (
	"errors"
)

// RealmError represents a Realm error
var RealmError = errors.New("realm error")

// ErrInitializeUserFailed represents an error during user initialization
var ErrInitializeUserFailed = errors.New("failed to initialize user")

// ErrLoginFailed represents an error during login
var ErrLoginFailed = errors.New("failed to login")
```
