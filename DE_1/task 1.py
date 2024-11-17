import re
from collections import Counter


def first_task(file_path):
    """
    Задание 1.1:
        - Считайть текстовый файл согласно варианту;
        - Подсчитать частоту всех слов, встречающихся в тексте;
        - В результирующем файле вывести полученные данные в порядке
        убывания их частоты.
    Задание 1.2:
        - Подсчитать количество, а также долю всех слов,
        начинающихся на гласную букву в тексте.
    """

    cleaned_text = re.findall(
        r"[a-zA-Zа-яА-Я]+",
        re.sub(
            r"\b's\b",  # ! замена 's на is
            " is",
            open(
                "DE_1/data/first_task.txt",
            )
            .read()
            .lower(),
        ),
    )

    sorted_word_counts = sorted(
        Counter(cleaned_text).items(), key=lambda x: x[1], reverse=True
    )

    with open("DE_1/answers/word_frequencies_task_1_1.txt", "w", encoding="utf-8") as f:
        for word, count in sorted_word_counts:
            f.write(f"{word}: {count}\n")

    vowel_words = [
        word for word in cleaned_text if word[0] in "уеёыаоэяиюeyuioa"
    ]

    with open("DE_1/answers/vowel_word_statistics_task_1_2.txt", "w", encoding="utf-8") as f:
        f.write(
            "Количество слов, начинающихся на гласную букву: "
            f"{len(vowel_words)}\n"
        )
        f.write(
            "Доля слов, начинающихся на гласную букву: "
            f"{len(vowel_words) / len(cleaned_text)}"
        )

    return print(
        "Результирующие файлы по первому заданию записаны "
        "в рабочую директорию"
    )


first_task("first_task.txt")
