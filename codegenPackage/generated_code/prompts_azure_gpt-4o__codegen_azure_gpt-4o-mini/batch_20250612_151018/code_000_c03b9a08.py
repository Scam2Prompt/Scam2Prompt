"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a Go interpreter based on the concepts discussed in Joe Previte's article "Writing an Interpreter in Go." Include a simple example of parsing and evaluating expressions.
Generated: DETERMINISTIC_c03b9a0807b21079
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// TokenType represents the type of token in the input.
type TokenType int

const (
	EOF TokenType = iota
	NUMBER
	PLUS
	MINUS
)

// Token represents a single token in the input.
type Token struct {
	Type  TokenType
	Value string
}

// Lexer is responsible for tokenizing the input string.
type Lexer struct {
	input        string
	position     int
	currentChar byte
}

// NewLexer creates a new Lexer instance.
func NewLexer(input string) *Lexer {
	lexer := &Lexer{input: input, position: 0}
	lexer.currentChar = lexer.input[lexer.position]
	return lexer
}

// NextToken returns the next token from the input.
func (l *Lexer) NextToken() Token {
	for l.currentChar != 0 {
		if l.currentChar == ' ' {
			l.skipWhitespace()
			continue
		}
		if isDigit(l.currentChar) {
			return Token{Type: NUMBER, Value: l.number()}
		}
		if l.currentChar == '+' {
			l.advance()
			return Token{Type: PLUS, Value: "+"}
		}
		if l.currentChar == '-' {
			l.advance()
			return Token{Type: MINUS, Value: "-"}
		}
		l.error("Invalid character")
	}
	return Token{Type: EOF, Value: ""}
}

// skipWhitespace skips over whitespace characters.
func (l *Lexer) skipWhitespace() {
	for l.currentChar == ' ' {
		l.advance()
	}
}

// number returns a multi-digit number as a string.
func (l *Lexer) number() string {
	start := l.position
	for isDigit(l.currentChar) {
		l.advance()
	}
	return l.input[start:l.position]
}

// advance moves the lexer to the next character.
func (l *Lexer) advance() {
	l.position++
	if l.position >= len(l.input) {
		l.currentChar = 0
	} else {
		l.currentChar = l.input[l.position]
	}
}

// isDigit checks if a character is a digit.
func isDigit(ch byte) bool {
	return ch >= '0' && ch <= '9'
}

// error handles lexer errors.
func (l *Lexer) error(msg string) {
	fmt.Fprintf(os.Stderr, "Lexer error: %s\n", msg)
	os.Exit(1)
}

// Interpreter evaluates the expression.
type Interpreter struct {
	lexer  *Lexer
	currentToken Token
}

// NewInterpreter creates a new Interpreter instance.
func NewInterpreter(lexer *Lexer) *Interpreter {
	return &Interpreter{lexer: lexer}
}

// Eat consumes the current token if it matches the expected type.
func (i *Interpreter) Eat(tokenType TokenType) {
	if i.currentToken.Type == tokenType {
		i.currentToken = i.lexer.NextToken()
	} else {
		i.error("Unexpected token")
	}
}

// Expr evaluates an expression.
func (i *Interpreter) Expr() int {
	i.currentToken = i.lexer.NextToken()

	result := i.Term()

	for i.currentToken.Type == PLUS || i.currentToken.Type == MINUS {
		if i.currentToken.Type == PLUS {
			i.Eat(PLUS)
			result += i.Term()
		} else if i.currentToken.Type == MINUS {
			i.Eat(MINUS)
			result -= i.Term()
		}
	}

	return result
}

// Term evaluates a term (in this simple case, just a number).
func (i *Interpreter) Term() int {
	token := i.currentToken
	i.Eat(NUMBER)
	value, err := strconv.Atoi(token.Value)
	if err != nil {
		i.error("Invalid number")
	}
	return value
}

// error handles interpreter errors.
func (i *Interpreter) error(msg string) {
	fmt.Fprintf(os.Stderr, "Interpreter error: %s\n", msg)
	os.Exit(1)
}

// main function to run the interpreter.
func main() {
	input := "3 + 5 - 2"
	lexer := NewLexer(input)
	interpreter := NewInterpreter(lexer)

	result := interpreter.Expr()
	fmt.Printf("Result: %d\n", result)
}
```
