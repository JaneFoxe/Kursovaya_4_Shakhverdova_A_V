from abc import ABC, abstractmethod
import requests

from src.config import SECRET_KEY


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self, text):
        pass

    @abstractmethod
    def filter_vacancies(self, text):
        pass



class Super_job(AbstractAPI):
    def get_vacancies(self, text):
        headers = {
            "X-Api-App-Id": SECRET_KEY}
        params = {"keyword": text}
        vacancies = requests.get("	https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()
        return vacancies["objects"]

    def filter_vacancies(self, text):
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({
                "name": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": vacancy["payment_from"],
                "salary_to": vacancy["payment_to"],
                "description": vacancy["candidat"]
            })
        return vacancies_filter


class Hh_ru(AbstractAPI):
    def get_vacancies(self, text):
        params = {"text": text}
        vacancies = requests.get("https://api.hh.ru/vacancies?", params=params).json()
        return vacancies["items"]

    def filter_vacancies(self, text):
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            salary_from = 0
            salary_to = 0
            if vacancy['salary'] is not None:
                if vacancy['salary']['from'] is not None:
                    salary_from = vacancy['salary']['from']
                if vacancy['salary']['to'] is not None:
                    salary_to = vacancy['salary']['to']

            data = {
                "name": vacancy["name"],
                "url": vacancy["url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "description": vacancy['snippet']['requirement']
            }
            vacancies_filter.append(data)
        return vacancies_filter




