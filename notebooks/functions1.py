# Zach method chaining
import pandas as pd

def load_and_process(file):

    # load csv file into dataframe
    df = pd.read_csv(file)

    # clean and process the data
    df_processed = pd.concat(
    [df['Winner'],df['R_fighter'],df['B_fighter'],df['weight_class'],
    df['R_Height_cms'],df['B_Height_cms'],df['R_win_by_Submission'],df['B_win_by_Submission']], 
    axis = 1
    ).drop(df[df['Winner']=='Draw'].index).dropna().reset_index().drop(columns='index').rename(columns={
    'Winner':'winner',
    'R_fighter':'r_fighter','B_fighter':'b_fighter',
    'R_Height_cms':'r_height_in','B_Height_cms':'b_height_in',
    'R_win_by_Submission':'r_submission_w','B_win_by_Submission':'b_submission_w'
    })
    
    df_processed['r_height_in'] = [df_processed['r_height_in'][i]*(0.393701) for i in range(len(df_processed['r_height_in']))]
    df_processed['b_height_in'] = [df_processed['b_height_in'][i]*(0.393701) for i in range(len(df_processed['r_height_in']))]

    return df_processed


