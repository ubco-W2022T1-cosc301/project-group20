# Gerren Method Chaining 
import pandas as pd

def load_and_process(file): 
  
  #load csv into dataframe 
  df = pd.read_csv(file)
  
  #clean data 
  
   df_processed = pd.concat(
    [df['B_avg_opp_HEAD_landed'],df['B_wins'],df['B_win_by_Decision_Majority'],df['B_win_by_Decision_Split'],df['B_win_by_Decision_Unanimous'],df['B_win_by_KO/TKO'],
    df['B_win_by_Submission'],df['B_win_by_TKO_Doctor_Stoppage'],  [df['R_avg_opp_HEAD_landed'],df['R_wins'],df['R_win_by_Decision_Majority'],df['R_win_by_Decision_Split'],df['R_win_by_Decision_Unanimous'],df['R_win_by_KO/TKO'],
    df['R_win_by_Submission'],df['R_win_by_TKO_Doctor_Stoppage'],
    axis = 1
    )
                                                                    
                                                                    
                                                                   
   return df_processed.dropna()
                                                                    
                                                                    
    
    
  
