
from src.JSON_saver import JSONSaver

from src.Classes import Super_job, Hh_ru


def user_answer():
    while True:
        answer_number = input("На каком сайте будем искать? 1 - HH.ru, 2 - SuperJob, 3 - все сразу\n")

        if answer_number in ["1", "2", "3"]:
            break
        else:
            print("Попробуйте еще раз")

    keyword = input("По какому ключевому слову будем искать?\n")
    n_max = int(input("Какое максимальное количество ваканасий показать?\n"))

    if answer_number == "1":
        hh_vacancies = Hh_ru().filter_vacancies(keyword)
        merged_vacancies = JSONSaver("Hh_ru.json")
        merged_vacancies.write_vacancies(hh_vacancies[:n_max])

    if answer_number == "2":
        sj_vacancies = Super_job().filter_vacancies(keyword)
        merged_vacancies = JSONSaver("Super_job.json")
        merged_vacancies.write_vacancies(sj_vacancies[:n_max])

    if answer_number == "3":
        hh_vacancies = Hh_ru().filter_vacancies(keyword)
        sj_vacancies = Super_job().filter_vacancies(keyword)
        merged_vacancies = JSONSaver("Hh_ru_and_Super_job.json")
        merged_vacancies.write_vacancies((hh_vacancies + sj_vacancies)[:n_max])

    print_merged_vacancies = merged_vacancies.read_vacancies()
    for vacancy in sorted(print_merged_vacancies):
        print(vacancy)
        print("*" * 50)


if __name__ == '__main__':
    user_answer()

