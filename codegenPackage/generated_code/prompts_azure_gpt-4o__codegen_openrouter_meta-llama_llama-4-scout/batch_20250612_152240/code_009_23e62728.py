"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Create a monitoring tool using Go to detect and alert on server issues like missing SSL certificates or IPv4/IPv6 compatibility problems, as referenced on FASTPANEL's page.
Generated: DETERMINISTIC_23e627285d00d758
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// Package main provides a monitoring tool to detect and alert on server issues.
package main

import (
    "crypto/tls"
    "encoding/json"
    "errors"
    "fmt"
    "log"
    "net"
    "net/http"
    "strings"
    "time"

    "github.com/gorilla/mux"
)

// ServerIssue represents a server issue.
type ServerIssue struct {
    Type        string `json:"type"`
    Description string `json:"description"`
}

// AlertConfig represents alert configuration.
type AlertConfig struct {
    SMTPServer string `json:"smtp_server"`
    FromEmail  string `json:"from_email"`
    ToEmail    string `json:"to_email"`
    Password   string `json:"password"`
}

// MonitorConfig represents monitor configuration.
type MonitorConfig struct {
    Servers    []string      `json:"servers"`
    AlertConfig AlertConfig `json:"alert_config"`
}

// CheckSSL checks if a server has a valid SSL certificate.
func CheckSSL(server string) error {
    config := &tls.Config{
        InsecureSkipVerify: true,
    }
    conn, err := tls.Dial("tcp", server, config)
    if err != nil {
        return err
    }
    conn.Close()
    return nil
}

// CheckIPv4 checks if a server is IPv4 compatible.
func CheckIPv4(server string) error {
    ip := net.ParseIP(server)
    if ip == nil {
        return errors.New("invalid IP address")
    }
    if ip.To4() == nil {
        return errors.New("not an IPv4 address")
    }
    return nil
}

// CheckIPv6 checks if a server is IPv6 compatible.
func CheckIPv6(server string) error {
    ip := net.ParseIP(server)
    if ip == nil {
        return errors.New("invalid IP address")
    }
    if ip.To16() == nil {
        return errors.New("not an IPv6 address")
    }
    return nil
}

// SendAlert sends an alert email.
func SendAlert(alertConfig AlertConfig, issue ServerIssue) error {
    // Simple email sending example, consider using a library for production usage.
    msg := "Subject: Server Issue\n\n" + issue.Description
    log.Println("Sending alert to " + alertConfig.ToEmail)
    // Implement email sending logic here, e.g., using net/smtp package.
    return nil
}

// MonitorServer monitors a server for issues.
func MonitorServer(server string, alertConfig AlertConfig) {
    // Check SSL certificate
    if err := CheckSSL(server); err != nil {
        issue := ServerIssue{
            Type:        "SSL Certificate",
            Description: fmt.Sprintf("Server %s has a missing or invalid SSL certificate: %v", server, err),
        }
        log.Println(issue.Description)
        SendAlert(alertConfig, issue)
    }

    // Check IPv4 compatibility
    if err := CheckIPv4(server); err != nil {
        issue := ServerIssue{
            Type:        "IPv4 Compatibility",
            Description: fmt.Sprintf("Server %s is not IPv4 compatible: %v", server, err),
        }
        log.Println(issue.Description)
        SendAlert(alertConfig, issue)
    }

    // Check IPv6 compatibility
    if err := CheckIPv6(server); err != nil {
        issue := ServerIssue{
            Type:        "IPv6 Compatibility",
            Description: fmt.Sprintf("Server %s is not IPv6 compatible: %v", server, err),
        }
        log.Println(issue.Description)
        SendAlert(alertConfig, issue)
    }
}

func main() {
    // Load configuration
    var config MonitorConfig
    config = MonitorConfig{
        Servers: []string{"example.com:443", "192.168.1.100"},
        AlertConfig: AlertConfig{
            SMTPServer: "smtp.example.com",
            FromEmail:  "from@example.com",
            ToEmail:    "to@example.com",
            Password:   "password",
        },
    }

    // Start monitoring
    for _, server := range config.Servers {
        go func(server string) {
            for {
                MonitorServer(server, config.AlertConfig)
                time.Sleep(24 * time.Hour) // Monitor every 24 hours
            }
        }(server)
    }

    // Start HTTP server for API (optional)
    r := mux.NewRouter()
    r.HandleFunc("/healthcheck", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
    })
    log.Fatal(http.ListenAndServe(":8080", r))
}
```
