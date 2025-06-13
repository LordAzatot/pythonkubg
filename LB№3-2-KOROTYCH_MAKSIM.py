import csv

def modifier(filename):
    people = []

    # Читання даних з файлу
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Обробка кожного рядка і створення об'єктів Person
    for row in rows:
        person = Person(
            surname=row['surname'],
            first_name=row['first_name'],
            birth_date_str=row['birth_date'],
            nickname=row.get('nickname') or None
        )
        row['fullname'] = person.get_fullname()
        row['age'] = person.get_age()
        people.append(row)

    # Визначення нового порядку полів
    fieldnames = ['surname', 'first_name', 'fullname', 'nickname', 'birth_date', 'age']

    # Запис змінених даних назад у файл
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)

    print(f"Файл '{filename}' успішно оновлено.")
