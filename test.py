import requests
import os

# адрес нашего API
url = "http://127.0.0.1:8000/match"


# отправляем CSV
with open("01_hotels_external.csv", "rb") as file:

    response = requests.post(
        url,
        files={
            "file": file
        }
    )

path = "output/"
os.makedirs(os.path.dirname(path), exist_ok=True)

# сохраняем ответ в output
with open("output/matches.csv", "wb") as result_file:
    result_file.write(response.content)


print("Готово! Файл сохранён в output/matches.csv")