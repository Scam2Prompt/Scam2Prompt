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
	"net/http"
	"time"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/opentracing/opentracing-go"
	"github.com/uber/jaeger-client-go"
	jaegercfg "github.com/uber/jaeger-client-go/config"
	jaegerlog "github.com/uber/jaeger-client-go/log"
	"github.com/uber/jaeger-lib/metrics"
)

// User represents a user model
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

// initJaeger initializes Jaeger tracer
func initJaeger(serviceName string) (opentracing.Tracer, error) {
	cfg := jaegercfg.Configuration{
		ServiceName: serviceName,
		Sampler: &jaegercfg.SamplerConfig{
			Type:  jaeger.SamplerTypeConst,
			Param: 1,
		},
		Reporter: &jaegercfg.ReporterConfig{
			LogSpans:           true,
			LocalAgentHostPort: "localhost:6831",
		},
	}

	jLogger := jaegerlog.StdLogger
	jMetricsFactory := metrics.NullFactory

	tracer, _, err := cfg.NewTracer(
		jaegercfg.Logger(jLogger),
		jaegercfg.Metrics(jMetricsFactory),
	)
	if err != nil {
		return nil, err
	}

	opentracing.SetGlobalTracer(tracer)
	return tracer, nil
}

// simulateDatabaseCall simulates a database operation with delay
func simulateDatabaseCall(ctx echo.Context) (User, error) {
	span, _ := opentracing.StartSpanFromContext(ctx.Request().Context(), "database_call")
	defer span.Finish()

	// Simulate database latency
	time.Sleep(100 * time.Millisecond)

	return User{
		ID:    1,
		Name:  "John Doe",
		Email: "john@example.com",
	}, nil
}

// simulateExternalAPICall simulates an external API call with delay
func simulateExternalAPICall(ctx echo.Context) error {
	span, _ := opentracing.StartSpanFromContext(ctx.Request().Context(), "external_api_call")
	defer span.Finish()

	// Simulate API latency
	time.Sleep(200 * time.Millisecond)

	return nil
}

// getUserHandler handles GET /users/:id request
func getUserHandler(c echo.Context) error {
	span, ctx := opentracing.StartSpanFromContext(c.Request().Context(), "getUserHandler")
	defer span.Finish()

	// Simulate database operation
	user, err := simulateDatabaseCall(c)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "database error"})
	}

	// Simulate external API call
	err = simulateExternalAPICall(c)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "external API error"})
	}

	return c.JSON(http.StatusOK, user)
}

func main() {
	// Initialize Jaeger tracer
	tracer, err := initJaeger("echo-jaeger-demo")
	if err != nil {
		panic(err)
	}
	defer tracer.(*jaeger.Tracer).Close()

	// Create Echo instance
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Jaeger middleware
	e.Use(func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			req := c.Request()
			span := tracer.StartSpan(req.URL.Path)
			defer span.Finish()

			ctx := opentracing.ContextWithSpan(req.Context(), span)
			c.SetRequest(req.WithContext(ctx))

			return next(c)
		}
	})

	// Routes
	e.GET("/users/:id", getUserHandler)

	// Start server
	e.Logger.Fatal(e.Start(":8080"))
}
```
