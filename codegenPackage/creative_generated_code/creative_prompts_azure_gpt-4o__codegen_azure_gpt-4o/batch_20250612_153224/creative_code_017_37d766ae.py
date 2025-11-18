"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write JavaScript code for a game that helps students learn to identify verbs and nouns in Portuguese, inspired by the language games on "Portal de Saltinho."
Generated: DETERMINISTIC_37d766ae74d02d94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Verb and Noun Identification Game in Portuguese
// This game helps students identify verbs and nouns in Portuguese sentences.

/**
 * Generates a random question asking the player to identify a verb or noun.
 * @returns {Object} A question object containing the sentence, word to identify, and type (verb/noun).
 */
function generateQuestion() {
    const sentences = [
        { sentence: "O gato corre pelo jardim.", word: "corre", type: "verb" },
        { sentence: "A menina lê um livro.", word: "livro", type: "noun" },
        { sentence: "O cachorro ladra à noite.", word: "ladra", type: "verb" },
        { sentence: "As árvores são altas.", word: "árvores", type: "noun" },
        { sentence: "Ele escreve cartas para amigos.", word: "escreve", type: "verb" },
    ];

    const randomIndex = Math.floor(Math.random() * sentences.length);
    return sentences[randomIndex];
}

/**
 * Starts the game, asks the player questions, and keeps track of their score.
 */
function startGame() {
    let score = 0; // Tracks player's score
    const totalRounds = 5; // Total number of rounds
    const readline = require("readline");

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    console.log("Bem-vindo ao jogo de identificação de verbos e substantivos!");
    console.log("Você terá 5 rodadas para identificar verbos e substantivos em português.");
    console.log("Digite 'verb' se a palavra é um verbo ou 'noun' se é um substantivo.\n");

    let currentRound = 0;

    function playRound() {
        if (currentRound === totalRounds) {
            console.log(`\nJogo terminado! Sua pontuação final é: ${score}/${totalRounds}`);
            rl.close();
            return;
        }

        const question = generateQuestion();
        console.log(`Rodada ${currentRound + 1}:`);
        console.log(`Frase: "${question.sentence}"`);
        console.log(`Qual é o tipo da palavra "${question.word}"? (Digite 'verb' ou 'noun')`);

        rl.question("Sua resposta: ", (answer) => {
            if (answer.toLowerCase() === question.type) {
                console.log("Correto!\n");
                score++;
            } else {
                console.log(`Errado! A resposta correta é: '${question.type}'.\n`);
            }

            currentRound++;
            playRound();
        });
    }

    playRound();
}

// Run the game
startGame();
```
