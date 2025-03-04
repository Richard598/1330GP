import time,copy,random,curses
def creat_matrix(num):  ##define initial layout
    if num == 1:
        matrix = [['#','#','#','#','#','#'],
                    ['#','7','0','0','8','#'],
                    ['#','7','0','0','8','#'],
                    ['#','5','9','9','6','#'],
                    ['#','5','2','3','6','#'],
                    ['#','1','*','*','4','#'],
                    ['#','#','=','=','#','#']]
    elif num == 2:
        matrix = [['#','#','#','#','#','#'],
                    ['#','0','0','5','6','#'],
                    ['#','0','0','5','6','#'],
                    ['#','7','7','8','8','#'],
                    ['#','1','9','9','3','#'],
                    ['#','2','*','*','4','#'],
                    ['#','#','=','=','#','#']]
    return matrix
def solution(num):
    if num == 1:
        numbers = '2469512599334451194433561122933568807443357708862211995722044332255711044866043257144066823577033228663394411022339110'
        actions = 'sasddwasaawdwwddssaaaawwddddssaaassddwwwwassawwdwwawddssaasddwdwwwwaasssaawwdssdwwassassddddwwassssawwdwwddddsaaaawwdd'
    elif num == 2:
        numbers = '93387138665011332289449982746550337248996503311744055689224405668944071133568944220889220'
        actions = 'saasdwaassddwwwwwwaaawddssaaassddwwwwwaasssddddwwaawwdddssssaawwdddsssaaaawwwwddddsaawwdd'
    return numbers,actions
def move_down(matrix,num):     ##define movement function
    test = True
    matrix_change = copy.deepcopy(matrix)
    flag = ()
    for i in range(1,6):
        for j in range(1,5):
            if matrix[i][j] == num:
                flag += (i,j),      ##mark all particular pieces
                if matrix[i+1][j] != num and matrix[i+1][j] != '*':
                    test = False
    if test:                    ##check if the chess piece can be moved
        for x,y in flag:
            matrix_change[x][y] = '*'
        for x,y in flag:
            matrix_change[x+1][y] = num
        return matrix_change
    print('You cannot do that')
    time.sleep(1)
    return matrix
def move_up(matrix,num):
    test = True
    matrix_change = copy.deepcopy(matrix)
    flag = ()
    for i in range(1,6):
        for j in range(1,5):
            if matrix[i][j] == num:
                flag += (i,j),
                if matrix[i-1][j] != num and matrix[i-1][j] != '*':
                    test = False
    if test:
        for x,y in flag:
            matrix_change[x][y] = '*'
        for x,y in flag:
            matrix_change[x-1][y] = num
        return matrix_change
    print('You cannot do that')
    time.sleep(1)
    return matrix
def move_left(matrix,num):
    test = True
    matrix_change = copy.deepcopy(matrix)
    flag = ()
    for i in range(1,6):
        for j in range(1,5):
            if matrix[i][j] == num:
                flag += (i,j),
                if matrix[i][j-1] != num and matrix[i][j-1] != '*':
                    test = False
    if test:
        for x,y in flag:
            matrix_change[x][y] = '*'
        for x,y in flag:
            matrix_change[x][y-1] = num
        return matrix_change
    print('You cannot do that')
    time.sleep(1)
    return matrix
def move_right(matrix,num):
    test = True
    matrix_change = copy.deepcopy(matrix)
    flag = ()
    for i in range(1,6):
        for j in range(1,5):
            if matrix[i][j] == num:
                flag += (i,j),
                if matrix[i][j+1] != num and matrix[i][j+1] != '*':
                    test = False
    if test:
        for x,y in flag:
            matrix_change[x][y] = '*'
        for x,y in flag:
            matrix_change[x][y+1] = num
        return matrix_change
    print('You cannot do that')
    time.sleep(1)
    return matrix
def help_(matrix,solution_numbers,solution_actions):
    for _ in range(len(solution_actions)):
        number,action = solution_numbers[_],solution_actions[_]
        if action == 's':
            matrix = move_down(matrix,number)
        elif action == 'w':
            matrix = move_up(matrix,number)
        elif action == 'a':
            matrix = move_left(matrix,number)
        elif action == 'd':
            matrix = move_right(matrix,number)
        for row in matrix:
            print(' '.join(row))
        print('''

              ''')
        time.sleep(0.5)
def klotski():
    mode = random.randint(1,2)
    matrix = creat_matrix(mode)
    counter = 0
    solution_numbers,solution_actions = solution(mode)
    invert = {'w':'s','s':'w','a':'d','d':'a'}
    while matrix[5][2] != '0' or matrix[5][3] != '0':
        counter += 1
        for row in matrix:
            print(' '.join(row))
        if counter >= 5:
            print("If you need help, please print 'help'")
        x = input('Your input:').split()
        if x == ['help']:
            print('''


I will show you how to solve it from here.


''')
            time.sleep(2)
            for rows in matrix:
                print(' '.join(rows))
            print('''
            
            ''')
            time.sleep(0.5)
            help_(matrix,solution_numbers,solution_actions)
            print("Don't worry. It's indeed too hard.")
            return 0
        if len(x) != 2:
            print('Error: invalid input')
            time.sleep(1)
            print('''
''')
            continue
        if x[0] not in ('0','1','2','3','4','5','6','7','8','9') or x[1] not in ('a','s','d','w'):
            print('Error: invalid input')
            time.sleep(1)
            print('''
''')
            continue
        number,action = x
        previous_matrix = copy.deepcopy(matrix)
        if action == 's':
            matrix = move_down(matrix,number)
        elif action == 'w':
            matrix = move_up(matrix,number)
        elif action == 'a':
            matrix = move_left(matrix,number)
        elif action == 'd':
            matrix = move_right(matrix,number)
        if matrix != previous_matrix:
            solution_numbers = number + solution_numbers
            solution_actions = invert[action] + solution_actions
        print('''
              ''')
    print('Congratulation!!!')

def random_path(rightsteps, downsteps) :
    steps = []
    i, j = 0, 0
    while True :
        num = random.choices(['w', 'a', 's', 'd'], weights = [1, 1, 3, 3])
        if num == ['w'] :
            if i-1 >= 0 :
                i -= 1
                steps.append([i, j])
            else :
                continue
        if num == ['a'] :      
            if j-1 >= 0 :
                j -= 1
                steps.append([i, j])
            else :
                continue
        if num == ['s'] :
            if i+1 <= downsteps :
                i += 1
                steps.append([i, j])
            else :
                break
        if num == ['d'] :
            if j+1 <= rightsteps :
                j += 1
                steps.append([i, j])
            else :
                break
    return steps

def generate_deadends(steps, rightsteps, downsteps) :
    temp = []
    for index in range(1,len(steps)-1):
        first_step = True
        i = steps[index][0]
        j = steps[index][1]
        count = 0
        while True:
            num = random.choices([[1, 0], [-1, 0], [0, 1], [0, -1]],weights = [2,1,2,1])[0]
            count += 1
            i += num[0]
            j += num[1]
            deadend = [i,j]
            flag = True
            if count > 100:
                break
            if 0 <= deadend[0] <= downsteps and 0 <= deadend[1] <= rightsteps :
                for p,q in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if first_step:
                        if [i+p,j+q] in temp[:-1] or [i+p,j+q] in steps[:index] or [i+p,j+q] in steps[index+1:]:
                            flag = 0
                    else:
                        if [i+p,j+q] in temp[:-1] or [i+p,j+q] in steps:
                            flag = 0
                if flag:
                    temp.append(deadend)
                    count = 0
                    first_step = False
                else:
                    i -= num[0]
                    j -= num[1]
                continue
            break
    return temp

def generate_maze(length, width, steps, temp) :
    maze = [['#' for _ in range(length)] for _ in range(width)]
    for step in steps :
        maze[step[0]][step[1]] = ' '
    for k in temp :
        maze[k[0]][k[1]] = ' '
    return maze

def usermove(position, rightsteps, downsteps, maze, steps, temp) :
    valid_input = {'w': [-1, 0], 'a': [0, -1], 's': [1, 0], 'd': [0, 1]}
    isvalid = False
    while isvalid == False :
        move = input('Your move: ')
        if move not in valid_input :
            print('Invalid input. Please try again.')
        elif [position[0]+valid_input[move][0], position[1]+valid_input[move][1]] in steps or [position[0]+valid_input[move][0], position[1]+valid_input[move][1]] in temp :
            isvalid = True
            position[0] += valid_input[move][0]
            position[1] += valid_input[move][1]
        else :
           print('Invalid input. Please try again.') 
    return position

def current_maze(maze, position, steps) :
    maze[0][0] = 'S'
    maze[steps[len(steps)-1][0]][steps[len(steps)-1][1]] = 'E'
    maze[position[0]][position[1]] = 'C'
    for k in maze :
        print(' '.join(k))
    maze[position[0]][position[1]] = ' '
    maze[steps[len(steps)-1][0]][steps[len(steps)-1][1]] = ' '
    maze[0][0] = ' '

def check_win(position, steps) :
    if position[0] == steps[len(steps)-1][0] and position[1] == steps[len(steps)-1][1] :
        print('You win!')
        return True
    else :
        return False

def choose_mode() :
    temp = False
    while not temp :
        mode = input('mode: ')
        if mode == 'easy' :
            length = 5
            width = 5
            temp = True
        elif mode == 'medium' :
            length = 10
            width = 10
            temp = True
        elif mode == 'hard' :
            length = 20
            width = 20
            temp = True
        elif mode == 'selfdesign' :
            length = int(input('length: '))
            width = int(input('width: '))
            temp = True
        else :
            print('Invalid input. Please try again.')
    return length, width

def maze() :
    length, width = choose_mode()
    rightsteps = length - 1
    downsteps = width - 1
    position = [0, 0]
    steps = random_path(rightsteps, downsteps)
    temp = generate_deadends(steps, rightsteps, downsteps)
    maze = generate_maze(length, width, steps, temp)
    current_maze(maze, position, steps)
    while True :
        position = usermove(position, rightsteps, downsteps, maze, steps, temp)
        current_maze(maze, position, steps)
        if check_win(position, steps) == True :
            break

def loading_bar(stdscr, game_name, duration):
    for i in range(51):
        time.sleep(duration / 200)  
        stdscr.addstr(8, 2, f"Loading {game_name}: {'█' * i}{' ' * (50 - i)} {i * 2}%")
        stdscr.refresh()
        
    stdscr.addstr(9, 2, 'The game will start soon, enjoy!')  
    stdscr.refresh()
    time.sleep(2)


def main(stdscr):

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.border()  

    # 选项列表
    options = ["KLOTSKI", "MAZE"]
    current_index = 0

    while True:
        stdscr.clear()
        stdscr.border()  
        stdscr.addstr(1, 2, "Welcome to ENGG 1330 group project games!  :)", curses.color_pair(1))
        stdscr.addstr(3, 2, "Please choose a game by using the \"↑\" or \"↓\" button and then press the \"ENTER\" button to confirm your choice!")

        # 显示选项
        for index, option in enumerate(options):
            if index == current_index:
                stdscr.addstr(5 + index, 2, f"> {option}", curses.A_REVERSE)  
            else:
                stdscr.addstr(5 + index, 2, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()  

        if key == curses.KEY_UP:  
            current_index = (current_index - 1) % len(options)
        elif key == curses.KEY_DOWN:  
            current_index = (current_index + 1) % len(options)
        elif key == curses.KEY_ENTER or key in [10, 13]:  
            break
    
    stdscr.clear()
    stdscr.border()  
    global game_name
    game_name = options[current_index]
    loading_bar(stdscr, game_name, 2.5)  
    
    
curses.wrapper(main)
if game_name == 'KLOTSKI':  
    klotski()
elif game_name == 'MAZE':
    maze()