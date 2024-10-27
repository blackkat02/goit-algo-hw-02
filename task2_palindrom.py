from collections import deque


def palindromic(word: str):
    d = deque()

    # Додаємо символи, ігноруючи пробіли та регістр
    for i in word.lower():
        if i != " ":
            d.append(i)

    # Перевіряємо всі символи
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False  # Якщо хоча б одна пара не співпадає, це не паліндром

    return True  # Якщо всі символи співпали, це паліндром


# Тестування
print(palindromic("qwerttrewq"))  # True
print(palindromic("1234567"))  # False
print(palindromic("qwertytrewq"))  # True
print(palindromic("1234321"))  # True
print(palindromic("A man a plan a canal Panama"))  # True
print(palindromic("madam in eden im adam"))
print(palindromic("qw  ert tr ewq"))
print(palindromic("1234567"))
print(palindromic("qwErtytreWq"))
print(palindromic("1234321"))
print(palindromic("A man"))


