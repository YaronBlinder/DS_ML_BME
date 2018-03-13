plt.style.use('classic')
fig, axes = plt.subplots(nrows=3, ncols=1)
for ax, y, name in zip(axes, [y1, y2, y3], names):
    ax.plot(x, y, 'k')
    ax.set(xticks=[], yticks=[] ,title=name)
plt.show()