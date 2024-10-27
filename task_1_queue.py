from queue import Queue
import queue
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки
def generate_request(number_of_operations):
    try:
        # Перевіряємо, чи введено достатньо елементів
        parts = number_of_operations.split()
        if len(parts) != 2:
            raise ValueError("Invalid input: please enter both a task number and a task name.")

        number, name = parts
        n = int(number)
        task_number = 0
    except (ValueError, TypeError) as e:
        print(e)
        return  # Вийти, якщо сталася помилка
    else:
        for i in range(1, n + 1):
            task_number += 1
            task_name = f"{name}{task_number}"
            request_queue.put(task_name)
            print(f"Added task-{name}{task_number} to the queue")

# Функція для обробки заявок
def process_request():
    if request_queue.empty():
        print("Queue is empty, no requests to process.")
    else:
        while not request_queue.empty():
            task_name = request_queue.get()
            print(f"Processing task-{task_name}")
            time.sleep(2)  # Затримка для симуляції обробки

def main():
    while True:
        user_input = input("Enter a task of number and name [number, name] or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break
        else:
            generate_request(user_input)
            process_request()

if __name__ == "__main__":
    main()
