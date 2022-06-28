import os
import pandas as pd 
from itertools import combinations

# read similar csv files 
sim_file = pd.read_csv('csv_files/similar_images.csv')
# remove multiple origin
sim_file = sim_file.drop(sim_file[sim_file.image_list.str.count('origin')>1].index)
# remove .gif files 
sim_file = sim_file.drop(sim_file[sim_file.image_list.str.count('.gif')>0].index)
#replace spaces at image path with underscore
sim_file['image_path'] = sim_file['image_path'].apply(lambda x: x.replace(' ','_').replace('&',''))
sim_file['main_category'] = sim_file['main_category'].apply(lambda x: x.replace(' ','_').replace('&',''))


train_file_path = 'csv_files/train_triplet.csv'
test_file_path = 'csv_files/test_triplet.csv'
val_file_path = 'csv_files/val_triplet.csv'

def add_path(df):
    return  df['image_path'] + '/' + df['image_list'].replace(']','').replace('[','').replace("'",'').replace(' ','').split(',')[0]

def save_triplets(set_list,file_path):

    set_df = pd.DataFrame(set_list,columns =['anchor', 'positive', 'negative','label'])
    if os.path.exists(file_path):
        set_df.to_csv(file_path,mode='a',index=False,header=False)
    else :
        set_df.to_csv(file_path,index=False)

i = 0 
j = 0 
for index, row in sim_file.iterrows():
    try:
        print("the pin number is ...",i)
        print("the pin is ... ", row['pin'])
        # create list from image and similar list
        sim_list = row['image_list'].replace(']','').replace('[','').replace("'",'').replace(' ','').split(',')
        # ignore .ong files 
        if '.png' in sim_list[0]:
            i = i + 1
            continue 
        # remove .png files 
        sim_list = [row['image_path'] + '/' + img for img in sim_list if '.png' not in img]
        # generate combinition list from sim_list generate anch and pos images 
        com_list = list(combinations(sim_list,2))
        df_tmp = sim_file.loc[(sim_file['main_category'] != row['main_category']) & (sim_file['gender'] != row['gender']) & ('.png' not in row['image_list'])]
        # generatt neg images 
        df_tmp = df_tmp.sample(len(com_list))
        df_tmp['image_list'] = df_tmp.apply(add_path, axis = 1)
        com_list = list(map(lambda x,y:  list(x) + [y], com_list,list(df_tmp['image_list'])))
        # adding labels 
        com_list = list(map(lambda x:  list(x) + [row['main_category']] , com_list))
    
        # slit train test val triplets
        split_length = int(len(com_list)/3)
        train_length = 2*split_length
        test_length =  int(split_length/2)
        train_list = com_list[:train_length]
        val_list = com_list[train_length:train_length+test_length]
        test_list = com_list[train_length+test_length:]

        # save in csv files
        save_triplets(train_list,train_file_path)
        save_triplets(val_list,val_file_path)
        save_triplets(test_list,test_file_path)
        print(len(train_list),len(val_list),len(test_list))
        i = i + 1
    except:
        i = i + 1
        j = j+1 
        continue
print("the number of fail:", j)
