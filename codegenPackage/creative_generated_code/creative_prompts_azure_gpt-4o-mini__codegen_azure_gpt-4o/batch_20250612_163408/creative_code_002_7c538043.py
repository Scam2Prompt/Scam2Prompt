"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Explain how to write an interpreter in Go, incorporating insights from Joe Previte's book review on the subject.
Generated: DETERMINISTIC_7c5380432831b98f
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
	"strconv"
	"strings"
)

// Token defines a structure for individual tokens in the input
type Token struct {
	Type    string
	Literal string
}

// Constants for token types
const (
	TokenTypeInt       = "INT"
	TokenTypePlus      = "PLUS"
	TokenTypeMinus     = "MINUS"
	TokenTypeEOF       = "EOF"
	TokenTypeIllegal   = "ILLEGAL"
	TokenTypeWhitespace = "WHITESPACE"
)

// Lexer is responsible for tokenizing the input string
type Lexer struct {
	input        string
	position     int
	readPosition int
	ch           byte
}

// NewLexer initializes a new Lexer instance
func NewLexer(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

// readChar reads the next character and advances the position
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0 // End of file
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

// NextToken parses the next token from the input
func (l *Lexer) NextToken() Token {
	var tok Token

	switch l.ch {
	case '+':
		tok = Token{Type: TokenTypePlus, Literal: string(l.ch)}
	case '-':
		tok = Token{Type: TokenTypeMinus, Literal: string(l.ch)}
	case 0:
		tok = Token{Type: TokenTypeEOF, Literal: ""}
	default:
		if isDigit(l.ch) {
			tok = Token{Type: TokenTypeInt, Literal: l.readNumber()}
			return tok
		} else if isWhitespace(l.ch) {
			l.readChar()
			return l.NextToken()
		} else {
			tok = Token{Type: TokenTypeIllegal, Literal: string(l.ch)}
		}
	}
	l.readChar()
	return tok
}

// readNumber reads a full integer token
func (l *Lexer) readNumber() string {
	start := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[start:l.position]
}

// isDigit checks whether a character is numeric
func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// isWhitespace checks whether a character is a whitespace
func isWhitespace(ch byte) bool {
	return ch == ' ' || ch == '\t' || ch == '\n'
}

// Interpreter evaluates the tokens and performs calculations
type Interpreter struct{}

// Eval parses and calculates the result based on tokens
func (i *Interpreter) Eval(input string) (int, error) {
	lexer := NewLexer(input)
	var result int
	var operator string

	// Process tokens one by one
	for {
		tok := lexer.NextToken()
		switch tok.Type {
		case TokenTypeInt:
			value, err := strconv.Atoi(tok.Literal)
			if err != nil {
				return 0, fmt.Errorf("invalid number: %s", tok.Literal)
			}
			if operator == "" {
				result = value
			} else {
				switch operator {
				case "+":
					result += value
				case "-":
					result -= value
				default:
					return 0, fmt.Errorf("unsupported operator: %s", operator)
				}
			}
		case TokenTypePlus, TokenTypeMinus:
			operator = tok.Literal
		case TokenTypeEOF:
			return result, nil
		case TokenTypeIllegal:
			return 0, fmt.Errorf("illegal token: %s", tok.Literal)
		}
	}
}

// main is the entry point of the program
func main() {
	scanner := bufio.NewScanner(os.Stdin)
	interpreter := &Interpreter{}

	fmt.Println("Welcome to the Go Interpreter!")
	fmt.Println("Enter expressions using integers and '+' or '-' operators, or 'exit' to quit.")

	for {
		fmt.Print("> ")
		scanner.Scan()
		input := scanner.Text()

		if strings.TrimSpace(input) == "exit" {
			fmt.Println("Goodbye!")
			break
		}

		result, err := interpreter.Eval(input)
		if err != nil {
			fmt.Printf("Error: %v\n", err)
		} else {
			fmt.Printf("Result: %d\n", result)
		}
	}
}
```
