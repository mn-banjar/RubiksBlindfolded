
import RubiksBlindfolded


'''
#defual scramble
sides = {'U': ['D', 'B', 'U', 'L', 'U', 'U', 'R', 'R', 'B'],
         'F': ['U', 'F', 'R', 'F', 'F', 'R', 'U', 'R', 'R'],
         'R': ['D', 'F', 'B', 'D', 'R', 'D', 'F', 'R', 'D'],
         'D': ['F', 'U', 'U', 'D', 'D', 'B', 'F', 'L', 'L'],
         'B': ['L', 'U', 'R', 'B', 'B', 'L', 'B', 'B', 'D'],
         'L': ['F', 'F', 'B', 'U', 'L', 'D', 'L', 'L', 'L']}

#scramble U R F
sides = {'U': ['U', 'U', 'R', 'U', 'U', 'F', 'L', 'L', 'F'],
         'F': ['F', 'F', 'R', 'F', 'F', 'R', 'D', 'D', 'D'],
         'R': ['U', 'R', 'B', 'U', 'R', 'B', 'F', 'R', 'B'],
         'D': ['R', 'R', 'R', 'D', 'D', 'B', 'D', 'D', 'L'],
         'B': ['U', 'L', 'L', 'U', 'B', 'B', 'U', 'B', 'B'],
         'L': ['F', 'F', 'D', 'L', 'L', 'D', 'L', 'L', 'B']}
       
#scramble R B U
sides = {'U': ['U', 'U', 'R', 'U', 'U', 'R', 'F', 'F', 'R'],
         'F': ['R', 'R', 'B', 'F', 'F', 'D', 'F', 'F', 'D'],
         'R': ['U', 'U', 'U', 'R', 'R', 'D', 'R', 'R', 'D'],
         'D': ['D', 'D', 'B', 'D', 'D', 'B', 'L', 'L', 'L'],
         'B': ['F', 'L', 'L', 'B', 'B', 'B', 'B', 'B', 'B'],
         'L': ['F', 'F', 'D', 'U', 'L', 'L', 'U', 'L', 'L']}

#scramble D L B L 
sides = {'U': ['D', 'R', 'F', 'B', 'U', 'U', 'B', 'U', 'U'],
         'F': ['R', 'F', 'F', 'B', 'F', 'F', 'B', 'L', 'L'],
         'R': ['R', 'R', 'D', 'R', 'R', 'D', 'F', 'F', 'L'],
         'D': ['U', 'D', 'D', 'U', 'D', 'D', 'U', 'B', 'B'],
         'B': ['R', 'B', 'B', 'R', 'B', 'F', 'D', 'D', 'F'],
         'L': ['R', 'U', 'U', 'L', 'L', 'L', 'L', 'L', 'L']}
'''
#scramble L
sides = {'U': ['B', 'U', 'U', 'B', 'U', 'U', 'B', 'U', 'U'], 
         'F': ['U', 'F', 'F', 'U', 'F', 'F', 'U', 'F', 'F'], 
         'R': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], 
         'D': ['F', 'D', 'D', 'F', 'D', 'D', 'F', 'D', 'D'],
         'B': ['B', 'B', 'D', 'B', 'B', 'D', 'B', 'B', 'D'],
         'L': ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']}
'''
#solved cube
sides = {'U': ['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'], 
         'F': ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'], 
         'R': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], 
         'D': ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
         'B': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
         'L': ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']}
'''

#uncomment below line to display the edge priority
#print('edge priority:')
#print(RubiksBlindfolded.displayEdgePriority())

#uncomment below line to update the edge priority
#RubiksBlindfolded.updateEdgePriority({0:['U',0,'U',0],3:['U',0,'U',0]})
#print(RubiksBlindfolded.displayEdgePriority())


#uncomment below line to display the corner priority
#print('corner priority:')
#print(RubiksBlindfolded.displayCornerPriority())

#uncomment below line to update the corner priority
#RubiksBlindfolded.updateCornerPriority({0:['U',0,'U',0,'U',0],3:['U',0,'U',0,'U',0]})
#print(RubiksBlindfolded.displayCornerPriority())
#print('\n')

RubiksBlindfolded.setCube(sides)
print(RubiksBlindfolded.displayCube())


print('solved edges:')
print(RubiksBlindfolded.getSolvedEdges())
print('solved corners:')
print(RubiksBlindfolded.getSolvedCorners())
print('\n')

print('SOLVING EDGES\n')
print('edge sequence:')
print(RubiksBlindfolded.solveEdges())
#print(RubiksBlindfolded.displayCube())

print('edge sequence indexex:')
print(RubiksBlindfolded.indexEdgeSequence())
print('current edge buffer:')
print(RubiksBlindfolded.currentEdgeBuffer())
print('\n')

print('parity check {}'.format(RubiksBlindfolded.parityCheck()))
RubiksBlindfolded.parityAlgorithm()
#print(RubiksBlindfolded.displayCube())
print('\n')

print('SOLVING CORNERS\n')
print('corner sequence:')
print(RubiksBlindfolded.solveCorners())
#print(RubiksBlindfolded.displayCube())

print('corner sequence indexex')
print(RubiksBlindfolded.indexCornerSequence())
print('current corner buffer:')
print(RubiksBlindfolded.currentCornerBuffer())
print('\n')

