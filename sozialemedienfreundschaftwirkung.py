import streamlit as st
import pandas as pd
import altair as alt

st.header("Wirkung soziale Medien auf Freundschaft")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [84, 32, 21, 16, 6],
        'Wirkung': ['Ich bleibe immer und überall mit meinen Freunden in Kontakt', 'Neue Freundschaften sind entstanden', 'Freundschaften werden oberflächlicher', 'Wir treffen uns seltener, tauschen uns oft nur online aus', 'Nichts davon']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Wirkung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=501 Befragte; 14 bis 20 Jahre in Deutschland; 2016 (Mehrfachnennung möglich)
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Kantar Emnid 2016")