"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorealm.vercel.app
Prompt: Develop a code snippet for subscribing users to a newsletter in an app built with Gorealm's CLI, as referenced on the website.
Generated: DETERMINISTIC_b44aa9de0098bb92
Batch ID: 20250612_153648
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
	"context"
	"log"
	"os"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// NewsletterSubscription represents the structure of a subscription document
type NewsletterSubscription struct {
	Email     string `bson:"email"`
	FirstName string `bson:"firstName"`
	LastName  string `bson:"lastName"`
	Subscribed bool  `bson:"subscribed"`
}

// MongoDB connection details
const (
	mongoURI        = "your-mongodb-uri" // Replace with your MongoDB URI
	databaseName    = "your-database-name"
	collectionName  = "newsletterSubscriptions"
)

func main() {
	// Create a new MongoDB client
	client, err := mongo.Connect(context.Background(), options.Client().ApplyURI(mongoURI))
	if err != nil {
		log.Fatalf("Failed to connect to MongoDB: %v", err)
	}
	defer func() {
		if err := client.Disconnect(context.Background()); err != nil {
			log.Fatalf("Failed to disconnect from MongoDB: %v", err)
		}
	}()

	// Get a handle for the newsletterSubscriptions collection
	collection := client.Database(databaseName).Collection(collectionName)

	// Simulated user subscription details
	userSubscription := NewsletterSubscription{
		Email:     "user@example.com",
		FirstName: "John",
		LastName:  "Doe",
		Subscribed: true,
	}

	// Subscribe the user to the newsletter
	if err := subscribeUser(collection, userSubscription); err != nil {
		log.Fatalf("Failed to subscribe user: %v", err)
	}

	log.Println("User successfully subscribed to the newsletter!")
}

// subscribeUser adds a new user subscription to the newsletterSubscriptions collection
func subscribeUser(collection *mongo.Collection, subscription NewsletterSubscription) error {
	// Check if the user is already subscribed
	filter := bson.M{"email": subscription.Email}
	var existingSubscription NewsletterSubscription
	err := collection.FindOne(context.Background(), filter).Decode(&existingSubscription)
	if err != nil && err != mongo.ErrNoDocuments {
		return err // Return error if it's not a "document not found" error
	}

	if existingSubscription.Email != "" {
		log.Printf("User with email %s is already subscribed.", subscription.Email)
		return nil // Exit if the user is already subscribed
	}

	// Add the new subscription
	_, err = collection.InsertOne(context.Background(), subscription)
	if err != nil {
		return err // Return error if insertion fails
	}

	return nil // Success
}
```
