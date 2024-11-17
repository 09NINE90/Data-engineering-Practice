import requests
from bs4 import BeautifulSoup

def get_covid_data(country="USA"):
    # Получает данные о COVID-19 из API и возвращает JSON.
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки HTTP
    return response.json()


def json_to_html(data):
    # Преобразует JSON-данные в HTML-представление.
    soup = BeautifulSoup("<html><body></body></html>", "html.parser")
    body = soup.find("body")

    # Добавление заголовка
    h1 = soup.new_tag("h1")
    h1.string = f"COVID-19 Data for {data.get('country', 'Unknown')}"
    body.append(h1)

    # Добавление отдельных элементов данных
    for key, value in data.items():
        if key in ['cases', 'todayCases', 'deaths', 'recovered', 'active', 'critical', 'tests']:
            p = soup.new_tag("p")
            p.string = f"{key.replace('_', ' ').title()}: {value}"
            body.append(p)

    return str(soup)


if __name__ == "__main__":
    country = input("Введите название страны (по умолчанию Russia): ") or "Russia"
    covid_data = get_covid_data(country)
    html_output = json_to_html(covid_data)
    print(html_output)

    # Для сохранения в файл:
    with open("DE_1/answers/covid_data_task_6.html", "w", encoding="utf-8") as f:
        f.write(html_output)

