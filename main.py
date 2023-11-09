import os, math

n = 23

def main_menu():
    while True:
        os.system("cls")
        print("|1| Завдання 1")
        print("|2| Завдання 2.1")
        print("|3| Завдання 2.2")
        print("|4| Завдання 2.3")
        print("|5| Завдання 2.4")
        print("|6| Завдання 2.5")
        print("|7| Завдання 2.6")
        print("|8| Запитання та відповіді")
        print("|9| Вихід")

        choice = input("\nВиберіть завдання: \n")

        if choice == "1":
            section1()
        elif choice == "2":
            section2_1()
        elif choice == "3":
            section2_2()
        elif choice == "4":
            section2_3()
        elif choice == "5":
            section2_4()
        elif choice == "6":
            section2_5()
        elif choice == "7":
            section2_6()
        elif choice == "8":
            section2_7()
        elif choice == "9":
            os.system('cls')
            print("Програму завершено")
            break
        else:
            print("Некоректний вибір.")

def section1():
    os.system('cls')
    d, m = 2, 12
    result = (123/d+45*m-66*(3+n))
    print(f"\n\nРезультат : {result}\n\n") 
    input("Натисніть Enter, щоб повернутися в головне меню.\n")

def section2_1():
    os.system('cls')
    result = 2.3 + 106 * n
    print(f"\n\nРезультат : {result}\n\n")
    input("Натисніть Enter, щоб повернутися в головне меню.\n")

def section2_2():
    os.system("cls")
    result = 2.3 + 106 / n
    print(f"\n\nРезультат : {result}\n\n")
    input("Натисніть Enter, щоб повернутися в головне меню.\n")

def section2_3():
    os.system("cls")
    print("Обчислення площі трикутника\n\n")
    while True:
        try:
            first_side = float(input('\nВведіть першу сторону в см : \n'))
            second_side = float(input('Введіть другу сторону в см : \n'))
            third_side = float(input('Введіть третю сторону в см : \n'))
            break
        except ValueError:
            print("Помилка: Введені значення мають бути числами. Спробуйте знову.")

    p = (first_side + second_side + third_side) / 2
    result = (p * (p - first_side) * (p - second_side) * (p - third_side)) ** 0.5
    print(f"\nРезультат : {result} см^2")
    input("\nНатисніть Enter, щоб повернутися в головне меню.\n")

def section2_4():
    os.system("cls")
    print("Обчислення площі прямокутного трикутника\n\n")
    while True:
        try:
            katet1 = float(input('Введіть довжину першого катета в см: \n'))
            katet2 = float(input('Введіть довжину другого катета в см: \n'))
            break
        except ValueError:
            print("Помилка: Введені значення мають бути числами. Спробуйте знову.")

    result = (katet1**2)+(katet2**2)
    print(f"\nРезультат: {result ** 0.5}")
    input("\nНатисніть Enter, щоб повернутися в головне меню.\n")

def section2_5():
    os.system("cls")
    print("Визначення площі кола, яку не зайнято трикутником.\n\n")
    r = float(input("Введіть радіус кола в см: \n"))
    full_circle_area = math.pi * r**2
    triangle_area = (3 * math.sqrt(3) / 2) * r**2
    remaining_area = full_circle_area - triangle_area
    print(f"\nРезультат: {remaining_area:.2f}  - площа кола, яку не займає трикутник")
    input("\nНатисніть Enter, щоб повернутися в головне меню.\n")

def section2_6():
    os.system("cls")
    a = float(input("Введіть площу трикутника в см : \n"))
    triangle_area = (a**2 * math.sqrt(3)) / 4
    r = (a * math.sqrt(3)) / 6
    circle_area = math.pi * r**2
    print(f"\n{triangle_area - circle_area} - площа трикутника, яку не зайнято колом.")
    input("\nНатисніть Enter, щоб повернутися в головне меню.\n")
def section2_7():
    questions = {
        "question1": "За якими ознаками класифікують мови програмування?\n",
        "answer1": "\n1. Рівень абстракції: мови низького рівня (машинно-залежні) і мови високого рівня (машинно-незалежні).\n2. Парадигма програмування: мови імперативні (структурні, об’єктно-орієнтовані, процедурні), декларативні (функціональні, логічні), гібридні (багатопарадигмові).\n3. Спосіб перетворення коду в машинні інструкції: мови компільовані (трансляція виконується один раз перед запуском програми), мови інтерпретовані (трансляція виконується під час запуску програми), мови змішаного типу (трансляція виконується частково перед запуском і частково під час запуску програми).\n4. Галузь застосування: мови загального призначення (можуть використовуватися для різних задач), мови спеціального призначення (призначені для певної галузі або класу задач).",
        "question2": "Як завершується робота інтерпретатора в інтерактивному режимі?\n",
        "answer2": "\nРобота інтерпретатора в інтерактивному режимі завершується, коли користувач вводить спеціальну команду для виходу з інтерпретатора. Наприклад, в Python ця команда - quit() або exit().",
    }
    os.system("cls")
    while True:
        try:
            choose = int(input("Щоб вибрати завдання натисніть 1-2\nЩоб вийти натисніть 0 \n\n"))
            if choose == 1:
                os.system("cls")
                print(questions["question1"] + questions["answer1"])
                input("\nНатисніть Enter, щоб повернутися до меню завдань.\n")
            if choose == 2:
                os.system("cls")
                print(questions["question2"] + questions["answer2"])
                input("\nНатисніть Enter, щоб повернутися до меню завдань.\n")
            if choose == 0:
                break
            else:
                os.system("cls")
                print("Помилка, немає такого завдання")
        except KeyError:
            print("Помилка. Спробуйте ще раз.")
        


if __name__ == "__main__":
    main_menu()
