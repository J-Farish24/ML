from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

#1) load the dataset and use the KNeighborsClassifier to train and test your model
train_set =pd.read_csv('gameratings.csv')
test_set = pd.read_csv('test_esrb.csv')
esrb_ratings = pd.read_csv('target_names.csv')

train_game_attributes = train_set.iloc[:,1:33]
train_game_ratings = np.array(train_set.Target)




test_game_titles = test_set.title
test_game_attributes = test_set.iloc[:,1:33]
test_game_ratings = np.array(test_set.Target)





knn = KNeighborsClassifier()
knn.fit(X=train_game_attributes, y= train_game_ratings)

predicted = knn.predict(X = test_game_attributes)

expected = test_game_ratings


#2) Display all wrong predicted and expected pairs
predicted_rating = [esrb_ratings.target_name.loc[p-1] for p in predicted]
expected_rating = [esrb_ratings.target_name.loc[e-1] for e in expected]


wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)

print(format(knn.score(test_game_attributes, test_game_ratings), ".2%"))

#3) produce a csv file of the name of the game and the predicted rating

outfile = open('Predicted Rating.csv', 'w')
outfile.write('Title' + ',' + 'Rating' +'\n')
for game in zip(test_game_titles, predicted_rating):
    outfile.write(game[0] + ',' + game[1] + '\n')
outfile.close()
