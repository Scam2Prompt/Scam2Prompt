"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-1.pages.dev
Prompt: Write a SvelteKit middleware that checks if a user is connected to a wallet via Wallet Connect before accessing protected routes.
Generated: DETERMINISTIC_aa53e74997b245d5
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/hooks.server.js

import { json } from '@sveltejs/kit';

/**
 * Middleware hook to check if the user is connected to a wallet via WalletConnect
 * before accessing protected routes.
 *
 * @param {Object} event - The request event object provided by SvelteKit.
 * @param {Function} resolve - Function to continue with the request processing.
 * @returns {Response | Promise<Response>} - Returns the response or a promise resolving to a response.
 */
export async function handle({ event, resolve }) {
	// List of protected routes that require wallet connection
	const protectedRoutes = ['/dashboard', '/profile', '/protected'];

	// Check if the current route is protected
	const isProtectedRoute = protectedRoutes.some((route) =>
		event.url.pathname.startsWith(route)
	);

	// If the route is not protected, continue with the request normally
	if (!isProtectedRoute) {
		return resolve(event);
	}

	try {
		// Retrieve wallet connection status from cookies (or headers/session, etc.)
		const walletConnected = event.cookies.get('walletConnected'); // Example: using cookies

		// If walletConnected is not set or false, deny access
		if (!walletConnected || walletConnected !== 'true') {
			return json(
				{
					error: 'Access denied. Please connect your wallet to proceed.'
				},
				{ status: 401 }
			);
		}

		// If wallet is connected, proceed with the request
		return resolve(event);
	} catch (error) {
		// Handle unexpected errors gracefully
		console.error('Error during wallet connection check:', error);
		return json(
			{
				error: 'An unexpected error occurred. Please try again later.'
			},
			{ status: 500 }
		);
	}
}
```
