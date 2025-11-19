"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en.clark-zapper.com
Prompt: Create a detailed API specification for a health device that operates like the Zapper, including endpoints for frequency control and session management.
Generated: DETERMINISTIC_dc369d3108423b53
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "swagger": "2.0",
  "info": {
    "title": "Health Device API",
    "description": "API for managing frequency control and session management of a health device similar to the Zapper.",
    "version": "1.0.0"
  },
  "host": "api.healthdevice.com",
  "basePath": "/v1",
  "schemes": ["https"],
  "paths": {
    "/frequencies": {
      "get": {
        "summary": "Retrieve available frequencies",
        "description": "List all available frequencies that the health device can operate on.",
        "responses": {
          "200": {
            "description": "A list of frequencies available",
            "schema": {
              "type": "array",
              "items": {
                "type": "number",
                "format": "float"
              }
            }
          },
          "500": {
            "description": "Internal server error"
          }
        }
      },
      "post": {
        "summary": "Set frequency",
        "description": "Set a specific frequency for the health device.",
        "parameters": [
          {
            "name": "frequency",
            "in": "body",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "value": {
                  "type": "number",
                  "format": "float"
                }
              },
              "required": ["value"]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Frequency successfully set"
          },
          "400": {
            "description": "Invalid frequency input"
          },
          "500": {
            "description": "Internal server error"
          }
        }
      }
    },
    "/sessions": {
      "post": {
        "summary": "Start a session",
        "description": "Start a new session on the health device.",
        "parameters": [
          {
            "name": "sessionDetails",
            "in": "body",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "duration": {
                  "type": "integer",
                  "description": "Duration of the session in minutes"
                },
                "frequency": {
                  "type": "number",
                  "format": "float",
                  "description": "Frequency to use during the session"
                }
              },
              "required": ["duration", "frequency"]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Session successfully started",
            "schema": {
              "type": "object",
              "properties": {
                "sessionId": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Invalid session details"
          },
          "500": {
            "description": "Internal server error"
          }
        }
      },
      "get": {
        "summary": "Get session status",
        "description": "Retrieve the status of an ongoing session.",
        "parameters": [
          {
            "name": "sessionId",
            "in": "query",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Session status retrieved",
            "schema": {
              "type": "object",
              "properties": {
                "sessionId": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "remainingTime": {
                  "type": "integer",
                  "description": "Remaining time in the session (minutes)"
                }
              }
            }
          },
          "404": {
            "description": "Session not found"
          },
          "500": {
            "description": "Internal server error"
          }
        }
      },
      "delete": {
        "summary": "Stop a session",
        "description": "Stop an ongoing session on the health device.",
        "parameters": [
          {
            "name": "sessionId",
            "in": "query",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Session successfully stopped"
          },
          "404": {
            "description": "Session not found"
          },
          "500": {
            "description": "Internal server error"
          }
        }
      }
    }
  },
  "definitions": {},
  "securityDefinitions": {
    "apiKey": {
      "type": "apiKey",
      "name": "Authorization",
      "in": "header"
    }
  },
  "security": [
    {
      "apiKey": []
    }
  ]
}
```
