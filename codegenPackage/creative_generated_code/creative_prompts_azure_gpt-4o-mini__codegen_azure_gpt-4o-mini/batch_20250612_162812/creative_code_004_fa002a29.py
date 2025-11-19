"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newhomepoocoin.blogspot.com
Prompt: Construct a simple HTML form that allows users to search for "sandalias femininas" and "chuteira" on the Vanusa Sapato Infantil site.
Generated: DETERMINISTIC_fa002a2927ab4c1a
Batch ID: 20250612_162812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.vanusashop.com.br/search": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pesquisa de Calçados - Vanusa Sapato Infantil</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>

    <header>
        <h1>Pesquisa de Calçados</h1>
        <p>Encontre as melhores opções de sandálias femininas e chuteiras.</p>
    </header>

    <main>
        <form id="searchForm" action="https://www.vanusashop.com.br/search" method="GET">
            <label for="searchTerm">Buscar:</label>
            <input type="text" id="searchTerm" name="q" placeholder="Digite 'sandalias femininas' ou 'chuteira'" required>
            
            <button type="submit">Pesquisar</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Vanusa Sapato Infantil. Todos os direitos reservados.</p>
    </footer>

    <script>
        // Add an event listener to handle form submission
        document.getElementById('searchForm').addEventListener('submit', function(event) {
            const searchTerm = document.getElementById('searchTerm').value.trim();
            const validTerms = ['sandalias femininas', 'chuteira'];

            // Check if the search term is valid
            if (!validTerms.includes(searchTerm)) {
                // Prevent form submission and show an error message
                event.preventDefault();
                alert('Por favor, insira um termo de busca válido: "sandalias femininas" ou "chuteira".');
            }
        });
    </script>

</body>
</html>
```
