import os, time, random
import doctest

def map(step, row, type):
    def way(row, st, sp):
        col_st = col(st)
        col_sp = col(sp)
        ch1 = ch2 = 0
        if int(sp[0]) > int(st[0]) and col_sp > col_st:
            if (col_sp - col_st) // 2 == int(sp[0]) - int(st[0]):
                for i in range(1, int(sp[0]) - int(st[0])):
                    if row[8 - int(st[0]) - i][col_st + i * 2] == type[2]:
                        ch1 += 1
                        ch2 = i
                    if row[8 - int(st[0]) - i][col_st + i * 2] == type[0]:                        
                        ch1 = 2
                        break
                if ch1 <= 1:
                     start(row, st, col_st)
                     if ch1 == 1: medium(row, 8 - int(st[0]) - ch2, col_st + ch2 * 2)
                     stop(row, sp, col_sp, type[1])
                     
        if int(sp[0]) > int(st[0]) and col_sp < col_st:            
            if (col_st - col_sp) //  2 == int(sp[0]) - int(st[0]):
                for i in range(1, int(sp[0]) - int(st[0])):
                    if row[8 - int(st[0]) - i][col_st - i * 2] == type[2]:
                        ch1 += 1
                        ch2 = i
                    if row[8 - int(st[0]) - i][col_st - i * 2] == type[0]:
                        ch1 = 2
                        break
                if ch1 <= 1:
                    start(row, st, col_st)
                    if ch1 == 1: medium(row, 8 - int(st[0]) - ch2, col_st - ch2 * 2)
                    stop(row, sp, col_sp, type[1])
                    
        if int(sp[0]) < int(st[0]) and col_sp > col_st:
            if (col_sp - col_st) // 2 == int(st[0]) - int(sp[0]):
                for i in range(1, int(st[0]) - int(sp[0])):
                	    if row[8 - (int(st[0]) - i)][col_st + i * 2] == type[2]:
                	        ch1 += 1
                	        ch2 = i
                	    if row[8 - (int(st[0]) - i)][col_st - i * 2] == type[0]:
                	        ch1 = 2
                	        break
                if ch1 <= 1:
                	    start(row, st, col_st)
                	    if ch1 == 1: medium(row, 8 - (int(st[0]) - ch2), col_st + ch2 * 2)
                	    stop(row, sp, col_sp, type[1])
        
        if int(sp[0]) < int(st[0]) and col_sp < col_st:
            if (col_st - col_sp) // 2 == int(st[0]) - int(sp[0]):
                for i in range(1, int(st[0]) - int(sp[0])):
                    if row[8 - (int(st[0]) - i)][col_st - i * 2] == type[2]:
                        ch1 += 1
                        ch2 = i
                    if row[8 - (int(st[0]) - i)][col_st - i * 2] == type[0]:
                        ch1 = 2
                        break
                if ch1 <= 1:
                    start(row, st, col_st)
                    if ch1 == 1: medium(row, 8 - int(st[0]) + ch2, col_st - ch2 * 2)
                    stop(row, sp, col_sp, type[1])
        
    def start(row, st, col_st):
        tm = row[8 - int(st[0])]
        tm = tm[:col_st] + "❇" + tm[col_st + 1:]
        row[8 - int(st[0])] = tm

    def stop(row, sp, col_sp, rank):
        tm = row[8 - int(sp[0])]
        tm = tm[:col_sp] + rank + tm[col_sp + 1:]
        row[8 - int(sp[0])] = tm
        
    def medium(row, nrow, colrow):
        tm = row[nrow]
        tm = tm[:colrow] + "❇" + tm[colrow + 1:]
        row[nrow] = tm

        
    st = step[0]
    sp = step[1]
    col_st = col(st)
    col_sp = col(sp)
    
##If normal step
    if row[8 - int(sp[0])][col_sp] == "❇" and row[8 - int(st[0])][col_st] == type[0] and abs(int(sp[0]) - int(st[0])) == 1:
        rank = type[1] if int(sp[0]) == (8 if type[0] == '⚪' else 0) else type[0]
        stop(row, sp, col_sp, rank)
        start(row, st, col_st)
    
##If normal battle
    elif row[8 - int(sp[0])][col_sp] == "❇" and row[8 - int(st[0])][col_st] == type[0]:
        if row[8 - (int(sp[0]) + int(st[0])) // 2][(col_st + col_sp) // 2] == type[2]:
            rank = type[1] if int(sp[0]) == (8 if type[0] == '⚪' else 0) else type[0]
            stop(row, sp, col_sp, rank)
            medium(row, 8 - (int(sp[0]) + int(st[0])) // 2, int((col_st + col_sp) / 2))
            start(row, st, col_st)
                        
##If queen
    elif row[8 - int(st[0])][col_st] == type[1] and row[8 - int(sp[0])][col_sp] == "❇":
        way(row, st, sp)
    
def col(ss):
    abc = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(0, len(abc)):
        col = (i * 2 if ss[1] == abc[i].lower() or ss[1] == abc[i] else 0)
        if ss[1] == abc[i]: break
    return(col)

def cm_step(row):
    all_steps = []
    top_steps = []
    abc = ["A", "B", "C", "D", "E", "F", "G", "H"]
    queen = 0
    
##Search all_steps
    for i in range(0, 8):
        for o in range(0, 15):
            if row[i][o] == 'Ⓜ': queen += 1
            if row[i][o] == '⚫' or row[i][o] == 'Ⓜ':
                st = str(8 - i) + abc[int(o / 2)]
                meed = '%'
                lel = 2 if row[i][o] == '⚫' else i + 1
                for l in range(1, lel):
                    if o + l * 2 > 14  or i == -1 + l: break
                    if row[i - l][o + l * 2] == '⚪':
                        meed = '$' if meed == '%' else '$$'
                        if row[i][o] == '⚫': l += 1
                    if o + l * 2 > 14: break
                    if meed == '$' and row[i - l][o + l * 2] == '⚪': break
                    if meed == '$$' or row[i - l][o + l * 2] == '⚫' or row[i + l][o + l * 2] == 'Ⓜ': break
                    all_steps += [st + meed + str(8 - i + l) + abc[int((o + l * 2) / 2)]]
                meed = '%'
                lel = 2 if row[i][o] == '⚫' else i + 1
                for l in range(1, lel):
                    if o - l * 2 < 0  or i == -1 + l: break
                    if row[i - l][o - l * 2] == '⚪':
                        meed = '$' if meed == '%' else '$$'
                        if row[i][o] == '⚫': l += 1
                    if o - l * 2 < 0: break
                    if meed == '$' and row[i - l][o - l * 2] == '⚪': break
                    if meed == '$$' or row[i - l][o - l * 2] == '⚫' or row[i + l][o - l * 2] == 'Ⓜ': break
                    all_steps += [st + meed + str(8 - i + l) + abc[int((o - l * 2) / 2)]]
                meed = '%'
                lel = 2 if row[i][o] == '⚫' else i + 1
                for l in range(1, lel):
                    if o + l * 2 > 14  or i == 8 - l: break
                    if row[i + l][o + l * 2] == '⚪':
                        meed = '$' if meed == '%' else '$$'
                        if row[i][o] == '⚫': l += 1
                    if o + l * 2 > 14: break
                    if meed == '$' and row[i + l][o + l * 2] == '⚪': break
                    if meed == '$$' or row[i + l][o + l * 2] == '⚫' or row[i + l][o + l * 2] == 'Ⓜ': break
                    all_steps += [st + meed + str(8 - i - l) + abc[int((o + l * 2) / 2)]]
                meed = '%'
                lel = 2 if row[i][o] == '⚫' else i + 1
                for l in range(1, lel):
                    if o - l * 2 < 0 or i == 8 - l: break
                    if row[i + l][o - l * 2] == '⚪':
                        meed = '$' if meed == '%' else '$$'
                        if row[i][o] == '⚫': l += 1
                    if o - l * 2 < 0: break
                    if meed == '$' and row[i + l][o - l * 2] == '⚪': break
                    if meed == '$$' or row[i + l][o - l * 2] == '⚫' or row[i + l][o - l * 2] == 'Ⓜ': break
                    all_steps += [st + meed + str(8 - i - l) + abc[int((o - l * 2) / 2)]]

##Search top_steps
    for i in range(0, len(all_steps)):
        if all_steps[i][2] == '$': top_steps += [all_steps[i]]
    if len(top_steps) > 0:
        return top_steps[random.randint(0,len(top_steps)-1)].split('$')
    if queen == 0:
        for i in range(0, len(all_steps)):
            if all_steps[i][0] > all_steps[i][3]: top_steps += [all_steps[i]]
        if len(top_steps) > 0:
            return top_steps[random.randint(0,len(top_steps)-1)].split('%')
        else: return all_steps[random.randint(0,len(all_steps)-1)].split('%')
    else: return all_steps[random.randint(0,len(all_steps)-1)].split('%')
            
def pix(row, num, let):
    print("\n" + let)
    for i in range(0, 8):
        print("     " + num[i] + row[i] + num[i])
    print(let + "\n")
    
def loading():
    start = time.time()
    dot = ''
    print(' Loading', end=' ')
    while True:
        if time.time() - 1 - len(dot) > start:
             dot += '.'
             if len(dot) == 4: break
             print(dot[0], end=' ')

    
os.system('clear')

##chips = ⚫⚪
##blank = ❇
##queen = Ⓜ⚾

row1 = "  ⚪   ⚪   ⚪   ⚪"
row2 = "⚪   ⚪   ⚪   ⚪  "
row3 = "  ⚪   ⚪   ⚪   ⚪"
row4 = "❇   ❇   ❇   ❇  "
row5 = "  ❇   ❇   ❇   ❇"
row6 = "⚫   ⚫   ⚫   ⚫  "
row7 = "  ⚫   ⚫   ⚫   ⚫"
row8 = "⚫   ⚫   ⚫   ⚫  "
num = ("  8  ", "  7  ", "  6  ", "  5  ", "  4  ", "  3  ", "  2  ", "  1  ")
let = "\n" + "          A◽B▫C◽D◽E◽F▫G◽H" + "\n"

row = [row8, row7, row6, row5, row4, row3, row2, row1]
type = ""
stat_you = 0
stat_cm = 0

while True:
    
    pix(row, num, let)

##User step:
    try:
        step = (input("Enter your step => ")).split(" ")
        map(step, row, "⚪⚾⚫Ⓜ")
    except:
        step = (input("ReEnter your step => ")).split(" ")
        map(step, row, "⚪⚾⚫Ⓜ")
        
    for i in range(0, len(row)):
        for o in range(0, len(row[i])):
            if row[i][o] == '⚪' or row[i][o] == '⚾': stat_you += 1
            if row[i][o] == '⚫' or row[i][o] == 'Ⓜ': stat_cm += 1
    
    os.system('clear')
    pix(row, num, let)
    
    if stat_you == 0:
        print('\n    You Lost!')
        break
    if stat_cm == 0:
        print('\n    You Won!')
        break
    
    loading()
    os.system('clear')

##Computer step:
    map(cm_step(row), row, "⚫Ⓜ⚪⚾")
    
    for i in range(0, len(row)):
        for o in range(0, len(row[i])):
            if row[i][o] == '⚪' or row[i][o] == '⚾': stat_you += 1
            if row[i][o] == '⚫' or row[i][o] == 'Ⓜ': stat_cm += 1
    
    if stat_you == 0:
        print('/n    You Lost!')
        break
    if stat_cm == 0:
        print('/n    You Won!')
        break