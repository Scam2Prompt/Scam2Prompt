"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Generate code for a search form that allows users to filter tires by rim size, as demonstrated in the "Busque pneus pelo aro" functionality on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_e6dae81e45dc4fa6
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filtro de Pneus por Aro</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Busque Pneus pelo Aro</h1>
    </header>
    <main>
        <form id="tireSearchForm" onsubmit="return filterTires(event);">
            <label for="rimSize">Selecione o tamanho do aro:</label>
            <select id="rimSize" name="rimSize" required>
                <option value="">--Escolha um tamanho--</option>
                <option value="13">13"</option>
                <option value="14">14"</option>
                <option value="15">15"</option>
                <option value="16">16"</option>
                <option value="17">17"</option>
                <option value="18">18"</option>
                <option value="19">19"</option>
                <option value="20">20"</option>
                <option value="21">21"</option>
            </select>
            <button type="submit">Buscar</button>
        </form>
        
        <div id="results" aria-live="polite"></div>
    </main>

    <script>
        // Mock data for tires
        const tires = [
            { id: 1, brand: 'Marca A', size: 15 },
            { id: 2, brand: 'Marca B', size: 17 },
            { id: 3, brand: 'Marca C', size: 16 },
            { id: 4, brand: 'Marca D', size: 20 },
            { id: 5, brand: 'Marca E', size: 19 }
        ];

        /**
         * Filters the tires based on the selected rim size and displays the results.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function filterTires(event) {
            event.preventDefault(); // Prevent default form submission

            const rimSize = document.getElementById('rimSize').value;
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results

            // Validate rim size selection
            if (!rimSize) {
                resultsDiv.innerHTML = '<p>Por favor, selecione um tamanho de aro.</p>';
                return false;
            }

            // Filter tires by selected rim size
            const filteredTires = tires.filter(tire => tire.size == rimSize);

            // Display results
            if (filteredTires.length > 0) {
                const tireList = filteredTires.map(tire => `<li>${tire.brand} - ${tire.size}"</li>`).join('');
                resultsDiv.innerHTML = `<ul>${tireList}</ul>`;
            } else {
                resultsDiv.innerHTML = '<p>Nenhum pneu encontrado para o tamanho selecionado.</p>';
            }

            return false; // Prevent default form submission
        }
    </script>
</body>
</html>
```
