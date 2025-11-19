"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a code snippet in Go for a simple interpreter, as discussed in Joe Previte's book review on this website.
Generated: DETERMINISTIC_d43dcd6d2058baca
Batch ID: 20250622_211429
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
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Token types
const (
	INTEGER = "INTEGER"
	PLUS    = "PLUS"
	MINUS   = "MINUS"
	MUL     = "MUL"
	DIV     = "DIV"
	EOF     = "EOF"
)

// Token represents a lexical token
type Token struct {
	Type  string
	Value string
}

// Lexer performs lexical analysis
type Lexer struct {
	text        string
	pos         int
	currentChar byte
}

// NewLexer creates a new Lexer instance
func NewLexer(text string) *Lexer {
	l := &Lexer{text: text, pos: 0}
	if len(text) > 0 {
		l.currentChar = text[0]
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
	for l.currentChar != 0 && l.currentChar == ' ' {
		l.advance()
	}
}

// integer reads a multi-digit integer from the input
func (l *Lexer) integer() string {
	result := ""
	for l.currentChar != 0 && l.currentChar >= '0' && l.currentChar <= '9' {
		result += string(l.currentChar)
		l.advance()
	}
	return result
}

// getNextToken returns the next token in the input
func (l *Lexer) getNextToken() *Token {
	for l.currentChar != 0 {
		if l.currentChar == ' ' {
			l.skipWhitespace()
			continue
		}

		if l.currentChar >= '0' && l.currentChar <= '9' {
			return &Token{INTEGER, l.integer()}
		}

		switch l.currentChar {
		case '+':
			l.advance()
			return &Token{PLUS, "+"}
		case '-':
			l.advance()
			return &Token{MINUS, "-"}
		case '*':
			l.advance()
			return &Token{MUL, "*"}
		case '/':
			l.advance()
			return &Token{DIV, "/"}
		default:
			panic(fmt.Sprintf("Invalid character: %c", l.currentChar))
		}
	}

	return &Token{EOF, ""}
}

// Interpreter parses and interprets the input
type Interpreter struct {
	lexer        *Lexer
	currentToken *Token
}

// NewInterpreter creates a new Interpreter instance
func NewInterpreter(lexer *Lexer) *Interpreter {
	return &Interpreter{
		lexer:        lexer,
		currentToken: lexer.getNextToken(),
	}
}

// eat verifies the current token type and advances to the next token
func (i *Interpreter) eat(tokenType string) {
	if i.currentToken.Type == tokenType {
		i.currentToken = i.lexer.getNextToken()
	} else {
		panic(fmt.Sprintf("Expected %s, got %s", tokenType, i.currentToken.Type))
	}
}

// factor parses an integer factor
func (i *Interpreter) factor() int {
	token := i.currentToken
	i.eat(INTEGER)
	value, err := strconv.Atoi(token.Value)
	if err != nil {
		panic(fmt.Sprintf("Failed to parse integer: %v", err))
	}
	return value
}

// term handles multiplication and division
func (i *Interpreter) term() int {
	result := i.factor()

	for i.currentToken.Type == MUL || i.currentToken.Type == DIV {
		token := i.currentToken
		if token.Type == MUL {
			i.eat(MUL)
			result *= i.factor()
		} else if token.Type == DIV {
			i.eat(DIV)
			result /= i.factor()
		}
	}

	return result
}

// expr handles addition and subtraction
func (i *Interpreter) expr() int {
	result := i.term()

	for i.currentToken.Type == PLUS || i.currentToken.Type == MINUS {
		token := i.currentToken
		if token.Type == PLUS {
			i.eat(PLUS)
			result += i.term()
		} else if token.Type == MINUS {
			i.eat(MINUS)
			result -= i.term()
		}
	}

	return result
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("calc> ")
	text, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	text = strings.TrimSpace(text)
	lexer := NewLexer(text)
	interpreter := NewInterpreter(lexer)

	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Error:", r)
		}
	}()

	result := interpreter.expr()
	fmt.Println(result)
}
```
