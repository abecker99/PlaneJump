import matplotlib.pyplot as plt

X = []
Y = []

inFile = open("JumpData.txt", "r")
for line in inFile:
    t, x = line.split(" ")
    X.append(float(t))
    Y.append(float(x))
inFile.close()

plt.xlabel("$x$ (sec)")
plt.ylabel("$y$ (m)")
plt.plot(X,Y)
plt.show()