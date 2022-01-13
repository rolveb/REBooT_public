"""
Runner for REBooT related programs
"""
import os
import REBooT
import REBooT.rundfunk as R
import streamlit as st


def REBooT_program(programs=('icerisk',))):
     st.sidebar.header('Configuration (from env)')
     redis_url = st.sidebar.selectbox('REDIS_URL', (os.environ.get('REDIS_URL',None),))
     reboot_config = st.sidebar.selectbox('REBooT_config', (os.environ.get('REBooT_config', None),))
     reboot_section = st.sidebar.selectbox('REBooT_section', (os.environ.get('REBooT_section', None),))
     database_url = st.sidebar.selectbox('DATABASE_URL', (os.environ.get('DATABASE_URL', ':memory'), ':memory:'))
     option = st.sidebar.selectbox(
          'Which program do you want to run?',
          programs)
     st.write('You selected:', option)
     if option == 'icerisk' and reboot_section is not None:
          try:
               import icerisk.model
          except:
               st.error('icerisk is not installed')
               return
          try:
               r = get_runner(reboot_section)
          except Exception as e:
               st.error(e)
               return 
          R.test_streamlit()

if __name__ == '__main__':
     
     REBooT_program()

def test_icerisk():
     os.environ.update({'REBooT_section': 
                        '' 
     })