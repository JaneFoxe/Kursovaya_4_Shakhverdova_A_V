

class Vacancy:
    def __int__(self, name, url, salary_from, salary_to, description):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description

    def __str__(self):
        return f"""Название вакансии: {self.name}
Ссылка: {self.url}
Зарплата: {self.salary_from} - {self.salary_to}
Описание вакансии: {self.description}
"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from

