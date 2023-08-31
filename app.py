import streamlit as st
import pickle 
import pandas as pd

teams=['Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Mumbai Indians', 'Chennai Super Kings', 'Deccan Chargers',
       'Sunrisers Hyderabad', 'Gujarat Lions', 'Delhi Capitals',
       'Punjab Kings', 'Gujarat Titans', 'Lucknow Super Giants']


cities=['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Dubai', 'Rajkot', 'Kanpur', 'Bengaluru', 'Indore',
       'Navi Mumbai', 'Lucknow', 'Guwahati']
pipe=pickle.load(open('pipe.pkl','rb'))
st.title('My first ipl win predector')

col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select the batting team',sorted(teams))
with col2:
      bowling_team=st.selectbox('Select the bowling team',sorted(teams))

selected_city=st.selectbox('Select the city ', sorted (cities))
target=st.number_input('Target')
col3,col4,col5=st.columns(3)
with col3:
     score=st.number_input("Score")
with col4:
     overs=st.number_input("Overs Completed")
with col5:
     wickets=st.number_input("Wickets Out")
     
if st.button('Predict Probability'):
     runs_left=target-score
     balls_left=120-(overs*6)
     rem_wickets=10-wickets
     crr=score/overs
     rrr=(target-score)*6/balls_left

     input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'rem_wickets':[rem_wickets],'runs_per_ball_x':[target],'crr':[crr],'rrr':[rrr]})
     result=pipe.predict_proba(input_df)
     loss=result[0][0]
     win=result[0][1]
     st.header(batting_team+"- " +str(round(win*100))+"%")
     st.header(bowling_team+"- " +str(round(loss*100))+"%")