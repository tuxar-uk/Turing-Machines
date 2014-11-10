# Add unary numbers (e.g. 2+5)
#
# prog is indexed by the current tape symbol (0 or 1) and then by state
# (a kind of instruction pointer) to get an 'instruction' comprising:
#	symbol to write on current tape position,
#	head action (-1 = move left, +1 = move right)
#	next state (like a goto jump).

prog=[[(1,+1,1),(0,-1,2),(0,+1,2)],		# 0 on tape
      [(1,+1,0),(1,+1,1),(0,+1,9)]]	    # 1 on tape
tape=[1,1,0,1,1,1,0,0,0]			    # The data tape
head=0						            # head position on tape
state=0						            # instruction pointer
print tape
while state != 9:				        # while not halt:
    symbol=tape[head]				        # read current tape symbol
    symbol,dir,state=t=prog[symbol][state]	# lookup instruction
    print ' '*(head*3+1)+'^  '+str(t)		# display progress
    tape[head]=symbol				        # write new symbol on tape
    print tape
    head=head+dir				            # move tape head