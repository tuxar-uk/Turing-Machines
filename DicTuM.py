# Add unary numbers (e.g. 2 + 1)
table={ '1':{'0':'1>2','1':'1>1'},
        '2':{'0':'0<3','1':'1>2'},
        '3':{'0':'0>3','1':'0>0'}}
tape='01101000'
head=2
state='1'
while state != '0':
    print tape
    symbol=tape[head]
    next=table[state]
    tuple=next[symbol]
    tape=tape[:head]+tuple[0]+tape[head+1:]
    action=tuple[1]
    if (action=='<'):
        head=head-1
    else:
        head=head+1
    state=tuple[2]
print tape