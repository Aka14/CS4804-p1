# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

from game import Directions
import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


'''
SearchNode class to represent each item in a search tree
'''
class SearchNode:
    
    def __init__(self, state, parent, path, cost=1):
        self.__state = state
        self.__parent = parent
        self.__path = path
        self.__cost = cost
        
    def get_state(self):
        return self.__state
        
    def get_parent(self):
        return self.__parent
        
    def get_path(self):
        return self.__path
        
    def get_cost(self):
        return self.__cost
        
    def set_path(self, new_path):
        self.__path = new_path
        
    def set_cost(self, new_cost):
        self.__cost = new_cost





def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]




def depth_first_search(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.get_start_state())
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """
    
    frontier = Stack()
    startState = problem.get_start_state()
    startNode = SearchNode(startState, None, [])
    frontier.push(startNode)
    visited = set()
    while not frontier.is_empty():
        node = frontier.pop()
        state = node.get_state()
        if problem.is_goal_state(state):
            return node.get_path()
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.get_successors(state):
                child = SearchNode(successor, node, node.get_path() + [action])
                frontier.push(child)

    return []

    
    util.raise_not_defined()
    

def breadth_first_search(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    frontier = Queue()
    startState = problem.get_start_state()
    startNode = SearchNode(startState, None, [])
    frontier.push(startNode)
    visited = set()
    while not frontier.is_empty():
        node = frontier.pop()
        state = node.get_state()
        if problem.is_goal_state(state):
            return node.get_path()
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.get_successors(state):
                child = SearchNode(successor, node, node.get_path() + [action])
                frontier.push(child)
    return []

    util.raise_not_defined()
            



def uniform_cost_search(problem: SearchProblem):
    """Search the node of least total cost first."""
    
    frontier = PriorityQueue()
    startState = problem.get_start_state()
    startNode = SearchNode(startState, None, [])
    frontier.push(startNode, startNode.get_cost())
    visited = set()
    while not frontier.is_empty():
        node = frontier.pop()
        state = node.get_state()
        cost = node.get_cost()
        if problem.is_goal_state(state):
            return node.get_path()
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.get_successors(state):
                new_cost = step_cost + cost
                child = SearchNode(successor, node, node.get_path() + [action], new_cost)
                frontier.push(child, new_cost)
    return []


    util.raise_not_defined()
    
    
    
    
    

def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def a_star_search(problem: SearchProblem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = PriorityQueue()
    startState = problem.get_start_state()
    start_node = (startState, [], 0) 
    frontier.push(start_node, heuristic(startState, problem))
    bestCost = {startState: 0}
    while not frontier.is_empty():
        state, path, cost = frontier.pop()        
        if problem.is_goal_state(state):
            return path         
        for successor, action, step_cost in problem.get_successors(state):
            new_cost = cost + step_cost
            estimatedCost = new_cost + heuristic(successor, problem)
            if successor not in bestCost or new_cost < bestCost[successor]:
                bestCost[successor] = new_cost
                frontier.push((successor, path + [action], new_cost), estimatedCost)
    return []  
 

    util.raise_not_defined()
 
 
 


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
