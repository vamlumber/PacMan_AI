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
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack = util.Stack()
    discovered = []
    stack.push( (problem.getStartState(), []) )
    # discovered.append( problem.getStartState() )

    while not stack.isEmpty():
        current_node = stack.pop()
        if problem.isGoalState(current_node[0]):
            print "Goal",current_node
            return current_node[1]
        if current_node[0] in discovered:
            # discovered.append(current_node[0])
            continue
        for node in problem.getSuccessors(current_node[0]):
            # print node
            if node[0] not in discovered:
                stack.push( (node[0], current_node[1] + [node[1]]) )
        discovered.append(current_node[0])
                # discovered.append( node[0] )
    # directs ={'West':'East','East':'West','North':'South','South':'North','Stop':'Stop'}
    # action =["Stop"]
    # parent_map = {}
    # discovered = set()
    # stak = util.Stack()
    # target = (problem.getStartState(),"Stop",0)
    # parent_map[target] = None
    # stak.push(target)
    # while not stak.isEmpty():
    #     current_node = stak.pop()
    #     #print current_node[0]
    #     #print discover 
    #     if current_node[0] in discovered:    
    #         continue
    #     # action.append(current_node[1])
    #     if problem.isGoalState(current_node[0]):
    #         target = current_node
    #         break
    #     # print problem.getSuccessors(current_node[0])
    #     for x in problem.getSuccessors(current_node[0]):
    #         if x[0] not in discovered:
    #             stak.push(x)
    #             if x not in parent_map:
    #                 parent_map[x]=current_node
    #     discovered.add(current_node[0])
    #     #print "What is discovered",discover
    # #action.append(target[1])
    # # print "Target",target
    # while (target != None):
    #     action.append(target[1])
    #     target = parent_map.get(target)
    #     # print "Goal",target
    #     # print "Action",action
    # action = action[::-1]
    # return action

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    que = util.Queue()
    discovered = []
    if problem.isGoalState(problem.getStartState()):
        return ["Stop"]
    que.push( (problem.getStartState(), []) )
    while que.isEmpty() == 0:
        current_node = que.pop()
        if problem.isGoalState(current_node[0]):
            return current_node[1]
        if current_node[0] in discovered:
            continue
        for node in problem.getSuccessors(current_node[0]):
            if node[0] not in discovered:
                que.push( (node[0],current_node[1] + [node[1]]) )
        discovered.append(current_node[0])
    # if type(problem.getStartState()[0]) is int:
        # que = util.Queue()
        # que.push([(problem.getStartState(), "Stop", 0)])
        # discovered = []
        # # print type(problem.getStartState()[0]) is int
        # while not que.isEmpty():
        #     path = que.pop()
        #     current_node = path[-1][0]
        #     if problem.isGoalState(current_node):
        #         return [x[1] for x in path][1:]
        #     if current_node not in discovered:
        #         discovered.append(current_node)
        #         for node in problem.getSuccessors(current_node):
        #             if node[0] not in discovered:
        #                 successorPath = path[:]
        #                 successorPath.append(node)
        #                 que.push(successorPath)
    # else:
    #     que = util.Queue()
    #     start_state,corners = problem.getStartState()
    #     que.push([(start_state, "Stop", 0)])
    #     discovered = []
    #     while not que.isEmpty():
    #         path = que.pop()
    #         current_node = path[-1][0]

    #         if problem.isGoalState((current_node,corners)):
    #             return [x[1] for x in path][1:]

    #         if current_node not in discovered:
                
    #             discovered.append(path[-1])

    #             for node in problem.getSuccessors((current_node,corners)):
    #                 print discovered
    #                 print node[0][0],node[1],node[2]
    #                 if (node[0][0],node[1],node[2]) not in discovered:

    #                     corners = node[0][1]
    #                     successorPath = path[:]
                     
    #                     successorPath.append((node[0][0],node[1],node[2]))

    #                     que.push(successorPath)



    # util.raiseNotDefined()

    # action=["Stop"]
    # parent_map = {}
    # discovered = set()
    # que = util.Queue()
    # target = (problem.getStartState(),"Stop",0)
    # que.push((problem.getStartState(),"Stop",0))
    # while not que.isEmpty():
    #     current_node = que.pop()
    #     # print current_node
    #     if current_node[0] in discovered:
    #         continue
    #     if problem.isGoalState(current_node[0]):
    #         print "Goal State"
    #         target = current_node
    #         break
    #     for node in problem.getSuccessors(current_node[0]):
    #         if node[0] not in discovered:
    #             que.push(node)
    #             if node not in parent_map:
    #                 parent_map[node] = current_node
    #     discovered.add(current_node[0])
    
    # while (target != None):
    #     action.append(target[1])
    #     target = parent_map.get(target)
        
    # action = action[::-1]
    # return action


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # priority_que = util.PriorityQueue()
    # action = []
    # discovered = set()
    # priority_que.push((problem.getStartState(),"Stop",0),0)
    # while not priority_que.isEmpty():
    #     current_node = priority_que.pop()
    #     if current_node[0] in discovered:
    #         continue
    #     if problem.isGoalState(current_node[0]):
    #         break
    #     for node in problem.getSuccessors(current_node[0]):
    #         if node in discovered:
    #             node[3] = current_node[3]+1
    #             priority_que.update(node,node[3])
    #         else:
    #             node[3] = current_node[3]+1
    #             priority_que.push(node)
    #     discovered.add(current_node[0])
    priority_que = util.PriorityQueue()
    visited_node = []
    priority_que.push((problem.getStartState(), []), 0 )
    # visited_node.append( problem.getStartState() )

    while not priority_que.isEmpty():
        current_node = priority_que.pop()
        print current_node
        if problem.isGoalState(current_node[0]):
            return current_node[1]

        if current_node[0] in visited_node:
            continue

        for node in problem.getSuccessors(current_node[0]):
            if node[0] not in visited_node:
                priority_que.update((node[0], current_node[1] + [node[1]]), problem.getCostOfActions(current_node[1]+[node[1]]))
        visited_node.append(current_node[0])

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priority_que = util.PriorityQueue()
    visited_node = []
    priority_que.push((problem.getStartState(),[]),heuristic(problem.getStartState(),problem))
    # visited_node.add(problem.getStartState())
    while not priority_que.isEmpty():
        current_node = priority_que.pop()
        if problem.isGoalState(current_node[0]):
            return current_node[1]

        if current_node[0] in visited_node:
            continue

        for node in problem.getSuccessors(current_node[0]):
            if node[0] not in visited_node:
                priority_que.update((node[0], current_node[1] + [node[1]]), problem.getCostOfActions(current_node[1]+[node[1]])+heuristic(node[0],problem))
        visited_node.append(current_node[0])
                
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
