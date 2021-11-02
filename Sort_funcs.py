# -*- coding: utf-8 -*-

import numpy as np
import pygame
# from win32api import GetSystemMetrics #To get user's monitor resolutionn

#Finds first row in absolute numbering of file, where the 'P' symbol was met
def find_1P(data):
    i = 0
    while i < len(data):
        if data[i][71] == '1' and data[i][72] == 'P':
            break
        i += 1
    Start_number = i
    
    return Start_number

#Finds int value before P (P stands in 72 row of *.igs file)
#data is list of strings; line_number is int number of line in file
def find_value_before_P(data, line_number):
    i = line_number
    j = 0
    Temp = 0
    while  j < len(data[line_number]):
        if data[line_number][j] == ' ':
            Temp = j
            break
        j += 1
    j = Temp
    Temp_str = ''
    for j in range(Temp, 72):
        Temp_str = Temp_str + data[line_number][j]
        j += 1
    Temp = int(Temp_str)

    return Temp

#Finds int value of number of row in internal numbering in rows, that contains 'P'. 
#data is list of strings; line_number is int number of line in file
def find_P_row_number(data, line_number):
    i = line_number
    j = 0
    Temp = 0
    while  j < len(data[line_number]):
        if data[line_number][j] == 'P':
            Temp = j + 1
            break
        j += 1
    j = Temp
    Temp_str = ''
    for j in range(Temp, 80):
        Temp_str = Temp_str + data[line_number][j]
        j += 1
    Temp = int(Temp_str)

    return Temp

def find_126(data, Start_number):
    i = Start_number
    Temp1 = 0
    Temp1_T = True
    Temp2 = 0
    Type = 0
    counter = 0
    counter_T = False
    while i < len(data):
    
        Type = data[i][0] + data[i][1] + data[i][2] + data[i][3]
        before_P1 = find_value_before_P(data, i)
        if Type == '126,' and Temp1_T == True:
            Temp1 = i
            Temp1_T = False
    
        if Type != '126,' and counter_T == True and Temp1_T == False:
            Temp2 = i
            break
        
        
        i += 1
        before_P2 = find_value_before_P(data, i)
        if before_P2 != before_P1:
            counter += 1
            counter_T = True
        else:
            counter_T = False
    
    return (Temp1, Temp2)

def find_110(data, Start_number):
    i = Start_number
    Temp1 = 0
    Temp1_T = True
    Temp2 = 0
    Type = 0
    counter = 0
    counter_T = False
    while i < len(data):
    
        Type = data[i][0] + data[i][1] + data[i][2] + data[i][3]
        before_P1 = find_value_before_P(data, i)
        if Type == '110,' and Temp1_T == True:
            Temp1 = i
            Temp1_T = False
    
        if Type != '110,' and counter_T == True and Temp1_T == False:
            Temp2 = i
            break
        
        
        i += 1
        before_P2 = find_value_before_P(data, i)
        if before_P2 != before_P1:
            counter += 1
            counter_T = True
        else:
            counter_T = False
    
    return (Temp1, Temp2)

def find_axis_P_number(data):
    i = 4
    Temp = ''
    Color = ''
    Color1 = ''
    Color2 = ''
    Type = ''
    while i < len(data):
        Color = data[i][16] + data[i][17]+data[i][18]+data[i][19]+data[i][20]+data[i][21]+data[i][22]+data[i][23]
        i = i + 2
        Color1 = data[i][16] + data[i][17]+data[i][18]+data[i][19]+data[i][20]+data[i][21]+data[i][22]+data[i][23]
        i = i + 2
        Color2 = data[i][16] + data[i][17]+data[i][18]+data[i][19]+data[i][20]+data[i][21]+data[i][22]+data[i][23]
        i -= 4
        Type = data[i][0]+data[i][1]+data[i][2]+data[i][3]+data[i][4]+data[i][5]+data[i][6]+data[i][7]
        if Color != Color1 and Color != Color2 and Type == '     110':
            Temp =  data[i+1][9]+data[i+1][10]+data[i+1][11]+data[i+1][12]+data[i+1][13]+data[i+1][14]+data[i+1][15]+data[i+1][16]
            break
        i += 1
    return int(Temp)-2 

#Forms the numpy array of axis line
def form_axis(data, Start_number):
    array = np.zeros((2,2),float)
    i = find_110(data, Start_number)[0]
    TF = 0
    counter = 0
    while i < find_110(data, Start_number)[1]:
        Temp = data[i][73]+data[i][74]+data[i][75]+data[i][76]+data[i][77]+data[i][78]+data[i][79]
        if find_axis_P_number(data) == int(Temp):
            TF += 1
        Temp = ''
        j = 0
        while TF == 1 and j < 64:
            if data [i][j] == ',':
                counter += 1
                if counter < 7:
                    if counter == 1:
                        Temp = ''
                    elif counter == 2:
                        array[0][0] = float(Temp)
                        Temp = ''
                    elif counter == 3:
                        array[0][1] = float(Temp)
                        Temp = ''
                    elif counter == 4:
                        Temp = ''
                    elif counter == 5:
                        array[1][0] = float(Temp)
                        Temp = ''
                    elif counter == 6:
                        array[1][1] = float(Temp)
                        Temp =''
                    else:
                        Temp = ''
                else:
                    break
            else:
                Temp = Temp + data[i][j]
            j += 1
        if counter >= 7:
            break
    
        i += 1
    
    return array

# Function forms list of coordinates of point:
# It goes this way for first 4 points, that forms trapezoid: 1st number is x coord, 2nd number in y coord of 1st point
# then there goes x and y of 2nd point and so on... 2nd trapezoid points start after 8 numbers. 3nd after 16 numbers and so on...
def form_points_list(data, Start_number):
    
    i = find_126(data, Start_number)[0]
    j = 0
    k = 0
    counter = 0
    Temp = ''
    Temp2 = ''
    Temp_final = []
    while i < find_126(data, Start_number)[1]:
        j = 0
        while j < 65:
            if data[i][j] == ';':
                #Here starts cycle, that forms np.array
                k = 4
                counter = 0
                K = int(Temp[4])
                M = int(Temp[6])
                MAX_C = 9+2*K+M
                while k < len(Temp):
                    if Temp[k] == ',':
                        counter +=1
                    if MAX_C <= counter < MAX_C + 4*3:
                        if Temp2 == '0.':
                            Temp2 = ''
                        else:
                            if Temp[k] == ',':
                                Temp_final.append((Temp2))
                                Temp2 = ''
                            else:
                                Temp2 = Temp2 + Temp[k]
                
                    k = k + 1
                    K = 0
                    M = 0
            
                #Here ends cycle, that forms np.array
                Temp = ''
                K = 0
                M = 0
                break
            if data[i][j] == ' ':
                break
            else:
                Temp = Temp + data[i][j]

            j = j + 1
        i = i + 1
        
    Temp_final.remove('')
    return Temp_final
 
#Forms numpy array of coordinates of points of trapezoids.
#Takes as input the result of function form_points_list
#First index of array stands for the trapezoid number
#Second one stands for the point number of trapezoid(there are whole 4 points)
#Third index is for x coordiante and y coordinate
def form_points_array(list_a):

    array = np.zeros((len(list_a) // 8, 4, 2), float)
    i = 0
    k = 0
    counter = 0
    while i < len(list_a):
        if counter == 8:
            counter = 0
            k += 1
        if counter == 0:
            array[k][0][0] = float(list_a[i])
        elif counter == 1:
            array[k][0][1] = float(list_a[i])
        elif counter == 2:
            array[k][1][0] = float(list_a[i])
        elif counter == 3:
            array[k][1][1] = float(list_a[i])
        elif counter == 4:
            array[k][2][0] = float(list_a[i])
        elif counter == 5:
            array[k][2][1] = float(list_a[i])
        elif counter == 6:
            array[k][3][0] = float(list_a[i])
        elif counter == 7:
            array[k][3][1] = float(list_a[i])

        counter += 1
        i += 1
    return array
#Takes result of form_points_array as input
#Returns the same numpy array, but coordinates are moved in order to appropriate the axis that starts at the (0,0)
def normalize_trapezoids(array, Axis):
    for i in range(0, np.shape(array)[0]):
        for j in range(0, np.shape(array)[1]):
            array[i][j][0] = abs(array[i][j][0] - Axis[0][0])
            array[i][j][1] = array[i][j][1] - min(Axis[0][1], Axis[1][1])
        
        #Sorting the values into the one trapezoid
        array[i] = array[i][array[i][:,1].argsort()]
        if array[i][0][0] > array[i][1][0]:
            (array[i][0][0], array[i][1][0]) = (array[i][1][0], array[i][0][0])
        if array[i][2][0] > array[i][3][0]:
            (array[i][2][0], array[i][3][0]) = (array[i][3][0], array[i][2][0])
            
    #Sorting the trapezoids by the Z
    #Form arrays of indexes and Z coords of 4th points
    Temp_array = np.zeros((np.shape(array)[0]),float)
    for i in range(0, np.shape(array)[0]):
        Temp_array[i] = array[i][3][1]
    Temp_array = np.argsort(Temp_array) #Array of indexes in right order
    array2 = array[Temp_array]
                   
    return array2

def normalize_axis(Axis):
    Axis[0][0] = 0 
    Axis[0][1] = Axis[0][1] - min(Axis[0][1], Axis[1][1])
    Axis[1][0] = 0
    Axis[1][1] = Axis[1][1] - min(Axis[0][1], Axis[1][1])
    
    return Axis

#Takes the result of normalize_trapezoids as input
#Gives out numpy array of points (,2)
def form_trapezoid_centers(array):
    new_array = np.zeros((np.shape(array)[0], 2), float)
    for i in range(0, np.shape(array)[0]):
        new_array[i][0] = (array[i][0][0]+array[i][1][0]+array[i][2][0]+array[i][3][0]) / 4
        new_array[i][1] = (array[i][0][1]+array[i][1][1]+array[i][2][1]+array[i][3][1]) / 4   
    
    return new_array
#Creates thcond file
def create_thcond(array):

    thcond = open('THCOND.DAT', 'w')
    i = 0
    for i in range(0, np.shape(array)[i]):
        thcond.write('con'+str(i))
        thcond.write('\n')
        thcond.write(str(array[i][0][1])+','+str(array[i][2][1]))
        thcond.write('\n')
        thcond.write(str(array[i][0][0])+','+str(array[i][1][0])+','+str(array[i][2][0])+','+str(array[i][3][0]))
        thcond.write('\n')
        thcond.write('-\n')
        thcond.write('-\n')
    thcond.close()        

#Function returns number of pixels equal to the font size in pt
def pt_px(fs_pt):
    x = np.array([6., 6.75, 7., 7.5, 8., 8.25, 9., 9.75, 10., 10.5, 11., 11.25, 12., 12.75, 13., 13.5, 14., 14.25, 15., 15.75, 16., 16.5, 17., 17.25, 18., 18.75, 19., 19.5, 20.])
    y = np.array([8., 9., 9.333, 10., 10.667, 11., 12., 13., 13.333, 14., 14.667, 15., 16., 17., 17.333, 18., 18.667, 19., 20., 21., 21.333, 22., 22.667, 23., 24., 25., 25.333, 26., 26.667])
    fs_px = np.interp(fs_pt, x, y)
    
    return fs_px

#Connect all functions above to make thcond
def run_main_algorithm(filename):
    if filename == '' or filename == ' 'or filename == None:
        print('No file chosen')
    else:
        f = open(filename, 'r')
        data = f.readlines()
        Start_number = find_1P(data)
        list_a = form_points_list(data, Start_number)
        Axis = form_axis(data, Start_number)
        array = form_points_array(list_a)
        #Normalizing lines and axis to (0;0)
        array = normalize_trapezoids(array, Axis)
        create_thcond(array)
        f.close()


def thcond_to_np_array():    
    fname = 'THCOND.DAT'
    f = open(fname, 'r')
    data = f.readlines()
    i = 0
    for line in data:
        for sym in line:
            if sym == 'c':
                break
        i += 1
    data = data[:i]
    print(data)
    Array1 = np.zeros((len(data)//3,6), float)
    i = 0
    j = 0
    Temp = ''
    for line in data:
        for sym in line:
            if j == 6:
                j = 0
                i += 1
            if sym == 'c' or sym == '-':
                Temp = ''
                break
            else:
                if sym == ',' or sym == '\n':
                    Array1[i][j] = float(Temp)
                    j += 1
                    Temp = ''
                else:
                    Temp = Temp + sym
    return Array1
    

def run_pygame():    
    
    Array1 = thcond_to_np_array()
    #Preparing data
    array = np.zeros((np.shape(Array1)[0],4,2),float)
    for i in range(0, np.shape(Array1)[0]):
        array[i][0][0] = Array1[i][2]
        array[i][0][1] = Array1[i][0]
        array[i][1][0] = Array1[i][3]
        array[i][1][1] = Array1[i][0]
        array[i][2][0] = Array1[i][5]
        array[i][2][1] = Array1[i][1]
        array[i][3][0] = Array1[i][4]
        array[i][3][1] = Array1[i][1]
    
    Center = form_trapezoid_centers(array) 
    Axis = np.array([[0,0],[0,array[np.shape(Array1)[0] - 1][3][1]]])
    #Initialize pygame at the screen
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 14)
    clock = pygame.time.Clock() #Frame rate
    #Getting the monitor resolution
    Screen_scale = 0.5 #Multiplier in order to prevent of using user's full monitor space
    # Screen_Width = int(Screen_scale * GetSystemMetrics(0))
    # Screen_Height = int(Screen_scale * GetSystemMetrics(1))
    Screen_Width = 800
    Screen_Height = 600
    #Setting up screen with Width and Height above
    screen = pygame.display.set_mode((Screen_Width, Screen_Height))
    pygame.display.set_caption('Visualization')    
    #Initializing visualization arrays
    alpha = 1
    Array_V = array
    Center_V = Center
    Axis_V  = Axis
    #Defining colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    loop = 1
    CORAL = (128,0,0)
    DARKGREEN = (0, 255 ,128)
    COLOR = WHITE
    Font_size = 10
    while loop:
        screen.fill(COLOR)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                loop = 0                    
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:
                    print('MOUSEWHEEL UP')
                    alpha = 1.01
                    #Here we change the (0,0) to scale the screen from our mouse position
                    for i in range(0, np.shape(array)[0]):
                        Array_V[i][0][0] = alpha*(Array_V[i][0][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][0][1] = alpha*(Array_V[i][0][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][1][0] = alpha*(Array_V[i][1][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][1][1] = alpha*(Array_V[i][1][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][2][0] = alpha*(Array_V[i][2][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][2][1] = alpha*(Array_V[i][2][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][3][0] = alpha*(Array_V[i][3][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][3][1] = alpha*(Array_V[i][3][1] - event.pos[1]) + event.pos[1]
                        Center_V[i][0] = alpha*(Center_V[i][0] - event.pos[0]) + event.pos[0]
                        Center_V[i][1] = alpha*(Center_V[i][1] - event.pos[1]) + event.pos[1]
                    #Modify the axis
                    Axis_V[0][0] = alpha*(Axis_V[0][0] - event.pos[0]) + event.pos[0]
                    Axis_V[0][1] = alpha*(Axis_V[0][1] - event.pos[1]) + event.pos[1]
                    Axis_V[1][0] = alpha*(Axis_V[1][0] - event.pos[0]) + event.pos[0]
                    Axis_V[1][1] = alpha*(Axis_V[1][1] - event.pos[1]) + event.pos[1]
                    #End-------
                if event.button == 5:
                    print('MOUSEWHEEL DOWN')
                    alpha = 0.99
                    #Here we change the (0,0) to scale the screen from our mouse position
                    for i in range(0, np.shape(array)[0]):
                        Array_V[i][0][0] = alpha*(Array_V[i][0][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][0][1] = alpha*(Array_V[i][0][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][1][0] = alpha*(Array_V[i][1][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][1][1] = alpha*(Array_V[i][1][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][2][0] = alpha*(Array_V[i][2][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][2][1] = alpha*(Array_V[i][2][1] - event.pos[1]) + event.pos[1]
                        Array_V[i][3][0] = alpha*(Array_V[i][3][0] - event.pos[0]) + event.pos[0]
                        Array_V[i][3][1] = alpha*(Array_V[i][3][1] - event.pos[1]) + event.pos[1]
                        Center_V[i][0] = alpha*(Center_V[i][0] - event.pos[0]) + event.pos[0]
                        Center_V[i][1] = alpha*(Center_V[i][1] - event.pos[1]) + event.pos[1]
                    #Modify the axis
                    Axis_V[0][0] = alpha*(Axis_V[0][0] - event.pos[0]) + event.pos[0]
                    Axis_V[0][1] = alpha*(Axis_V[0][1] - event.pos[1]) + event.pos[1]
                    Axis_V[1][0] = alpha*(Axis_V[1][0] - event.pos[0]) + event.pos[0]
                    Axis_V[1][1] = alpha*(Axis_V[1][1] - event.pos[1]) + event.pos[1]
                    #End-------

        #Visualizing trapezoids
        for i in range(0, np.shape(array)[0]):
            pygame.draw.line(screen, BLACK, [Array_V[i][0][0], Array_V[i][0][1]], [Array_V[i][1][0], Array_V[i][1][1]], 2)
            pygame.draw.line(screen, BLACK, [Array_V[i][1][0], Array_V[i][1][1]], [Array_V[i][2][0], Array_V[i][2][1]], 2)
            pygame.draw.line(screen, BLACK, [Array_V[i][2][0], Array_V[i][2][1]], [Array_V[i][3][0], Array_V[i][3][1]], 2)
            pygame.draw.line(screen, BLACK, [Array_V[i][3][0], Array_V[i][3][1]], [Array_V[i][0][0], Array_V[i][0][1]], 2)
        #Vizualising centers of trapezoids with text number
        for i in range(0, np.shape(Center_V)[0]):
            font = pygame.font.SysFont('Times New Roman', int(Font_size), True, False)
            text = font.render(str(i+1), True, BLACK)
            screen.blit(text, [Center_V[i][0] - pt_px(Font_size)/3 , Center_V[i][1] - pt_px(Font_size)/3])
        #Visualising axis
        pygame.draw.line(screen, RED, [Axis_V[0][0], Axis_V[0][1]], [Axis_V[1][0], Axis_V[1][1]], 2)
        pygame.display.flip()
    clock.tick(60)
    pygame.quit()
