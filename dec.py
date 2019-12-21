from PIL import Image


def decode_img(img, k):
    pix = img.load()
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
        sm = pix[43, 1] == (0, 0, 0)
        for i in range(40 + 3, img.size[0], 4):
            s = pix[i, 1] == (0, 0, 0)
            no = pix[i, 1] == (0, 0, 0)
            if sm:
                no = not no
            if no:
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
    return codes

