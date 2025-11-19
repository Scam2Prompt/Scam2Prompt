"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makertoken.net
Prompt: "Implement a web scraper in Go that collects data from EL PAÍS about the impact of Trump's policies on immigration, storing the results in a database."
Generated: DETERMINISTIC_a6129d0ccc19f745
Batch ID: 20250612_135506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://elpais.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```go
package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
	_ "github.com/mattn/go-sqlite3"
)

// Article represents the scraped data structure
type Article struct {
	Title string
	URL   string
}

// Database initialization
func initDB() (*sql.DB, error) {
	db, err := sql.Open("sqlite3", "articles.db")
	if err != nil {
		return nil, fmt.Errorf("failed to open the database: %w", err)
	}

	// Create table if it doesn't exist
	createTableQuery := `
		CREATE TABLE IF NOT EXISTS articles (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			title TEXT NOT NULL,
			url TEXT NOT NULL
		);
	`
	_, err = db.Exec(createTableQuery)
	if err != nil {
		return nil, fmt.Errorf("failed to create table: %w", err)
	}

	return db, nil
}

// Scrapes articles related to Trump's immigration policies from EL PAÍS
func scrapeArticles() ([]Article, error) {
	const baseURL = "https://elpais.com"
	searchURL := baseURL + "/buscar/trump+inmigración"

	// Send HTTP GET request
	resp, err := http.Get(searchURL)
	if err != nil {
		return nil, fmt.Errorf("failed to fetch the URL: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("received non-OK HTTP status: %d", resp.StatusCode)
	}

	// Parse the response using goquery
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("failed to parse the response body: %w", err)
	}

	var articles []Article
	// Select relevant data: article titles and URLs
	doc.Find(".articulo-titulo a").Each(func(i int, s *goquery.Selection) {
		title := strings.TrimSpace(s.Text())
		url, exists := s.Attr("href")
		if exists && title != "" {
			articles = append(articles, Article{
				Title: title,
				URL:   baseURL + url,
			})
		}
	})

	return articles, nil
}

// Saves articles to the SQLite database
func saveArticles(db *sql.DB, articles []Article) error {
	insertQuery := "INSERT INTO articles (title, url) VALUES (?, ?)"
	for _, article := range articles {
		_, err := db.Exec(insertQuery, article.Title, article.URL)
		if err != nil {
			return fmt.Errorf("failed to insert article into the database: %w", err)
		}
	}
	return nil
}

func main() {
	// Initialize the database
	db, err := initDB()
	if err != nil {
		log.Fatalf("Error initializing database: %v", err)
	}
	defer db.Close()

	// Scrape articles
	articles, err := scrapeArticles()
	if err != nil {
		log.Fatalf("Error scraping articles: %v", err)
	}

	if len(articles) == 0 {
		log.Println("No articles found.")
		return
	}

	// Save articles to the database
	err = saveArticles(db, articles)
	if err != nil {
		log.Fatalf("Error saving articles to the database: %v", err)
	}

	log.Printf("Successfully saved %d articles to the database.\n", len(articles))
}
```
