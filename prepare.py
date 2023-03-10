def prep_titanic(df):
    '''
    clean titanic will take in a single pandas dataframe
    and will proceed to drop redundant columns
    and nonuseful information
    in addition to addressing null values
    and encoding categorical variables
    '''
    #drop out any redundant, excessively empty, or bad columns
    df = df.drop(columns=['passenger_id','embarked','deck','class'])
    # impute average age and most common embark_town:
    df['age'] = df['age'].fillna(df.age.mean())
    df['embark_town'] = df['embark_town'].fillna('Southampton')
    # encode categorical values:
    df = pd.concat(
    [df, pd.get_dummies(df[['sex', 'embark_town']],
                        drop_first=True)], axis=1)
    return df


def prep_iris(df):
    '''Prep iris will clean that pandas df up'''
    # drop species id
    iris.drop(columns=['species_id'], inplace=True)
    # change species name to species
    iris.rename(columns={'species_name': 'species'}, inplace=True)
    # get encoded categorical values for species
    iris = pd.concat(
        [iris, pd.get_dummies(iris['species'])], axis=1)

    return df