import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_copy = pd.read_csv("new.csv")


def gr1():
    graph = sns.countplot(data=df_copy,
              x='cp',
              hue='target',
              palette=["#a6cee3", "#1f78b4"])
    plt.title('Chest Pain Type vs Target')
    plt.xlabel('Chest Pain Type')
    plt.xticks(ticks=[0,1,2,3],
           labels=['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'], rotation=0)
    return graph
def gr2():
    grath = sns.countplot(data=df_copy, x='age_cat',
                  hue='target',
                  order=['0', '1', '2'],
                  palette=["#a6cee3", "#1f78b4"])
    plt.title('Age Categories vs Target');
    plt.xlabel('Age Categories')
    plt.xticks(ticks=['0', '1', '2'],
               labels=['Adult', 'Middle Age Adult ', 'Senior Adult'], rotation=0);
    return grath
def gr3():
    graph = sns.countplot(data=df_copy,
              x='sex',
              hue='target',
              palette=["#a6cee3", "#1f78b4"])
    plt.title('Sex vs Target')
    plt.xlabel('Sex')
    plt.xticks(ticks=[0,1],
           labels=['female', 'male'], rotation=0)
    return graph

def gr4():
    fig = sns.countplot(data=df_copy, x='pres_type',
              hue='target',
              order=['0', '1', '2', '3'],
              palette=["#a6cee3", "#1f78b4"])
    plt.title('Pressure Type vs Target');
    plt.xlabel('Pressure Type')
    plt.xticks(ticks=['0','1','2', '3'],
           labels=['Normal', 'Elevated', 'HP ST1', 'HP ST2'], rotation=0);
    return fig

st.title('Hypothesis')
st.text('There are some categorical aspects of my dataset, that wasnt fully describeв by its creator. So, I have no idea what they mean and I cant check it anywhere. The categorising idea of these aspects are not traditional. Hence, I should drop this data out of the dataset to make the research more objective.')
st.text('My Hypothesis is: female gender, atypical angina, middle age category and HP ST2 are the main features of people who are at heart attack risk group')

st.header('DataSet:')
st.dataframe(df_copy, height=300)

if st.button('Check Hypothesis!'):
    st.pyplot(gr1().get_figure())
    st.pyplot(gr2().get_figure())
    st.pyplot(gr3().get_figure())
    st.pyplot(gr4().get_figure())
else:
    st.info('Click on the button to see the graph.')
st.header("Heart Attack Risk Group Observations")

st.subheader("1. Chest Pain Type vs Target(1)")
st.write("~43% - Atypical Angina **New result**")
st.write("~24% - Non-anginal Pain **Not Confirmed**")
st.write("~24% - Typical Angina")
st.write("~9% - Typical Angina")

st.subheader("2. Sex vs Target(1)")
st.write("~45% - female **Not Confirmed**")
st.write("~55% - male people **New result**")

st.subheader("3. Age vs Target(1)")
st.write("~10% - Adults")
st.write("~68% - Middle age **Confirmed**")
st.write("~22% - Senior")

st.subheader("4. Pressure Type vs Target(1)")
st.write("~22% - Normal")
st.write("~23% - Elevated")
st.write("~25% - High Pressure Stage 1 **New Result**")
st.write("~25% - High Pressure Stage 2 **Partially Confirmed**")
st.text('Made by Ivan Fomin.')
