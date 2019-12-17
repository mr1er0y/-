from PIL import Image, ImageDraw, ImageFont
# выделение места под надпись на картинке
beg = 40
print("Введите числовую полседовательность")
N = list(map(int, input().split()))
print("Выберите способ кодирования", "NRZ", "NRZI", "MANCH", sep='\n')
im = Image.new('RGB', (beg + 64*len(N)+2, 13), color='white')
draw_s = ImageDraw.Draw(im)
# шрифт текста на картинке
font = ImageFont.truetype('minreg.ttf', 10)


def polyline_vertically(xy, color="black", width_l=1):
    """
    :param xy: coordinates of the beginning of the dotted line
    :param color: color of the dotted line
    :param width_l: width1 of the dotted line
    функция предназначенная для рисования пунктирных линий по вертикали
    """
    for i in range(xy[0][1], xy[1][1] - 5, 7):
        draw_s.line([(xy[0][0], i), (xy[1][0], i + 2)], fill=color, width=width_l)
    draw_s.line([(xy[0][0], xy[1][1] - 2), (xy[1][0], xy[1][1])], fill=color, width=width_l)


def polyline_horizon(xy, color='black', width1=1):
    """ 
    :param xy: координаты начала пунктирной линии
    :param color: цвет
    :param width1: ширина
    функция предназначенная для рисования пунктирных линий по горизонтали
    """
    for i in range(xy[0][0], xy[1][0] - 3, 8):
        draw_s.line([(i, xy[0][1]), (i + 3, xy[1][1])], fill=color, width=width1)


def nrz(code):
    """
    :param code: список заполненный значениями от 0 до 255
    функция предназначенная для рисования цифрового сигнала в кодировке NRZ
    Кодирование NRZ
    Для передачи единиц и нулей используются два устойчиво различаемых потенциала:
        биты 0 представляются нулевым напряжением 0 (В);
        биты 1 представляются значением U (В)
    """
    # вывод текста в начале картики
    draw_s.text((3, 1), text="NRZ", fill="black", width=1, font=font)
    point = [beg, im.size[1] - 2]
    # заполняю предыдущее значенние иверсией первого
    ls = not int(('0' * (8 - len((str(bin(code[0])))[2:])) + (str(bin(code[0])))[2:])[0])
    for i in code:
        t = (str(bin(i)))[2:]
        t = '0' * (8 - len(t)) + t
        for s in t:
            if not int(s) and ls:
                draw_s.line([(point[0], point[1]), (point[0], im.size[1] - 2)], fill="black", width=1)
                point[1] = im.size[1] - 2
            elif int(s) and not ls:
                point[1] = 1
                draw_s.line([(point[0], point[1]), (point[0], im.size[1] - 2)], fill="black", width=1)

            ls = int(s)
            draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black",  width=1)
            point[0] += 4


def nrzi(code):
    """
    :param code: список заполненный значениями от 0 до 255
    функция предназначенная для рисования цифрового сигнала в кодировке NRZI
    Кодирование NRZI
     При передаче последовательности единиц, сигнал, в отличие от других методов кодирования,
     не возвращается к нулю в течение такта.
     То есть смена сигнала происходит при передаче единицы, а передача нуля не приводит к изменению напряжения
    """
    # вывод текста в начале картинки
    draw_s.text((1, 1), text="NRZI", fill="black", width=1, font=font)
    point = [beg, im.size[1] - 2]
    # заполняю предыдущее значенние иверсией первого
    ls = not int(('0' * (8 - len((str(bin(code[0])))[2:])) + (str(bin(code[0])))[2:])[0])
    sm = 0
    for i in code:
        t = (str(bin(i)))[2:]
        t = '0' * (8 - len(t)) + t
        print(t)
        # polyline_vertically([(point[0], 2), (point[0], im.size[1] - 2)], 'grey')
        for s in t:
            # ищем 1 в последовательность и инвертируем ее
            if sm:
                s = not int(s)
            if not int(s) and ls:
                draw_s.line([(point[0], point[1]), (point[0], im.size[1] - 2)], fill="black", width=1)
                point[1] = im.size[1] - 2
            elif int(s) and not ls:
                point[1] = 1
                draw_s.line([(point[0], point[1]), (point[0], im.size[1] - 2)], fill="black", width=1)

            ls = int(s)
            draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black", width=1)
            point[0] += 4
            if s:
                sm = not sm


def manch(code):
    """
    :param code: список заполненный значениями от 0 до 255
    функция предназначенная для рисования цифрового сигнала в кодировке MANCH
    Манчестерский код
    Для передачи единиц и нулей используются два устойчиво различаемых потенциала:
        биты 0 представляются переходом от низкого напряжения к высокому
        биты 1 представляются переходом от высоко напряжения к низко
    """
    # вывод текста в начале картинки
    draw_s.text((1, 1), text="MANCH", fill="black", width=1, font=font)
    point = [beg, im.size[1] - 2]
    for i in code:
        t = (str(bin(i)))[2:]
        t = '0' * (8 - len(t)) + t
        for s in t:
            if int(s):
                if point[1] != 1:
                    draw_s.line([(point[0], 1), (point[0], im.size[1] - 2)], fill="black", width=1)
                    point[1] = 1
                # линия вправо
                draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black", width=1)
                point[0] += 4
                # линия вниз
                draw_s.line([(point[0], point[1]), (point[0], im.size[1] - 2)], fill="black", width=1)
                point[1] = im.size[1] - 2
                # линия вправо
                draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black", width=1)
                point[0] += 4
            else:
                if point[1] != (im.size[1] - 2):
                    draw_s.line([(point[0], im.size[1] - 2), (point[0], 1)], fill="black", width=1)
                    point[1] = im.size[1] - 2
                # линия вправо
                draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black", width=1)
                point[0] += 4
                # линия вверх
                draw_s.line([(point[0], im.size[1] - 2), (point[0], 1)], fill="black", width=1)
                point[1] = 1
                # линия вправо
                draw_s.line([(point[0], point[1]), (point[0] + 4, point[1])], fill="black", width=1)
                point[0] += 4


# рисую верхнюю и нижнюю линию с чередыющимся красным и зеленым цветом
polyline_horizon([(beg, 0), (im.size[0], 0)], 'red', 1)
polyline_horizon([(beg + 4, 0), (im.size[0], 0)], 'green', 1)
polyline_horizon([(beg, im.size[1]-1), (im.size[0], im.size[1]-1)], 'red', 1)
polyline_horizon([(beg + 4, im.size[1]-1), (im.size[0], im.size[1]-1)], 'green', 1)

tmp = input()
if tmp == "NRZ":
    nrz(N)
    print("Complete")
elif tmp == "NRZI":
    nrzi(N)
    print("Complete")
elif tmp == "MANCH":
    manch(N)
    print("Complete")
im.save('digital_signal.png')
im.show()
