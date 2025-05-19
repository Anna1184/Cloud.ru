# Описание проекта
cloud_arr.py - Python-скрипт для работы с числовыми списками

test_py.py - UI-тест веб-страницы https://example.com с использованием библиотеки Playwright

## Требования
* Python 3.7 или выше

## Установка зависимостей
###### bash
    pip install pytest
    pip install playwright
    playwright install

## Используемые библиотеки:
  * playwright==1.52.0 (для test_py.py)
  * pytest==8.3.5 (для test_py.py)

# Запуск скрипта cloud_arr.py
1) Запустите скрипт:
    ###### bash
        python cloud_arr.py
2) Введите числа через запятую (пример ввода: 1, 3, 4, 7, 8, 10).

3) Результат появится на экране.

# Запуск test_py.py
1) Запустите тест:
    ###### bash
        python test_py.py

2) Тестирование веб-страницы

   * Открывает страницу https://example.com.
   * Проверяет, что заголовок содержит  "Example".
   * Находит кнопку "More information" и кликает.
   * Проверяет, что URL изменился на https://www.iana.org/help/example-domains.
