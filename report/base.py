from abc import ABC, abstractmethod
from typing import List, Dict

class Report(ABC):
    @abstractmethod
    def generate(self, data: List[Dict[str, str]]) -> str:
        pass
