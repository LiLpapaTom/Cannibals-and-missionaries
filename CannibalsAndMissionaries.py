import random
#All cannibals & missionaries are on starting on the left side
#goal is to take all of them, to the right side
s_state = [3,3,1]
t_state = [0,0,0]
r_can = 0
r_mis = 0
path = []
path.append([3,3,1])
counter = 0

flag = True
while flag:
    #If boat on the left side
    if s_state[2] == 1:
        rand = int(random.uniform(1,4))
        #Move 2 cannibals
        if rand == 1 and s_state[1]>1:
            s_state[1] -= 2
            r_can += 2
            #boat is on the right side
            s_state[2] = 0
        #Move 2 missionaries
        elif rand == 2 and s_state[0]>1:
            s_state[0] -= 2
            r_mis += 2
            s_state[2] = 0
        #Move one of each
        elif s_state[0]>0 and s_state[1]>0:
            s_state[0] -= 1
            s_state[1] -= 1
            r_can += 1
            r_mis += 1
            s_state[2] = 0
        #print("Missionaries on the left side:",s_state[0]," Cannibals:",s_state[1]," Boat is on the left")
    #if boat is on the right side
    elif s_state[2] == 0:
        rand = int(random.uniform(1,5))
        #1 missionary brings the boat back
        if rand == 1 and s_state[0]<3:
            s_state[0] += 1
            s_state[2] = 1
            r_mis -= 1
        #2 missionaries bring the boat back
        elif rand == 2 and s_state[0]<2:
            s_state[0] += 2
            s_state[2] = 1
            r_mis -= 2
        #1 cannibal brings the boat back
        elif rand == 3 and s_state[1]<3:
            s_state[1] += 1
            s_state[2] = 1
            r_can -= 1
        #2 cannibals bring the boat back
        elif rand == 4 and s_state[1]<2:
            s_state[1] += 2
            s_state[2] = 1
            r_can -= 2
        #print("Missionaries on the left side:",s_state[0]," Cannibals:",s_state[1]," Boat is on the right")
    #if cannibals are more than missionaries reset
    print(s_state,"Right side: cannibals", r_can,"missionaries", r_mis)
    #if cannibals are greater than missionaries on either side, reset, start over
    if s_state[1] > s_state[0] and s_state[2] == 0:
        #if r_mis > 0 and s_state[2] == 0:
        print("RESET\n")
        s_state[0] = 3
        s_state[1] = 3
        s_state[2] = 1
        path.clear();path.append([3,3,1])
        r_can = 0; r_mis = 0;
    #If all made it to the other side, end programm
    elif  r_can > r_mis and s_state[2] == 1:
        print("RESET\n")
        s_state[0] = 3
        s_state[1] = 3
        s_state[2] = 1
        path.clear();path.append([3,3,1])
        r_can = 0; r_mis = 0;
    #If we meet the final state, end the programm
    elif s_state == t_state:
        print("\nWe made it")
        path.append(t_state)
        flag = False
    if path[-1] != s_state:
        path.append([s_state[0],s_state[1],s_state[2]])
#print the steps
for i in path:
    if counter < 10:
        print("Step:",counter,"  move: ",i)
    else:
        print("Step:",counter," move: ",i)
    counter += 1
