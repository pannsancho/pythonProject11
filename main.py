def get_file_extension(file_name):
    try:
        file_parts = file_name.split(".")
        if len(file_parts) > 1:
            return file_parts[-1]
        else:
            raise ValueError("Файл не имеет расширения.")
    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    ...


if __name__ == "__main__":
    main()
