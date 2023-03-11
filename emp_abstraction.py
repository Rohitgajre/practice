from abc import ABC, abstractmethod



class EmpAbstraction(ABC):
    @abstractmethod
    def write_headers(self):
        pass

    @abstractmethod
    def write_data(self):
        pass
    
    @abstractmethod
    def read_data(self):
        pass

