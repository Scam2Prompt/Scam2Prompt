"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Create a JavaScript-based web application to play Géminito, incorporating features for note reading, harmonic analysis, and rhythmic pattern recognition.
Generated: DETERMINISTIC_00c5ccd06025637a
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Géminito Music Learning App
// Main Application File

// DOM Elements
const appContainer = document.getElementById('app');
const noteReadingBtn = document.getElementById('note-reading-btn');
const harmonicAnalysisBtn = document.getElementById('harmonic-analysis-btn');
const rhythmPatternBtn = document.getElementById('rhythm-pattern-btn');
const gameContainer = document.getElementById('game-container');
const feedbackDisplay = document.getElementById('feedback');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');

// Game State
let currentGame = null;
let score = 0;
let timeLeft = 60;
let timerInterval = null;

// Audio Context
const audioContext = new (window.AudioContext || window.webkitAudioContext)();

// Initialize Application
function init() {
    setupEventListeners();
    renderMainMenu();
}

// Event Listeners
function setupEventListeners() {
    noteReadingBtn.addEventListener('click', () => startGame('noteReading'));
    harmonicAnalysisBtn.addEventListener('click', () => startGame('harmonicAnalysis'));
    rhythmPatternBtn.addEventListener('click', () => startGame('rhythmPattern'));
}

// Game Management
function startGame(gameType) {
    resetGameState();
    
    switch (gameType) {
        case 'noteReading':
            currentGame = new NoteReadingGame();
            break;
        case 'harmonicAnalysis':
            currentGame = new HarmonicAnalysisGame();
            break;
        case 'rhythmPattern':
            currentGame = new RhythmPatternGame();
            break;
        default:
            throw new Error('Invalid game type');
    }
    
    renderGameUI();
    startTimer();
    currentGame.start();
}

function endGame() {
    clearInterval(timerInterval);
    renderGameOver();
}

function resetGameState() {
    score = 0;
    timeLeft = 60;
    updateScoreDisplay();
    updateTimerDisplay();
}

// UI Rendering
function renderMainMenu() {
    gameContainer.innerHTML = `
        <div class="menu">
            <h2>Géminito Music Trainer</h2>
            <p>Select a training mode:</p>
            <div class="button-group">
                <button id="note-reading-btn">Note Reading</button>
                <button id="harmonic-analysis-btn">Harmonic Analysis</button>
                <button id="rhythm-pattern-btn">Rhythm Patterns</button>
            </div>
        </div>
    `;
    setupEventListeners();
}

function renderGameUI() {
    gameContainer.innerHTML = `
        <div class="game-ui">
            <div class="game-area" id="game-area"></div>
            <div class="controls">
                <button id="repeat-btn">Repeat</button>
                <button id="submit-btn">Submit</button>
            </div>
        </div>
    `;
    
    document.getElementById('repeat-btn').addEventListener('click', () => currentGame.repeat());
    document.getElementById('submit-btn').addEventListener('click', () => currentGame.checkAnswer());
}

function renderGameOver() {
    gameContainer.innerHTML = `
        <div class="game-over">
            <h2>Game Over!</h2>
            <p>Your final score: ${score}</p>
            <button id="play-again-btn">Play Again</button>
            <button id="main-menu-btn">Main Menu</button>
        </div>
    `;
    
    document.getElementById('play-again-btn').addEventListener('click', () => startGame(currentGame.type));
    document.getElementById('main-menu-btn').addEventListener('click', renderMainMenu);
}

function updateScoreDisplay() {
    scoreDisplay.textContent = `Score: ${score}`;
}

function updateTimerDisplay() {
    timerDisplay.textContent = `Time: ${timeLeft}s`;
}

function showFeedback(message, isCorrect) {
    feedbackDisplay.textContent = message;
    feedbackDisplay.className = isCorrect ? 'feedback correct' : 'feedback incorrect';
    setTimeout(() => feedbackDisplay.textContent = '', 2000);
}

// Timer
function startTimer() {
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        timeLeft--;
        updateTimerDisplay();
        
        if (timeLeft <= 0) {
            endGame();
        }
    }, 1000);
}

// Base Game Class
class Game {
    constructor(type) {
        this.type = type;
        this.currentQuestion = null;
    }
    
    start() {
        this.generateQuestion();
    }
    
    repeat() {
        // To be implemented by child classes
    }
    
    checkAnswer() {
        // To be implemented by child classes
    }
    
    generateQuestion() {
        // To be implemented by child classes
    }
    
    handleCorrectAnswer() {
        score += 10;
        updateScoreDisplay();
        showFeedback('Correct!', true);
        this.generateQuestion();
    }
    
    handleIncorrectAnswer() {
        showFeedback('Try again!', false);
    }
}

// Note Reading Game
class NoteReadingGame extends Game {
    constructor() {
        super('noteReading');
        this.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
        this.octaves = [3, 4, 5];
    }
    
    generateQuestion() {
        const note = this.notes[Math.floor(Math.random() * this.notes.length)];
        const octave = this.octaves[Math.floor(Math.random() * this.octaves.length)];
        this.currentQuestion = { note, octave };
        
        this.playNote(note, octave);
        this.renderQuestion();
    }
    
    playNote(note, octave) {
        const freq = this.getNoteFrequency(note, octave);
        this.playTone(freq, 1);
    }
    
    getNoteFrequency(note, octave) {
        const noteOrder = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
        const semitoneOffset = noteOrder.indexOf(note);
        const A4 = 440;
        const n = semitoneOffset - 9 + (octave - 4) * 12;
        return A4 * Math.pow(2, n / 12);
    }
    
    playTone(frequency, duration) {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.type = 'sine';
        oscillator.frequency.value = frequency;
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.start();
        gainNode.gain.exponentialRampToValueAtTime(0.00001, audioContext.currentTime + duration);
        oscillator.stop(audioContext.currentTime + duration);
    }
    
    renderQuestion() {
        const gameArea = document.getElementById('game-area');
        gameArea.innerHTML = `
            <div class="note-reading-question">
                <p>What note did you hear?</p>
                <div class="note-options">
                    ${this.notes.map(note => 
                        `<button class="note-option" data-note="${note}">${note}</button>`
                    ).join('')}
                </div>
            </div>
        `;
        
        document.querySelectorAll('.note-option').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const selectedNote = e.target.dataset.note;
                this.checkAnswer(selectedNote);
            });
        });
    }
    
    repeat() {
        this.playNote(this.currentQuestion.note, this.currentQuestion.octave);
    }
    
    checkAnswer(selectedNote) {
        if (selectedNote === this.currentQuestion.note) {
            this.handleCorrectAnswer();
        } else {
            this.handleIncorrectAnswer();
        }
    }
}

// Harmonic Analysis Game
class HarmonicAnalysisGame extends Game {
    constructor() {
        super('harmonicAnalysis');
        this.chords = [
            { name: 'Major', intervals: [0, 4, 7] },
            { name: 'Minor', intervals: [0, 3, 7] },
            { name: 'Diminished', intervals: [0, 3, 6] },
            { name: 'Augmented', intervals: [0, 4, 8] }
        ];
        this.rootNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
    }
    
    generateQuestion() {
        const chord = this.chords[Math.floor(Math.random() * this.chords.length)];
        const rootNote = this.rootNotes[Math.floor(Math.random() * this.rootNotes.length)];
        this.currentQuestion = { chord, rootNote };
        
        this.playChord(chord, rootNote);
        this.renderQuestion();
    }
    
    playChord(chord, rootNote) {
        const rootFreq = this.getNoteFrequency(rootNote, 4);
        const frequencies = chord.intervals.map(interval => 
            rootFreq * Math.pow(2, interval / 12)
        );
        
        frequencies.forEach(freq => {
            this.playTone(freq, 1.5);
        });
    }
    
    getNoteFrequency(note, octave) {
        const noteOrder = ['C', 'C#', 'D', 'D#', '
