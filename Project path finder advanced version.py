def create_maze():
    maze=[]
    maze.append(['#','#','#','#','#','#','#','#'])
    maze.append(['*',' ',' ',' ',' ',' ',' ','#'])
    maze.append(['#',' ','#','#','#','#',' ','#'])
    maze.append(['#',' ',' ',' ',' ','#',' ','#'])
    maze.append(['#',' ','#',' ',' ',' ',' ','#'])
    maze.append(['#',' ','#',' ','#','#',' ','#'])
    maze.append(['#',' ','#',' ','#','#','S','#'])
    maze.append(['#','#','#','#','#','#','#','#'])

    return maze

def create_maze2():
    maze=[]
    maze.append(['#','#','#','#','#','#','#','#','#','#','#'])
    maze.append(['#','#',' ',' ',' ','#',' ','*',' ',' ','#'])
    maze.append(['#','#',' ','#','#','#','#','#','#',' ','#'])
    maze.append(['#','#',' ','#','#','#','#','#',' ',' ','#'])
    maze.append(['#','#',' ',' ',' ','#',' ','#',' ','#','#'])
    maze.append(['#','#',' ','#',' ','#',' ','#',' ',' ','#'])
    maze.append(['S',' ',' ','#',' ',' ',' ',' ',' ','#','#'])
    maze.append(['#','#',' ',' ','#','#',' ','#',' ','#','#'])
    maze.append(['#','#','#','#','#','#',' ',' ',' ','#','#'])
    maze.append(['#','#','#','#','#','#',' ',' ',' ','#','#'])
    maze.append(['#','#','#','#','#','#','#','#','#','#','#'])




    return maze


def position_start(maze):
    pos=[]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]=='S':
                pos.append(i)
                pos.append(j)
                return pos

def all_false(l):
    A=[]
    for i in range(l):
        m=[]
        for j in range(l):
            m.append('False')
        A.append(m)
    return A

def end_position(maze):
    A=[]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]=='*':
                A.append(i)
                A.append(j)
                return A

def min_length(maze,A,a,b):
    frontier=[[a,b]]
    x=dict()
    while len(frontier)!=0:
        current=frontier[0]
        if A[current[0]][current[1]]!='True':
            A[current[0]][current[1]]='True'
            if current[0]!=len(maze)-1 and (maze[current[0]+1][current[1]]==' ' or maze[current[0]+1][current[1]]=='*') and A[current[0]+1][current[1]]=='False':
                x[current[0]+1,current[1]]=[current[0],current[1]]
                frontier.append([current[0]+1,current[1]])
            if current[0]!=0 and (maze[current[0]-1][current[1]]==' ' or maze[current[0]-1][current[1]]=='*') and A[current[0]-1][current[1]]=='False':
                x[current[0]-1,current[1]]=[current[0],current[1]]
                frontier.append([current[0]-1,current[1]])
            if current[1]!=0 and (maze[current[0]][current[1]-1]==' ' or maze[current[0]][current[1]-1]=='*') and A[current[0]][current[1]-1]=='False':
                x[current[0],current[1]-1]=[current[0],current[1]]
                frontier.append([current[0],current[1]-1])
            if current[1]!=len(maze)-1 and (maze[current[0]][current[1]+1]==' ' or maze[current[0]][current[1]+1]=='*') and A[current[0]][current[1]+1]=='False':
                x[current[0],current[1]+1]=[current[0],current[1]]
                frontier.append([current[0],current[1]+1])
        frontier.pop(0)
    return x

def print_maze(x,p,q,a,b,maze):
    m,n=p,q
    count=1
    while x[m,n]!=[a,b]:
        d=[]
        count+=1
        d=x[m,n]
        m,n=d[0],d[1]
        maze[m][n]='O'
    print()
    print('Shortest path length is: ',count)
    print()
    for s in maze:
        print(*s)
        

maze=create_maze2()
for s in maze:
    print(*s)
pos,end=[],[]
pos=position_start(maze)
a,b=pos[0],pos[1]
end=end_position(maze)
p,q=end[0],end[1]
queue=[]
A=all_false(len(maze))
m_len={}
m_len=min_length(maze,A,a,b)
print_maze(m_len,p,q,a,b,maze)

