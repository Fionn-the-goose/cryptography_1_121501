#21501, 121067, 121588
#Bachelor
#!/usr/bin/env python3

initial_state = [1,0,0,1,1,1,0,0]
l = len(initial_state)
output = []
solution = []

for x in range(2**len(initial_state)):
    out = initial_state[l-1]
    output.insert(0,out)
    new = (out ^ initial_state[l-3]) ^ initial_state[1]
    initial_state.pop()
    initial_state.insert(0,new)

for i in range(l):
    solution.append(output[len(output)-l])

print(output)

