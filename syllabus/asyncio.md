# Курс: Async Python (async/await/asyncio)

## Формат
- Урок → задание → тесты → рефакторинг → коммит
- Команда проверки: `make check`

## Модули
### M1. База async/await
1. Coroutine, await, asyncio.run
2. Event loop и точки переключения (await)
3. Concurrency: gather vs последовательное await

### M2. Управление задачами
4. create_task, Task lifecycle
5. as_completed, wait, порядок результатов

### M3. Надёжность
6. Таймауты (wait_for / timeout)
7. Cancel, CancelledError, cleanup
8. Исключения: gather(return_exceptions), “Task exception was never retrieved”

### M4. Async I/O
9. HTTP (aiohttp): сессии, таймауты, лимиты
10. Файлы (aiofiles) и пайплайн “скачал → сохранил”

### M5. Debug/профилирование
11. asyncio debug mode, logging, slow callbacks
12. Мини-проект: асинхронный агрегатор
