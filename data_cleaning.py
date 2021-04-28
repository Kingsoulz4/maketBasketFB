import json
import pandas as pd

json_file = open('like_page.json')
data = json.load(json_file)
link_user = []
liked_pages =[]
for da in data["like page user"]:
    if len(da["Liked Pages"]) != 2:
       for d in da["Liked Pages"]:
           if d not in liked_pages and "likes" not in str(d):
               #print(d)
               liked_pages.append(d)
#print(liked_pages)
for da in data["like page user"]:
    #print(da["Link user"])
    if da["Link user"] not in link_user:
       link_user.append(da["Link user"])
print(len(link_user))
likedf = pd.DataFrame(columns=liked_pages, index=link_user)
for da in data["like page user"]:
    pages = {}
    for page in da["Liked Pages"]:
        pages[page] = 1
    likedf.loc[da["Link user"]] = pd.Series(pages)
likedf.fillna(0, inplace=True)
print(likedf)
likedf.to_csv("basket.csv")