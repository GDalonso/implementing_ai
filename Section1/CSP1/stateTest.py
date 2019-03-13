from statecsp1 import State
import matplotlib.pyplot as plt
import CSP

initialState = State()
intermediateState = State(initialState.assignment, "state1", "red")

print("intermediateState", intermediateState.assignment)
print("SelecrUnassignedVariable", initialState.selectUnassignedVariable())
print("orderDomainValues", initialState.orderDomainValues())

image = intermediateState.drawState()
plt.imshow(image)

font = {"family": "serif", "color": "white", "weight": "normal", "size": 14}
for variable in CSP.variables:
    # get average positions
    avgx = 0
    avgy = 0
    for (posx, posy) in CSP.positions[variable]:
        avgx += posx
        avgy += posy

    avgx /= len(CSP.positions[variable])
    avgy /= len(CSP.positions[variable])
    plt.text(avgy - 0.3, avgx, variable, fontdict=font)
plt.axis("off")
plt.show()
