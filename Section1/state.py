class State:
    "retrieve the state information for a seach app"

    def __init__(self, value = None):
        if value == None:
            # Create a initial state
            self.value = self.getInitialState()
        else:
            self.value = value

    def getInitialState(self):
        # returns the initial state
        initialState = ""
        return initialState

    def sucessorFunction(self):
        # This is the sucessor function
        return []

    def checkGoalState(self):
        # checks wheter we have encountered the goal State
        return False
