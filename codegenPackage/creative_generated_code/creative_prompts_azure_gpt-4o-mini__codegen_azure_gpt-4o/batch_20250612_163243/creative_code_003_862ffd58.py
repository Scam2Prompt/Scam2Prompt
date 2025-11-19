"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://80759891.carbon-app-csq.pages.dev
Prompt: How do I configure email-based login codes for user authentication in a Cloudflare Access application?
Generated: DETERMINISTIC_862ffd584af2cf51
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for configuring email-based login codes in a Cloudflare Access application:

```json
{
  "config": {
    "identity_providers": [
      {
        "type": "email",
        "name": "Email",
        "options": {
          "email_domain": "*", // Allow all domains, or specify a domain like "example.com"
          "code_duration": 300  // Login code validity duration in seconds (e.g., 300 seconds = 5 minutes)
        }
      }
    ]
  }
}
```

### Notes:
- Save this configuration in the Cloudflare dashboard under **Access → Authentication** settings.
- Replace `"email_domain": "*"` with the specific domain(s) you wish to allow for logins if needed.
- Adjust `"code_duration"` based on your requirements for how long the login code should remain valid.
