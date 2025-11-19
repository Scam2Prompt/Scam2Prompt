"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Generate a code snippet in JavaScript to implement a cookie consent banner on a dental clinic website, following GDPR guidelines, as seen on Studio Dentistico dott.ssa Vira Palazzo's website.
Generated: DETERMINISTIC_530eff023d52ea6f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Banner Implementation for GDPR Compliance
document.addEventListener('DOMContentLoaded', function() {
    const cookieBanner = document.createElement('div');
    cookieBanner.id = 'cookie-consent-banner';
    cookieBanner.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background-color: #f8f9fa;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    `;

    const message = document.createElement('p');
    message.textContent = 'This website uses cookies to ensure you get the best experience. By continuing to browse, you agree to our use of cookies.';
    message.style.margin = '0 0 15px 0';
    message.style.color = '#333';
    message.style.fontSize = '14px';

    const buttonContainer = document.createElement('div');
    buttonContainer.style.display = 'flex';
    buttonContainer.style.gap = '10px';

    const acceptButton = document.createElement('button');
    acceptButton.textContent = 'Accept';
    acceptButton.style.cssText = `
        padding: 8px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    `;

    const rejectButton = document.createElement('button');
    rejectButton.textContent = 'Reject';
    rejectButton.style.cssText = `
        padding: 8px 20px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    `;

    const cookieSettingsButton = document.createElement('button');
    cookieSettingsButton.textContent = 'Cookie Settings';
    cookieSettingsButton.style.cssText = `
        padding: 8px 20px;
        background-color: transparent;
        color: #007bff;
        border: 1px solid #007bff;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    `;

    buttonContainer.appendChild(acceptButton);
    buttonContainer.appendChild(rejectButton);
    buttonContainer.appendChild(cookieSettingsButton);

    cookieBanner.appendChild(message);
    cookieBanner.appendChild(buttonContainer);
    document.body.appendChild(cookieBanner);

    // Check if consent was already given
    if (document.cookie.includes('cookieConsent=accepted')) {
        cookieBanner.style.display = 'none';
    }

    // Handle button clicks
    acceptButton.addEventListener('click', function() {
        document.cookie = 'cookieConsent=accepted; max-age=31536000; path=/; SameSite=Lax';
        cookieBanner.style.display = 'none';
        // Optional: Trigger analytics or other cookies
    });

    rejectButton.addEventListener('click', function() {
        document.cookie = 'cookieConsent=rejected; max-age=31536000; path=/; SameSite=Lax';
        cookieBanner.style.display = 'none';
        // Optional: Delete existing cookies
        deleteAllCookies();
    });

    cookieSettingsButton.addEventListener('click', function() {
        // Implement your cookie settings modal or page here
        alert('Cookie settings would be displayed here. Implement according to your specific requirements.');
    });

    function deleteAllCookies() {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i];
            const eqPos = cookie.indexOf('=');
            const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
        }
    }
});
```
