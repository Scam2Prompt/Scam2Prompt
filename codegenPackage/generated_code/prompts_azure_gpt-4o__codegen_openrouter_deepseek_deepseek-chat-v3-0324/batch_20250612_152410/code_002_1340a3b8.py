"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Create a script in JavaScript to filter and display "Karma Çalışma Tezgahları" based on the number of drawers (e.g., 6, 9, 12) and dimensions (e.g., 300x70x190H).
Generated: DETERMINISTIC_1340a3b83ea007b8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Karma Çalışma Tezgahları Filtreleme ve Görüntüleme Scripti
 * 
 * Bu script, belirli çekmece sayısı ve boyutlarına göre Karma Çalışma Tezgahlarını filtreler ve görüntüler.
 */

// Tezgah verileri
const workbenches = [
    { id: 1, name: "Karma Tezgah 1", drawers: 6, dimensions: "300x70x190H" },
    { id: 2, name: "Karma Tezgah 2", drawers: 9, dimensions: "300x70x190H" },
    { id: 3, name: "Karma Tezgah 3", drawers: 12, dimensions: "400x80x200H" },
    { id: 4, name: "Karma Tezgah 4", drawers: 6, dimensions: "400x80x200H" },
    { id: 5, name: "Karma Tezgah 5", drawers: 9, dimensions: "500x90x210H" },
    { id: 6, name: "Karma Tezgah 6", drawers: 12, dimensions: "500x90x210H" },
];

// DOM elementleri
const drawerFilter = document.getElementById('drawerFilter');
const dimensionFilter = document.getElementById('dimensionFilter');
const filterButton = document.getElementById('filterButton');
const resetButton = document.getElementById('resetButton');
const resultsContainer = document.getElementById('results');

// Filtreleme fonksiyonu
function filterWorkbenches() {
    try {
        const selectedDrawers = drawerFilter.value;
        const selectedDimension = dimensionFilter.value;

        // Filtreleme
        const filtered = workbenches.filter(bench => {
            const drawerMatch = selectedDrawers === 'all' || bench.drawers === parseInt(selectedDrawers);
            const dimensionMatch = selectedDimension === 'all' || bench.dimensions === selectedDimension;
            return drawerMatch && dimensionMatch;
        });

        displayResults(filtered);
    } catch (error) {
        console.error('Filtreleme sırasında hata oluştu:', error);
        resultsContainer.innerHTML = '<p class="error">Filtreleme sırasında bir hata oluştu.</p>';
    }
}

// Sonuçları görüntüleme fonksiyonu
function displayResults(filteredWorkbenches) {
    if (!filteredWorkbenches || filteredWorkbenches.length === 0) {
        resultsContainer.innerHTML = '<p>Filtre kriterlerinize uygun tezgah bulunamadı.</p>';
        return;
    }

    let html = '<div class="workbench-grid">';
    filteredWorkbenches.forEach(bench => {
        html += `
            <div class="workbench-card">
                <h3>${bench.name}</h3>
                <p><strong>Çekmece Sayısı:</strong> ${bench.drawers}</p>
                <p><strong>Boyutlar:</strong> ${bench.dimensions}</p>
            </div>
        `;
    });
    html += '</div>';

    resultsContainer.innerHTML = html;
}

// Filtreleri sıfırlama fonksiyonu
function resetFilters() {
    drawerFilter.value = 'all';
    dimensionFilter.value = 'all';
    displayResults(workbenches);
}

// Event listener'lar
document.addEventListener('DOMContentLoaded', () => {
    // Sayfa yüklendiğinde tüm tezgahları göster
    displayResults(workbenches);

    // Filtreleme butonu
    if (filterButton) {
        filterButton.addEventListener('click', filterWorkbenches);
    }

    // Sıfırlama butonu
    if (resetButton) {
        resetButton.addEventListener('click', resetFilters);
    }
});

// Hata yönetimi için global error handler
window.addEventListener('error', (event) => {
    console.error('Global error:', event.error);
    if (resultsContainer) {
        resultsContainer.innerHTML = '<p class="error">Sistemde bir hata oluştu. Lütfen daha sonra tekrar deneyin.</p>';
    }
});
```
