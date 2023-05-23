import pandas as pd 
import matplotlib.pyplot as plt

file_path = "star_with_gravity.csv"
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin-1')

df.drop(columns='Unnamed: 0', axis=1, inplace=True)

df = df.dropna()
df_list = df.values.tolist()

new_df_list = []
for row in df_list:
    dist = row[1]
    dist_split = dist.split(',')
    dist_value = float(''.join(dist_split))
    if dist_value <= 100:
        row[1] = dist_value
        new_df_list.append(row)

df_list = new_df_list

gravity_df_list = []
for row in df_list:
    try:
        gravity = float(row[4])
        if gravity >= 150 and gravity <= 350:
            gravity_df_list.append(row)
    except:
        continue

final_df = pd.DataFrame(gravity_df_list, columns=["Name", "Distance", "Mass", "Radius", "Gravity"])
final_df.to_csv('Gravity_Dist_Support.csv', index=False, encoding='utf-8')