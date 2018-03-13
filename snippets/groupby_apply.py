zscore = lambda x: (x - x.mean()) / x.std()
transformed = df.groupby('Category').transform(zscore)
df['transformed'] = transformed
df.groupby('Category').agg(['mean', 'std'])