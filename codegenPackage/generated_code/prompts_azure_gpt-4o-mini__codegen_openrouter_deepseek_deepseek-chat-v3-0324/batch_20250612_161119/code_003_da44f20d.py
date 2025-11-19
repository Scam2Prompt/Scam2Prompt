"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a JavaScript function that displays the different consórcio plans (Mais Fácil, Normal, Premium) and their respective features as outlined on the Consórcio Chevrolet page.
Generated: DETERMINISTIC_da44f20d7a3dcd01
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays consórcio plans and their features in a structured format.
 * @param {string} containerId - The ID of the container element where plans will be rendered.
 */
function displayConsorcioPlans(containerId) {
    // Validate input
    if (!containerId || typeof containerId !== 'string') {
        console.error('Invalid container ID provided');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container element with ID '${containerId}' not found`);
        return;
    }

    // Plan data
    const plans = [
        {
            name: 'Mais Fácil',
            features: [
                'Entrada reduzida',
                'Parcelas mensais acessíveis',
                'Prazo de até 84 meses',
                'Sorteios mensais',
                'Lance livre opcional'
            ],
            highlight: false
        },
        {
            name: 'Normal',
            features: [
                'Entrada flexível',
                'Parcelas competitivas',
                'Prazo de até 84 meses',
                'Sorteios mensais',
                'Lance livre e fixo opcionais',
                'Possibilidade de contemplação por crédito'
            ],
            highlight: false
        },
        {
            name: 'Premium',
            features: [
                'Entrada diferenciada',
                'Parcelas personalizadas',
                'Prazo de até 84 meses',
                'Sorteios mensais',
                'Lance livre e fixo opcionais',
                'Contemplação por crédito',
                'Assistência 24h',
                'Seguro de proteção de parcelas'
            ],
            highlight: true
        }
    ];

    try {
        // Create HTML structure
        const plansContainer = document.createElement('div');
        plansContainer.className = 'consorcio-plans-container';

        plans.forEach(plan => {
            const planElement = document.createElement('div');
            planElement.className = `consorcio-plan ${plan.highlight ? 'highlight' : ''}`;

            const titleElement = document.createElement('h3');
            titleElement.textContent = plan.name;
            planElement.appendChild(titleElement);

            const featuresList = document.createElement('ul');
            plan.features.forEach(feature => {
                const featureItem = document.createElement('li');
                featureItem.textContent = feature;
                featuresList.appendChild(featureItem);
            });

            planElement.appendChild(featuresList);
            plansContainer.appendChild(planElement);
        });

        // Clear container and append new content
        container.innerHTML = '';
        container.appendChild(plansContainer);

    } catch (error) {
        console.error('Error rendering consórcio plans:', error);
        container.innerHTML = '<p>Ocorreu um erro ao carregar os planos. Por favor, tente novamente mais tarde.</p>';
    }
}

// Example CSS (should be in a separate stylesheet)
/*
.consorcio-plans-container {
    display: flex;
    gap: 20px;
    padding: 20px;
    flex-wrap: wrap;
    justify-content: center;
}

.consorcio-plan {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    width: 300px;
    background: white;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.consorcio-plan.highlight {
    border: 2px solid #0066cc;
    background: #f0f8ff;
}

.consorcio-plan h3 {
    color: #0066cc;
    margin-top: 0;
}

.consorcio-plan ul {
    padding-left: 20px;
}

.consorcio-plan li {
    margin-bottom: 8px;
}
*/
```
