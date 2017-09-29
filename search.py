"""search.py

Champlain College CSI-480, Fall 2017
The following code was adapted by Joshua Auerbach (jauerbach@champlain.edu)
from the UC Berkeley Pacman Projects (see license and attribution below).

----------------------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

import util


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
        action, step_cost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'step_cost' is
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


def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def graph_search(problem, fringe):
    # push start node onto fringe
    fringe.push([(problem.get_start_state(), "Start", 0)])
    # create empy list of visited nodes
    visited = []
    # loop through fringe until empty
    while not fringe.is_empty():
        # get the path from the top of the fringe
        path = fringe.pop()
        # get the leaf node from the path
        leaf_node = path[-1]
        leaf_node = leaf_node[0]
        # for states that hold goals
        # if instanceof(leaf_node, tuple):
        #     leaf_node = leaf_node[0]
        # check if node is solution
        is_solution = problem.is_goal_state(leaf_node)
        if is_solution:
            return [step[1] for step in path[1:]]
        # for multigoal to avoid non complete searches
        if is_solution == -1:
            visited = []
            visited.append(leaf_node)
        # Check if node has already been visited
        if leaf_node not in visited:
            # Add to visited
            visited.append(leaf_node)
            # check each successor
            for successor in problem.get_successors(leaf_node):
                successor_node = successor[0]
                # if the successor has not been visited
                if successor_node not in visited:
                    # Add node and relevant path to fringe
                    successor_path = path[:]
                    successor_path.append(successor)
                    fringe.push(successor_path)
    print ("SEARCH FAILED. NO SOLUTION FOUND")




def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.get_start_state()
    print "Is the start a goal?", problem.is_goal_state(problem.get_start_state())
    print "Start's successors:", problem.get_successors(problem.get_start_state())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    return graph_search(problem, fringe)
    
    



def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    return graph_search(problem, fringe)


def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_function = lambda path: problem.get_cost_of_actions([step[1] for step in path[1:]])
    fringe = util.PriorityQueueWithFunction(priority_function)
    return graph_search(problem,  fringe)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_function = lambda path: problem.get_cost_of_actions([step[1] for step in path[1:]]) + heuristic(path[-1][0], problem)
    fringe = util.PriorityQueueWithFunction(priority_function)
    return graph_search(problem, fringe)

# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
