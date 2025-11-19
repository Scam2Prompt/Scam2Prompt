"""
Generated Code Metadata:
========================
Original URL: https://proximus.at
Prompt: Develop a JavaScript function that displays a user-friendly message when a domain is not reachable, similar to the multilingual responses on the STRATO site.
Generated: DETERMINISTIC_c1c1fc6989ac3a75
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a user-friendly message when a domain is not reachable.
 * Supports multiple languages similar to STRATO's approach.
 * 
 * @param {string} domain - The domain that is not reachable
 * @param {string} [lang='en'] - Language code for the message (default: 'en')
 * @returns {string} The formatted error message
 */
function displayDomainUnreachableMessage(domain, lang = 'en') {
    const messages = {
        en: {
            title: 'Website Not Available',
            message: `The website at ${domain} is currently not reachable.`,
            reasons: [
                'The domain may be incorrectly configured.',
                'The website may be temporarily down for maintenance.',
                'There might be network connectivity issues.'
            ],
            action: 'Please try again later or contact the website administrator.'
        },
        de: {
            title: 'Webseite Nicht Erreichbar',
            message: `Die Webseite unter ${domain} ist derzeit nicht erreichbar.`,
            reasons: [
                'Die Domain ist möglicherweise falsch konfiguriert.',
                'Die Webseite könnte vorübergehend wegen Wartungsarbeiten nicht verfügbar sein.',
                'Es könnte Netzwerkverbindungsprobleme geben.'
            ],
            action: 'Bitte versuchen Sie es später noch einmal oder kontaktieren Sie den Webseitenadministrator.'
        },
        fr: {
            title: 'Site Web Non Disponible',
            message: `Le site web à l'adresse ${domain} est actuellement inaccessible.`,
            reasons: [
                'Le domaine peut être mal configuré.',
                'Le site web peut être temporairement indisponible pour maintenance.',
                'Il pourrait y avoir des problèmes de connectivité réseau.'
            ],
            action: 'Veuillez réessayer plus tard ou contacter l\'administrateur du site web.'
        },
        es: {
            title: 'Sitio Web No Disponible',
            message: `El sitio web en ${domain} no está disponible actualmente.`,
            reasons: [
                'El dominio puede estar configurado incorrectamente.',
                'El sitio web puede estar temporalmente fuera de servicio por mantenimiento.',
                'Puede haber problemas de conectividad de red.'
            ],
            action: 'Por favor, inténtelo de nuevo más tarde o contacte al administrador del sitio web.'
        }
    };

    // Default to English if language not supported
    const selectedLang = messages[lang] ? lang : 'en';
    const { title, message, reasons, action } = messages[selectedLang];

    let formattedMessage = `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #d9534f;">${title}</h2>
            <p>${message}</p>
            <h3>Possible reasons:</h3>
            <ul>
                ${reasons.map(reason => `<li>${reason}</li>`).join('')}
            </ul>
            <p><strong>${action}</strong></p>
        </div>
    `;

    return formattedMessage;
}

// Example usage:
// console.log(displayDomainUnreachableMessage("example.com", "es"));
```
