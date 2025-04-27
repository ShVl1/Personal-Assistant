
# Вказуємо базовий образ з потрібною версією Python
FROM python:3.12-slim

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту
COPY . .

# Встановлюємо залежності
RUN pip install pipenv && \
    pipenv install --system --deploy

# Вказуємо команду для запуску
ENTRYPOINT ["python", "./__main__.py"]
