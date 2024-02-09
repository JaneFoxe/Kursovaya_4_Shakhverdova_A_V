from abc import ABC, abstractmethod
import requests


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
            "X-Api-App-Id": "v3.r.138164921.800046555def46f665df567d74eae1830a078497.7da492b6fa77911d59b5f93011f3f359d2866a99"}
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
