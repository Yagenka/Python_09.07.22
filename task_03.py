# Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти

number = int(input('Введите номер четверти - '))

if number == 1:
   print ('x > 0, y > 0')
elif number == 2:
   print ('x < 0, y > 0')
elif number == 3:
   print ('x < 0, y < 0')
elif number == 4:
   print ('x > 0, y < 0')
else: print('координаты не определены')