#Создаем игру угадай число
import random
quessesTaken = 0
print('Привет, давай познакомимся. Как твое имя?')
name = input()
print('Ну чтож', name, 'хочешь сыграть со мной в игру?')
quest1 = input()
if quest1 == 'нет' or quest1 == 'Нет':
    print('ну тогда пока, приходи когда захочешь')
if quest1 == 'да' or quest1 == 'Да':
    print('игра называется УГАДАЙ ЧИСЛО')
    print('Тебе нужно отгадать число от 1 до 10, ЗА 3 попытки')
    print('Какое твое первое число?')
    number = random.randint(1, 10)
    for i in range(3):
        num = int(input())
        if num == number:
            print('Молодец! Ты победил, именно это число я загадал')
            break
        if num < number:
            print('Число точно больше, попробуй еще раз')
        if num > number:
            print('Число точно меньше, попробуй еще раз')
    if num!=number:
        print('ТЫ ПРОИГРАЛ! моя взяла, попробуй в другой раз', name)

        
