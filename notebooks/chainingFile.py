# Gerren Method Chaining

import pandas as pd



def load_and_process(file):

    # load csv into dataframe
    df = pd.read_csv(file)

    # clean data

    df_processed = df[["B_avg_opp_HEAD_landed", "B_wins", "B_win_by_Decision_Majority", "B_win_by_Decision_Split", "B_win_by_Decision_Unanimous", "B_win_by_KO/TKO", "B_win_by_Submission", "B_win_by_TKO_Doctor_Stoppage", "B_Reach_cms","R_avg_opp_HEAD_landed", "R_wins", "R_win_by_Decision_Majority", "R_win_by_Decision_Split", "R_win_by_Decision_Unanimous", "R_win_by_KO/TKO", "R_win_by_Submission", "R_win_by_TKO_Doctor_Stoppage", "R_Reach_cms"]]

    return df_processed.dropna()
    
    










