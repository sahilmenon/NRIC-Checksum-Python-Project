def ST(d):
    dict = {
        0: 'J', 1: 'Z',2: 'I', 3: 'H', 4: 'G', 5: 'F', 6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'}
    return dict.get(d)

def FG(d):
    dict = {0: 'X', 1: 'W', 2: 'U', 3: 'T', 4: 'R', 5: 'Q', 6: 'P', 7: 'N', 8: 'M', 9: 'L', 10: 'K'}
    return dict.get(d)

nric = input('Enter the nric to validate: ')

d = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

if nric[0] == 'T' or nric[0] == 'G':
    d = d + 4

d = d % 11

if nric[0] == 'S' or nric[0] == 'T':
    x = ST(d)

    if nric[8] == x:
        print('nric is valid')
        quit()
    else:
        print('nric is invalid')
        quit()
elif nric[0] == 'F' or nric[0] == 'G':
    x = FG(d)

    if nric[8] == x:
        print('nric is valid')
    else:
        print('nric is invalid')

