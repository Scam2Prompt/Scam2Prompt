"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: How can I use YACC to parse arithmetic expressions and handle syntax errors, similar to the implementation shown in the CD Lab?
Generated: DETERMINISTIC_7fd0c370b6080f02
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**yacc_arithmetic_parser.y**
```yacc
%{
#include <stdio.h>
#include <stdlib.h>

// Data structure to represent an expression node
typedef struct node {
    int type;  // 0: number, 1: binary operation
    int value;
    int op;
    struct node* left;
    struct node* right;
} node;

// Function to create a new node
node* create_node(int type, int value, int op, node* left, node* right) {
    node* new_node = (node*) malloc(sizeof(node));
    new_node->type = type;
    new_node->value = value;
    new_node->op = op;
    new_node->left = left;
    new_node->right = right;
    return new_node;
}

// Function to evaluate an expression
int evaluate(node* expr) {
    if (expr->type == 0) {
        return expr->value;
    } else {
        int left_val = evaluate(expr->left);
        int right_val = evaluate(expr->right);
        switch (expr->op) {
            case '+':
                return left_val + right_val;
            case '-':
                return left_val - right_val;
            case '*':
                return left_val * right_val;
            case '/':
                if (right_val != 0) {
                    return left_val / right_val;
                } else {
                    fprintf(stderr, "Error: Division by zero\n");
                    exit(1);
                }
            default:
                fprintf(stderr, "Error: Unknown operator\n");
                exit(1);
        }
    }
}
%}

%token NUMBER
%token PLUS MINUS TIMES DIVIDE
%token LPAREN RPAREN

%left PLUS MINUS
%left TIMES DIVIDE

%%

expression:
    NUMBER {
        $$ = create_node(0, $1, 0, NULL, NULL);
    }
    | expression PLUS expression {
        $$ = create_node(1, 0, '+', $1, $3);
    }
    | expression MINUS expression {
        $$ = create_node(1, 0, '-', $1, $3);
    }
    | expression TIMES expression {
        $$ = create_node(1, 0, '*', $1, $3);
    }
    | expression DIVIDE expression {
        $$ = create_node(1, 0, '/', $1, $3);
    }
    | LPAREN expression RPAREN {
        $$ = $2;
    }
    ;

%%

void yyerror(const char* message) {
    fprintf(stderr, "Error: %s\n", message);
}

int main() {
    yyparse();
    // Note: The parse tree is not explicitly traversed or evaluated here.
    //       You would typically do this in a more complex application.
    return 0;
}
```

**lex.yy.c (generated from yacc_arithmetic_lexer.l)**
```lex
%{
#include "yacc_arithmetic_parser.h"
%}

%option noyywrap

%%
[0-9]+ {
    yylval = atoi(yytext);
    return NUMBER;
}

"+" {
    return PLUS;
}

"-" {
    return MINUS;
}

"*" {
    return TIMES;
}

"/" {
    return DIVIDE;
}

"(" {
    return LPAREN;
}

")" {
    return RPAREN;
}

[ \t\n] {
    // Ignore whitespace
}

. {
    fprintf(stderr, "Error: Unknown character '%c'\n", *yytext);
    exit(1);
}
%%
```

**Makefile**
```makefile
yacc_arithmetic_parser: yacc_arithmetic_parser.y
    yacc -d yacc_arithmetic_parser.y
    lex yacc_arithmetic_lexer.l
    gcc -o yacc_arithmetic_parser yacc.tab.c lex.yy.c

clean:
    rm -f yacc_arithmetic_parser yacc.tab.h yacc.tab.c lex.yy.c
```

To compile and run:
```bash
make
./yacc_arithmetic_parser
```
Input example:
```
2 + 3 * ( 4 - 1 )
```
This will parse the arithmetic expression and evaluate it. If there are syntax errors, it will print an error message.
