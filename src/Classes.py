from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self, text):
        pass

    @abstractmethod
    def filter_vacancies(self, text):
        pass
