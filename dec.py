from PIL import Image
img = Image.open("digital_signal.png")
pix = img.load()
print("Выберите способ кодирования", "NRZ", "NRZI", "MANCH", sep='\n')
k = input()
codes = []
if k == 'NRZ':
    t = ''
    for i in range(40 + 3, img.size[0], 4):
        if pix[i, 1] == (0, 0, 0):
            t = t + '1'
        else:
            t = t + '0'
        if len(t) == 8:
            codes.append(int(t, 2))
            t = ''
elif k == 'NRZI':
    t = ''
    ls = pix[43, 1] == (0, 0, 0)
    s = pix[43, 1] == (0, 0, 0)
    sm = 0
    for i in range(40 + 3, img.size[0], 4):
        if sm:
            s = not pix[i, 1] == (0, 0, 0)
        else:
            s = pix[i, 1] == (0, 0, 0)
        if s:
            t = t + '1'
        else:
            t = t + '0'

        if s != ls:
            sm = not sm
        ls = s
        if len(t) == 8:
            codes.append(int(t, 2))
            t = ''
elif k == 'MANCH':
    t = ''
    for i in range(40 + 3, img.size[0] - 4, 8):
        # print(pix[i + 4, img.size[1]-2])
        if pix[i, 1] == (0, 0, 0) and pix[i + 4, img.size[1]-2] == (0, 0, 0):
            t = t + '1'
        else:
            t = t + '0'
        if len(t) == 8:
            codes.append(int(t, 2))
            t = ''
for i in codes:
    print(i, end=" ")
