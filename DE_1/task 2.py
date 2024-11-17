def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        sums = []
        
        # Считываем строки из файла
        for line in file:
            numbers = map(int, line.split())  # Преобразуем строку в список чисел
            # Суммируем только абсолютные значения отрицательных чисел
            sums.append(sum(abs(num) for num in numbers if num < 0))
    
    # Открываем файл для записи результата
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Записываем суммы в файл
        for s in sums:
            output_file.write(f"{s}\n")
        
        output_file.write("-----------\n")
        
        # Расчет среднего значения
        if sums:
            average = sum(sums) / len(sums)
            output_file.write(f"average {average:.2f}\n")
        else:
            output_file.write("average 0.00\n")

input_file_path = "DE_1/data/second_task.txt"
output_file_path = "DE_1/answers/output_task_2.txt" 
process_file(input_file_path, output_file_path)