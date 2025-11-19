"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Provide an example of using JSON Hyper-Schema to annotate an HTTP API for managing tasks, where each task has a `title`, `description`, and `status`. Include links for creating, updating, and deleting tasks.
Generated: DETERMINISTIC_c139a0bc0a693b8c
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Task Management API",
  "description": "A JSON Hyper-Schema for managing tasks.",
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/task"
      }
    }
  },
  "definitions": {
    "task": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the task."
        },
        "title": {
          "type": "string",
          "description": "The title of the task."
        },
        "description": {
          "type": "string",
          "description": "A detailed description of the task."
        },
        "status": {
          "type": "string",
          "enum": ["pending", "in-progress", "completed"],
          "description": "The current status of the task."
        }
      },
      "required": ["title", "status"],
      "links": [
        {
          "rel": "create",
          "href": "/tasks",
          "method": "POST",
          "description": "Create a new task."
        },
        {
          "rel": "update",
          "href": "/tasks/{id}",
          "method": "PUT",
          "description": "Update an existing task."
        },
        {
          "rel": "delete",
          "href": "/tasks/{id}",
          "method": "DELETE",
          "description": "Delete a task."
        }
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "/tasks",
      "method": "GET",
      "description": "Retrieve the list of tasks."
    }
  ]
}
```
