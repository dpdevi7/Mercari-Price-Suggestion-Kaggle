# https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe

# concat cat_1, cat_2, cat_3 
def concat_c1_c2_c3(c_1, c_2, c_3):
    return c_1 + "/" + c_2 + "/" + c_3


# filling missing cat_1 column from item_description and name
def miss_cat1(row):
    
    cat1 = row['cat_1']
    
    if row['cat_1']=='unknown':
        
        for i in setofCat1:
            if i in row['item_description'].lower():
                
                # print("1 desc {}".format(i))
                
                cat1 = i
                break
            elif i in row['name'].lower():
                
                # print("1 name {}".format(i))
                
                cat1 = i
                break   
    
    return cat1


## filling missing cat_2 column from item_description and name
def miss_cat2(row):
    
    cat2 = row['cat_2']
    
    if row['cat_2']=='unknown':
        
        for i in setofCat2:
            if i in row['item_description'].lower():
                
                # print("2 desc {}".format(i))
                
                cat2 = i
                break
            elif i in row['name'].lower():
                
                # print("2 name {}".format(i))
                
                cat2 = i
                break   
    
    return cat2


## filling missing cat_3 column from item_description and name
def miss_cat3(row):
    
    cat3 = row['cat_3']
    
    if row['cat_3']=='unknown':
        
        for i in setofCat3:
            if i in row['item_description'].lower():
                
                # print("3 desc {}".format(i))
                
                cat3 = i
                break
            elif i in row['name'].lower():
                
                # print("3 name {}".format(i))
                
                cat3 = i
                break   
    
    return cat3
    

## get missing brand name from name and description
def miss_brand(row):
    
    brand_name = row['brand_name']
    desc = row['item_description'].lower()
    name = row['name'].lower()
    
    if row['brand_name']=='unknown':
        
        for i in setofBrands:
            if i in desc:
                                
                brand_name = i
                break
            elif i in name:
                
                brand_name = i
                break   
    
    return brand_name


def fill_missing_data(df):
    
    df['cat_1']         = df.apply(miss_cat1, axis=1)
    df['cat_2']         = df.apply(miss_cat2, axis=1)
    df['cat_3']         = df.apply(miss_cat3, axis=1)
    df['brand_name']    = df.apply(miss_brand, axis=1)
    df['category_name'] = df.apply(lambda x: concat_c1_c2_c3(str(x.cat_1), str(x.cat_2), str(x.cat_3)), axis=1)
    
    return df
