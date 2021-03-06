from abc import ABC, abstractmethod
from ortools.linear_solver import pywraplp


class BaseSpOptSolver(ABC):
    """
    Base class for all spatial optimization model solvers

    """
    @abstractmethod
    def solve(self):
        """
        Solve the optimization model

        """
        pass


class BaseSpOptExactSolver(BaseSpOptSolver):
    """
    Base class for all spatial optimization model exact solvers

    Attributes
    ----------
    spOptSolver : pywraplp.Solver
        The or-tools MIP solver.

    """
    def __init__(self, name):
        self.spOptSolver = pywraplp.Solver(
            name, pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    def solve(self):
        self.spOptSolver.Solve()


class BaseSpOptHeuristicSolver(BaseSpOptSolver):
    """
    Base class for all spatial optimization model heuristic solvers

    """
    @abstractmethod
    def solve(self):
        """
        Solve the optimization model

        """
        pass


if __name__ != 'main':
    #hs = BaseSpOptHeuristicSolver()
    #hs.solve()
    es = BaseSpOptExactSolver('testes')
    es.solve()
