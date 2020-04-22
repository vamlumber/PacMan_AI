# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        # print "successorGameState",successorGameState
        newPos = successorGameState.getPacmanPosition()
        # print "newPos",newPos
        newFood = successorGameState.getFood()
        # print "New Food",newFood
        newGhostStates = successorGameState.getGhostStates()
        # print "newGhostStates",newGhostStates
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        # print "newScaredTimes",newScaredTimes

        minimum_ghost_distance = min([util.manhattanDistance(newPos, state.getPosition()) for state in newGhostStates])
        # minimum_ghost_distance = min(ghost_distances)
        score = successorGameState.getScore() - currentGameState.getScore()
        # print score
        pos = currentGameState.getPacmanPosition()
        foods = currentGameState.getFood().asList()
        closest_food = min([util.manhattanDistance(pos, food) for food in foods])
        # closest_food = min(food_distances)
        newFoods = newFood.asList()
        new_foods_distances = [util.manhattanDistance(newPos, food) for food in foods]
        new_nearest_food = 0 
        if not new_foods_distances:
          new_nearest_food = 0 
        else: 
          new_nearest_food = min(new_foods_distances)
        is_nearer = closest_food - new_nearest_food
        direction = currentGameState.getPacmanState().getDirection()
        newDirection = successorGameState.getPacmanState().getDirection()

        if minimum_ghost_distance <= 1 or action == Directions.STOP:
            return 0
        if score > 0:
            return 8
        elif is_nearer > 0:
            return 4
        elif action == direction:
            return 2
        else:
            return 1
        # return successorGameState.getScore()

        

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        # util.raiseNotDefined()
        values = []
        legal_actions = gameState.getLegalActions(0)
        # print legalActions
        for action in legal_actions:
          min_max = self.minimax(gameState.generateSuccessor(0,action), 1, 0)
          values.append((min_max, action))
        return max(values)[1]

    def minimax(self, gameState, agent, depth):
      if agent >= gameState.getNumAgents():
        agent = 0
        depth += 1

      if depth == self.depth:
        return self.evaluationFunction(gameState)

      legal_actions = gameState.getLegalActions(agent)

      if not legal_actions:
        return self.evaluationFunction(gameState)

      values = []
  
      if agent == 0:
        for action in legal_actions:
          min_max = self.minimax(gameState.generateSuccessor(agent,action), agent+1, depth)
          values.append((min_max, action))
        return max(values)[0]

      else:
        for action in legal_actions:
          min_max = self.minimax(gameState.generateSuccessor(agent,action), agent+1, depth)
          values.append((min_max, action))
        return min(values)[0]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        n = (float("-inf"), 'None')
        alpha = float('-inf')
        beta = float('inf')
        legal_actions = gameState.getLegalActions(0)
        for action in legal_actions:
          n = max(n, (self.alphabeta(gameState.generateSuccessor(0, action), 1, 0, alpha, beta), action))
          if n[0] > beta:
            return n[1]
          alpha = max(alpha, n[0])
        return n[1]

    def alphabeta(self, gameState, agent,depth, alpha, beta):
      if agent >= gameState.getNumAgents():
        depth += 1
        agent = 0
        
      if depth == self.depth or gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      legal_actions = gameState.getLegalActions(agent)
      if agent == 0:
        n = float("-inf")
        for action in legal_actions:
          n = max(n, self.alphabeta(gameState.generateSuccessor(agent, action), agent + 1,depth, alpha, beta))
          if n > beta:
            return n
          alpha = max(alpha, n)
        return n
      else:
        n = float("inf")
        for action in legal_actions:
          n = min(n, self.alphabeta(gameState.generateSuccessor(agent, action), agent + 1,depth, alpha, beta))
          if n < alpha:
            return n
          beta = min(beta, n)
        return n

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        n = []
        legal_actions = gameState.getLegalActions(0)
        for action in legal_actions:
          expected_values = self.expectimax(gameState.generateSuccessor(0,action),1,0)
          n.append((expected_values, action))
        best_score = max(n)
        best_indices = [index for index in range(len(n)) if n[index] == best_score]
        chosen_index = random.choice(best_indices) # Pick randomly among the best
        return n[chosen_index][1]

    def expectimax(self, gameState, agent, depth):
      # upper_bound = float("-inf")
      if agent >= gameState.getNumAgents():
        agent = 0
        depth += 1

      if depth == self.depth or gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      legal_actions = gameState.getLegalActions(agent)
      if agent == 0:
        n = float("-inf")
        for action in legal_actions:
          n = max(n, self.expectimax(gameState.generateSuccessor(agent, action), agent + 1,depth))
        return n
      else:
        n = []
        prob = 1.0/len(legal_actions)
        for action in legal_actions:
          expected_values = self.expectimax(gameState.generateSuccessor(agent, action), agent + 1,depth)
          n.append(expected_values)
        res = sum(n)/len(legal_actions)
        return res

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    pos = currentGameState.getPacmanPosition()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    
    foods = currentGameState.getFood().asList()
    food_distances = [util.manhattanDistance(pos, food) for food in foods]

    ghost_distances = [util.manhattanDistance(pos, state.getPosition()) for state in newGhostStates]

    number_of_capsules = len(currentGameState.getCapsules())

    number_of_foods = len(food_distances)           
    sum_of_scared_times = sum(newScaredTimes)
    sum_of_ghost_distance = sum (ghost_distances)
    reciprocal_food_distance = 0
    if sum(food_distances) > 0:
        reciprocal_food_distance = 1.0 / sum(food_distances)
    score = 0
    score += currentGameState.getScore()  + reciprocal_food_distance + number_of_foods

    if sum_of_scared_times > 0:    
        score +=   sum_of_scared_times + (-1 * number_of_capsules) + (-1 * sum_of_ghost_distance)
    else :
        score +=  sum_of_ghost_distance + number_of_capsules
    return score

# Abbreviation
better = betterEvaluationFunction

