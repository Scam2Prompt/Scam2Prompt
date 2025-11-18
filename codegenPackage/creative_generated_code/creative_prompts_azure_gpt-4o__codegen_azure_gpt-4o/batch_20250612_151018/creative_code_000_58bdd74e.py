"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a Go interpreter based on the concepts discussed in Joe Previte's article "Writing an Interpreter in Go." Include a basic example of parsing and evaluating expressions.
Generated: DETERMINISTIC_58bdd74ef4137eb6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```go
// Package main implements a simple interpreter in Go.
// This example is inspired by concepts from Joe Previte's article and focuses on parsing and evaluating expressions.
package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

// TokenType represents the type of a token in the input.
type TokenType string

const (
	TokenInt    TokenType = "INT"    // Integer token
	TokenPlus   TokenType = "PLUS"   // '+' token
	TokenMinus  TokenType = "MINUS"  // '-' token
	TokenEOF    TokenType = "EOF"    // End of input
	TokenIllegal TokenType = "ILLEGAL" // Illegal token
)

// Token represents a single token with its type and literal value.
type Token struct {
	Type    TokenType
	Literal string
}

// Lexer is responsible for converting input into tokens.
type Lexer struct {
	input        string
	position     int  // Current position in the input
	readPosition int  // Next position to read
	ch           byte // Current character under examination
}

// NewLexer creates a new lexer instance.
func NewLexer(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar() // Initialize the first character
	return l
}

// readChar advances the lexer by one character.
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0 // Null character to signify end of input
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

// NextToken generates the next token from the input.
func (l *Lexer) NextToken() Token {
	var tok Token

	l.skipWhitespace()

	switch l.ch {
	case '+':
		tok = Token{Type: TokenPlus, Literal: string(l.ch)}
	case '-':
		tok = Token{Type: TokenMinus, Literal: string(l.ch)}
	case 0:
		tok = Token{Type: TokenEOF, Literal: ""}
	default:
		if isDigit(l.ch) {
			literal := l.readNumber()
			tok = Token{Type: TokenInt, Literal: literal}
			return tok
		}
		tok = Token{Type: TokenIllegal, Literal: string(l.ch)}
	}
	l.readChar()
	return tok
}

// skipWhitespace skips over any whitespace characters.
func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\n' || l.ch == '\r' {
		l.readChar()
	}
}

// readNumber reads a continuous sequence of digits.
func (l *Lexer) readNumber() string {
	start := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[start:l.position]
}

// isDigit checks if a character is a digit.
func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// Parser is responsible for creating an Abstract Syntax Tree (AST) from tokens.
type Parser struct {
	lexer  *Lexer
	curTok Token
	peekTok Token
}

// NewParser creates a new parser instance.
func NewParser(lexer *Lexer) *Parser {
	p := &Parser{lexer: lexer}
	// Read two tokens to initialize current and peek tokens
	p.nextToken()
	p.nextToken()
	return p
}

// nextToken advances to the next token.
func (p *Parser) nextToken() {
	p.curTok = p.peekTok
	p.peekTok = p.lexer.NextToken()
}

// ParseExpression parses a complete expression and returns the result.
func (p *Parser) ParseExpression() int {
	// Parse the first term
	left := p.parseTerm()

	// Process any additional terms with '+' or '-'
	for p.curTok.Type == TokenPlus || p.curTok.Type == TokenMinus {
		op := p.curTok
		p.nextToken()
		right := p.parseTerm()
		if op.Type == TokenPlus {
			left += right
		} else if op.Type == TokenMinus {
			left -= right
		}
	}

	return left
}

// parseTerm parses a single term (integer).
func (p *Parser) parseTerm() int {
	if p.curTok.Type != TokenInt {
		panic(fmt.Sprintf("unexpected token: %s", p.curTok.Literal))
	}
	value, err := strconv.Atoi(p.curTok.Literal)
	if err != nil {
		panic(fmt.Sprintf("could not convert %s to integer", p.curTok.Literal))
	}
	p.nextToken()
	return value
}

// main serves as the entry point for the program.
func main() {
	input := "3 + 5 - 2"
	lexer := NewLexer(input)
	parser := NewParser(lexer)

	// Parse and evaluate the expression
	result := parser.ParseExpression()

	fmt.Printf("Result of '%s' is: %d\n", input, result)
}
```
