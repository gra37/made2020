x = int(input())
final = []


for _ in range(x):
    s = int(input()) # число тегов
    teg = []
    bad_teg = []

    for i in  range(s):

        cur_teg = input().strip().lower()
        if list(cur_teg)[1] != '/':
            last_teg = cur_teg
            teg.append(cur_teg)
        elif list(cur_teg)[1] == '/' and len(teg) == 0:
            bad_teg.append(cur_teg)
        elif list(cur_teg)[1] == '/' and len(teg) != 0:
            if list(cur_teg)[2:-1] == list(teg[-1])[1:-1]:
                teg.pop()
            else:
                bad_teg.append(cur_teg)

    if len(teg) == 0 and len(bad_teg) == 0:
        final.append('CORRECT')
    elif len(teg) == 0 and len(bad_teg) == 1:
        final.append('ALMOST ' + bad_teg[0].upper())
    elif len(teg) == 1 and len(bad_teg) == 0:
        final.append('ALMOST ' + teg[0].upper())
    else:
        final.append('INCORRECT')

for x in final: print(x)
