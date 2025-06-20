def calculator():
    print("=== Калькулятор ===")
    print("Доступные операции: +, -, *, /, ** (степень), % (остаток от деления)")
    print("Для выхода введите 'выход' или 'exit'")
    print()
    
    while True:
        try:
            # Ввод первого числа
            num1_input = input("Введите первое число: ")
            if num1_input.lower() in ['выход', 'exit']:
                print("До свидания!")
                break
            num1 = float(num1_input)
            
            # Ввод операции
            operation = input("Введите операцию (+, -, *, /, **, %): ")
            if operation not in ['+', '-', '*', '/', '**', '%']:
                print("Ошибка: неверная операция!")
                continue
            
            # Ввод второго числа
            num2_input = input("Введите второе число: ")
            if num2_input.lower() in ['выход', 'exit']:
                print("До свидания!")
                break
            num2 = float(num2_input)
            
            # Выполнение операции
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 % num2
            
            # Вывод результата
            print(f"Результат: {num1} {operation} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("Ошибка: введите корректное число!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        
        print()

# Запуск калькулятора
if __name__ == "__main__":
    calculator()