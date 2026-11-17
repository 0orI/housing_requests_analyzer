days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]
requests = [12, 8, 15, 6, 19, 10]
total = 0
min_requests = requests [0]
complete_days = 0
failed_days = 0
max_requests = requests [0]
max_day = days [0]
for i in range(len(requests)):
    total += requests[i]
    if requests[i] > max_requests:
        max_requests = requests[i]
        max_day = days[i]
    if requests[i] < min_requests:
        min_requests = requests[i]
    if requests[i] >= 10:
        complete_days += 1
    else:
        failed_days += 1
average_requests = total / len (requests)
percent_complete = complete_days / len(requests) * 100
print(f"Общее количество заявок: {total}")
print(f"Среднее количество заявок: {average_requests:.2f}")
print(f"Максимальное количество заявок за день: {max_requests}")
print(f"Самый загруженный день: {max_day}")
print(f"Минимальное количество заявок за день: {min_requests}")
print(f"Количество дней, когда план выполнен: {complete_days}")
print(f"Количество дней, когда план не выполнен: {failed_days}")
print(f"Процент дней с выполненным планом: {percent_complete:.2f}%")