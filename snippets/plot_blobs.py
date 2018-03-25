plt.style.use('default')
fig, ax = plt.subplots()
ax.scatter(X[y==0,0], X[y==0,1], c='b', label='0')
ax.scatter(X[y==1,0], X[y==1,1], c='r', label='1')
ax.set(xlabel='Feature 1', 
       ylabel='Feature 2', 
       title='2 Blobs')
ax.legend()