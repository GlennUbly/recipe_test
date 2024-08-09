# Attempt at a minimal app for returning a random selection from a set of lists
import streamlit as st
import numpy as np
import pandas as pd
import random

# dummy recipe as default
recipe = ['Create your random recipe before downloading!']
recipe_csv = np.savetxt("file_name.csv", recipe, delimiter=",", fmt='%s')
recipe_df = pd.DataFrame(recipe, columns=['Recipe items'])

# define initial lists
list_1 = ['list_1_item_a', 'list_1_item_b', 'list_1_item_c', 'list_1_item_d']
list_2 = ['list_2_item_1', 'list_2_item_2', 'list_2_item_3']
list_3 = ['list_3_item_V','list_3_item_W','list_3_item_X','list_3_item_Y','list_3_item_Z']
list_of_lists = [list_1, list_2, list_3]

# random select function
def get_selection (list_of_lists):
    output = []
    for list in list_of_lists:
        output.append(random.choice(list))
    return output
# get_selection (list_of_lists)

# Streamlit content
st.title('Create a random recipe!')
st.write('Click here to select a random item from each list:')

if st.button('Create!'):
    recipe = get_selection (list_of_lists)
    list_for_md = ''
    for item in recipe:
        list_for_md += "- " + item + "\n"
    st.markdown(list_for_md)
    recipe_csv = np.savetxt("file_name.csv", recipe, delimiter=",", fmt='%s')
    recipe_df = pd.DataFrame(recipe, columns=['Recipe items'])

recipe_df = recipe_df.to_csv(index=False).encode('utf-8')

@st.experimental_fragment
def show_download_button(file=recipe_df):
    #text_contents = recipe_df_1
    st.download_button(label="Download data as csv",
                       data=file,
                       file_name="recipe.csv",
                       mime="text/csv",
                       )
show_download_button(recipe_df)

# Inspect the lists
st.markdown('#### View list contents here:')
counter = 0
for lst in list_of_lists:
    counter += 1
    list_name = 'List '+str(counter)
    list_to_show = ''
    for item in lst:
        list_to_show += "- " + item + "\n"
    with st.expander(list_name, expanded=False):
        st.markdown(list_to_show)

