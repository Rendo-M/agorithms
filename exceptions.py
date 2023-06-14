from datetime import datetime

def main():
    try:
        data = input("Введите данные (в формате: Фамилия Имя Отчество dd.mm.yyyy номер_телефона пол): ").split()
        if len(data) != 6:
            raise ValueError("Ошибка: требуется 6 параметров")

        surname, name, patronymic, dob_str, phone_str, gender = data
        dob = datetime.strptime(dob_str, "%d.%m.%Y").date()
        phone = int(phone_str)

        if gender not in ("f", "m"):
            raise ValueError("Ошибка: значение пола должно быть f или m")

    except ValueError as e:
        if "time data" in str(e) and "does not match format" in str(e):
            print("Ошибка: неверный формат даты рождения. Должен быть формат dd.mm.yyyy")
            return
        print(e)
        return
    except TypeError:
        print("номер телефона должен содержать только цифры")
        return
    except Exception as e:
        print("Ошибка:", e)
        return

    try:
        with open(surname + ".txt", "a") as file:
            file.write(surname + name + patronymic + dob_str + " " + phone_str + gender + "\n")
        print("Данные успешно записаны в файл", surname + ".txt")
    except Exception as e:
        print("Ошибка при записи в файл:", e)

if __name__ == "__main__":
    main()