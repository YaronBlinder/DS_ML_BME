plt.style.use('classic')
fig, ax = plt.subplots()
ax.bar(x_pos, y_avg, color=barcolor, yerr=y_err, width=bar_width, edgecolor='k')
ax.plot(x_raw, y_raw, linecolor)
ax.fill_between(x_pred, y_min_pred, y_max_pred, color=fillcolor)
ax.set(title='Future projections of whatever', 
       xlabel='Time [time units]', 
       ylabel='whatever [whatever units]')
plt.show()