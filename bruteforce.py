def ST(d):
    dict = {
        0: 'J', 1: 'Z',2: 'I', 3: 'H', 4: 'G', 5: 'F', 6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'}
    return dict.get(d)

def FG(d):
    dict = {0: 'X', 1: 'W', 2: 'U', 3: 'T', 4: 'R', 5: 'Q', 6: 'P', 7: 'N', 8: 'M', 9: 'L', 10: 'K'}
    return dict.get(d)

def validator(nric):
    d = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

    if nric[0] == 'T' or nric[0] == 'G':
        d = d + 4

    d = d % 11

    if nric[0] == 'S' or nric[0] == 'T':
        x = ST(d)

        if nric[8] == x:
            return True
        else:
            return False
    elif nric[0] == 'F' or nric[0] == 'G':
        x = FG(d)

        if nric[8] == x:
            return True
        else:
            return False

def permutator(list, n):

    if n==0: yield []
    else:
        for i in range(len(list)):
            for f in permutator(list,n-1):
                yield [list[i]]+f

def brute_forcer(nric4):
    f = open('nric.txt', 'a')
    f.write(f'All posible combinations for NRIC ending with {nric4}\n')
    f.close()
    for r in permutator(['0','1','2','3','4','5','6','7','8','9'],4):
        for i in range(4):
            nric = []
            if i == 0:
                nric.append('S')
                nric.append(''.join(r))
                nric.append(nric4)
                
                # try nric
                success = validator(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            elif i == 1:
                nric.append('T')
                nric.append(''.join(r))
                nric.append(nric4)

                success = validator(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            elif i == 2:
                nric.append('F')
                nric.append(''.join(r))
                nric.append(nric4)

                success = validator(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            else:
                nric.append('G')
                nric.append(''.join(r))
                nric.append(nric4)

                success = validator(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()

nric4 = input("Please input the last 4 digits of the nric: ")
brute_forcer(nric4)