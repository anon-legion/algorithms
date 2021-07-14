# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:38:58 2020

@author: Anon
"""

# map environment and aesthetics
def createMaze():
    maze = []
    maze.append(["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"])
    maze.append(["#"," "," "," "," "," "," "," "," ","#"," "," "," ","#"," "," ","#"," "," ","#"])
    maze.append(["#"," ","#","#","#"," ","#","#"," ","#"," ","#"," ","#","#"," ","#","#"," ","#"])
    maze.append(["#"," ","#"," "," "," "," ","#"," ","#"," ","#"," "," ","#"," "," "," "," ","#"])
    maze.append(["#"," ","#"," ","#","#"," ","#","#","#"," ","#","#"," "," "," ","#","#","#","#"])
    maze.append(["#"," ","#"," ","#"," "," "," "," ","#"," ","#"," "," ","#"," "," "," "," ","#"])
    maze.append(["#"," ","#"," "," "," ","#","#"," ","#"," ","#"," ","#","#","#","#","#"," ","#"])
    maze.append(["O"," "," "," ","#","#","#"," "," "," "," ","#"," "," ","#"," "," "," "," ","#"])
    maze.append(["#","#"," ","#","#"," "," "," ","#","#","#","#"," "," ","#"," ","#","#","#","#"])
    maze.append(["#"," "," "," "," "," ","#"," "," ","#"," "," "," "," ","#"," "," "," "," ","#"])
    maze.append(["#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"])
    maze.append(["#"," ","#"," "," ","#"," "," "," "," ","#"," "," "," ","#"," "," "," "," ","#"])
    maze.append(["#"," "," "," ","#","#"," ","#","#"," "," "," ","#"," ","#"," ","#"," ","#","#"])
    maze.append(["#"," ","#","#","#"," "," "," ","#","#","#","#","#"," ","#","#","#"," "," ","#"])
    maze.append(["#"," "," ","#"," "," ","#"," "," "," "," "," ","#"," "," "," ","#","#"," ","X"])
    maze.append(["#","#"," ","#","#","#","#","#","#","#","#"," ","#"," ","#","#","#"," "," ","#"])
    maze.append(["#"," "," ","#"," "," ","#"," "," "," ","#"," ","#"," "," "," ","#"," ","#","#"])
    maze.append(["#"," ","#","#","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," "," ","#"])
    maze.append(["#"," "," "," "," "," ","#"," ","#"," "," "," ","#"," ","#"," "," "," "," ","#"])
    maze.append(["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"])

    return maze


def createMaze2():
    maze = []
    maze.append(["#","O", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(maze, path=""):
    start = [(x,y) for y, row in enumerate(maze) for x, column in enumerate(row) if column == 'O'][0]
    x = start[0]
    y = start[1]
    pos = []
    for move in path:
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "U":
            y -= 1
        elif move == "D":
            y += 1
        pos.append((x, y))
   
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if (x, y) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


# bfs algorithm
memo = {}
def isValid(maze, coordinate):
    x, y = coordinate
    try:
        assert type(coordinate) == tuple and len(maze[coordinate[1]]) > coordinate[0] >= 0 <= coordinate[1] < len(maze)
        if maze[y][x] == '#' or maze[y][x] == 'O' or coordinate in memo.values():
            return False
        else:
            return True
    except (IndexError, AssertionError):
        return False


def newCoordinate(fr, path):
    x, y = fr
    for move in path:
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "U":
            y -= 1
        elif move == "D":
                y += 1
    return (x, y)


def shortestPath(maze):
    moves = 'UDLR'
    queue = [None]
    end = ''
    start = [(x,y) for y, row in enumerate(maze) for x, column in enumerate(row) if column == 'O'][0]
    while not end:
        path, queue[:] = queue[0], queue[1:]
        if len(memo) == 0:
            loc = start
        else:
            loc = memo[path]
        for move in moves:
            if isValid(maze, newCoordinate(loc, move)):
                newX, newY = newCoordinate(loc, move)
                if path == None:
                    newMove = move
                else:
                    newMove = path + move
                if maze[newY][newX] == 'X':
                    end = newMove
                    print('Found: {}\nNumber of moves: {}'.format(end, len(end)))
                    break
                else:
                    queue.append(newMove)
                    memo[queue[-1]] = (newX, newY)
            else:
                continue
    return end


   

maze = createMaze()
end = shortestPath(maze)
printMaze(maze, end)