import csv

# Чтение CSV-файла и обработка данных
with open("DE_1/data/fourth_task.csv", "r", encoding="utf-8") as csvfile: # предполагаю что кодировка UTF-8, проверьте ваш файл
  reader = csv.DictReader(csvfile)
  prices = []
  quantities = []
  modified_data = []

  for row in reader:
    try:
      price = int(row["price"])
      quantity = int(row["quantity"])
      prices.append(price)
      quantities.append(quantity)
      modified_row = {
        "product_id": row["product_id"],
        "name": row["name"],
        "price": price,
        "quantity": quantity
      }
      if price > 4984:
        modified_data.append(modified_row)
    except ValueError:
      print(f"Ошибка преобразования типа в строке: {row}") # обрабатываем ошибки преобразования

# Вычисление статистических показателей
average_price = sum(prices) / len(prices) if prices else 0
max_price = max(prices) if prices else 0
min_quantity = min(quantities) if quantities else 0

# Запись результатов в файл
with open("DE_1/answers/results_task_4.txt", "w") as outfile:
  outfile.write(str(average_price) + "\n")
  outfile.write(str(max_price) + "\n")
  outfile.write(str(min_quantity) + "\n")

# Запись модифицированных данных в CSV-файл
with open("DE_1/answers/output_task_4.csv", "w", newline="", encoding="utf-8") as csvfile:
  fieldnames = ["product_id", "name", "price", "quantity"] # исправлено имя поля
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(modified_data)

print("Обработка завершена. Результаты сохранены в файлы results.txt и output.csv")
