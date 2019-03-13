import CSP
import collections
import numpy as np
import copy

class State:
    "retrieve the state information for a seach app"

    def __init__(self, assignment = None, variable=None, value=None):
        if value == None:
            # Create a initial state
            self.assignment = self.getInitialState()
        else:
            assignment1 = copy.deepcopy(assignment)
            assignment1[variable] = value
            self.assignment = assignment1
            # self.value = value

    def getInitialState(self):
        # returns the initial state
        # initialState = ""
        # return initialState
        return collections.OrderedDict()

    def selectUnassignedVariable(self):
        "return a variable not yet assigned"
        for variable in CSP.variables:
            if variable not in self.assignment:
                return variable
    def orderDomainValues(self):
        # returns the values in a particulas orderDomainValues
        return CSP.domainValues

    def checkGoalState(self):
        # checks wheter we have encountered the goal State
        return len(self.assignment) == len(CSP.variables)

    def drawState(self):
        # draws the state6
        image = np.zeros((7,7,3), np.uint8)
        for key in self.assignment:
            # find the channel index
            if self.assignment[key] == "red":
                # code for red
                channelIndex = 0
            elif self.assignment[key] == "green":
                # code for green
                channelIndex = 1
            else:
                # code for blue
                channelIndex = 2
            for (xcoord, ycoord) in CSP.positions[key]:
                image[xcoord,ycoord,channelIndex] = 255
        return image

    # def sucessorFunction(self):
    #     # This is the sucessor function
    #     return []
