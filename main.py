def get_file_extension(file_name):
    # FIXME: функция не должна обрабатывать исключения, а только вызывать их, блок try перенести в main
    try:
        file_parts = file_name.split(".")
        # FIXME: а если после точки пустота?
        if len(file_parts) > 1:
            return file_parts[-1]
        else:
            raise ValueError("Файл не имеет расширения.")
    # FIXME: вы бросаете ValueError, а отлавливаете Exeption? Почему? Собственно, блок except также перенести в main
    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    file_name = input("Введите имя файла: ")
    # TODO: здесь должен начинаться блок try - except - else - finally
    extension = get_file_extension(file_name)

    # FIXME: та проверка не потребуется, если правильно описать блок try - except - else - finally
    if extension:
        print(f"Расширение файла: {extension}")


if __name__ == "__main__":
    main()
