from dataexp import Dataexp
import seaborn as sns

df = sns.load_dataset('titanic')

test = Dataexp(df)

print(test.numeric_summary())
print('--------------------------------------')
print(test.text_summary())
print('--------------------------------------')
print(test.category_summary())
print('--------------------------------------')
print(test.date_summary())
print('--------------------------------------')
print(test.bool_summary())
print('--------------------------------------')
