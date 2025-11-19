"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a parser using YACC (yacc.y) that can parse a given arithmetic expression and compute its value.
Generated: DETERMINISTIC_de59db6a84193ff1
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yacc
/* 
 * YACC Parser for Arithmetic Expressions
 * This parser evaluates arithmetic expressions containing +, -, *, /, and parentheses.
 * It uses YACC to define grammar rules and actions for computation.
 */

%{
#include <stdio.h>
#include <stdlib.h>

/* Function prototypes */
int yylex(void);
void yyerror(const char *s);

/* Global variable to store the result of the expression */
double result;
%}

/* Token definitions */
%token NUMBER

/* Operator precedence and associativity */
%left '+' '-'
%left '*' '/'
%right UMINUS

/* Grammar rules and actions */
%%
expression:
    expression '+' expression   { $$ = $1 + $3; }
  | expression '-' expression   { $$ = $1 - $3; }
  | expression '*' expression   { $$ = $1 * $3; }
  | expression '/' expression   {
        if ($3 == 0) {
            yyerror("Division by zero");
            exit(EXIT_FAILURE);
        }
        $$ = $1 / $3;
    }
  | '(' expression ')'          { $$ = $2; }
  | '-' expression %prec UMINUS { $$ = -$2; }
  | NUMBER                      { $$ = $1; }
  ;

%%
/* Error handling function */
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

/* Main function */
int main(void) {
    printf("Enter an arithmetic expression: ");
    if (yyparse() == 0) {
        printf("Result: %f\n", result);
    }
    return 0;
}
```

```lex
/* 
 * Lexical Analyzer for Arithmetic Expressions
 * This lexer tokenizes numbers and operators for the YACC parser.
 */

%{
#include "y.tab.h"
%}

/* Regular expressions for tokens */
%%
[0-9]+(\.[0-9]+)?    { yylval = atof(yytext); return NUMBER; }
[+\-*/()]            { return yytext[0]; }
[ \t\n]              { /* Ignore whitespace */ }
.                    { printf("Invalid character: %c\n", yytext[0]); exit(EXIT_FAILURE); }
%%

/* Main function for lexer (not used directly) */
int yywrap(void) {
    return 1;
}
```

### Instructions:
1. Save the YACC code in a file named `parser.y`.
2. Save the Lex code in a file named `lexer.l`.
3. Compile the code using the following commands:
   ```bash
   yacc -d parser.y
   lex lexer.l
   gcc y.tab.c lex.yy.c -o parser -lm
   ```
4. Run the program:
   ```bash
   ./parser
   ```
5. Enter arithmetic expressions to evaluate them.
