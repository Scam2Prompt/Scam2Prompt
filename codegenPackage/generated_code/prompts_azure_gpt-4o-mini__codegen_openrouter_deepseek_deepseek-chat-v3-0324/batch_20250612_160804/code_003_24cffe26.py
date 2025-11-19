"""
Generated Code Metadata:
========================
Original URL: https://get-link.io
Prompt: Develop a JavaScript function that visualizes the contributions of MIT to regional innovation and economic growth through patents and startups.
Generated: DETERMINISTIC_24cffe264c6a646f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Visualizes MIT's contributions to regional innovation and economic growth through patents and startups.
 * @param {Object} data - The dataset containing MIT's contributions.
 * @param {string} containerId - The ID of the DOM element to render the visualization.
 */
function visualizeMITContributions(data, containerId) {
    // Validate input parameters
    if (!data || typeof data !== 'object') {
        console.error('Invalid data provided');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container element with ID '${containerId}' not found`);
        return;
    }

    // Clear previous content
    container.innerHTML = '';

    try {
        // Create the main visualization container
        const visualization = document.createElement('div');
        visualization.className = 'mit-contributions-visualization';
        visualization.style.fontFamily = 'Arial, sans-serif';
        visualization.style.maxWidth = '1000px';
        visualization.style.margin = '0 auto';

        // Add title
        const title = document.createElement('h1');
        title.textContent = 'MIT Contributions to Regional Innovation and Economic Growth';
        title.style.textAlign = 'center';
        title.style.color = '#333';
        visualization.appendChild(title);

        // Create tabs for different visualization types
        const tabs = document.createElement('div');
        tabs.style.display = 'flex';
        tabs.style.marginBottom = '20px';
        tabs.style.borderBottom = '1px solid #ddd';

        const patentTab = createTab('Patents', true);
        const startupTab = createTab('Startups', false);
        const economicImpactTab = createTab('Economic Impact', false);

        tabs.appendChild(patentTab);
        tabs.appendChild(startupTab);
        tabs.appendChild(economicImpactTab);
        visualization.appendChild(tabs);

        // Create content containers
        const contentContainer = document.createElement('div');
        contentContainer.style.padding = '20px';
        contentContainer.style.border = '1px solid #ddd';
        contentContainer.style.borderTop = 'none';
        contentContainer.style.borderRadius = '0 0 5px 5px';

        const patentContent = createPatentContent(data.patents);
        const startupContent = createStartupContent(data.startups);
        const economicImpactContent = createEconomicImpactContent(data.economicImpact);

        contentContainer.appendChild(patentContent);
        contentContainer.appendChild(startupContent);
        contentContainer.appendChild(economicImpactContent);

        // Initially show only patents content
        startupContent.style.display = 'none';
        economicImpactContent.style.display = 'none';

        visualization.appendChild(contentContainer);
        container.appendChild(visualization);

        // Add tab switching functionality
        patentTab.addEventListener('click', () => {
            patentTab.style.backgroundColor = '#f1f1f1';
            startupTab.style.backgroundColor = '';
            economicImpactTab.style.backgroundColor = '';
            patentContent.style.display = 'block';
            startupContent.style.display = 'none';
            economicImpactContent.style.display = 'none';
        });

        startupTab.addEventListener('click', () => {
            patentTab.style.backgroundColor = '';
            startupTab.style.backgroundColor = '#f1f1f1';
            economicImpactTab.style.backgroundColor = '';
            patentContent.style.display = 'none';
            startupContent.style.display = 'block';
            economicImpactContent.style.display = 'none';
        });

        economicImpactTab.addEventListener('click', () => {
            patentTab.style.backgroundColor = '';
            startupTab.style.backgroundColor = '';
            economicImpactTab.style.backgroundColor = '#f1f1f1';
            patentContent.style.display = 'none';
            startupContent.style.display = 'none';
            economicImpactContent.style.display = 'block';
        });

    } catch (error) {
        console.error('Error rendering visualization:', error);
        container.innerHTML = '<p>An error occurred while rendering the visualization.</p>';
    }

    /**
     * Creates a tab element.
     * @param {string} text - The text to display on the tab.
     * @param {boolean} isActive - Whether the tab should be active initially.
     * @returns {HTMLElement} The created tab element.
     */
    function createTab(text, isActive) {
        const tab = document.createElement('div');
        tab.textContent = text;
        tab.style.padding = '10px 20px';
        tab.style.cursor = 'pointer';
        tab.style.border = '1px solid #ddd';
        tab.style.borderBottom = 'none';
        tab.style.borderRadius = '5px 5px 0 0';
        tab.style.marginRight = '5px';
        tab.style.backgroundColor = isActive ? '#f1f1f1' : '';
        return tab;
    }

    /**
     * Creates the patents visualization content.
     * @param {Object} patentsData - The patents data.
     * @returns {HTMLElement} The created content element.
     */
    function createPatentContent(patentsData) {
        const content = document.createElement('div');
        
        const subtitle = document.createElement('h2');
        subtitle.textContent = 'Patents Granted';
        subtitle.style.color = '#444';
        content.appendChild(subtitle);

        if (!patentsData || !patentsData.years || !patentsData.counts) {
            content.appendChild(document.createTextNode('No patent data available.'));
            return content;
        }

        // Create a simple bar chart
        const chartContainer = document.createElement('div');
        chartContainer.style.height = '300px';
        chartContainer.style.display = 'flex';
        chartContainer.style.alignItems = 'flex-end';
        chartContainer.style.gap = '10px';
        chartContainer.style.marginTop = '20px';

        const maxCount = Math.max(...patentsData.counts);
        
        patentsData.years.forEach((year, index) => {
            const barContainer = document.createElement('div');
            barContainer.style.display = 'flex';
            barContainer.style.flexDirection = 'column';
            barContainer.style.alignItems = 'center';
            
            const bar = document.createElement('div');
            const height = (patentsData.counts[index] / maxCount) * 250;
            bar.style.height = `${height}px`;
            bar.style.width = '40px';
            bar.style.backgroundColor = '#8a2be2';
            bar.style.borderRadius = '3px 3px 0 0';
            
            const label = document.createElement('div');
            label.textContent = year;
            label.style.marginTop = '5px';
            label.style.fontSize = '12px';
            
            barContainer.appendChild(bar);
            barContainer.appendChild(label);
            chartContainer.appendChild(barContainer);
        });

        content.appendChild(chartContainer);

        // Add summary
        const summary = document.createElement('p');
        summary.textContent = `MIT has been granted ${patentsData.total} patents from ${patentsData.years[0]} to ${patentsData.years[patentsData.years.length - 1]}.`;
        summary.style.marginTop = '20px';
        content.appendChild(summary);

        return content;
    }

    /**
     * Creates the startups visualization content.
     * @param {Object} startupsData - The startups data.
     * @returns {HTMLElement} The created content element.
     */
    function createStartupContent(startupsData) {
        const content = document.createElement('div');
        
        const subtitle = document.createElement('h2');
        subtitle.textContent = 'Startups Founded';
        subtitle.style.color = '#444';
        content.appendChild(subtitle);

        if (!startupsData || !startupsData.years || !startupsData.counts) {
            content.appendChild(document.createTextNode('No startup data available.'));
            return content;
        }

        // Create a simple line chart
        const chartContainer = document.createElement('div');
        chartContainer.style.height = '300px';
        chartContainer.style.position = 'relative';
        chartContainer.style.marginTop = '20px';

        const canvas = document.createElement('canvas');
        canvas.width = chartContainer.offsetWidth;
        canvas.height = 300;
        chartContainer.appendChild(canvas);

        // Draw the line chart
        const ctx = canvas.getContext('2d');
        const maxCount = Math.max(...startupsData.counts);
        const step = canvas.width / (startupsData.years.length - 1);
        
        ctx.beginPath();
        ctx.strokeStyle = '#ff7f50';
        ctx.lineWidth = 3;
        
        startupsData.years.forEach((year, index) => {
            const x = index * step;
            const y = canvas.height - (startupsData.counts[index] / maxCount) * (canvas.height - 40);
            
            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
            
            // Add points
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2);
            ctx.fillStyle = '#ff7f50';
            ctx.fill();
            
            // Add year labels
            ctx.fillStyle = '#666';
            ctx.font = '10px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(year, x, canvas.height - 10);
        });
        
        ctx.stroke();

        content.appendChild(chartContainer);
