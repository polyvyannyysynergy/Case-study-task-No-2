from datetime import datetime

# Запрос данных у пользователя
def get_birth_date():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return day, month, year

# Определение дня недели для даты рождения
def get_weekday(day, month, year):
    date = datetime(year, month, day)
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days_of_week[date.weekday()]

# Проверка на високосный год
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Определение текущего возраста
def calculate_age(day, month, year):
    today = datetime.today()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Функция для отображения даты рождения звездочками
def display_star_date(day, month, year):
    digits = {
        '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        '1': ['  *  ', ' **  ', '  *  ', '  *  ', '*****'],
        '2': [' *** ', '*   *', '   * ', '  *  ', '*****'],
        '3': [' *** ', '*   *', '   **', '*   *', ' *** '],
        '4': ['   * ', '  ** ', ' * * ', '*****', '   * '],
        '5': ['*****', '*    ', ' *** ', '    *', ' *** '],
        '6': [' *** ', '*    ', '**** ', '*   *', ' *** '],
        '7': ['*****', '    *', '   * ', '  *  ', ' *   '],
        '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
        '9': [' *** ', '*   *', ' ****', '    *', ' *** ']
    }

    def print_digit(num):
        lines = ['' for _ in range(5)]
        for digit in str(num):
            for i in range(5):
                lines[i] += digits[digit][i] + '  '
        return lines

    day_lines = print_digit(f'{day:02d}')
    month_lines = print_digit(f'{month:02d}')
    year_lines = print_digit(str(year))

    for i in range(5):
        print(day_lines[i] + '  ' + month_lines[i] + '  ' + year_lines[i])

# Вывод даты рождения в формате, как на электронном табло с использованием звездочек.
def main():
    day, month, year = get_birth_date()
    print(f"Вы родились в: {get_weekday(day, month, year)}")
    print(f"Високосный год? {'Да' if is_leap_year(year) else 'Нет'}")
    print(f"Ваш возраст: {calculate_age(day, month, year)} лет")
    print("Дата рождения:")
    display_star_date(day, month, year)

if __name__ == "__main__":
    main()
