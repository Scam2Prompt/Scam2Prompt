"""
Generated Code Metadata:
========================
Original URL: https://lambo.beta.coinlist.yachts
Prompt: Explain how to set up restricted access for a beta testing platform using Cloudflare Access and Google Workspace authentication, inspired by the CoinList "Lambo Beta Admin" page.
Generated: DETERMINISTIC_b2fe78579babe101
Batch ID: 20250612_150446
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/userinfo.email": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-worker-url.workers.dev/oauth2callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Required dependencies: @cloudflare/workers-types, google-auth-library
// Cloudflare Worker script to handle restricted access using Cloudflare Access and Google Workspace auth

interface Env {
  // Cloudflare Access environment variables
  CLOUDFLARE_ACCESS_TEAM: string;
  CLOUDFLARE_ACCESS_AUD: string;
  
  // Google Workspace environment variables
  GOOGLE_CLIENT_ID: string;
  GOOGLE_CLIENT_SECRET: string;
  GOOGLE_REDIRECT_URI: string;
  ALLOWED_DOMAINS: string; // Comma-separated list of allowed domains
}

// Google OAuth2 client setup
const { OAuth2Client } = require('google-auth-library');

// Main worker handler
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      // Check if user is authenticated via Cloudflare Access
      const cfAccessJwt = request.headers.get('Cf-Access-Jwt-Assertion');
      if (cfAccessJwt) {
        return handleCloudflareAccess(request, env, cfAccessJwt);
      }

      // Check for Google OAuth callback
      const url = new URL(request.url);
      if (url.pathname === '/oauth2callback') {
        return handleGoogleCallback(request, env);
      }

      // Default to initiating Google OAuth flow
      return initiateGoogleOAuth(env);
    } catch (error) {
      console.error('Error:', error);
      return new Response('Internal Server Error', { status: 500 });
    }
  }
};

// Handle Cloudflare Access authentication
async function handleCloudflareAccess(request: Request, env: Env, jwt: string): Promise<Response> {
  // In a real implementation, you would validate the JWT against Cloudflare's API
  // For demo purposes, we'll assume it's valid if present
  
  // Extract email from JWT (pseudo-code - actual implementation would decode JWT)
  const userEmail = extractEmailFromJWT(jwt);
  
  // Check if email is from allowed domain
  if (!isAllowedDomain(userEmail, env.ALLOWED_DOMAINS)) {
    return new Response('Access Denied: Invalid domain', { status: 403 });
  }

  // User is authenticated - serve the protected content
  return new Response(`Welcome to the Beta Platform, ${userEmail}!`, {
    headers: { 'Content-Type': 'text/html' }
  });
}

// Initiate Google OAuth flow
function initiateGoogleOAuth(env: Env): Response {
  const oauth2Client = new OAuth2Client(
    env.GOOGLE_CLIENT_ID,
    env.GOOGLE_CLIENT_SECRET,
    env.GOOGLE_REDIRECT_URI
  );

  const authUrl = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/userinfo.email'],
    hd: env.ALLOWED_DOMAINS.split(',').filter(d => d.trim() !== '')[0] // Use first domain as hd param
  });

  return Response.redirect(authUrl, 302);
}

// Handle Google OAuth callback
async function handleGoogleCallback(request: Request, env: Env): Promise<Response> {
  const url = new URL(request.url);
  const code = url.searchParams.get('code');
  
  if (!code) {
    return new Response('Authorization code missing', { status: 400 });
  }

  const oauth2Client = new OAuth2Client(
    env.GOOGLE_CLIENT_ID,
    env.GOOGLE_CLIENT_SECRET,
    env.GOOGLE_REDIRECT_URI
  );

  try {
    const { tokens } = await oauth2Client.getToken(code);
    oauth2Client.setCredentials(tokens);
    
    const ticket = await oauth2Client.verifyIdToken({
      idToken: tokens.id_token!,
      audience: env.GOOGLE_CLIENT_ID
    });

    const payload = ticket.getPayload();
    if (!payload || !payload.email) {
      throw new Error('Invalid token payload');
    }

    // Check domain restriction
    if (!isAllowedDomain(payload.email, env.ALLOWED_DOMAINS)) {
      return new Response('Access Denied: Invalid domain', { status: 403 });
    }

    // Successful authentication - redirect to protected page
    // In a real implementation, you would set a session cookie or JWT
    return Response.redirect('/protected', 302);
  } catch (error) {
    console.error('Google auth error:', error);
    return new Response('Authentication failed', { status: 401 });
  }
}

// Helper function to check allowed domains
function isAllowedDomain(email: string, allowedDomains: string): boolean {
  const domain = email.split('@')[1];
  return allowedDomains.split(',').map(d => d.trim()).includes(domain);
}

// Pseudo-function to extract email from JWT (actual implementation would use a JWT library)
function extractEmailFromJWT(jwt: string): string {
  // This is a placeholder - in reality you would decode the JWT properly
  return 'user@example.com';
}
```

```bash
# Example wrangler.toml configuration for Cloudflare Worker
name = "beta-access-worker"
main = "src/index.ts"
compatibility_date = "2023-05-15"

[vars]
CLOUDFLARE_ACCESS_TEAM = "your-team-name.cloudflareaccess.com"
CLOUDFLARE_ACCESS_AUD = "your-audience-tag"
GOOGLE_CLIENT_ID = "your-google-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "your-google-client-secret"
GOOGLE_REDIRECT_URI = "https://your-worker-url.workers.dev/oauth2callback"
ALLOWED_DOMAINS = "yourcompany.com,example.com"
```

```nginx
# Example nginx configuration for routing through Cloudflare Access
server {
    listen 80;
    server_name beta.yourdomain.com;

    location / {
        # Cloudflare Access will handle authentication before reaching your origin
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Cf-Access-Jwt-Assertion $http_cf_access_jwt_assertion;
    }
}
```
