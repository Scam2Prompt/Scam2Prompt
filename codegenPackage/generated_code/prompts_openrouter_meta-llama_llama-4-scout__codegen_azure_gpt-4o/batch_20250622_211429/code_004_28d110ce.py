"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Go code snippet using Echo and Jaeger for bottleneck investigation, similar to the one described in the blog post "GoのEchoでJaegerを使ってボトルネックを調査する".
Generated: DETERMINISTIC_28d110ce556fac5a
Batch ID: 20250622_211429
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
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/labstack/echo/v4"
	"github.com/opentracing/opentracing-go"
	"github.com/uber/jaeger-client-go"
	"github.com/uber/jaeger-client-go/config"
	"github.com/uber/jaeger-lib/metrics"
)

// initTracer initializes and returns a Jaeger tracer.
func initTracer(serviceName string) (opentracing.Tracer, func(), error) {
	cfg := &config.Configuration{
		ServiceName: serviceName,
		Sampler: &config.SamplerConfig{
			Type:  "const",
			Param: 1,
		},
		Reporter: &config.ReporterConfig{
			LogSpans:           true,
			LocalAgentHostPort: "127.0.0.1:6831", // Default Jaeger agent port
		},
	}

	metricsFactory := metrics.NullFactory
	tracer, closer, err := cfg.NewTracer(config.Metrics(metricsFactory))
	if err != nil {
		return nil, nil, fmt.Errorf("failed to initialize tracer: %w", err)
	}

	opentracing.SetGlobalTracer(tracer)
	return tracer, func() { closer.Close() }, nil
}

func main() {
	// Initialize Jaeger tracer
	tracer, closer, err := initTracer("echo-jaeger-example")
	if err != nil {
		log.Fatalf("Could not initialize Jaeger tracer: %v", err)
	}
	defer closer()

	// Create a new Echo instance
	e := echo.New()

	// Middleware to trace requests
	e.Use(func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			// Start a new span for the request
			span := tracer.StartSpan(c.Request().URL.Path)
			defer span.Finish()

			// Add span context to the request context
			ctx := opentracing.ContextWithSpan(c.Request().Context(), span)
			c.SetRequest(c.Request().WithContext(ctx))

			// Proceed to the next handler
			return next(c)
		}
	})

	// Define a sample route
	e.GET("/hello", func(c echo.Context) error {
		// Extract the span from the context
		span := opentracing.SpanFromContext(c.Request().Context())
		if span != nil {
			span.SetTag("endpoint", "/hello")
		}

		// Simulate some processing
		time.Sleep(100 * time.Millisecond)

		return c.String(http.StatusOK, "Hello, World!")
	})

	// Start the server
	if err := e.Start(":8080"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
```
