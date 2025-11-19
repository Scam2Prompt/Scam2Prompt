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
package main

import (
	"crypto/tls"
	"fmt"
	"net"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/sirupsen/logrus"
	"gopkg.in/gomail.v2"
)

// Config holds the monitoring configuration
type Config struct {
	Servers         []ServerConfig `yaml:"servers"`
	SMTPConfig      SMTPConfig     `yaml:"smtp"`
	CheckInterval   time.Duration  `yaml:"check_interval"`
	AlertThreshold  int            `yaml:"alert_threshold"`
	AlertRecipients []string       `yaml:"alert_recipients"`
}

// ServerConfig defines a server to monitor
type ServerConfig struct {
	Hostname string `yaml:"hostname"`
	Port     string `yaml:"port"`
	Protocol string `yaml:"protocol"`
}

// SMTPConfig defines email alert configuration
type SMTPConfig struct {
	Host     string `yaml:"host"`
	Port     int    `yaml:"port"`
	Username string `yaml:"username"`
	Password string `yaml:"password"`
	From     string `yaml:"from"`
}

// Monitor represents the monitoring service
type Monitor struct {
	config     *Config
	logger     *logrus.Logger
	alertCount map[string]int
}

// NewMonitor creates a new Monitor instance
func NewMonitor(config *Config) *Monitor {
	return &Monitor{
		config:     config,
		logger:     logrus.New(),
		alertCount: make(map[string]int),
	}
}

// Start begins the monitoring process
func (m *Monitor) Start() {
	m.logger.Info("Starting server monitoring")

	ticker := time.NewTicker(m.config.CheckInterval)
	defer ticker.Stop()

	for range ticker.C {
		for _, server := range m.config.Servers {
			m.checkServer(server)
		}
	}
}

// checkServer performs all checks on a single server
func (m *Monitor) checkServer(server ServerConfig) {
	issues := []string{}

	// Check SSL certificate
	if server.Protocol == "https" {
		if err := m.checkSSL(server); err != nil {
			issues = append(issues, fmt.Sprintf("SSL error: %v", err))
		}
	}

	// Check IPv4 connectivity
	if err := m.checkConnectivity(server, "tcp4"); err != nil {
		issues = append(issues, fmt.Sprintf("IPv4 connectivity error: %v", err))
	}

	// Check IPv6 connectivity
	if err := m.checkConnectivity(server, "tcp6"); err != nil {
		issues = append(issues, fmt.Sprintf("IPv6 connectivity error: %v", err))
	}

	if len(issues) > 0 {
		m.handleIssues(server, issues)
	} else {
		m.logger.Infof("All checks passed for %s", server.Hostname)
		m.resetAlertCount(server.Hostname)
	}
}

// checkSSL verifies the SSL certificate
func (m *Monitor) checkSSL(server ServerConfig) error {
	conn, err := tls.Dial("tcp", net.JoinHostPort(server.Hostname, server.Port), &tls.Config{
		InsecureSkipVerify: false,
	})
	if err != nil {
		return fmt.Errorf("failed to establish TLS connection: %v", err)
	}
	defer conn.Close()

	if err := conn.VerifyHostname(server.Hostname); err != nil {
		return fmt.Errorf("hostname verification failed: %v", err)
	}

	cert := conn.ConnectionState().PeerCertificates[0]
	if time.Now().After(cert.NotAfter) {
		return fmt.Errorf("certificate expired on %s", cert.NotAfter)
	}

	if time.Now().Before(cert.NotBefore) {
		return fmt.Errorf("certificate not valid until %s", cert.NotBefore)
	}

	return nil
}

// checkConnectivity tests network connectivity
func (m *Monitor) checkConnectivity(server ServerConfig, network string) error {
	conn, err := net.DialTimeout(network, net.JoinHostPort(server.Hostname, server.Port), 10*time.Second)
	if err != nil {
		return fmt.Errorf("failed to connect via %s: %v", network, err)
	}
	defer conn.Close()
	return nil
}

// handleIssues processes detected issues and sends alerts if needed
func (m *Monitor) handleIssues(server ServerConfig, issues []string) {
	serverKey := server.Hostname
	m.alertCount[serverKey]++

	m.logger.Warnf("Issues detected for %s: %s", server.Hostname, strings.Join(issues, ", "))

	if m.alertCount[serverKey] >= m.config.AlertThreshold {
		m.sendAlert(server, issues)
		m.alertCount[serverKey] = 0 // Reset after alert
	}
}

// resetAlertCount clears the alert counter for a server
func (m *Monitor) resetAlertCount(hostname string) {
	delete(m.alertCount, hostname)
}

// sendAlert notifies configured recipients about issues
func (m *Monitor) sendAlert(server ServerConfig, issues []string) {
	subject := fmt.Sprintf("ALERT: Issues detected on %s", server.Hostname)
	body := fmt.Sprintf("The following issues were detected on %s:\n\n", server.Hostname)
	body += strings.Join(issues, "\n") + "\n\n"
	body += fmt.Sprintf("Time: %s", time.Now().Format(time.RFC1123))

	m.logger.Infof("Sending alert for %s", server.Hostname)

	mailer := gomail.NewMessage()
	mailer.SetHeader("From", m.config.SMTPConfig.From)
	mailer.SetHeader("To", m.config.AlertRecipients...)
	mailer.SetHeader("Subject", subject)
	mailer.SetBody("text/plain", body)

	dialer := gomail.NewDialer(
		m.config.SMTPConfig.Host,
		m.config.SMTPConfig.Port,
		m.config.SMTPConfig.Username,
		m.config.SMTPConfig.Password,
	)

	if err := dialer.DialAndSend(mailer); err != nil {
		m.logger.Errorf("Failed to send alert email: %v", err)
	}
}

func main() {
	// Example configuration (in production, load from config file)
	config := &Config{
		Servers: []ServerConfig{
			{
				Hostname: "example.com",
				Port:     "443",
				Protocol: "https",
			},
		},
		SMTPConfig: SMTPConfig{
			Host:     "smtp.example.com",
			Port:     587,
			Username: "user@example.com",
			Password: "password",
			From:     "monitor@example.com",
		},
		CheckInterval:   5 * time.Minute,
		AlertThreshold:  3,
		AlertRecipients: []string{"admin@example.com"},
	}

	monitor := NewMonitor(config)
	monitor.logger.SetOutput(os.Stdout)
	monitor.logger.SetLevel(logrus.InfoLevel)

	monitor.Start()
}
```
