



import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'VARIABLE','NUMBER' , 
    )

literals = ['=','+','-','<=','>=' , '<' , '>' , 'min' , 'max']

t_NAME    = r'[a-zA-Z][a-zA-Z]*[_]*[0-9]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lex.lex()


# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )

# dictionary of variables
x_matrix = []
c_matrix = []
b_matrix = []
a_matrix = [[]]

l_o_e = {}
g_o_e = {}
l_t = {}
g_t = {}


goal = ''

def p_statement_assign(p):
    'statement: goal subject constraint'
    if p[1] == 'max' : goal = 'max'
	elif p[1] == 'min' : goal = 'min'

def p_statement_goal(p):
    '''goal: 'min' statement 
       | 'max' statement'''
    if p[1] == 'max' : goal = 'max'
    elif p[1] == 'min' : goal = 'min'
    
def p_statement_subject(p):
    '''subject: subject subject | 
    statement '=' NUMBER | 
    statement '<=' NUMBER | 
    statement '>=' NUMBER '''
    if p[1] == 'max' : goal = 'max'
    elif p[1] == 'min' : goal = 'min'
    
def p_statement_statement(p):
    '''statement: NUMBER VARIABLE '+' | NUMBER VARIABLE '-' | NUMBER VARIABLE  | 
        VARIABLE '+' | VARIABLE '-' | VARIABLE'''
    if p[1] == 'max' : goal = 'max'
    elif p[1] == 'min' : goal = 'min'
    

def p_statement_constraint(p):
    '''constraint: VARIABLE '<=' NUMBER |
    VARIABLE '>=' NUMBER | 
    VARIABLE '<' NUMBER | 
    VARIABLE '>' NUMBER  '''
    if p[1] == '<=' : l_o_e[p[1]] = p[3]
    elif p[1] == '>=' : g_o_e[p[1]] = p[3]
    elif p[1] == '<' : l_t[p[1]] = p[3]
    elif p[1] == '>' : g_t[p[1]] = p[3]
    


# 'statement: goal subject constraint'
# '''goal: 'min' statement 
# 		| 'max' statement'''
# '''subject: subject subject | 
# 	statement '=' NUMBER | 
# 	statement '<=' NUMBER | 
# 	statement '>=' NUMBER '''
# '''statement: VARIABLE '+' | VARIABLE '-' | VARIABLE '''
# '''constraint: VARIABLE '<=' NUMBER |
# 	VARIABLE '>=' NUMBER | 
# 	VARIABLE '<' NUMBER | 
# 	VARIABLE '>' NUMBER  '''