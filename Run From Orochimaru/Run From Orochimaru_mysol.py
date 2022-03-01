# I TRIED DOING WITH THE SAME CODE WHICH I USED IN AOC-2021 AS THE QUESTION LOOKED SAME
# file_input = open("day-15-input.txt", "r")

# # file_input = open("day-15-test.txt", "r")
# for i in file_input:
#     a = [int(_) for _ in i.strip()]
#     _mapp.append(a)
#     # print(a)        
# file_input.close()
import math
_mapp = []
'''
def find_short(mapp):
    start = (0, 0) # y, x
    end = (len(mapp)-1, len(mapp[0])-1) # y, x

    # print(start, end)
    neww = []
    for i in range(len(mapp)):
        arr = []
        for j in range(len(mapp[0])):
            arr.append(0)
        neww.append(arr)
    # print("new arr\n", neww)
    neww[0][0] = mapp[0][0]

    # visited = []

    for i in range(1, len(mapp)):
        neww[i][0] = mapp[i][0] + neww[i-1][0]

    for j in range(1, len(mapp[0])):
        neww[0][j] = mapp[0][j] + neww[0][j-1]

    # print(mapp)
    # print(neww)

    for i in range(1, len(mapp)):
        for j in range(1, len(mapp[0])):
            neww[i][j] = mapp[i][j] + min(neww[i-1][j], neww[i][j-1])

    # for i in range(len(mapp)):
    #     print([_ for _ in neww[i]])
    
    # print(neww[0][0], neww[-1][-1])
    # print("Ans = ", neww[-1][-1]-neww[0][0])
    print(neww[-1][-1])
'''
def neighbors(xy):
    (x, y) = xy
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def traverse_cost(start, end, c):
    steps = 1
    cost = { start: 0 }
    active = set([start])
    visited = set([])
    
    while active:
        steps+=1
        current = min(active, key=cost.get)

        if current == end:
            return cost[current]

        active.remove(current)
        visited.add(current)
        for xy in neighbors(current):
            if xy in c and xy not in active:
                n_cost = cost.get(current, 0) + c[xy]
                if n_cost < cost.get(xy, math.inf):
                    cost[xy] = n_cost
                    active.add(xy)
        # print(steps, end="\r")
        # updated_mapp(c, visited, steps)



# c1 = C


# print("\nAns :",cos)
if __name__ =="__main__":
    
    testcases = int(input())
    for i in range(testcases):
        n,m = map(int, input().split())
        for i in range(n):
            _mapp.append(list(map(int, input().split())))
        C = {}
        for i in range(len(_mapp)):
            for j in range(len(_mapp[0])):
                C[(j, i)] = _mapp[i][j]
        start = (0, 0)
        end = (len(_mapp[0])-1, len(_mapp)-1)
        cos = traverse_cost(start, end, C)
        print(cos+_mapp[0][0])
        # find_short(_mapp)
