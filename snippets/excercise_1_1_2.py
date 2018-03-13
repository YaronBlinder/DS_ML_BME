colors = ['r', 'g', 'b']
fig, ax = plt.subplots()
for y, name, color in zip([y1, y2, y3], names, colors):
    ax.plot(x, y, color)
ax.legend(names, loc='best')
plt.show()