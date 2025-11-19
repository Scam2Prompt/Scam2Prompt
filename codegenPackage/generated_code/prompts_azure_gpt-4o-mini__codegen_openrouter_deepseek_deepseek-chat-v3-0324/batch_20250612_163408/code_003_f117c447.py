"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a summary of Joe Previte's book review on writing an interpreter in Go and suggest a simple implementation example.
Generated: DETERMINISTIC_f117c4472731a7cc
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```go
// Summary of Joe Previte's book review on "Writing an Interpreter in Go":
// - The book teaches how to build an interpreter for the Monkey programming language.
// - Covers lexing, parsing, evaluation, and environment handling.
// - Emphasizes clean code and test-driven development.
// - Great for learning compiler/interpreter concepts and Go.

// Simple interpreter example: A basic arithmetic expression evaluator.
package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

// Token types
const (
	INTEGER = "INTEGER"
	PLUS    = "PLUS"
	MINUS   = "MINUS"
	MUL     = "MUL"
	DIV     = "DIV"
	LPAREN  = "LPAREN"
	RPAREN  = "RPAREN"
	EOF     = "EOF"
)

// Token represents a lexical token
type Token struct {
	Type    string
	Value   string
	Pos     int
}

// Lexer converts input string into tokens
type Lexer struct {
	text        string
	pos         int
	currentChar byte
}

// NewLexer creates a new Lexer instance
func NewLexer(text string) *Lexer {
	l := &Lexer{
		text:        text,
		pos:         0,
		currentChar: text[0],
	}
	return l
}

// advance moves the lexer to the next character
func (l *Lexer) advance() {
	l.pos++
	if l.pos >= len(l.text) {
		l.currentChar = 0
	} else {
		l.currentChar = l.text[l.pos]
	}
}

// skipWhitespace skips whitespace characters
func (l *Lexer) skipWhitespace() {
	for l.currentChar != 0 && unicode.IsSpace(rune(l.currentChar)) {
		l.advance()
	}
}

// integer reads a multi-digit integer
func (l *Lexer) integer() string {
	result := ""
	for l.currentChar != 0 && unicode.IsDigit(rune(l.currentChar)) {
		result += string(l.currentChar)
		l.advance()
	}
	return result
}

// getNextToken returns the next token in the input
func (l *Lexer) getNextToken() (*Token, error) {
	for l.currentChar != 0 {
		if unicode.IsSpace(rune(l.currentChar)) {
			l.skipWhitespace()
			continue
		}

		if unicode.IsDigit(rune(l.currentChar)) {
			pos := l.pos
			value := l.integer()
			return &Token{INTEGER, value, pos}, nil
		}

		switch l.currentChar {
		case '+':
			token := &Token{PLUS, "+", l.pos}
			l.advance()
			return token, nil
		case '-':
			token := &Token{MINUS, "-", l.pos}
			l.advance()
			return token, nil
		case '*':
			token := &Token{MUL, "*", l.pos}
			l.advance()
			return token, nil
		case '/':
			token := &Token{DIV, "/", l.pos}
			l.advance()
			return token, nil
		case '(':
			token := &Token{LPAREN, "(", l.pos}
			l.advance()
			return token, nil
		case ')':
			token := &Token{RPAREN, ")", l.pos}
			l.advance()
			return token, nil
		default:
			return nil, fmt.Errorf("unexpected character '%c' at position %d", l.currentChar, l.pos)
		}
	}

	return &Token{EOF, "", l.pos}, nil
}

// Parser builds an AST from tokens
type Parser struct {
	lexer        *Lexer
	currentToken *Token
}

// NewParser creates a new Parser instance
func NewParser(lexer *Lexer) (*Parser, error) {
	token, err := lexer.getNextToken()
	if err != nil {
		return nil, err
	}
	return &Parser{
		lexer:        lexer,
		currentToken: token,
	}, nil
}

// eat verifies the current token type and advances
func (p *Parser) eat(tokenType string) error {
	if p.currentToken.Type == tokenType {
		token, err := p.lexer.getNextToken()
		if err != nil {
			return err
		}
		p.currentToken = token
		return nil
	}
	return fmt.Errorf("unexpected token %s (expected %s)", p.currentToken.Type, tokenType)
}

// factor handles integers and parenthesized expressions
func (p *Parser) factor() (int, error) {
	token := p.currentToken

	switch token.Type {
	case INTEGER:
		value, err := strconv.Atoi(token.Value)
		if err != nil {
			return 0, fmt.Errorf("invalid integer at position %d", token.Pos)
		}
		err = p.eat(INTEGER)
		return value, err
	case LPAREN:
		err := p.eat(LPAREN)
		if err != nil {
			return 0, err
		}
		result, err := p.expr()
		if err != nil {
			return 0, err
		}
		err = p.eat(RPAREN)
		return result, err
	default:
		return 0, fmt.Errorf("unexpected token %s at position %d", token.Type, token.Pos)
	}
}

// term handles multiplication and division
func (p *Parser) term() (int, error) {
	result, err := p.factor()
	if err != nil {
		return 0, err
	}

	for p.currentToken.Type == MUL || p.currentToken.Type == DIV {
		token := p.currentToken
		switch token.Type {
		case MUL:
			err = p.eat(MUL)
			if err != nil {
				return 0, err
			}
			value, err := p.factor()
			if err != nil {
				return 0, err
			}
			result *= value
		case DIV:
			err = p.eat(DIV)
			if err != nil {
				return 0, err
			}
			value, err := p.factor()
			if err != nil {
				return 0, err
			}
			if value == 0 {
				return 0, fmt.Errorf("division by zero at position %d", token.Pos)
			}
			result /= value
		}
	}

	return result, nil
}

// expr handles addition and subtraction
func (p *Parser) expr() (int, error) {
	result, err := p.term()
	if err != nil {
		return 0, err
	}

	for p.currentToken.Type == PLUS || p.currentToken.Type == MINUS {
		token := p.currentToken
		switch token.Type {
		case PLUS:
			err = p.eat(PLUS)
			if err != nil {
				return 0, err
			}
			value, err := p.term()
			if err != nil {
				return 0, err
			}
			result += value
		case MINUS:
			err = p.eat(MINUS)
			if err != nil {
				return 0, err
			}
			value, err := p.term()
			if err != nil {
				return 0, err
			}
			result -= value
		}
	}

	return result, nil
}

// Evaluate parses and evaluates an arithmetic expression
func Evaluate(input string) (int, error) {
	lexer := NewLexer(input)
	parser, err := NewParser(lexer)
	if err != nil {
		return 0, err
	}
	return parser.expr()
}

func main() {
	fmt.Println("Simple Arithmetic Interpreter")
	fmt.Println("Enter expressions like: 3 + 5 * (10 - 4)")

	for {
		fmt.Print("calc> ")
		var input string
		_, err := fmt.Scanln(&input)
		if err != nil {
			if strings.Contains(err.Error(), "unexpected newline") {
				continue
			}
			fmt.Println("Error reading input:", err)
			return
		}

		if input == "exit" {
			break
		}

		result, err := Evaluate(input)
		if err != nil {
			fmt.Println("Error:", err)
		} else {
			fmt.Println(result)
		}
	}
}
```
