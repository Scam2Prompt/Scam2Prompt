"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a summary of Joe Previte's book review on writing an interpreter in Go and suggest a simple implementation example.
Generated: DETERMINISTIC_f117c4472731a7cc
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Token types
const (
	EOF     = "EOF"
	ILLEGAL = "ILLEGAL"
	INT     = "INT"
	PLUS    = "+"
	MINUS   = "-"
)

// Token represents a basic unit in the interpreter
type Token struct {
	Type    string
	Literal string
}

// Lexer converts input into tokens
type Lexer struct {
	input        string
	position     int  // current position in input
	readPosition int  // next position in input
	ch           byte // current character being examined
}

// NewLexer initializes a new Lexer with the input
func NewLexer(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar() // initialize the first character
	return l
}

// readChar advances the position in the input and reads the next character
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0 // 0 represents EOF
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

// NextToken returns the next token in the input
func (l *Lexer) NextToken() Token {
	var tok Token

	// Skip whitespaces
	l.skipWhitespace()

	switch l.ch {
	case '+':
		tok = Token{Type: PLUS, Literal: string(l.ch)}
	case '-':
		tok = Token{Type: MINUS, Literal: string(l.ch)}
	case 0:
		tok = Token{Type: EOF, Literal: ""}
	default:
		// Check if it's an integer
		if isDigit(l.ch) {
			tok.Literal = l.readNumber()
			tok.Type = INT
			return tok
		} else {
			tok = Token{Type: ILLEGAL, Literal: string(l.ch)}
		}
	}

	l.readChar() // Advance to the next character
	return tok
}

// readNumber reads a sequence of digits to form a complete integer token
func (l *Lexer) readNumber() string {
	position := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]
}

// skipWhitespace skips over spaces, tabs, and newlines
func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\n' || l.ch == '\r' {
		l.readChar()
	}
}

// isDigit checks if a character is a digit
func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// Evaluator processes the tokens and performs calculations
func Evaluator(input string) (int, error) {
	lexer := NewLexer(input)
	var result int
	var currentOp string

	// Evaluate tokens one by one
	for tok := lexer.NextToken(); tok.Type != EOF; tok = lexer.NextToken() {
		switch tok.Type {
		case INT:
			// Convert string to integer
			value := 0
			fmt.Sscanf(tok.Literal, "%d", &value)

			// Apply the current operation
			if currentOp == "+" {
				result += value
			} else if currentOp == "-" {
				result -= value
			} else {
				// Default to initial number (no operator yet)
				result = value
			}
		case PLUS:
			currentOp = "+"
		case MINUS:
			currentOp = "-"
		case ILLEGAL:
			return 0, fmt.Errorf("illegal character: %s", tok.Literal)
		}
	}

	return result, nil
}

func main() {
	// Display instructions to the user
	fmt.Println("Simple Interpreter in Go")
	fmt.Println("Enter an expression with integers and + or - operators (e.g., '5 + 3 - 2'). Type 'exit' to quit.")

	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print(">> ")
		scanner.Scan()

		// Read user input
		input := strings.TrimSpace(scanner.Text())

		if input == "exit" {
			fmt.Println("Goodbye!")
			break
		}

		// Evaluate the expression
		result, err := Evaluator(input)
		if err != nil {
			fmt.Printf("Error: %s\n", err)
		} else {
			fmt.Printf("Result: %d\n", result)
		}
	}
}
```
