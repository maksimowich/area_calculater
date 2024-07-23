from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> float:
        """
        Computes figure area.
        """
        pass
