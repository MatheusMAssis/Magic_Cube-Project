import numpy as np
import random as rd

#--- auxiliar function ---#

def change(n):
    color_dict = {0: 'W',
                  1: 'O',
                  2: 'G',
                  3: 'R',
                  4: 'B',
                  5: 'Y'}
    return color_dict[n]

#--- cube class (in this case, a 2x2x2) ---#

class cube:
    
    #--- initializing the cube in it's solved form ---#
    
    def __init__(self):
        self.state = np.array([0, 0, 0, 0, #up
                               1, 1, 2, 2, 
                               3, 3, 4, 4,
                               1, 1, 2, 2,
                               3, 3, 4, 4,
                               5, 5, 5, 5]) #down
    
    #--- printing the colors of cube faces ---#
    
    def show(self):
        up, down, front, back, right, left = [], [], [], [], [], []
        
        for i in range(len(self.state)):
            if i < 4:
                color = change(self.state[i])
                up.append(color)
            elif i < 6 or (i < 14 and i >= 12):
                color = change(self.state[i])
                left.append(color)
            elif i < 8 or (i < 16 and i >= 14):
                color = change(self.state[i])
                front.append(color)
            elif i < 10 or (i < 18 and i >= 16):
                color = change(self.state[i])
                right.append(color)
            elif i < 12 or (i < 20 and i >= 18):
                color = change(self.state[i])
                back.append(color)
            else:
                color = change(self.state[i])
                down.append(color)
        
        print('up    :', up[:2], '\n', '      ', up[2:])
        print('down  :', down[:2], '\n', '      ', down[2:])
        print('front :', front[:2], '\n', '      ', front[2:])
        print('back  :', back[:2], '\n', '      ', back[2:])
        print('right :', right[:2], '\n', '      ', right[2:])
        print('left  :', left[:2], '\n', '      ', left[2:])
    
    #--- defining moves in clock or counterclock wise ---#
    
    def move(self, movement):
        
    #--- up ---#
    
        #clock
        if movement == 'U':
            
            #up
            aux1, aux2 = self.state[0], self.state[1]
            self.state[0], self.state[1] = self.state[2], aux1
            self.state[2], self.state[3] = self.state[3], aux2
            
            #lateral
            [aux1, aux2] = self.state[4:6]
            self.state[4:10] = self.state[6:12]
            self.state[10:12] = [aux1, aux2]
        
        #counterclock
        elif movement == 'Ui':
                
            #up
            aux1, aux2 = self.state[0], self.state[2]
            self.state[0], self.state[1] = self.state[1], self.state[3]
            self.state[2], self.state[3] = aux1, aux2
            
            #lateral
            [aux1, aux2] = self.state[10:12]
            self.state[6:12] = self.state[4:10]
            self.state[4:6] =  [aux1, aux2]
        
    #--- down ---#
    
        #clock
        elif movement == 'D':
            
            #down
            aux1, aux2 = self.state[20], self.state[21]
            self.state[20], self.state[21] = self.state[22], aux1
            self.state[22], self.state[23] = self.state[23], aux2
            
            #lateral
            [aux1, aux2] = self.state[18:20]
            self.state[14:20] = self.state[12:18]
            self.state[12:14] =  [aux1, aux2]
        
        #counterclock
        elif movement == 'Di':
            
            #down
            aux1, aux2 = self.state[20], self.state[22]
            self.state[20], self.state[21] = self.state[21], self.state[23]
            self.state[22], self.state[23] = aux1, aux2
            
            #lateral
            [aux1, aux2] = self.state[12:14]
            self.state[12:18] = self.state[14:20]
            self.state[18:20] = [aux1, aux2]
         
    #--- right ---#
    
        #clock
        elif movement == 'R':
            
            #right
            aux1, aux2 = self.state[8], self.state[9]
            self.state[8], self.state[9] = self.state[16], aux1
            self.state[16], self.state[17] = self.state[17], aux2
            
            #vertical
            aux_list = [self.state[1], self.state[3],
                        self.state[7], self.state[15],
                        self.state[21], self.state[23],
                        self.state[18], self.state[10]]
            [aux1, aux2] = aux_list[0:2]
            aux_list[0:6] = aux_list[2:8]
            aux_list[6:8] = [aux1, aux2]
            [self.state[1], self.state[3],
             self.state[7], self.state[15],
             self.state[21], self.state[23],
             self.state[18], self.state[10]] = aux_list
        
        #counterclock
        elif movement == 'Ri':
            
            #right
            aux1, aux2 = self.state[8], self.state[16]
            self.state[8], self.state[9] = self.state[9], self.state[17]
            self.state[16], self.state[17] = aux1, aux2
            
            #vertical
            aux_list = [self.state[1], self.state[3],
                        self.state[7], self.state[15],
                        self.state[21], self.state[23],
                        self.state[18], self.state[10]]
            [aux1, aux2] = aux_list[6:8]
            aux_list[2:8] = aux_list[0:6]
            aux_list[0:2] = [aux1, aux2]
            [self.state[1], self.state[3],
             self.state[7], self.state[15],
             self.state[21], self.state[23],
             self.state[18], self.state[10]] = aux_list
            
    #--- left ---#
    
        #clock    
        elif movement == 'L':
            
            #left
            aux1, aux2 = self.state[4], self.state[5]
            self.state[4], self.state[5] = self.state[12], aux1
            self.state[12], self.state[13] = self.state[13], aux2
            
            #vertical
            aux_list = [self.state[0], self.state[2],
                        self.state[6], self.state[14],
                        self.state[20], self.state[22],
                        self.state[19], self.state[11]]
            [aux1, aux2] = aux_list[6:8]
            aux_list[2:8] = aux_list[0:6]
            aux_list[0:2] = [aux1, aux2]
            [self.state[0], self.state[2],
             self.state[6], self.state[14],
             self.state[20], self.state[22],
             self.state[19], self.state[11]] = aux_list
        
        #counterclock
        elif movement == 'Li':
            
            #left
            aux1, aux2 = self.state[4], self.state[12]
            self.state[4], self.state[5] = self.state[5], self.state[13]
            self.state[12], self.state[13] = aux1, aux2
            
            #vertical
            aux_list = [self.state[0], self.state[2],
                        self.state[6], self.state[14],
                        self.state[20], self.state[22],
                        self.state[19], self.state[11]]
            [aux1, aux2] = aux_list[0:2]
            aux_list[0:6] = aux_list[2:8]
            aux_list[6:8] = [aux1, aux2]
            [self.state[0], self.state[2],
             self.state[6], self.state[14],
             self.state[20], self.state[22],
             self.state[19], self.state[11]] = aux_list
         
    #--- front ---#
        
        #clock
        elif movement == 'F':
            
            #front
            aux1, aux2 = self.state[6], self.state[7]
            self.state[6], self.state[7] = self.state[14], aux1
            self.state[14], self.state[15] = self.state[15], aux2
            
            #horizontal
            aux_list = [self.state[2], self.state[3],
                        self.state[8], self.state[16],
                        self.state[20], self.state[21],
                        self.state[5], self.state[13]]
            [aux1, aux2] = aux_list[6:8][-1::-1]
            aux_list[6:8] = aux_list[4:6]
            aux_list[4:6] = aux_list[2:4][-1::-1]
            aux_list[2:4] = aux_list[0:2]
            aux_list[0:2] = [aux1, aux2]
            [self.state[2], self.state[3],
             self.state[8], self.state[16],
             self.state[20], self.state[21],
             self.state[5], self.state[13]] = aux_list
            
        #counterclock    
        elif movement == 'Fi':
            
            #front
            aux1, aux2 = self.state[6], self.state[14]
            self.state[6], self.state[7] = self.state[7], self.state[15]
            self.state[14], self.state[15] = aux1, aux2
            
            #horizontal
            aux_list = [self.state[2], self.state[3],
                        self.state[8], self.state[16],
                        self.state[20], self.state[21],
                        self.state[5], self.state[13]]
            [aux1, aux2] = aux_list[0:2][-1::-1]
            aux_list[0:2] = aux_list[2:4]
            aux_list[2:4] = aux_list[4:6][-1::-1]
            aux_list[4:6] = aux_list[6:8]
            aux_list[6:8] = [aux1, aux2]
            [self.state[2], self.state[3],
             self.state[8], self.state[16],
             self.state[20], self.state[21],
             self.state[5], self.state[13]] = aux_list
             
    #--- back ---#
    
        #clock
        elif movement == 'B':
            
            #back
            aux1, aux2 = self.state[10], self.state[11]
            self.state[10], self.state[11] = self.state[18], aux1
            self.state[18], self.state[19] = self.state[19], aux2
            
            #horizontal
            aux_list = [self.state[0], self.state[1],
                        self.state[4], self.state[12],
                        self.state[22], self.state[23],
                        self.state[9], self.state[17]]
            [aux1, aux2] = aux_list[6:8]
            aux_list[6:8] = aux_list[4:6][-1::-1]
            aux_list[4:6] = aux_list[2:4]
            aux_list[2:4] = aux_list[0:2][-1::-1]
            aux_list[0:2] = [aux1, aux2]
            [self.state[0], self.state[1],
             self.state[4], self.state[12],
             self.state[22], self.state[23],
             self.state[9], self.state[17]] = aux_list
            
            
        #counterclock    
        elif movement == 'Bi':
            
            #back
            aux1, aux2 = self.state[10], self.state[18]
            self.state[10], self.state[11] = self.state[11], self.state[19]
            self.state[18], self.state[19] = aux1, aux2
            
            #horizontal
            aux_list = [self.state[0], self.state[1],
                        self.state[4], self.state[12],
                        self.state[22], self.state[23],
                        self.state[9], self.state[17]]
            [aux1, aux2] = aux_list[0:2]
            aux_list[0:2] = aux_list[2:4][-1::-1]
            aux_list[2:4] = aux_list[4:6]
            aux_list[4:6] = aux_list[6:8][-1::-1]
            aux_list[6:8] = [aux1, aux2]
            [self.state[0], self.state[1],
             self.state[4], self.state[12],
             self.state[22], self.state[23],
             self.state[9], self.state[17]] = aux_list
    
    #--- scrambling the cube up to n movements ---#
        
    def scramble(self, n):
        
        list_of_movements = np.array(['U', 'Ui', 'D', 'Di', 'R', 'Ri', 'L', 'Li',
                                      'F', 'Fi', 'B', 'Bi'])
        scramble_list = []
        
        for i in range(n):
            mov = rd.choice(list_of_movements)
            scramble_list.append(mov)
            self.move(mov)
        
        return scramble_list
