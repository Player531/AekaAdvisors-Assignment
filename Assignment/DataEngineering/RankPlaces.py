import os 
import pandas as pd

def rank_places(city_name):
    file_path = os.path.abspath(os.getcwd())+"\DataEngineering\IndianPlacesToVisit.csv"
    df = pd.read_csv(file_path)
    city_df = df[df['City'].str.contains(city_name, case=False, na=False)].copy()

    # Calculating 3 score:     
    #       Review Score = Google review rating * Number of google review in lakhs
    #       Significance Score = 5 if historical/Architectural, 4 if scenic/nature, 3 if religious, 2 if shopping/market, else 1
    #       Fee Score = 5 if fee < 50, 3 if fee > 50 and < 100, else 1
    city_df.loc[:, 'Review Score'] = city_df['Google review rating'] * city_df['Number of google review in lakhs']
    city_df.loc[:, 'Significance Score'] = city_df['Significance'].apply(lambda x: 5 if x == 'Historical' or x=='Architectural' else (4 if x == 'Scenic' or x =='Nature' else (3 if x == 'Religious' else (2 if x == 'Shopping' or x=='Market' else 1))))
    city_df.loc[:, 'Fee Score'] = city_df['Entrance Fee in INR'].apply(lambda x: 5 if x <= 50 else (3 if x <= 100 else 1))
    
    # Summation of each score and ranking based on that score
    city_df.loc[:, 'Total Score'] = city_df['Review Score'] + city_df['Significance Score'] + city_df['Fee Score']
    ranked_places = city_df.sort_values(by='Total Score', ascending=False)
    return ranked_places

city_name = input("Enter a city name: ")
ranked_places = rank_places(city_name)
print(ranked_places[['Name', 'Total Score']])


