'''
The program passes in two numbers: a start position and an end position on a chessboard.
Program calculates the least number of moves it would take to get from the start to the end if you move as a standard knight
'''

def answer(src,dest):  
    #Node object
    class Node:

        def __init__(self, x, y, distance):
            self.x = x
            self.y = y
            self.dist = distance

        def is_equal(self, node):
            if (self.x == node.x and self.y == node.y):
                return True
            
    #x and y calculators
    def row_calc(space):
        return int(space/8)

    def col_calc(space):
        return space%8
        
    #legal move check
    def is_legal_move(node):
        if ((node.x > 7 or node.x < 0) and (node.y > 7 or node.y < 0)):
            return False
        else:
            return True
        
    #BFT driver function
    def bft(node_src,node_dest):

        visiting = []
        visited = {}
        row_movement = [1, 1, 2, 2, -1, -1, -2, -2]
        col_movement = [2, -2, 1, -1, 2, -2, 1, -1]


        visiting.append(node_src)

        while(visiting):
            current = visiting.pop(0)

            if (current.is_equal(node_dest)):
                return current.dist
                
            visited.setdefault(current, False)

            while(not visited[current]):
                visited[current] = True 
                for i in range(8):
                    x = current.x + col_movement[i]
                    y = current.y + row_movement[i]
                    dist = current.dist + 1
                    new_node = Node(x, y, dist)
                                
                    if (is_legal_move):
                        visiting.append(new_node)
                                                 
            

        return -1

    #initialization step
    src_node = Node(col_calc(src), row_calc(src), 0)

    dest_node = Node(col_calc(dest), row_calc(dest), 0)

    distance = bft(src_node, dest_node)   
    
    return distance

print(answer(10,0))
